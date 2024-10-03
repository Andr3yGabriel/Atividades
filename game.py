class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi1.atacar()

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()

heroi3 = Heroi("Bruce", 25, "monge")
heroi3.atacar()

heroi4 = Heroi("Ryu", 28, "ninja")
heroi4.atacar()