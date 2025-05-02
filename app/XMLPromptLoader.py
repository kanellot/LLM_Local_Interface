import os
import xml.etree.ElementTree as ET

class XMLPromptLoader:
    def __init__(self, lang: str = "es"):
        self.lang = lang
        self.app_config = {}
        self.rules = ""
        self.pre_prompt = ""
        self.leer_pre_prompt = ""
        self.leer_post_prompt = ""

    # LOAD app_config.xml
    def load_app_config(self, config_xml_path: str):
        try:
            full_path = self._resolve_path(config_xml_path)
            tree = ET.parse(full_path)
            root = tree.getroot()

            # Load app config values
            app_config_dict = {}
            app_config = root.find("app")
            if app_config is not None:
                app_config_dict["language"] = app_config.find("language").text
                app_config_dict["prompt_config_path"] = app_config.find("prompt_config_path").text

            # Load model config values
            model_config_dict = {}
            model_config = root.find("model")
            if model_config is not None:
                fields = ["MODEL_PATH", "USE_CUDA", "ENABLE_MODEL", "MAX_TOKENS", "MAX_FILE_CHARS"]
                for field in fields:
                    tag = model_config.find(field)
                    if tag is not None:
                        model_config_dict[field] = tag.text.strip()

            print(f"✅ App Configuration Load Successful'")

            return app_config_dict, model_config_dict

        except Exception as e:
            raise RuntimeError(f"❌ App Configuration Load Failed: {e}")

    # LOAD  prompt_config xml
    def load_prompt_config(self, prompt_xml_path: str, lang: str):
        try:
            full_path = self._resolve_path(prompt_xml_path)
            tree = ET.parse(full_path)
            prompt_config = tree.getroot()
            prompt_config_dict = {}

            if lang not in {"es", "en"}:
                raise ValueError(f"Idioma no soportado: '{lang}'. Usa 'es' o 'en'.")

            fields = ["rules", "pre_prompt", "leer_pre_prompt", "leer_post_prompt"]

            for field_name in fields:
                field_node = prompt_config.find(field_name)
                if field_node is not None:
                    lang_node = field_node.find(lang)
                    if lang_node is not None and lang_node.text is not None:
                        prompt_config_dict[field_name] = lang_node.text.strip()
                    else:
                        prompt_config_dict[field_name] = f"⚠️ '{field_name}' no definido para idioma '{lang}'"
                else:
                    prompt_config_dict[field_name] = f"⚠️ '{field_name}' no encontrado en configuración"

            print(f"✅ Prompt Configuration Load Successful for language: '{lang}'")
            return prompt_config_dict

        except Exception as e:
            print(f"❌ Error loading prompt configuration: {e}")
            return {}


    def _get_lang_text(self, root, tag_name):
        tag = root.find(tag_name)
        if tag is not None:
            lang_tag = tag.find(self.lang)
            if lang_tag is not None and lang_tag.text:
                return lang_tag.text.strip()
        return f"❌ '{tag_name}' no definido para idioma '{self.lang}'"

    def _resolve_path(self, relative_path: str) -> str:
        """Helper to get absolute path from a relative path."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, relative_path)
