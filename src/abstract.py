class Base:
    def __init__(self,url:str):
        raise NotImplementedError("Override init method")
    def _prepare_url(self , url:str):
        raise NotImplementedError("Override this method")
