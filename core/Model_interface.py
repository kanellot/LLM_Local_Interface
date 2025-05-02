import os
from llama_cpp import Llama
from app.Config import Config

class ModelInterface:
    def __init__(self):
        self.model = None
        if Config.model_config.get("ENABLE_MODEL"):
            self.model = self.load_model()

    def load_model(self):
        # TODO: Inicializar Llama con configuración según CUDA u opción CPU
        if Config.model_config.get("USE_CUDA"):
            return Llama(model_path=os.path.normpath(Config.model_config.get("MODEL_PATH")), n_ctx=4096, n_gpu_layers=1000, GPUverbose=True)
        else:
            return Llama(model_path=os.path.normpath(Config.model_config.get("MODEL_PATH")), n_ctx=4096, verbose=True)

    def prompt(self, text: str) -> str:
        # TODO: Enviar texto al modelo y devolver respuesta como string
        if self.model:
            response = self.model(text, max_tokens=Config.model_config.get("MAX_TOKENS"))
            return response['choices'][0]['text'].strip()
        return "❌ Modelo no inicializado."
