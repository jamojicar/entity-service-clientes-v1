# 🛸 Generated by zPy
from ..domain.repositories import CustomersRepository
from ..domain.requests import CustomerRequest
from typing import Any
import json
import uuid

class AwesomeCustomersRepository(CustomersRepository):

    def __init__(self):
        ...

    def customer_list(self, data: Any) -> Any:
        try:
            f = open('data.json')
            data = json.load(f)
            f.close()
            data.reverse()
            customers = {"customers":data}
            return customers
        finally:
            ...

    def customer_detail(self, cus_id: Any) -> Any:
        try:
            f = open('data.json')
            data = json.load(f)
            f.close()
            cus = []            
            for item in data:
                if item['id'] == cus_id:                                   
                    cus.append(item)                    
            customers = {"customers":cus}            
            return customers
        finally:
            ...

    def customer_add(self, cus: CustomerRequest) -> Any:
        try:
            f = open('data.json')
            data = json.load(f)   
            f.close()  
            cusArr = []        
            item = {"id": str(uuid.uuid1()),"name":cus.name,"email":cus.email}
            data.append(item)
            cusArr.append(item)  
            customers = {"customers":cusArr}
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
           
            return customers
        finally:
            ...
    
    def customer_update(self, cus: CustomerRequest) -> Any:
        try:
            f = open('data.json')
            data = json.load(f)               
            f.close()
            for item in data:
                if item['id'] == cus.id:
                   item['name'] = cus.name
                   item['email'] = cus.email                                 
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
           
            return 'ok'
        finally:
            ...

    def customer_delete(self, cus_id) -> Any:
        try:
            f = open('data.json')
            data = json.load(f)               
            f.close()
            for item in data:
                if item['id'] == cus_id:
                  data.remove(item)                                 
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
           
            return 'ok'
        finally:
            ...