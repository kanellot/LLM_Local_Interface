import os
from llama_cpp import Llama
from app.Config import Config
from app.Xml_Index_Constants import XMLIndexConstants

class ModelInterface:
    def __init__(self):
        self.model = None
        self.c = XMLIndexConstants()
        if Config.model_config.get(self.c.ENABLE_MODEL):
            self.model = self.load_model()

    def load_model(self):
        path = (Config.model_config.get(self.c.MODEL_PATH).strip('"'))
        if Config.model_config.get(self.c.USE_CUDA):
            return Llama(model_path=os.path.normpath(path), n_ctx=4096, n_gpu_layers=1000, GPUverbose=True)
        else:
            return Llama(model_path=os.path.normpath(path), n_ctx=4096, verbose=True)

    def prompt(self, text: str) -> str:
        if self.model:
            response = self.model(text, max_tokens=int(Config.model_config.get(self.c.MAX_TOKENS)))
            return response['choices'][0]['text'].strip()
        return "❌ Modelo no inicializado."
