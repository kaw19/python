def expedidor(linha):
    print(linha)
    
def load_ipython_extension(ipython, *args):
    ipython.register_magic_function(expedidor,'line',"mcm")   # nome: Meu Comando Mágico - mcm

def unload_ipython_extension(ipython):
    pass