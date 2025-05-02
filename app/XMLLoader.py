import os
import xml.etree.ElementTree as ET
from app.Xml_Index_Constants import XMLIndexConstants

class XMLLoader:
    def __init__(self, lang: str):
        """
        Inicializa una instancia de XMLLoader con un idioma por defecto.

        Args:
            lang (str): Idioma para las configuraciones (por ejemplo, 'es' o 'en').
        """
        self.lang = lang
        self.c = XMLIndexConstants()

    def load_app_config(self, config_xml_path: str) -> tuple[dict, dict]:
        """
        Carga el archivo app_config.xml y extrae la configuración de la app y del modelo.

        Args:
            config_xml_path (str): Ruta relativa al archivo XML de configuración.

        Returns:
            tuple[dict, dict]:
                - Primer diccionario con configuración de la app (ej. idioma, ruta de prompt config).
                - Segundo diccionario con configuración del modelo (valores definidos en MODEL_STR).

        Raises:
            RuntimeError: Si ocurre un error durante la carga del archivo XML.
        """
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
            raise RuntimeError(f"❌ App Configuration Load Failed: {e}")

    def load_prompt_config(self, prompt_xml_path: str, lang: str) -> dict:
        """
        Carga el archivo prompt_config.xml y extrae los textos de prompt para el idioma especificado.

        Args:
            prompt_xml_path (str): Ruta relativa al archivo XML de configuración de prompts.
            lang (str): Idioma a cargar ('es' o 'en').

        Returns:
            dict: Diccionario con los valores de los prompts por campo definido en PROMPT_STR.

        Raises:
            ValueError: Si se especifica un idioma no soportado.
        """
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
            print(f"❌ Error loading prompt configuration: {e}")
            return {}

    def _get_text(self, node: ET.Element, tag: str) -> str:
        """
        Obtiene el texto de una subetiqueta dentro de un nodo XML.

        Args:
            node (ET.Element): Nodo XML principal.
            tag (str): Nombre de la subetiqueta a buscar.

        Returns:
            str: Texto contenido en la subetiqueta, o cadena vacía si no se encuentra.
        """
        if node is not None:
            tag_node = node.find(tag)
            if tag_node is not None and tag_node.text:
                return tag_node.text.strip()
        return ""

    def _get_lang_node_text(self, field_node: ET.Element, lang: str, field_name: str) -> str:
        """
        Obtiene el texto de un campo para un idioma específico desde un nodo de configuración.

        Args:
            field_node (ET.Element): Nodo XML que contiene los idiomas.
            lang (str): Idioma solicitado ('es' o 'en').
            field_name (str): Nombre del campo para mostrar advertencias si falta.

        Returns:
            str: Texto del campo en el idioma dado o mensaje de advertencia si no se encuentra.
        """
        if field_node is not None:
            lang_node = field_node.find(lang)
            if lang_node is not None and lang_node.text:
                return lang_node.text.strip()
            return f"⚠️ '{field_name}' no definido para idioma '{lang}'"
        return f"⚠️ '{field_name}' no encontrado en configuración"

    def _resolve_path(self, relative_path: str) -> str:
        """
        Convierte una ruta relativa en una ruta absoluta basada en la raíz del proyecto.

        Args:
            relative_path (str): Ruta relativa al archivo.

        Returns:
            str: Ruta absoluta del archivo.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, relative_path)

    @classmethod
    def for_app_config(cls):
        """
        Crea una instancia de XMLLoader para uso exclusivo con app_config.xml.

        Returns:
            XMLLoader: Instancia del cargador con idioma predeterminado 'es'.
        """
        return cls(lang="es")

    @classmethod
    def for_prompt_config(cls, lang: str):
        """
        Crea una instancia de XMLLoader para uso con prompt_config.xml en un idioma específico.

        Args:
            lang (str): Idioma deseado ('es' o 'en').

        Returns:
            XMLLoader: Instancia del cargador configurado con el idioma dado.
        """
        return cls(lang=lang)
