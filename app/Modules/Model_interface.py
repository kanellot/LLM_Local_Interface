import os

from llama_cpp import Llama
from app.Modules.MessageManager import MessageManager

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
        en_cuda = self.str_to_bool((self.conf.get(self.c["USE_CUDA"])))
        console_dbg = self.str_to_bool((self.conf.get(self.c["CONSOLE_DBG"])))
        n_gpu_layers = int(self.conf.get(self.c["N_GPU_LAYERS"]))

        if (en_cuda):
            return Llama(
                model_path=os.path.normpath(path),
                n_ctx=4096,
                n_gpu_layers=n_gpu_layers,
                GPUverbose=console_dbg,
                verbose=console_dbg
            )
        else:
            return Llama(
                model_path=os.path.normpath(path),
                n_ctx=4096,
                n_gpu_layers=0,
                verbose=console_dbg
            )

    def prompt(self, text: str) -> str:

        if self.model:
            response = self.model(text, max_tokens=int(self.conf.get(self.c["MAX_TOKENS"])))
            return response['choices'][0]['text'].strip()
        return self.mm.print_info("MODEL_LOAD_ERROR")

    def str_to_bool(self, string_param: str):
        return str(string_param).strip().lower() in ("true", "on", "yes")
