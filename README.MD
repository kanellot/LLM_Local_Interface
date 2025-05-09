# 🧠 Local LLM CLI with File Commands

This project provides a minimalist command-line interface to interact with a local LLM (Large Language Model) using the [llama.cpp](https://github.com/ggerganov/llama.cpp) backend via the `llama-cpp-python` package. You can run prompts locally, inject file contents into prompts, and interact with the file system using simple commands.

---

## 📦 Features

- ✅ Local inference using GGUF models (e.g., Mistral, LLaMA 3)
- 📂 Command injection: read files and list folders from your prompt
- 🧱 Modular architecture: ready for future expansion with GUI (e.g., PyQt)
- 🛠️ Easy to customize or extend (add new commands or models)

---

## 🖥️ Requirements

- Python 3.9 or higher
- A compatible GGUF model (see below)
- Installed `llama-cpp-python` package
- Optional: CUDA-compatible GPU (for acceleration)

---

# 🚀 llama-cpp-python Installation Guide

1. **Clone the repository**

```bash
git clone https://github.com/kanellot/LLM_Local_Interface.git
cd LLM_Local_Interface
```
## Run the installation script

```
setup_llama_env.bat
```

This script will:

- Create a new Python virtual environment using venv
- Activate the virtual environment
- Install all required dependencies using pip

---

# 📥 Download a GGUF Model
You can get models from:

- [TheBloke](https://huggingface.co/TheBloke)
- [LM Studio](https://lmstudio.ai)

Place the .gguf model file in an accessible location and take note of its full path.

Set the path on to the app_config.xml

```
configs/app_config.xml
```

set the path on the node

```
<model_path> your model path </model_path>
```


---

## ⚡ CUDA Support (Optional)

During execution, the script will ask if want to install with CUDA support

### ✅ CUDA Requirements

- Hardware GPU CUDA compatible, (RTX...etc)
- CUDA Toolkit: Version 12.8 recommended 
- C++17-Compatible Compiler: Install Visual Studio with the "Desktop development with C++" workload
- 
Or use any other compiler that supports C++17

### Add CUDA to System PATH:

Add the following path to your environment variables:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin
```

To add it:
Open System Properties → Environment Variables Under System variables, find and edit the Path variable

---
