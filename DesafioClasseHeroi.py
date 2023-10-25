



class Heroi:

    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago" or self.tipo == "maga":
            ataque = "Usou magia"
        elif self.tipo == "gerreiro" or self.tipo == "gerreira":
            ataque = "Usou espada"
        elif self.tipo == "monge" or self.tipo == "monja":
            ataque = "Usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "Usou shuriken"
        else:
            ataque = "Não atacou."

        mensagem = f"O {self.tipo.capitalize()} atacou usando {ataque}"
        print(mensagem)

heroi1 = Heroi("Dante", 12, "gerreiro")
heroi2 = Heroi("Nero", 27, "monge")
heroi3 = Heroi("Michelly", 78, "maga")
heroi4 = Heroi("Lucas", 18, "ninja")



heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
