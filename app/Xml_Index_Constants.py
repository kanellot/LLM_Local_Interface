class XMLIndexConstants:

    # XML INDEX app config
    LANGUAGE = "language"
    PROMPT_CONFIG_PATH = "prompt_config_path"
    MODEL_PATH = "MODEL_PATH"
    USE_CUDA = "USE_CUDA"
    ENABLE_MODEL = "ENABLE_MODEL"
    MAX_TOKENS = "MAX_TOKENS"
    MAX_FILE_CHARS = "MAX_FILE_CHARS"

    APP_STR = [LANGUAGE, PROMPT_CONFIG_PATH]
    MODEL_STR = [MODEL_PATH, USE_CUDA, ENABLE_MODEL, MAX_TOKENS, MAX_FILE_CHARS]

    # XML INDEX prompt config
    RULES = "rules"
    PRE_PROMPT = "pre_prompt"
    LEER_PRE_PROMPT = "leer_pre_prompt"
    LEER_POST_PROMPT = "leer_post_prompt"

    PROMPT_STR = [RULES, PRE_PROMPT, LEER_PRE_PROMPT, LEER_POST_PROMPT]
