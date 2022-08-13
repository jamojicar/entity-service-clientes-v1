# 🛸 Generated by zPy
from abc import abstractmethod
from abc import ABC
from typing import Any


class CustomersRepository(ABC):
    @abstractmethod
    def customer_list(self, data: Any) -> Any:
        """
        Description

        :param data: input data
        :return: result
        """
        ...