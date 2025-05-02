import os
from llama_cpp import Llama
from app.Config import Config
from app.Xml_Index_Constants import XMLIndexConstants

class ModelInterface:
    """
    Clase de interfaz para la carga y ejecución de un modelo LLaMA a través de llama_cpp.

    Esta clase se encarga de inicializar el modelo con la configuración especificada y
    de enviar prompts para obtener respuestas.

    Atributos:
        model (Llama | None): Instancia del modelo LLaMA si está habilitado, o None.
        c (XMLIndexConstants): Constantes de clave para acceder a configuraciones.
    """

    def __init__(self):
        """
        Constructor que carga el modelo si la opción ENABLE_MODEL está activa en la configuración.
        """
        self.model = None
        self.c = XMLIndexConstants()
        if Config.model_config.get(self.c.ENABLE_MODEL):
            self.model = self.load_model()

    def load_model(self):
        """
        Carga el modelo LLaMA desde el path especificado en la configuración.

        Returns:
            Llama: Instancia del modelo cargado.
        """
        path = Config.model_config.get(self.c.MODEL_PATH).strip('"')
        if Config.model_config.get(self.c.USE_CUDA):
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
        """
        Envía un texto al modelo y devuelve la respuesta generada.

        Args:
            text (str): Texto de entrada (prompt) a procesar por el modelo.

        Returns:
            str: Respuesta del modelo o mensaje de error si el modelo no está inicializado.
        """
        if self.model:
            response = self.model(text, max_tokens=int(Config.model_config.get(self.c.MAX_TOKENS)))
            return response['choices'][0]['text'].strip()
        return "❌ Modelo no inicializado."
