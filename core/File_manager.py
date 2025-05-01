import os

class FileManager:
    def read_file(self, path: str) -> str:
        # TODO: Leer archivo desde el sistema y retornar contenido limitado
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()[:3000]
        except Exception as e:
            return f"❌ Error leyendo archivo: {e}"

    def list_directory(self, path: str) -> str:
        # TODO: Listar archivos en un directorio dado
        try:
            files = os.listdir(path)
            if files:
                return f"[Directorio: {os.path.basename(path)}]({', '.join(files)})"
            return "No hay archivos en el directorio."
        except Exception as e:
            return f"❌ Error listando archivos: {e}"
