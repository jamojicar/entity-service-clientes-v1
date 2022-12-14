# 🛸 Generated by zPy
from zpy.utils import get_env_or_throw as var
from zpy.app.usecase import UseCase
from typing import Any

# * Setup Dependencies 📃
from contexts.customers.domain.repositories import CustomersRepository
from contexts.customers.infraestructure.customers_repository import AwesomeCustomersRepository
from contexts.customers.application.customer_list import customer_list

# Import use case of customers context 📦
from contexts.customers.application.customer_detail import customer_detail

# Import use case of customers context 📦
from contexts.customers.application.customer_add import customer_add

from contexts.customers.application.customer_update import customer_update
from contexts.customers.application.customer_delete import customer_delete

repository: CustomersRepository = AwesomeCustomersRepository()
# Setup UseCases

# Creation instance of use cases of the context: customers 📦
customer_list_uc: UseCase[Any, None] = customer_list(repository)
customer_detail_uc: UseCase[Any, Any] = customer_detail(repository)
customer_add_uc: UseCase[Any, Any] = customer_add(repository)
customer_update_uc: UseCase[Any, Any] = customer_update(repository)
customer_delete_uc: UseCase[Any, Any] = customer_delete(repository)
print("🚀 Dependencies loaded successfully...")





