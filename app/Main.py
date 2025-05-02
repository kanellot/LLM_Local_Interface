from app.Config import Config
from core.Model_interface import ModelInterface
from core.Command_parser import CommandParser
from core.File_manager import FileManager

def main():
    print("🟢 Iniciando aplicación..")
    config = Config()
    model = ModelInterface()
    file_manager = FileManager()
    parser = CommandParser(file_manager)
    #print("m")
    while True:
        entrada = input('\n'+"🟢 <Tú: ")
        if entrada.startswith("/salir"):
            break

        entrada_procesada = parser.process_text(entrada)
        print(f"\n📥 Prompt procesado:\n{entrada_procesada}\n")

        respuesta = model.prompt(entrada_procesada)
        print(f"🤖 Modelo> {respuesta}\n")

if __name__ == "__main__":
    main()
