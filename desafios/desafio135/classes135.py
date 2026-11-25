from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            ValueError(f"O ano de {ano} é inválido!")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade! Mude o ano de nascimento.")

class Aluno(Pessoa):
    cursosOficiais = ["ADM", "ADS", "CONT", "ENG"]
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursosOficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")

    def adicionarCurso(self, curso):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 5:
            Aluno.cursosOficiais.append(curso)
        if curso in Aluno.cursosOficiais:
            raise ValueError(f"O curso {curso} já está na lista de cursos oficiais.")
        else:
            raise ValueError(f"O nome {curso} está fora do padrão para cursos.")

