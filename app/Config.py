from app.XMLLoader import XMLLoader
from app.Xml_Index_Constants import *


class Config:
    """
    Clase de utilidad para centralizar la carga de configuraciones de la aplicación,
    incluyendo configuración principal, del modelo y de los prompts en diferentes idiomas.

    Atributos de clase:
        APP_CONFIG_PATH (str): Ruta al archivo de configuración principal (app_config.xml).
        app_config (dict): Diccionario con la configuración general de la app.
        model_config (dict): Diccionario con la configuración del modelo.
        prompt_config (dict): Diccionario con los prompts cargados según el idioma.
    """

    # Ruta al archivo de configuración de la aplicación
    APP_CONFIG_PATH = "configs\\app_config.xml"

    # --- Cargar configuración de la app y del modelo ---
    loader = XMLLoader.for_app_config()
    app_config, model_config = loader.load_app_config(APP_CONFIG_PATH)

    # --- Cargar configuración de los prompts ---
    c = XMLIndexConstants
    loader = XMLLoader.for_prompt_config(app_config.get(XMLIndexConstants.LANGUAGE))
    prompt_config = loader.load_prompt_config(
        app_config.get(c.PROMPT_CONFIG_PATH),
        app_config.get(c.LANGUAGE)
    )

    @classmethod
    def update_language(cls, lang: str, path: str):
        """
        Actualiza la configuración de los prompts a un nuevo idioma.

        Args:
            lang (str): Nuevo idioma a usar ('es' o 'en').
            path (str): Ruta al archivo de configuración de prompts (prompt_config.xml).

        Side effects:
            Sobrescribe el atributo de clase `prompt_config` con los nuevos valores cargados.
        """
        loader = XMLLoader(lang=lang)
        cls.prompt_config = loader.load_prompt_config(path, lang)
