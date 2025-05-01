from app.XMLPromptLoader import XMLPromptLoader


class Config:
    #LARGE LANGUAGE MODEL CONFIG
    MODEL_PATH = r"C:\Users\kanel\.lmstudio\models\lmstudio-community\gemma-3-4B-it-qat-GGUF\gemma-3-4B-it-QAT-Q4_0.gguf"
    USE_CUDA = True
    ENABLE_MODEL = True
    MAX_TOKENS = 512
    MAX_FILE_CHARS = 3000

    #PROMPT CONFIG
    PROMPT_LANGUAGE = "es"  # Cambia a "en" o "es"
    PROMPT_CONFIG_PATH = "configs\\config01.xml"

    loader = XMLPromptLoader(PROMPT_CONFIG_PATH, PROMPT_LANGUAGE)

    RULES = loader.rules
    PRE_PROMPT = loader.pre_prompt
    LEER_PRE_PROMPT = loader.leer_pre_prompt
    LEER_POST_PROMPT = loader.leer_post_prompt

    @classmethod
    def update_language(cls, lang: str):
        cls.loader = XMLPromptLoader(cls.PROMPT_CONFIG_PATH, lang)
        cls.RULES = cls.loader.rules
        cls.PRE_PROMPT = cls.loader.pre_prompt
        cls.LEER_PRE_PROMPT = cls.loader.leer_pre_prompt
        cls.LEER_POST_PROMPT = cls.loader.leer_post_prompt
        cls.PROMPT_LANGUAGE = lang