import json
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age= age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' isnotJSON serializable')
    
some_man= Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who)) # Default es la función que se utiliza para 'serializar' el objeto