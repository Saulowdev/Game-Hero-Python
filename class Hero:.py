class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = input("Qual nome do personagem?")
        self.idade = input("Qual a idade?")
        self.tipo = input("Qual tipo?") 

    def atacar(self):
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

        mensagem = f"O {self.tipo} {self.nome} atacou usando {ataque}"
        print(mensagem)
        

# Exemplos de uso
hero_mago = Hero("Gandalf", 1500, "mago")
hero_guerreiro = Hero("Aragorn", 35, "guerreiro")
hero_monge = Hero("Bruce Lee", 32, "monge")
hero_ninja = Hero("Hattori Hanzo", 40, "ninja")

hero_mago.atacar()
hero_guerreiro.atacar()
hero_monge.atacar()
hero_ninja.atacar()
