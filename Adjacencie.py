class adjacencie:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __eq__(self, o):
        return  (self.a == o.a and self.b==o.b) or (self.b==o.a and self.a==o.b)
    
    @property
    def to_string(self):
        return self.a+"-"+self.b

    @staticmethod
    def from_string(string:str):
        a,b = string.split("-")
        return adjacencie(a,b)  

    def contains_vertex(self,v):
        return  self.a == v or self.b == v

