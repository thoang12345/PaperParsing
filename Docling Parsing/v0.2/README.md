# Starting the Docling + ROCm + WSL Development Environment

This project is designed to run inside **Ubuntu WSL2** using **VS Code Remote WSL**, **ROCm**, **PyTorch**, and **Docling**.

---

# Prerequisites

The following should already be installed:

- Windows 11
- WSL2
- Ubuntu 24.04
- VS Code
- VS Code WSL Extension
- ROCm
- Python virtual environment (`docparse-rocm`)

---

# Verify WSL is Installed

Open PowerShell and run:

```powershell
wsl --list --verbose
```

Expected output:

```text
  NAME            STATE           VERSION
* Ubuntu-24.04    Stopped         2
```

Version should be **2**.

---

# Start Ubuntu WSL

Open PowerShell:

```powershell
wsl -d Ubuntu-24.04
```

You should see:

```bash
thienan_hoang@Thienan-Flow-Z13:~$
```

---

# Navigate to the Project

```bash
cd ~/projects/docparse-rocm
```

Verify location:

```bash
pwd
```

Expected:

```text
/home/thienan_hoang/projects/docparse-rocm
```

---

# Activate the Python Environment

```bash
source ~/venvs/docparse-rocm/bin/activate
```

You should now see:

```text
(docparse-rocm)
```

at the beginning of your prompt.

Example:

```bash
(docparse-rocm) thienan_hoang@Thienan-Flow-Z13:~/projects/docparse-rocm$
```

---

# Verify Python Environment

Check the active interpreter:

```bash
which python
```

Expected:

```text
/home/thienan_hoang/venvs/docparse-rocm/bin/python
```

Verify PyTorch:

```bash
python -c "import torch; print(torch.__version__)"
```

Expected:

```text
2.9.1+rocm7.2.1
```

---

# Verify ROCm

Check that ROCm can see the GPU:

```bash
rocminfo | grep -E "Name:|Marketing Name:|gfx"
```

Expected output should contain:

```text
gfx1151
AMD Radeon(TM) 8060S Graphics
```

---

# Verify PyTorch GPU Access

Run:

```bash
python
```

Then:

```python
import torch

print(torch.version.hip)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

Expected:

```text
7.2.1
True
AMD Radeon(TM) 8060S Graphics
```

Exit Python:

```python
exit()
```

---

# Open VS Code

From the project directory:

```bash
code .
```

VS Code should open.

Verify the lower-left corner displays:

```text
WSL: Ubuntu-24.04
```

If it does not:

```text
Ctrl+Shift+P
WSL: Reopen Folder in WSL
```

---

# Verify VS Code Interpreter

In VS Code:

```text
Ctrl+Shift+P
Python: Select Interpreter
```

Choose:

```text
/home/thienan_hoang/venvs/docparse-rocm/bin/python
```

---

# Run Python Files

Open a Python file and click:

```text
▶ Run Python File
```

or use:

```text
Ctrl+F5
```

---

# Quick GPU Test

Create a file:

```python
import torch

print("Torch:", torch.__version__)
print("HIP:", torch.version.hip)
print("GPU Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Device:", torch.cuda.get_device_name(0))
```

Expected:

```text
Torch: 2.9.1+rocm7.2.1
HIP: 7.2.1
GPU Available: True
Device: AMD Radeon(TM) 8060S Graphics
```

---

# Common Commands

Activate Environment

```bash
source ~/venvs/docparse-rocm/bin/activate
```

Deactivate Environment

```bash
deactivate
```

Launch VS Code

```bash
code .
```

Check GPU

```bash
rocminfo
```

Check PyTorch GPU

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Monitor GPU Usage

```bash
watch -n 1 rocm-smi
```

---

# Typical Startup Workflow

Every development session:

```bash
wsl -d Ubuntu-24.04

cd ~/projects/docparse-rocm

source ~/venvs/docparse-rocm/bin/activate

code .
```

That's it.