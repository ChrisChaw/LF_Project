class BaseResponse(object):
    def __init__(self,):
        self.code = 100
        self.data = None
        self.errors = None

    @property
    def dict(self):
        return self.__dict__