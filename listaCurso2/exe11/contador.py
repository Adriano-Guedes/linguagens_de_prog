class Contador:
    def __init__(self, n):
        self.n = n
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual <= self.n:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration
