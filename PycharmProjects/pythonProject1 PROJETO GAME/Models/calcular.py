from random import randint

import __nome__


class Calcular:

    def __init__(self: object, dificuldade: int, ) -> __nome__:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resutaldo: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    @property
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'opereção desconhecida '
        return f'valor 1: {self.valor1} \nvalor2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op} '

    @property
    def _gerar_valor(self: object) -> int :
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass

    def checar_resultado(self:object,resposta: int) -> bool:
        pass
    def mostrar_operacao(self: object) -> __nome__ :
        pass

