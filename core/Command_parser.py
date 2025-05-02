import re
from app.Config import Config
from core.File_manager import FileManager

class CommandParser:
    def __init__(self, file_manager: FileManager):
        self.fm = file_manager
        self.pattern = re.compile(r'\((.*?)\)')

    # Extract command from prompt
    def extract_commands(self, text: str) -> list[str]:
        return self.pattern.findall(text)

    # Execute command and return the result
    def execute_command(self, command: str) -> str:
        if command.startswith("/leer "):
            path = command.replace("/leer ", "").strip()
            return  '\n'+Config.prompt_config.get("leer_pre_prompt") +'\n'+ self.fm.read_file(path) + '\n'+Config.prompt_config.get("leer_post_prompt")
        elif command.startswith("/listar "):
            path = command.replace("/listar ", "").strip()
            return self.fm.list_directory(path)
        return f"❌ Comando no reconocido: {command}"

    # Replace every command with the result
    def process_text(self, text: str) -> str:
        matches = self.extract_commands(text)
        for cmd in matches:
            result = self.execute_command(cmd)
            text = text.replace(f"({cmd})", result)
        return Config.prompt_config.get("rules")+'\n'+Config.prompt_config.get("pre_prompt")+'\n'+text

