from app.XMLLoader import XMLLoader
from app.Xml_Index_Constants import *


class Config:
    def __init__(self):
        self.APP_CONFIG_PATH = "configs\\app_config.xml"
        self.app_config = {}
        self.model_config = {}
        self.prompt_config = {}
        self.loader = XMLLoader()
        self.constants = XMLIndexConstants()

        # --- Load App Configuration ---
        self.app_config["app_config"] = self.loader.load_config(self.APP_CONFIG_PATH, "app_config")
        self.app_config["idx"] = self.constants.app_conf_keys
        # --- Load Model Configuration ---
        self.model_config["model_config"] = self.loader.load_config(self.APP_CONFIG_PATH, "model_config")
        self.model_config["idx"] = self.constants.model_conf_keys
        # --- Load Prompt Configuration ---
        lang = self.get_app_param("LANGUAGE")
        prompt_config_path = self.get_app_param("PROMPT_CONFIG_PATH")
        self.prompt_config["prompt_config"] = self.loader.load_config_lang(prompt_config_path, lang)
        self.prompt_config["idx"] = self.constants.prompt_conf_keys

    def get_app_param(self, param: str) -> str:
        language_key = self.app_config["idx"][param]
        return self.app_config["app_config"].get(language_key)

    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLLoader(lang=lang)
        cls.prompt_config = loader.load_prompt_config(path, lang)
