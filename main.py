import sqlite3

con = sqlite3.connect("usuarios.db")
cursor = con.cursor()

# CREATE — criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
con.commit()


def criar_usuario(nome, email):
    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )
    con.commit()


def listar_usuarios():
    cursor.execute("SELECT id, nome, email FROM usuarios")
    return cursor.fetchall()


def buscar_usuario(id):
    cursor.execute(
        "SELECT id, nome, email FROM usuarios WHERE id = ?",
        (id,)
    )
    return cursor.fetchone()


def atualizar_usuario(id, nome, email):
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, id)
    )
    con.commit()


def deletar_usuario(id):
    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id,)
    )
    con.commit()


# Exemplos
criar_usuario("João", "joao@email.com")

print("Usuários:", listar_usuarios())

atualizar_usuario(1, "João Silva", "joao.silva@email.com")

print("Usuário:", buscar_usuario(1))

deletar_usuario(1)

print("Depois de excluir:", listar_usuarios())

con.close()
