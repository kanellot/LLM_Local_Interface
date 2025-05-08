import os
import xml.etree.ElementTree as ET

class XMLLoader:
    def __init__(self):
        pass

    def load_config_lang(self, path_archivo: str, config_name, lang: str) -> dict:

        try:
            full_path = self._resolve_path(path_archivo)
            tree = ET.parse(full_path)
            root = tree.getroot()
            node = None

            # --- Node search ---
            if (root.tag == config_name): node = root
            else: node = root.find(config_name)
            if node is None: raise ValueError(f"No se encontró ninguna configuración con nombre ''.")

            # --- Node parse ---
            config = self._parse_recursive(node, lang)

        except Exception as e:
            raise RuntimeError("CONFIG_LOAD_ERROR")

        return config

    def _parse_recursive(self, node: ET.Element, lang: str = None) -> dict:
        config = {}
        for child in node:
            tag = child.tag
            lang_txt = child.find(lang)

            if lang and lang_txt is not None:
                # If node exists and lang node exists else return empty string,
                # avoid failure on an empty field on the xml configfiles
                config[tag] = lang_txt.text.strip() if lang_txt is not None and lang_txt.text else ""
            elif lang:
                config[tag] = f"⚠️ '{tag}' no definido para idioma '{lang}'"
            elif len(child) == 0:
                config[tag] = child.text.strip() if child.text else ""
            else:
                config[tag] = self._parse_recursive(child, lang)

        return config

    def _resolve_path(self, relative_path: str) -> str:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, relative_path)
