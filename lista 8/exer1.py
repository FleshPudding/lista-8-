import random

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"Animal: {self.nome}")

class Carnivoro(Animal):
    def cacar(self):
        print(f"{self.nome} está caçando!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Este é um animal carnívoro, ele se alimenta exclusivamente da carne de outros animais e não consegue extraír nutrientes de plantas.")

class Herbivoro(Animal):
    def pastar(self):
        print(f"{self.nome} está pastando!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Este é um animal herbívoro, ele se alimenta exclusivamente de plantas e não consegue extraír nutrientes da carne de outros animais.")

class CarnivoroOnivoro(Animal):
    def cacar(self):
        print(f"{self.nome} está caçando!")

    def pastar(self):
        print(f"{self.nome} está procurando por vegetação para complementar sua dieta!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Este é um animal carnívoro-onívoro, ele se alimenta principalmente da carne de outros animais, mas também é capaz de extraír nutrientes de plantas caso necessário.")

class HerbivoroOnivoro(Animal):
    def pastar(self):
        print(f"{self.nome} está pastando!")

    def cacar(self):
        print(f"{self.nome} está caçando pequenas cobras e pássaros!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Este é um animal herbívoro-onívoro, ele se alimenta principalmente de plantas, mas também é capaz de extraír nutrientes da carne de outros animais caso necessário.")

class Onivoro(Carnivoro, Herbivoro):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.cacar()
        else:
            self.pastar()

    def exibirDescricao(self):
        print(f"Animal: {self.nome}")
        print("Este é um animal onívoro, ele se alimenta de carne e plantas em quantidades semelhantes.")

onca = Carnivoro("Onça")
coala = Herbivoro("Coala")
cachorro = CarnivoroOnivoro("Cachorro")
vaca = HerbivoroOnivoro("Vaca")
urso = Onivoro("Urso")

onca.exibirDescricao()
onca.cacar()
print("\n")

coala.exibirDescricao()
coala.pastar()
print("\n")

cachorro.exibirDescricao()
cachorro.cacar()
cachorro.pastar()
print("\n")

vaca.exibirDescricao()
vaca.pastar()
vaca.cacar()
print("\n")

urso.exibirDescricao()
urso.comer()
print("\n")