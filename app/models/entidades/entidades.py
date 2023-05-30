import json

class feriados():

    def __init__(self, codigo=None, data=None, nome_feriado=None):
        self.codigo = codigo
        self.data = data
        self.nome_feriado= nome_feriado

    @classmethod
    def from_Json(cls, nome_feriado):
        to_dict = json.loads(nome_feriado)
        return cls(**to_dict)

