from llama_cpp import Llama
import os
import re

# Ruta al modelo GGUF
#MODEL_PATH = r"C:\Users\kanel\.lmstudio\models\lmstudio-community\Mistral-Nemo-Instruct-2407-GGUF\Mistral-Nemo-Instruct-2407-Q8_0.gguf"
MODEL_PATH = r"C:\Users\kanel\.lmstudio\models\hugging-quants\Llama-3.2-3B-Instruct-Q8_0-GGUF\llama-3.2-3b-instruct-q8_0.gguf"
MODEL = True
CUDA = True
# Inicializar el modelo
if(MODEL):
    if(CUDA):llm = Llama(model_path=os.path.normpath(MODEL_PATH), n_ctx=4096, n_gpu_layers=1000, GPUverbose=True)
    else:llm = Llama(model_path=os.path.normpath(MODEL_PATH), n_ctx=4096, verbose=True)


# Funciones del sistema
def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            return contenido[:3000]  # Limitar tamaño para evitar cuelgues
    except Exception as e:
        return f"❌ Error leyendo archivo: {e}"


def listar_archivos(directorio):
    try:
        archivos = os.listdir(directorio)
        nombre_padre = os.path.basename(directorio)
        if archivos:
            archivos_str = ", ".join(archivos)
            DIR = "Directorio: "
            return f"[{DIR}{nombre_padre}]({archivos_str})"
        else:
            return "No hay archivos en el directorio."
    except Exception as e:
        return f"❌ Error listando archivos: {e}"


# Función para ejecutar los comandos
def ejecutar_comando(comando):
    # Este es un ejemplo de cómo podrías manejar diferentes comandos
    if comando.startswith("/leer "):
        ruta = comando.replace("/leer ", "").strip()
        return leer_archivo(ruta)

    elif comando.startswith("/listar "):
        ruta = comando.replace("/listar ", "").strip()
        return listar_archivos(ruta)

    return f"❌ Comando no reconocido: {comando}"


# Función para procesar la entrada
def procesar_entrada(entrada):
    # Buscar comandos dentro de los paréntesis
    comandos_encontrados = re.findall(r'\((.*?)\)', entrada)

    for comando in comandos_encontrados:
        resultado_comando = ejecutar_comando(comando)
        entrada = entrada.replace(f"({comando})", resultado_comando)  # Sustituir el comando por el resultado

    return entrada


# Loop principal
while True:
    entrada = input("🟢 <Tú: ")

    if entrada.startswith("/salir"):
        break

    # Procesamos los comandos que aparecen en los paréntesis
    entrada_procesada = procesar_entrada(entrada)

    # Generar el prompt y enviarlo al modelo
    prompt = f"{entrada_procesada}"
    print(prompt)
    # Llamada al modelo Llama
    try:
        respuesta = ""
        if(MODEL):respuesta = llm(prompt, max_tokens=512)
        print(f"\n🤖 Modelo>: {respuesta['choices'][0]['text'].strip()}\n")
    except Exception as e:
        if(MODEL):print(f"❌ Error al interactuar con el modelo: {e}")
