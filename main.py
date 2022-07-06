from Classes.domain.pessoa import Pessoa
from Classes.domain.estadocivil import EstadoCivil
from datetime import date

if __name__ == '__main__':
    p = Pessoa('Ronaldo', EstadoCivil.SOLTEIRO, date(1997, 3, 29))

    print(p.get_idade())

