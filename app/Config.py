from app.XMLLoader import XMLLoader
from app.Xml_Index_Constants import *


class Config:
    def __init__(self):
        self.APP_CONFIG_PATH = "configs\\app_config.xml"
        self.app_config = {}
        self.model_config = {}
        self.prompt_config = {}
        self.loader = XMLLoader("es")
        self.constants = XMLIndexConstants()

        # --- Cargar configuración de la app y del modelo ---
        self.app_config, self.model_config = self.loader.load_app_config(self.APP_CONFIG_PATH)

        # --- Cargar configuración de los prompts ---
        self.loader = XMLLoader.for_prompt_config(self.app_config.get(self.constants.LANGUAGE))
        self.prompt_config = self.loader.load_prompt_config(
            self.app_config.get(self.constants.PROMPT_CONFIG_PATH),
            self.app_config.get(self.constants.LANGUAGE)
        )

    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLLoader(lang=lang)
        cls.prompt_config = loader.load_prompt_config(path, lang)
