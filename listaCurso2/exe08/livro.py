class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        print(f"O livro {self.titulo} do autor {self.autor} tem {self.paginas} páginas")

    def __len__(self):
        return self.paginas