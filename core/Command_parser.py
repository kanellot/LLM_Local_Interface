import re
from app.Config import Config
from core.File_manager import FileManager
from app.Xml_Index_Constants import XMLIndexConstants

class CommandParser:
    """
    Clase encargada de detectar, ejecutar y reemplazar comandos especiales embebidos en texto de usuario.

    Los comandos válidos se escriben entre paréntesis, por ejemplo: ("/leer ruta/archivo.txt").

    Comandos soportados:
        - /leer <ruta>: Lee el contenido de un archivo y lo inserta entre prompts pre y post definidos.
        - /listar <ruta>: Lista el contenido de un directorio.

    Atributos:
        fm (FileManager): Instancia encargada de manejar operaciones de archivos y directorios.
        pattern (Pattern): Expresión regular para extraer comandos entre paréntesis.
        c (XMLIndexConstants): Constantes para acceder a claves en los diccionarios de configuración.
    """

    def __init__(self, file_manager: FileManager):
        """
        Inicializa el CommandParser con el gestor de archivos dado.

        Args:
            file_manager (FileManager): Instancia para leer archivos y listar directorios.
        """
        self.fm = file_manager
        self.pattern = re.compile(r'\((.*?)\)')  # Comandos entre paréntesis
        self.c = XMLIndexConstants()

    def extract_commands(self, text: str) -> list[str]:
        """
        Extrae todos los comandos del texto encerrados entre paréntesis.

        Args:
            text (str): Texto de entrada del usuario.

        Returns:
            list[str]: Lista de comandos extraídos.
        """
        return self.pattern.findall(text)

    def execute_command(self, command: str) -> str:
        """
        Ejecuta un comando reconocido y devuelve su resultado textual.

        Args:
            command (str): Comando a ejecutar (ej: "/leer ruta/archivo.txt").

        Returns:
            str: Resultado del comando, o mensaje de error si no se reconoce.
        """
        if command.startswith("/leer "):
            path = command.replace("/leer ", "").strip()
            return (
                '\n' +
                Config.prompt_config.get(self.c.LEER_PRE_PROMPT) + '\n' +
                self.fm.read_file(path) + '\n' +
                Config.prompt_config.get(self.c.LEER_POST_PROMPT)
            )
        elif command.startswith("/listar "):
            path = command.replace("/listar ", "").strip()
            return self.fm.list_directory(path)
        return f"❌ Comando no reconocido: {command}"

    def process_text(self, text: str) -> str:
        """
        Procesa el texto del usuario reemplazando todos los comandos por sus resultados.

        Args:
            text (str): Texto de entrada con posibles comandos entre paréntesis.

        Returns:
            str: Texto final con comandos ejecutados y precedido por reglas/prompt base.
        """
        matches = self.extract_commands(text)
        for cmd in matches:
            result = self.execute_command(cmd)
            text = text.replace(f"({cmd})", result)

        return (
            Config.prompt_config.get(self.c.RULES) + '\n' +
            Config.prompt_config.get(self.c.PRE_PROMPT) + '\n' +
            text
        )
