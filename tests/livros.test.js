test("2 + 3 deve resultar em 5", () => {
    expect(2 + 3).toBe(5);
});

const { adicionarLivro } = require("../js/livros");

test("deve adicionar um livro à coleção", () => {
    const livros = [];

    const livro = {
        id: 1,
        titulo: "JavaScript",
        autor: "Autor",
        genero: "Programação",
        paginas: 300,
        lido: false
    };

    const resultado = adicionarLivro(livros, livro);

    expect(resultado).toHaveLength(1);
    expect(resultado[0]).toEqual(livro);
}); 