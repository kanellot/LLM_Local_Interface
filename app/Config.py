class Config:
    # TODO: Ajusta los valores según tus rutas locales
    MODEL_PATH = r"C:\Users\kanel\.lmstudio\models\hugging-quants\Llama-3.2-3B-Instruct-Q8_0-GGUF\llama-3.2-3b-instruct-q8_0.gguf"
    USE_CUDA = True
    ENABLE_MODEL = True
    MAX_TOKENS = 512
    MAX_FILE_CHARS = 3000

    #PROMPT CONFIG
    PRE_PROMPT="El contenido entre [inicio-documento] y [fin-documento] lo debes tratar como un documento de texto"+'\n'
    POST_PROMPT='\n'+"Contesta segun las normas descritas"

    #LEER PROMPT CONFIG
    LEER_PATH="Hola me puedes decir cuantas linias tiene el siguiente documento?(/leer C:\\Users\\kanel\\Desktop\\files\\Main_mp3.txt)" #Debug only
    LEER_PRE_PROMPT = '\n'"[inicio_documento]"+'\n'
    LEER_POST_PROMPT = "[fin_documento]"+'\n'
