from contexts.customers.domain.exceptions import InvalidData
import re

class name :
    def __init__(self,value: str) -> None:             
        pattern = '([a-zA-ZÁÉÍÓÚÑñáéíóú\s]+){3,99}'
        result = re.fullmatch(pattern, value,flags=0)
        print(result)
        if result is None:
            raise InvalidData("Debe de contener un nombre válido de mínimo 3 y máximo 99 carácteres","1")
        self.value = value

class email :
    def __init__(self,value: str) -> None:             
        pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        result = re.fullmatch(pattern, value,flags=0)
        print(result)
        if result is None:
            raise InvalidData("Debe de contener un email valido","2")
        self.value = value
class id:
    def __init__(self,value: str) -> None: 
        if value is None:
            raise InvalidData("La propiedad id es requerida","3")
        self.value = value

