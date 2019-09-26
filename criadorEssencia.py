import json

def procurarCategoria(nome):
    file_categorias = open("categorias.json", 'r')
    categorias = json.load(file_categorias)
    return categorias['categorias'][nome]

def criarEssencia(nome, marca, desc, preco_medio, foto, qtd_pacote, categoria):
    file_essencias = open("essencias.json", 'r+', encoding='utf8')
    essencias = json.load(file_essencias)

    nova_essencia = {
        'nome': nome,
        'marca': marca,
        'descricao': desc,
        'preco_medio': preco_medio,
        'foto': foto,
        'qtd_pacote': qtd_pacote,
        'categorias': [procurarCategoria(categoria)]
    }
    essencias['essencias'].append(nova_essencia)
    file_essencias.seek(0)
    file_essencias.truncate()
    json.dump(essencias, file_essencias, ensure_ascii=False)
