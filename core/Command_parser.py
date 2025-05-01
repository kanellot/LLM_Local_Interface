import re
from core.File_manager import FileManager

class CommandParser:
    def __init__(self, file_manager: FileManager):
        self.fm = file_manager
        self.pattern = re.compile(r'\((.*?)\)')

    def extract_commands(self, text: str) -> list[str]:
        # TODO: Devolver lista de comandos encontrados
        return self.pattern.findall(text)

    def execute_command(self, command: str) -> str:
        # TODO: Interpretar y ejecutar comandos como /leer o /listar
        if command.startswith("/leer "):
            path = command.replace("/leer ", "").strip()
            return self.fm.read_file(path)
        elif command.startswith("/listar "):
            path = command.replace("/listar ", "").strip()
            return self.fm.list_directory(path)
        return f"❌ Comando no reconocido: {command}"

    def process_text(self, text: str) -> str:
        # TODO: Reemplazar comandos en el texto por sus resultados
        matches = self.extract_commands(text)
        for cmd in matches:
            result = self.execute_command(cmd)
            text = text.replace(f"({cmd})", result)
        return text
