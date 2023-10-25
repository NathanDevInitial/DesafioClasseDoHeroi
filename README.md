# DesafioClasseDoHeroi
Desafio Classe do Heroi


```
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
```


Neste trecho, uma classe chamada Heroi é definida. A classe tem um construtor __init__ que é chamado quando um objeto Heroi é criado. O construtor aceita três parâmetros: nome, idade e tipo. Esses parâmetros são usados para inicializar as propriedades da classe.


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
            ataque = "não possui ataque definido"

        mensagem = f"O {self.tipo.capitalize()} atacou usando {ataque}"
        print(mensagem)

Neste trecho, é definido o método atacar na classe Heroi. O método verifica o valor da propriedade tipo do herói e, com base nesse tipo, atribui uma descrição de ataque correspondente. A primeira letra do tipo é convertida para maiúscula usando .capitalize(). A mensagem resultante é impressa na tela.

# Exemplo de uso:
    heroi1 = Heroi("Dante", 12, "gerreiro")
    heroi2 = Heroi("Nero", 27, "monge")
    heroi3 = Heroi("Michelly", 78, "maga")
    heroi4 = Heroi("Lucas", 18, "ninja")
    
    heroi1.atacar()
    heroi2.atacar()
    heroi3.atacar()
    heroi4.atacar()

Neste trecho, são criados quatro objetos Heroi com diferentes propriedades (nome, idade e tipo) e, em seguida, o método atacar é chamado para cada um desses heróis. Isso demonstra como a classe Heroi pode ser usada para criar heróis com diferentes tipos e executar ataques baseados em seus tipos.

# Resumo
Esse código Python cria uma classe Heroi que representa heróis de uma aventura, com a capacidade de atacar com base em seus tipos. A primeira letra do tipo é capitalizada na mensagem de ataque para uma exibição mais legível. 

# Observações:
Este código é um exemplo simples de orientação a objetos e controle de fluxo em Python.
