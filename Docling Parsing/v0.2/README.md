# Quick Start: Start WSL

Use this section when you just want to start the WSL development environment and open the project.

---

## 1. Open PowerShell

Open **PowerShell** from Windows.

---

## 2. Start Ubuntu WSL

```powershell
wsl -d Ubuntu-24.04
```

You should now be inside Ubuntu WSL.

Example prompt:

```bash
your_user@your-machine:~$
```

---

## 3. Go to the Project Folder

```bash
cd ~/projects/docparse-rocm
```

---

## 4. Activate the Python Environment

```bash
source ~/venvs/docparse-rocm/bin/activate
```

You should see:

```text
(docparse-rocm)
```

at the beginning of your terminal prompt.

---

## 5. Open the Project in VS Code

```bash
code .
```

VS Code should open in WSL mode.

Check the bottom-left corner of VS Code. It should say something like:

```text
WSL: Ubuntu-24.04
```

---

## 6. Optional: Monitor WSL RAM

Open another WSL terminal and run:

```bash
watch -n 1 free -h
```

This shows live WSL memory usage while Docling or Marker is running.

---

## One-Line Startup

After everything is installed, the normal startup flow is:

```bash
wsl -d Ubuntu-24.04
cd ~/projects/docparse-rocm
source ~/venvs/docparse-rocm/bin/activate
code .
```

---

# Docling + Marker + ROCm + WSL Development Setup

This project runs inside **Ubuntu WSL2** using **VS Code Remote WSL**, **ROCm PyTorch**, **Docling**, and optionally **Marker**.

The recommended workflow is:

```text
Windows 11
  ↓
WSL2 Ubuntu 24.04
  ↓
ROCm / ROCDXG
  ↓
Python venv: docparse-rocm
  ↓
VS Code Remote WSL
  ↓
Docling / Marker parsing
```

---

# 1. Start WSL

Open **PowerShell** and run:

```powershell
wsl -d Ubuntu-24.04
```

You should see a Linux prompt like:

```bash
your_user@your-machine:~$
```

---

# 2. Go to the Project Folder

Inside WSL:

```bash
cd ~/projects/docparse-rocm
```

Verify:

```bash
pwd
```

Expected:

```text
/home/your_user/projects/docparse-rocm
```

---

# 3. Activate the Python Environment

```bash
source ~/venvs/docparse-rocm/bin/activate
```

Your terminal should now show:

```text
(docparse-rocm)
```

Example:

```bash
(docparse-rocm) your_user@your-machine:~/projects/docparse-rocm$
```

---

# 4. Verify the Python Interpreter

```bash
which python
```

Expected:

```text
/home/your_user/venvs/docparse-rocm/bin/python
```

Check PyTorch:

```bash
python -c "import torch; print(torch.__version__)"
```

Expected:

```text
2.9.1+rocm7.2.1...
```

---

# 5. Verify ROCm / GPU Access

Check that ROCm can see the AMD GPU:

```bash
rocminfo | grep -E "Name:|Marketing Name:|gfx"
```

Expected output should include something like:

```text
gfx1151
AMD Radeon(TM) 8060S Graphics
```

Then verify PyTorch GPU access:

```bash
python - <<'PY'
import torch

print("Torch:", torch.__version__)
print("HIP:", torch.version.hip)
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
PY
```

Expected:

```text
CUDA Available: True
GPU: AMD Radeon(TM) 8060S Graphics
```

Note: on ROCm, PyTorch still uses the `torch.cuda` API. Seeing `cuda` here is normal.

---

# 6. Open VS Code from WSL

From the project folder:

```bash
code .
```

VS Code should open in WSL mode.

Check the bottom-left corner of VS Code. It should say something like:

```text
WSL: Ubuntu-24.04
```

If it does not, use:

```text
Ctrl + Shift + P
WSL: Reopen Folder in WSL
```

---

# 7. Select the Correct Python Interpreter in VS Code

In VS Code:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

Choose:

```text
/home/your_user/venvs/docparse-rocm/bin/python
```

If imports like `torch`, `docling`, `bs4`, or `httpx` show as unresolved, first verify that VS Code is using this interpreter before installing anything.

---

# 8. Run Python Files

Open a Python file and click:

```text
Run Python File
```

or run from the terminal:

```bash
python main.py
```

---

# 9. Monitor WSL RAM Usage

To check memory once:

```bash
free -h
```

Example output:

```text
               total        used        free      shared  buff/cache   available
Mem:            94Gi       1.5Gi        92Gi       3.6Mi       1.3Gi        92Gi
Swap:           32Gi          0B        32Gi
```

To monitor memory live while Docling or Marker is running:

```bash
watch -n 1 free -h
```

This refreshes memory usage every second.

Useful things to watch:

```text
Mem total      = RAM available to WSL
Mem used       = RAM currently used
Mem available  = RAM still available
Swap used      = whether WSL is spilling into swap
```

If `Swap used` starts climbing heavily, reduce parser batch sizes or increase WSL memory/swap in `.wslconfig`.

---

# 10. WSL Memory Configuration

The WSL memory configuration file is on the Windows side:

```text
C:\Users\<WindowsUsername>\.wslconfig
```

Example for a 128 GB system:

```ini
[wsl2]
memory=96GB
processors=32
swap=32GB
```

After changing `.wslconfig`, restart WSL from PowerShell:

```powershell
wsl --shutdown
```

Then start WSL again:

```powershell
wsl -d Ubuntu-24.04
```

Check the result:

```bash
free -h
```

You should see close to the configured memory amount.

---

# 11. GPU Monitoring Notes

In WSL with ROCm / ROCDXG, this command may not work:

```bash
watch -n 1 rocm-smi
```

It may return:

```text
Driver not initialized (amdgpu not found in modules)
```

That is expected in this WSL setup because the Windows AMD driver is handling the GPU.

Use these instead:

```text
Windows Task Manager → Performance → GPU
AMD Adrenalin → Performance → Metrics
```

Inside WSL, use PyTorch memory stats for basic GPU allocation checks:

```bash
python - <<'PY'
import torch

print("GPU Available:", torch.cuda.is_available())
print("Device:", torch.cuda.get_device_name(0))

print("Allocated GB:", round(torch.cuda.memory_allocated() / 1024**3, 2))
print("Reserved GB:", round(torch.cuda.memory_reserved() / 1024**3, 2))
print("Max Allocated GB:", round(torch.cuda.max_memory_allocated() / 1024**3, 2))
PY
```

---

# 12. Quick GPU Stress Test

Run this to confirm PyTorch can use the AMD GPU:

```bash
python - <<'PY'
import time
import torch

device = "cuda"

print("Torch:", torch.__version__)
print("HIP:", torch.version.hip)
print("CUDA Available:", torch.cuda.is_available())
print("Device:", torch.cuda.get_device_name(0))

x = torch.randn((4096, 4096), device=device, dtype=torch.float16)
y = torch.randn((4096, 4096), device=device, dtype=torch.float16)

torch.cuda.synchronize()
start = time.time()

for _ in range(20):
    z = x @ y

torch.cuda.synchronize()

print("Seconds:", round(time.time() - start, 3))
print("Result:", z.shape, z.dtype)
print("Allocated GB:", round(torch.cuda.memory_allocated() / 1024**3, 2))
PY
```

While it runs, monitor RAM in another WSL terminal:

```bash
watch -n 1 free -h
```

And monitor GPU activity from Windows Task Manager or AMD Adrenalin.

---

# 13. Common Commands

Activate environment:

```bash
source ~/venvs/docparse-rocm/bin/activate
```

Deactivate environment:

```bash
deactivate
```

Open project in VS Code:

```bash
cd ~/projects/docparse-rocm
code .
```

Check WSL RAM:

```bash
free -h
```

Watch WSL RAM live:

```bash
watch -n 1 free -h
```

Check ROCm GPU detection:

```bash
rocminfo | grep -E "Name:|Marketing Name:|gfx"
```

Check PyTorch GPU:

```bash
python -c "import torch; print(torch.version.hip); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Run the main script:

```bash
python main.py
```

---

# 14. Typical Startup Workflow

Every development session:

```bash
wsl -d Ubuntu-24.04

cd ~/projects/docparse-rocm

source ~/venvs/docparse-rocm/bin/activate

code .
```

Then in VS Code, use:

```text
Run Python File
```

or run manually:

```bash
python main.py
```

---

# 15. Troubleshooting

## VS Code cannot resolve imports

If Pylance says imports like `torch`, `docling`, `bs4`, or `httpx` cannot be resolved, check the selected interpreter:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

Choose:

```text
/home/your_user/venvs/docparse-rocm/bin/python
```

Then reload VS Code:

```text
Ctrl + Shift + P
Developer: Reload Window
```

---

## `torch` works in terminal but not in VS Code

Run this in the VS Code terminal:

```bash
which python
python -c "import torch; print(torch.__version__)"
```

Expected:

```text
/home/your_user/venvs/docparse-rocm/bin/python
2.9.1+rocm7.2.1...
```

If this works, the issue is VS Code interpreter selection, not pip.

---

## WSL shows only 62 GiB RAM on a 128 GB system

That usually means `.wslconfig` is not being applied.

Check from PowerShell:

```powershell
type $env:USERPROFILE\.wslconfig
```

Then restart WSL:

```powershell
wsl --shutdown
```

Start it again:

```powershell
wsl -d Ubuntu-24.04
```

Check:

```bash
free -h
```

---

## `rocm-smi` does not work

This is expected in WSL / ROCDXG.

Use:

```text
Windows Task Manager
AMD Adrenalin
PyTorch memory stats
watch -n 1 free -h
```

instead.

---

# 16. Recommended Project Layout

```text
docparse-rocm/
├── Input/
├── Output/
├── Functions/
│   ├── functions.py
│   └── functionsClassify.py
├── main.py
├── README.md
└── .vscode/
    └── settings.json
```

Recommended `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "/home/your_user/venvs/docparse-rocm/bin/python"
}
```