class ErrorMessages:
    MESSAGES = {
        'es': {
            'file_not_found': "❌ Archivo no encontrado: {path}",
            'read_error': "❌ Error al leer el archivo: {error}",
            'unknown_command': "❌ Comando no reconocido: {command}",
        },
        'en': {
            'file_not_found': "❌ File not found: {path}",
            'read_error': "❌ Error reading file: {error}",
            'unknown_command': "❌ Unknown command: {command}",
        }
    }

    @classmethod
    def get(cls, key: str, lang: str = 'es', **kwargs):
        msg = cls.MESSAGES.get(lang, {}).get(key, f"[{key}]")
        return msg.format(**kwargs)
