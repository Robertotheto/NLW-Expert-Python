from typing import Dict

class HttpRequest:
    def __init__(
            self, query_params: Dict = None, header: Dict = None, body: Dict = None) -> None:
        self.query_params = query_params
        self.header = header
        self.body = body
