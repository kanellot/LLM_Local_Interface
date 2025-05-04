from app.Config import Config
from app.MessageManager import MessageManager
from core.Command_parser import CommandParser
from core.File_manager import FileManager
from core.Model_interface import ModelInterface


def main():
    print("🟢 Iniciando aplicación..")

    conf = Config()
    mm = MessageManager(conf.app_info_msg, conf.app_error_msg)
    model = ModelInterface(conf.model_config, mm)
    file_manager = FileManager(mm)
    parser = CommandParser(file_manager, conf.prompt_config, mm)

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
