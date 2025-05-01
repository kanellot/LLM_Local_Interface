import os
import xml.etree.ElementTree as ET

class XMLPromptLoader:
    def __init__(self, xml_path: str, lang: str = "es"):
        self.xml_path = xml_path
        self.lang = lang
        self.rules = ""
        self.pre_prompt = ""
        self.leer_pre_prompt = ""
        self.leer_post_prompt = ""
        self.load()

    def load(self):
        try:
            # Generate the abslolute config file path
            base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(base_dir, self.xml_path)
            # XML parse
            tree = ET.parse(full_path)
            root = tree.getroot()

            self.rules = self._get_lang_text(root, "rules")
            self.pre_prompt = self._get_lang_text(root, "pre_prompt")
            self.leer_pre_prompt = self._get_lang_text(root, "leer_pre_prompt")
            self.leer_post_prompt = self._get_lang_text(root, "leer_post_prompt")
            print("Prompt Configuration Load Successful")
        except Exception as e:
            raise RuntimeError(f"❌ Prompt Configuration Load Failed: {e}")

    def _get_lang_text(self, root, tag_name):
        tag = root.find(tag_name)
        if tag is not None:
            lang_tag = tag.find(self.lang)
            if lang_tag is not None:
                return lang_tag.text.strip()
        return f"❌ '{tag_name}' no definido para idioma '{self.lang}'"
