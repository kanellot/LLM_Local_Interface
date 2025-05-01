# 🧠 Local LLM CLI with File Commands

Este proyecto proporciona una interfaz de línea de comandos minimalista para interactuar con un modelo LLM (Large Language Model) local utilizando el backend de [llama.cpp](https://github.com/ggerganov/llama.cpp) a través del paquete `llama-cpp-python`. Puedes ejecutar prompts localmente, insertar contenido de archivos en los prompts e interactuar con el sistema de archivos usando comandos simples.

---

## 📦 Características

- ✅ Inferencia local usando modelos GGUF (como Mistral, LLaMA 3)
- 📂 Inyección de comandos: lee archivos y lista carpetas desde tu prompt
- 🧱 Arquitectura modular: preparada para expansión futura con GUI (por ejemplo, PyQt)
- 🛠️ Fácil de personalizar o extender (agregar más comandos o modelos)

---

## 🧰 Estructura del Proyecto

```
your_project/
│
├── app/
│   ├── main.py           # Punto de entrada de la aplicación
│   └── config.py         # Parámetros de configuración
│
├── core/
│   ├── model_interface.py # Carga del modelo e interacción
│   ├── command_parser.py  # Detección y sustitución de comandos
│   └── file_manager.py    # Lógica de lectura y listado de archivos
│
└── README.md
```

---

## 🖥️ Requisitos

- Python 3.9 o superior
- Un modelo GGUF compatible (ver más abajo)
- Paquete `llama-cpp-python` instalado
- Opcional: GPU compatible con CUDA (para aceleración)

---

## 🚀 Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/yourusername/your_project.git
cd your_project
```

2. **Configura un entorno virtual (recomendado)**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias**

```bash
pip install llama-cpp-python
```

4. **Descarga un modelo GGUF**

Puedes obtener modelos desde:

- [TheBloke](https://huggingface.co/TheBloke)
- [LM Studio](https://lmstudio.ai)

Coloca el archivo `.gguf` en un lugar accesible y toma nota de su ruta completa.

5. **Configura el modelo**

Edita el archivo `app/config.py`:

```python
MODEL_PATH = r"C:\ruta\a\tu\modelo.gguf"
USE_CUDA = True           # Cambiar a False si usas CPU
ENABLE_MODEL = True       # Cambiar a False para depuración sin modelo
MAX_TOKENS = 512
MAX_FILE_CHARS = 3000     # Limita el contenido de archivo leído
```

---

## 🧪 Ejecutar la Aplicación

Desde el directorio raíz:

```bash
python app/main.py
```

Verás un mensaje como:

```
🟢 Iniciando aplicación...
🟢 <Tú:
```

Ahora puedes comenzar a escribir tus prompts.

---

## 💡 Uso de Prompts y Comandos

Puedes insertar comandos especiales dentro de paréntesis `(...)`, y la aplicación los resolverá antes de enviar el prompt al modelo.

### ✅ Comandos Soportados

| Comando         | Descripción                            | Ejemplo                      |
|----------------|----------------------------------------|------------------------------|
| `/leer <ruta>` | Lee un archivo de texto                | `( /leer notas.txt )`        |
| `/listar <dir>`| Lista archivos en un directorio        | `( /listar ./docs )`         |

Puedes combinarlos con texto libre, por ejemplo:

```text
Por favor resume el siguiente archivo: (/leer intro.txt) y lista los documentos: (/listar ./docs)
```

---

¡Fácil de extender, ideal para proyectos locales con LLM!
