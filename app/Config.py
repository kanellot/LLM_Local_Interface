from app.Xml_Loader import XMLLoader
from app.Xml_Index import *


class Config:
    def __init__(self):
        self.APP_CONFIG_PATH = "configs\\app_config.xml"
        self.app_config = {}
        self.app_info_msg = {}
        self.app_error_msg = {}
        self.model_config = {}
        self.prompt_config = {}
        self.loader = XMLLoader()
        self.constants = XMLIndexConstants()

        # --- Load App Configuration ---
        self.app_config["app_config"] = self.loader.load_config_lang(self.APP_CONFIG_PATH, "app_config", "")
        self.app_config["idx"] = self.constants.app_conf_keys
        lang = self.get_app_param("LANGUAGE")
        # --- Load App Info Messages ---
        msg_path = self.get_app_param("APP_MESSAGES_PATH")
        self.app_info_msg["app_info"] = self.loader.load_config_lang(msg_path, "info", lang)
        self.app_info_msg["idx"] = self.constants.app_info_conf_keys
        # --- Load App Error Messages ---
        self.app_error_msg["app_error"] = self.loader.load_config_lang(msg_path, "error", lang)
        self.app_error_msg["idx"] = self.constants.app_error_conf_keys
        # --- Load Model Configuration ---
        self.model_config["model_config"] = self.loader.load_config_lang(self.APP_CONFIG_PATH, "model_config", "")
        self.model_config["idx"] = self.constants.model_conf_keys
        # --- Load Prompt Configuration ---
        prompt_config_path = self.get_app_param("PROMPT_CONFIG_PATH")
        self.prompt_config["prompt_config"] = self.loader.load_config_lang(prompt_config_path, "prompt_config", lang)
        self.prompt_config["idx"] = self.constants.prompt_conf_keys

        del self.constants
        del self.loader
        del self.APP_CONFIG_PATH

    def get_app_param(self, param: str) -> str:
        language_key = self.app_config["idx"][param]
        return self.app_config["app_config"].get(language_key)

    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLLoader(lang=lang)
        cls.prompt_config = loader.load_prompt_config(path, lang)
