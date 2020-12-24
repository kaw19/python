def printCrescente(n):       # imprime de '1' a 'n'
    for i in range(n):
        print(i+1, end=", ")
    print("\b\b.")

def printDecrescente(n):     # imprime de 'n' a '1'
    for i in range(n):
        print(n-i, end=", ")
    print("\b\b.")