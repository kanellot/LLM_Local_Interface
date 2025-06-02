class MessageException(Exception):
    """Excepción personalizada con un mensaje identificable."""
    def __init__(self, msg_id, msg_text):
        super().__init__(msg_text)
        self.msg_id = msg_id


class MessageManager:
    def __init__(self, app_info_msg: dict, app_error_msg: dict):
        self.info_messages = app_info_msg
        self.error_messages = app_error_msg

    def get_info(self, msg_id, **kwargs):
        msg = self.info_messages.get(msg_id, f"[Mensaje info desconocido: {msg_id}]")
        return msg.format(**kwargs)

    def get_error(self, msg_id, **kwargs):
        msg = self.error_messages.get(msg_id, f"[Mensaje error desconocido: {msg_id}]")
        return msg.format(**kwargs)

    def print_info(self, msg_id, **kwargs):
        print(f"[INFO] {self.get_info(msg_id, **kwargs)}")

    def print_error(self, msg_id, **kwargs):
        print(f"[ERROR] {self.get_error(msg_id, **kwargs)}")

    def raise_error(self, msg_id, **kwargs):
        msg = self.get_error(msg_id, **kwargs)
        raise MessageException(msg_id, msg)
