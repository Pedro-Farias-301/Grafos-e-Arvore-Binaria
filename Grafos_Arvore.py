class Computador:
    def __init__(self, ip):
        self.ip = ip
        self.esquerdo = None
        self.direito = None


def exibir_arvore_grafica(raiz, nivel=0, prefixo=""):
    if raiz is None:
        return
   
    print(" " * (nivel * 4) + prefixo + f"IP: {raiz.ip}")
   
    exibir_arvore_grafica(raiz.esquerdo, nivel + 1, "├── ")
    exibir_arvore_grafica(raiz.direito, nivel + 1, "└── ")


def inserir_computador(raiz, ip):
    if raiz is None:
        return Computador(ip)
    if ip < raiz.ip:
        raiz.esquerdo = inserir_computador(raiz.esquerdo, ip)
    else:
        raiz.direito = inserir_computador(raiz.direito, ip)
    
    print(f"Árvore após inserir IP {ip}:")
    exibir_arvore_grafica(raiz)
    print()  
    return raiz


def buscar_computador(raiz, ip):
    if raiz is None:
        print(f"IP {ip} não encontrado")
        print("Árvore atual:")
        exibir_arvore_grafica(raiz)
        return "Não encontrado"
    if raiz.ip == ip:
        print(f"Computador encontrado: IP {ip}")
        print("Árvore com IP encontrado:")
        exibir_arvore_grafica(raiz)
        return "Encontrado"
    if ip < raiz.ip:
        return buscar_computador(raiz.esquerdo, ip)
    else:
        return buscar_computador(raiz.direito, ip)


def listar_computadores(raiz):
    if raiz is not None:
        listar_computadores(raiz.esquerdo)
        print(f"Computador com IP: {raiz.ip}")
        listar_computadores(raiz.direito)
    
    print("Árvore completa:")
    exibir_arvore_grafica(raiz)


def main():
    raiz = None
   
    ips = [100, 50, 150, 25, 75]
    for ip in ips:
        print(f"Inserindo IP {ip}...")
        raiz = inserir_computador(raiz, ip)
    
    
    print("\nBuscando IPs...")
    buscar_computador(raiz, 75) 
    buscar_computador(raiz, 99) 
    
    
    print("\nListando todos os computadores...")
    listar_computadores(raiz)

if __name__ == "__main__":
    main()