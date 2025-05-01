from llama_cpp import Llama
import os
from app.Config import Config

class ModelInterface:
    def __init__(self):
        self.model = None
        if Config.ENABLE_MODEL:
            self.model = self.load_model()

    def load_model(self):
        # TODO: Inicializar Llama con configuración según CUDA u opción CPU
        if Config.USE_CUDA:
            return Llama(model_path=os.path.normpath(Config.MODEL_PATH), n_ctx=4096, n_gpu_layers=1000, GPUverbose=True)
        else:
            return Llama(model_path=os.path.normpath(Config.MODEL_PATH), n_ctx=4096, verbose=True)

    def prompt(self, text: str) -> str:
        # TODO: Enviar texto al modelo y devolver respuesta como string
        if self.model:
            response = self.model(text, max_tokens=Config.MAX_TOKENS)
            return response['choices'][0]['text'].strip()
        return "❌ Modelo no inicializado."
