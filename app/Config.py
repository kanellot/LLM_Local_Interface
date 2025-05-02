from app.XMLLoader import XMLLoader
from app.Xml_Index_Constants import *

class Config:

    #APP CONGIG
    APP_CONFIG_PATH= "configs\\app_config.xml"

    # LOAD APP & MODEL CONFIG
    loader = XMLLoader()
    app_config, model_config = loader.load_app_config(APP_CONFIG_PATH)

    # LOAD PROMPT CONFIG
    c = XMLIndexConstants
    loader = XMLLoader(lang=app_config.get(c.LANGUAGE))
    pa = app_config.get(c.PROMPT_CONFIG_PATH)
    la = app_config.get(c.LANGUAGE)
    prompt_config = loader.load_prompt_config(app_config.get(c.PROMPT_CONFIG_PATH), app_config.get(c.LANGUAGE))

    # UPDATE PROMPT CONFIG (LANGUAGE)
    @classmethod
    def update_language(cls, lang: str, path: str):
        loader = XMLLoader(lang=lang)
        prompt_config = loader.load_prompt_config(path, lang)