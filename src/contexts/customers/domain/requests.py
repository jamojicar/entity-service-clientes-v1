from zpy.utils.objects import ZObjectModel, Str


class CustomerRequest(ZObjectModel):
     id = Str()
     name = Str(required=True)
     email = Str(required=True)
    
     def __init__(self, **kwargs):
          ZObjectModel.__init__(self, use_native_dumps=False, **kwargs)