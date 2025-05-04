import os

from llama_cpp import Llama

from app.Xml_Index_Constants import XMLIndexConstants


class ModelInterface:

    def __init__(self, model_config: []):

        self.model = None
        self.model_config = model_config[0]
        self.constants = model_config[1]

        if self.model_config.get(self.constants.ENABLE_MODEL):
            self.model = self.load_model()

    def load_model(self):

        path = self.model_config.get(self.constants.MODEL_PATH).strip('"')
        if self.model_config.get(self.constants.USE_CUDA):
            return Llama(
                model_path=os.path.normpath(path),
                n_ctx=4096,
                n_gpu_layers=1000,
                GPUverbose=True
            )
        else:
            return Llama(
                model_path=os.path.normpath(path),
                n_ctx=4096,
                verbose=True
            )

    def prompt(self, text: str) -> str:

        if self.model:
            response = self.model(text, max_tokens=int(self.model_config.get(self.constants.MAX_TOKENS)))
            return response['choices'][0]['text'].strip()
        return "❌ Modelo no inicializado."
