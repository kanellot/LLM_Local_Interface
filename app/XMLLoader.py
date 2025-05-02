import os
import xml.etree.ElementTree as ET
from app.ErrorHandler import ErrorHandler
from app.Xml_Index_Constants import XMLIndexConstants


class XMLLoader:
    def __init__(self, lang: str):

        self.lang = lang
        self.c = XMLIndexConstants()

    def load_app_config(self, config_xml_path: str) -> tuple[dict, dict]:

        try:
            full_path = self._resolve_path(config_xml_path)
            tree = ET.parse(full_path)
            root = tree.getroot()

            app_config = root.find("app")
            app_config_dict = {
                self.c.LANGUAGE: self._get_text(app_config, self.c.LANGUAGE),
                self.c.PROMPT_CONFIG_PATH: self._get_text(app_config, self.c.PROMPT_CONFIG_PATH),
            } if app_config is not None else {}

            model_config = root.find("model")
            model_config_dict = {
                field: self._get_text(model_config, field)
                for field in self.c.MODEL_STR
                if model_config is not None and model_config.find(field) is not None
            }

            print("✅ App Configuration Load Successful")
            return app_config_dict, model_config_dict

        except Exception as e:
            raise RuntimeError(ErrorHandler.format("CONFIG_LOAD_ERROR", error=str(e)))

    def load_prompt_config(self, prompt_xml_path: str, lang: str) -> dict:

        try:
            if lang not in {"es", "en"}:
                raise ValueError(f"Idioma no soportado: '{lang}'. Usa 'es' o 'en'.")

            full_path = self._resolve_path(prompt_xml_path)
            tree = ET.parse(full_path)
            root = tree.getroot()

            prompt_config_dict = {
                field: self._get_lang_node_text(root.find(field), lang, field)
                for field in self.c.PROMPT_STR
            }

            print(f"✅ Prompt Configuration Load Successful for language: '{lang}'")
            return prompt_config_dict

        except Exception as e:
            raise RuntimeError(ErrorHandler.format("CONFIG_LOAD_ERROR", error=str(e)))

    def _get_text(self, node: ET.Element, tag: str) -> str:

        if node is not None:
            tag_node = node.find(tag)
            if tag_node is not None and tag_node.text:
                return tag_node.text.strip()
        return ""

    def _get_lang_node_text(self, field_node: ET.Element, lang: str, field_name: str) -> str:

        if field_node is not None:
            lang_node = field_node.find(lang)
            if lang_node is not None and lang_node.text:
                return lang_node.text.strip()
            return f"⚠️ '{field_name}' no definido para idioma '{lang}'"
        return f"⚠️ '{field_name}' no encontrado en configuración"

    def _resolve_path(self, relative_path: str) -> str:

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, relative_path)

    @classmethod
    def for_app_config(cls):

        return cls(lang="es")

    @classmethod
    def for_prompt_config(cls, lang: str):

        return cls(lang=lang)
