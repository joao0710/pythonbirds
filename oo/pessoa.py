class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome, idade=25):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 42


    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass



if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    print(Homem.cumprimentar(luciano))
    print(id(luciano))
    for filhos in luciano.filhos:
        print(f'São filhos de {luciano.nome}: {filhos.nome}')

    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)
    del luciano.sobrenome
    print(luciano.__dict__)
    print(renzo.__dict__)

    print(Homem.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    luciano.olhos = 1
    print(luciano.__dict__)
    print(renzo.__dict__)

    print(Homem.metodo_estatico(), luciano.metodo_estatico())
    print(Homem.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

