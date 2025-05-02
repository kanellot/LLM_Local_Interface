import os
from app.ErrorHandler import ErrorHandler


class FileManager:
    """
    Clase responsable de operaciones básicas sobre el sistema de archivos,
    como lectura de archivos de texto y listado de contenido de directorios.
    """

    def read_file(self, path: str) -> str:
        """
        Lee el contenido de un archivo de texto (máximo 3000 caracteres).

        Args:
            path (str): Ruta del archivo a leer.

        Returns:
            str: Contenido del archivo o mensaje de error si la lectura falla.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()[:3000]
        except Exception as e:
            return ErrorHandler.format("FILE_READ_ERROR", error=str(e))

    def list_directory(self, path: str) -> str:
        """
        Lista los nombres de los archivos en el directorio dado.

        Args:
            path (str): Ruta del directorio a listar.

        Returns:
            str: Lista formateada de archivos o mensaje de error si falla.
        """
        try:
            files = os.listdir(path)
            if files:
                return f"[Directorio: {os.path.basename(path)}]({', '.join(files)})"
            return "No hay archivos en el directorio."
        except Exception as e:
            return ErrorHandler.format("DIR_LIST_ERROR", error=str(e))
