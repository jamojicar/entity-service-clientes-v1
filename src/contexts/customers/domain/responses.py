from marshmallow.fields import Dict, Integer
from marshmallow_objects import NestedModel
from zpy.api.http.response import SuccessResponse
from zpy.api.http.status_codes import HttpStatus
from zpy.utils.objects import ZObjectModel, Str


class Customer(ZObjectModel):
    id = Str()
    name = Str()
    email =Str()

class CustomersResponse(ZObjectModel, SuccessResponse):
    customers = NestedModel(nested=Customer, many=True, load_default=[]) 

    def __init__(self, **kwargs):
        ZObjectModel.__init__(self, use_native_dumps=True, **kwargs)
        SuccessResponse.__init__(self, HttpStatus.SUCCESS) 

