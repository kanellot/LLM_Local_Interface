import os

class FileManager:
    def read_file(self, path: str) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()[:3000]
        except Exception as e:
            return f"❌ Error leyendo archivo: {e}"

    def list_directory(self, path: str) -> str:
        try:
            files = os.listdir(path)
            if files:
                return f"[Directorio: {os.path.basename(path)}]({', '.join(files)})"
            return "No hay archivos en el directorio."
        except Exception as e:
            return f"❌ Error listando archivos: {e}"
