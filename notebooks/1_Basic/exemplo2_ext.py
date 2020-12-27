import requests as req

def despachador(linha):
    partes = linha.strip().split(' ')
    if len(partes) == 2 and partes[0] in ('GET','DELETE'):
        verbo, uri = partes
        if verbo == 'GET':
            return req.get(uri)
        elif verbo == 'DELETE':
            return req.delete(uri)
    elif len(partes) > 2 and partes[0] in ('GET', 'PUT', 'POST'):
        verbo = partes[0]
        uri = partes[1]
        cargautil = json.loads(" ".join(partes[2:]))
        if verbo == 'GET':
            return req.get(uri, params=cargautil)
        elif verbo == 'PUT':
            return req.put(uri, json=cargautil)
        elif verbo == 'POST':
            return req.post(uri, json=cargautil)        
    else:
        print(""" Uso:\n \
        %http GET <url>\n \
        %http DELETE <url>\n \
              Requisições HTTP GET/DELETE a uma <url>.\n \
        \n \
        %http GET <url> <parâmetros de consulta json>\n \
              Requisição HTTP GET a uma <url> e JSON será usado para criar string de consulta.\n \
        %http PUT <url> <json>\n \
        %http POST <url> <json>\n \
              Requisições HTTP PUT/POST a uma <url>, <json> será enviado como carga útil JSON.""")
    
def load_ipython_extension(ipython, *args):
    ipython.register_magic_function(despachador,'line',"http")

def unload_ipython_extension(ipython):
    pass