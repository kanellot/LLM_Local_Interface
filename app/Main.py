from app.Config import Config
from core.Model_interface import ModelInterface
from core.Command_parser import CommandParser
from core.File_manager import FileManager

def main():
    """
    Punto de entrada principal para la aplicación de línea de comandos.

    - Inicializa la configuración, el modelo de lenguaje, el gestor de archivos y el parser de comandos.
    - Inicia un bucle interactivo donde el usuario puede introducir texto o comandos.
    - Procesa el texto del usuario, lo envía al modelo, y muestra la respuesta.
    - Usa '/salir' para terminar la ejecución.
    """
    print("🟢 Iniciando aplicación..")

    config = Config()  # Carga la configuración al iniciar
    model = ModelInterface()  # Inicializa la interfaz del modelo (e.g. OpenAI API, LLM local)
    file_manager = FileManager()  # Gestor de archivos
    parser = CommandParser(file_manager)  # Parser que puede interpretar comandos especiales

    while True:
        entrada = input('\n🟢 <Tú: ')
        if entrada.startswith("/salir"):
            print("🔴 Finalizando aplicación.")
            break

        entrada_procesada = parser.process_text(entrada)
        print(f"\n📥 Prompt procesado:\n{entrada_procesada}\n")

        respuesta = model.prompt(entrada_procesada)
        print(f"🤖 Modelo> {respuesta}\n")

if __name__ == "__main__":
    """
    Ejecuta la función principal si el archivo se ejecuta como script.
    """
    main()
