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

# Current RAG Pipeline (Work in Progress)

> **Project Status:** 🚧 **Work in Progress**
>
> This project is an actively developed Retrieval-Augmented Generation (RAG) pipeline. The overall architecture is in place, but several stages are still being refined, optimized, and integrated. Features, parser configurations, chunking strategies, and retrieval quality should be considered experimental until the pipeline is complete.

## Overview

The goal of this project is to build a modular document-ingestion pipeline capable of processing a wide variety of technical documents into a searchable vector database.

The pipeline is designed around interchangeable parsing backends, allowing different document types to be processed using the parser best suited for the job. Current development focuses on integrating both **Docling** and **Marker 2** into a common workflow while maintaining a unified downstream chunking and retrieval process.

Current execution flow:

```text
Input/
   │
   ▼
GPU / System Initialization
   │
   ▼
Initialize Docling Chunker
   │
   ▼
Build Project Paths
   │
   ▼
Create ChromaDB Client
   │
   ▼
Classify Input Documents
   │
   ├── PDF Classification
   └── General File Classification
   │
   ▼
Display Parsing Plan
   │
   ▼
Create / Open Chroma Collection
   │
   ▼
(Optional) Query Existing Collection
   │
   ▼
Document Conversion
      ├── Marker 2
      └── Docling
```

## Current Components

### Document Classification

Every document is analyzed before parsing.

The classifier determines:

* Document type
* Appropriate parser
* Parsing profile
* Output location

This allows the pipeline to automatically route documents to the most suitable parsing backend.

---

### Parsing Backends

#### Marker 2

Marker is currently used for high-fidelity PDF extraction, particularly for:

* Scientific papers
* Technical reports
* Multi-column layouts
* Tables
* Mathematical content

Current features include:

* Native SDK integration (no CLI subprocesses)
* Optional Ollama-powered LLM processors
* Markdown export
* JSON export
* Embedded image extraction

---

#### Docling

Docling serves as the general-purpose document parser.

Current focus includes:

* General PDF parsing
* Office document support
* Native document chunking
* Rich document structure extraction

The long-term goal is for Docling to become the primary ingestion engine, with Marker acting as a specialized parser for complex PDFs.

---

### Chunking *(Currently Under Development)*

Chunking has been partially implemented but is not yet integrated into the main execution flow.

Current work includes:

* Docling HybridChunker
* Token-aware chunk sizing
* Metadata generation
* Parser-independent chunk normalization

Future work includes:

* Context-aware chunk generation
* Parser output normalization
* Chunk quality evaluation
* Retrieval benchmarking

---

### ChromaDB Integration *(Currently Under Development)*

A ChromaDB client is initialized at startup.

Current capabilities include:

* Creating collections
* Opening existing collections
* Basic query interface

Automatic ingestion of parsed chunks into ChromaDB is currently disabled while the chunking pipeline is being finalized.

---

### Query System

A basic query interface is available for interacting with existing Chroma collections.

Future work will expand this into a full retrieval pipeline supporting:

* Similarity search
* Metadata filtering
* Source citations
* Multi-document retrieval

---

## Current Development Priorities

Current work is focused on completing the ingestion pipeline in the following order:

1. Finish parser integration
2. Finalize chunk generation
3. Normalize metadata between parsers
4. Integrate automatic ChromaDB ingestion
5. Evaluate retrieval quality
6. Add answer generation using retrieved context

---

## Design Philosophy

The project is intentionally modular.

Rather than treating parsing, chunking, embedding, and retrieval as a single process, each stage is implemented as an independent component.

This allows:

* Multiple parsing backends
* Independent parser benchmarking
* Configurable chunking strategies
* Future embedding model replacement
* Vector database portability

The long-term objective is a flexible RAG ingestion pipeline that can reliably process technical documents while remaining easy to extend as new parsers, embedding models, and retrieval techniques become available.

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