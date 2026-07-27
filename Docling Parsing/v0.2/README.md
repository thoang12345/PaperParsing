## Quick Start

After the container has been created once:

Start the Surya inference server:

```bash
docker start surya-vllm
```

Follow the startup logs:

```bash
docker logs -f surya-vllm
```

Press **Ctrl+C** to stop following the logs. The container will continue running.

In another terminal:

```bash
python main.py
```

Marker will automatically connect to:

```text
http://localhost:8000/v1
```

When you're finished:

```bash
docker stop surya-vllm
```

Further instructions for creating the container below.

---

# Deploying Marker 2 & Surya OCR-2 with vLLM on AMD Strix Halo (ROCm)

This guide describes how to deploy **Marker 2** with **Surya OCR-2** using an external **vLLM** inference server running inside a Docker container.

This setup has been tested on **AMD Strix Halo APUs** (`gfx1151` / RDNA 3.5) running Arch Linux with ROCm. Marker performs document parsing locally while Surya uses a persistent OpenAI-compatible vLLM server for OCR, layout analysis, and vision-language inference.

---

## Why Use Docker?

Arch Linux is a rolling-release distribution where libraries such as `glibc`, ROCm, and compiler toolchains are updated frequently.

Running the vLLM inference server inside Docker isolates these dependencies from the host system while still allowing direct access to the AMD GPU through ROCm device passthrough.

Marker itself continues to run natively inside a Python virtual environment and communicates with the server through HTTP.

---

# Install Docker

Install Docker and enable the service:

```bash
sudo pacman -Syu docker

sudo systemctl enable --now docker
```

Allow your user to access Docker and the ROCm devices:

```bash
sudo usermod -aG docker,video,render $USER
```

Log out and back in (or reboot) so the new group memberships take effect.

---

# Configure Marker

Marker should always use the external Surya inference server.

Add the following to your shell configuration:

```bash
echo 'export SURYA_INFERENCE_BACKEND=vllm' >> ~/.bashrc
echo 'export SURYA_INFERENCE_URL=http://localhost:8000/v1' >> ~/.bashrc

source ~/.bashrc
```

Verify:

```bash
echo $SURYA_INFERENCE_BACKEND
echo $SURYA_INFERENCE_URL
```

Expected:

```text
vllm
http://localhost:8000/v1
```

---

# Create the Surya Server

Create the Docker container once:

```bash
docker run -d \
  --name surya-vllm \
  --device /dev/kfd \
  --device /dev/dri \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -p 8000:8000 \
  -e HSA_OVERRIDE_GFX_VERSION=11.5.0 \
  -e MIOPEN_FIND_MODE=2 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  vllm/vllm-openai-rocm:latest \
  --model datalab-to/surya-ocr-2 \
  --served-model-name datalab-to/surya-ocr-2 \
  --dtype bfloat16 \
  --max-model-len 16384 \
  --max-num-batched-tokens 4096 \
  --mm-processor-kwargs '{"min_pixels":3136,"max_pixels":1048576}' \
  --gpu-memory-utilization 0.2 \
  --port 8000
```

This only needs to be done once.

---

# Daily Startup

For normal development sessions, simply start the existing container:

```bash
docker start surya-vllm
```

Follow the startup logs if desired:

```bash
docker logs -f surya-vllm
```

Press **Ctrl+C** to stop following the logs. The container will continue running.

---

# Verify the Server

Confirm that the container is running:

```bash
docker ps
```

You should see:

```text
surya-vllm
```

Then verify the inference endpoint:

```bash
curl http://localhost:8000/v1/models
```

If model information is returned, the Surya inference server is ready.

---

## Recovering from a Failed Container

If the container exits during startup, remove it completely:

```bash
docker rm -f surya-vllm
```

Then recreate it using the **Create the Surya Server** command above.

# Install Marker

Inside your Python virtual environment:

```bash
pip install surya-ocr==0.22.1
pip install marker-pdf==2.0.0
```

Marker will automatically connect to the external Surya server using the environment variables configured earlier.

No additional OpenAI environment variables are required.

---

# Architecture

```text
PDF
 │
 ▼
Marker 2
 │
 ├── Layout
 ├── OCR
 ├── Table Recognition
 └── LLM Processors
 │
 ▼
Surya Inference Manager
 │
 ▼
External vLLM Server (Docker)
 │
 ▼
Surya OCR-2
 │
 ▼
Markdown + JSON + Images
```