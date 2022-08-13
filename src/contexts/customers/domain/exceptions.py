class InvalidData(Exception):
    
    def __init__(self, message: str,code: str,*args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.code = code
