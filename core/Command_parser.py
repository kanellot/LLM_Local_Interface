import re

from app.Xml_Index_Constants import XMLIndexConstants
from core.File_manager import FileManager


class CommandParser:

    def __init__(self, file_manager: FileManager, prompt_config: dict, constants: XMLIndexConstants):

        self.fm = file_manager
        self.prompt_config = prompt_config
        self.constants = constants
        self.pattern = re.compile(r'\((.*?)\)')  # Comandos entre paréntesis

    def extract_commands(self, text: str) -> list[str]:

        return self.pattern.findall(text)

    def execute_command(self, command: str) -> str:

        if command.startswith("/leer "):
            path = command.replace("/leer ", "").strip()
            return (
                    '\n' +
                    self.prompt_config.get(self.constants.LEER_PRE_PROMPT) + '\n' +
                    self.fm.read_file(path) + '\n' +
                    self.prompt_config.get(self.constants.LEER_POST_PROMPT)
            )
        elif command.startswith("/listar "):
            path = command.replace("/listar ", "").strip()
            return self.fm.list_directory(path)
        return f"❌ Comando no reconocido: {command}"

    def process_text(self, text: str) -> str:

        matches = self.extract_commands(text)
        for cmd in matches:
            result = self.execute_command(cmd)
            text = text.replace(f"({cmd})", result)

        return (
                self.prompt_config.get(self.constants.RULES) + '\n' +
                self.prompt_config.get(self.constants.PRE_PROMPT) + '\n' +
                text
        )
