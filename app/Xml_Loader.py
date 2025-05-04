import os
import xml.etree.ElementTree as ET
from app.ErrorHandler import ErrorHandler


class XMLLoader:
    def __init__(self):
        pass

    def load_config(self, path_archivo: str, nombre_config: str) -> dict:
        try:
            full_path = self._resolve_path(path_archivo)
            tree = ET.parse(full_path)
            root = tree.getroot()

            group_node = None
            for child in root:
                if child.tag == nombre_config:
                    group_node = child
                    break

            if group_node is None:
                raise ValueError(f"No se encontró ninguna configuración con nombre '{nombre_config}'.")

            config = self._parse_recursive(group_node)
            print("✅ Configuración cargada correctamente.")
            return config

        except Exception as e:
            raise RuntimeError(ErrorHandler.format("CONFIG_LOAD_ERROR", error=str(e)))

    def load_config_lang(self, path_archivo: str, lang: str) -> dict:
        """
        Carga un archivo XML filtrando los nodos que tienen subetiquetas por idioma (es/en).
        """
        try:
            if lang not in {"es", "en"}:
                raise ValueError(f"Idioma no soportado: '{lang}'. Usa 'es' o 'en'.")

            full_path = self._resolve_path(path_archivo)
            tree = ET.parse(full_path)
            root = tree.getroot()

            group_node = None
            for child in root:
                #if child.tag == nombre_config:
                group_node = child
                break

            if group_node is None:
                raise ValueError(f"No se encontró ninguna configuración con nombre ''.")

            config = self._parse_recursive(root, lang)
            print(f"✅ Configuración cargada correctamente para idioma: '{lang}'")
            return config

        except Exception as e:
            raise RuntimeError(ErrorHandler.format("CONFIG_LOAD_ERROR", error=str(e)))

    def _parse_recursive(self, node: ET.Element, lang: str = None) -> dict:
        """
        Recorrido recursivo de un nodo XML, extrae texto según idioma si es necesario.
        """
        config = {}
        for child in node:
            tag = child.tag

            if lang and child.find(lang) is not None:
                config[tag] = child.find(lang).text.strip()
            elif lang:
                config[tag] = f"⚠️ '{tag}' no definido para idioma '{lang}'"
            elif len(child) == 0:
                config[tag] = child.text.strip() if child.text else ""
            else:
                config[tag] = self._parse_recursive(child, lang=lang)

        return config

    def _resolve_path(self, relative_path: str) -> str:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, relative_path)
