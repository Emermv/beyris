class Api:
    response={"state":False,"message":""}
    db=None
    def __init__(self,db):
        self.db=db
    def set(self,key,value):
        self.response[key]=value
    def toJSON(self):
        return self.response