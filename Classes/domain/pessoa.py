from Classes.estadocivil import EstadoCivil
from datetime import date


class Pessoa:

    def __init__(self, nome, est_civil, data_nascimento):
        self.nome = nome
        self.est_civil = est_civil
        self.data_nascimento = data_nascimento

    def atualizar_estado_civil(self, novo_est_civil):
        if novo_est_civil == EstadoCivil.CASADO:
            desejo_casar = input("Tem certeza que deseja casar? S/N")
            if desejo_casar == "S":
                self.est_civil = novo_est_civil
        else:
            self.est_civil = novo_est_civil

    def get_idade(self):
        dias_no_ano = 365.2425
        idade = int((date.today() - self.data_nascimento).days / dias_no_ano)
        return idade
