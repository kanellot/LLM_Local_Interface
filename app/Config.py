from app.XMLPromptLoader import XMLPromptLoader

class Config:

    #APP CONGIG
    APP_CONFIG_PATH= "configs\\app_config.xml"
    PROMPT_CONFIG_PATH = "configs\\prompt_config01.xml"
    PROMPT_LANGUAGE = "en"  # Cambia a "en" o "es"

    # LOAD APP & MODEL CONFIG
    loader = XMLPromptLoader()
    app_config, model_config = loader.load_app_config(APP_CONFIG_PATH)

    # LOAD PROMPT CONFIG
    loader = XMLPromptLoader(lang=PROMPT_LANGUAGE)
    prompt_config = loader.load_prompt_config(PROMPT_CONFIG_PATH, PROMPT_LANGUAGE)

    # UPDATE PROMPT CONFIG (LANGUAGE)
    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLPromptLoader(lang=lang)
        prompt_config = loader.load_prompt_config(path, lang)