class Categoria:

    def __init__(self, codigo, nome, descricao):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao


class Essencia:

    def __init__(self, codigo, nome, marca, preco_medio, descricao, foto, quantidade_pacote, categorias):
        self.codigo = codigo
        self.nome = nome
        self.marca = marca
        self.preco_medio = preco_medio
        self.descricao = descricao
        self.foto = foto
        self.quantidade_pacote = quantidade_pacote
        self.categorias = categorias


class Mistura:

    def __init__(self, codigo, nome, descricao, essencia_1, essencia_2, porcentagem_1, porcentagem_2, categorias):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.categorias = categorias
        self.essencia_1 = essencia_1
        self.essencia_2 = essencia_2
        self.porcentagem_1 = porcentagem_1
        self.porcentagem_2 = porcentagem_2