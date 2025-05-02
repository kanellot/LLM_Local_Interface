# app/ErrorHandler.py
from app.ErrorMessages import ErrorMessages


class ErrorHandler:
    current_language = 'es'  # valor por defecto

    @classmethod
    def set_language(cls, lang: str):
        if lang in ErrorMessages.MESSAGES:
            cls.current_language = lang

    @classmethod
    def get_error(cls, key: str, **kwargs):
        return ErrorMessages.get(key, lang=cls.current_language, **kwargs)
