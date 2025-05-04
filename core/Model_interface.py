import os

from llama_cpp import Llama
from app.MessageManager import MessageManager

class ModelInterface:

    def __init__(self, model_config: dict, mm: MessageManager):

        self.model = None
        self.conf = model_config["model_config"]
        self.c = model_config["idx"]
        self.mm = mm
        if self.conf.get(self.c["ENABLE_MODEL"]):
            self.model = self.load_model()

    def load_model(self):

        path = self.conf.get(self.c["MODEL_PATH"]).strip('"')
        if self.conf.get(self.c["USE_CUDA"]):
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
        #if (False):
        if self.model:
            response = self.model(text, max_tokens=int(self.conf.get(self.c["MAX_TOKENS"])))
            return response['choices'][0]['text'].strip()
        return self.mm.print_info("MODEL_LOAD_ERROR")
