from app.XMLLoader import XMLLoader

class Config:

    # CONSTANTS
    # XML INDEX app config
    LANGUAGE = "language"
    PROMPT_CONFIG_PATH = "prompt_config_path"
    MODEL_PATH = "MODEL_PATH"
    USE_CUDA = "USE_CUDA"
    ENABLE_MODEL = "ENABLE_MODEL"
    MAX_TOKENS = "MAX_TOKENS"
    MAX_FILE_CHARS = "MAX_FILE_CHARS"
    app_Str = [LANGUAGE, PROMPT_CONFIG_PATH]
    model_Str = [MODEL_PATH, USE_CUDA, ENABLE_MODEL, MAX_TOKENS, MAX_FILE_CHARS]
    # XML INDEX prompt config
    RULES = "rules"
    PRE_PROMPT = "pre_prompt"
    LEER_PRE_PROMPT = "leer_pre_prompt"
    LEER_POST_PROMPT = "leer_post_prompt"
    prompt_str = [RULES, PRE_PROMPT, LEER_PRE_PROMPT, LEER_POST_PROMPT]

    #APP CONGIG
    APP_CONFIG_PATH= "configs\\app_config.xml"

    # LOAD APP & MODEL CONFIG
    loader = XMLLoader()
    app_config, model_config = loader.load_app_config(APP_CONFIG_PATH)

    # LOAD PROMPT CONFIG
    loader = XMLLoader(lang=app_config.get(LANGUAGE))
    pa = app_config.get(PROMPT_CONFIG_PATH)
    la = app_config.get(LANGUAGE)
    prompt_config = loader.load_prompt_config(app_config.get(PROMPT_CONFIG_PATH), app_config.get(LANGUAGE))

    # UPDATE PROMPT CONFIG (LANGUAGE)
    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLLoader(lang=lang)
        prompt_config = loader.load_prompt_config(path, lang)