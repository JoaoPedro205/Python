class Produto():
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip(): 
            self.__nome = nome
        else:
            print("Nome inválido!")

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco > 0:  
            self.__preco = preco
        else:
            print("Preço inválido!")

produto = Produto("Caneta", 10.0)

print(f"Produto: {produto.get_nome()}")
print(f"Preço: R${produto.get_preco():.2f}")

produto.set_nome("Camiseta Polo")
produto.set_preco(60.0)

print(f"Novo produto: {produto.get_nome()}")
print(f"Novo preço: R${produto.get_preco():.2f}")

produto.set_nome("")  
produto.set_preco(-10) 