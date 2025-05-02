class XMLIndexConstants:
    # --- Etiquetas del XML de configuración de la app ---
    LANGUAGE = "language"  #: Idioma principal de la aplicación ('es' o 'en')
    PROMPT_CONFIG_PATH = "prompt_config_path"  #: Ruta al archivo XML de configuración de prompts
    MODEL_PATH = "MODEL_PATH"  #: Ruta al modelo de lenguaje
    USE_CUDA = "USE_CUDA"  #: Indicador de uso de GPU (CUDA)
    ENABLE_MODEL = "ENABLE_MODEL"  #: Activar/desactivar el modelo
    MAX_TOKENS = "MAX_TOKENS"  #: Límite máximo de tokens en salida
    MAX_FILE_CHARS = "MAX_FILE_CHARS"  #: Límite de caracteres al leer archivos

    # Listado de claves esperadas dentro de <app> en app_config.xml
    APP_STR = [LANGUAGE, PROMPT_CONFIG_PATH]

    # Listado de claves esperadas dentro de <model> en app_config.xml
    MODEL_STR = [MODEL_PATH, USE_CUDA, ENABLE_MODEL, MAX_TOKENS, MAX_FILE_CHARS]

    # --- Etiquetas del XML de configuración de prompts ---
    RULES = "rules"  #: Instrucciones base que siguen todos los prompts
    PRE_PROMPT = "pre_prompt"  #: Prompt base previo a cualquier entrada del usuario
    LEER_PRE_PROMPT = "leer_pre_prompt"  #: Prompt específico antes de la lectura de archivos
    LEER_POST_PROMPT = "leer_post_prompt"  #: Prompt específico después de la lectura de archivos

    # Listado de claves esperadas en prompt_config.xml
    PROMPT_STR = [RULES, PRE_PROMPT, LEER_PRE_PROMPT, LEER_POST_PROMPT]
