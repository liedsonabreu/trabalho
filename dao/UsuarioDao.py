from model.Usuario import Usuario

class UsuarioDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarUsuarios(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM usuario'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            usuario = Usuario()
            usuario.id = item[0]
            usuario.nome = item[1]
            usuario.email = item[2]
            usuario.senha = item[3]

            lista.append(usuario)

        return lista

    def inserirUsuario(self, usuario: Usuario) -> Usuario:
        c = self.connection.cursor()
        sql = 'INSERT INTO usuario(nome, email, senha) VALUES (%s, %s, %s) RETURNING id'
        c.execute(sql, [usuario.nome, usuario.email, usuario.senha])
        usuario.id = c.fetchone()[0]
        self.connection.commit()

        return usuario

    def alterarUsuario(self, usuario: Usuario) -> Usuario:        
        c = self.connection.cursor()         
        sql = 'UPDATE usuario SET nome = %(nome)s, email = %(email)s, senha = %(senha)s WHERE id = %(some_id)s'        
        c.execute(sql, {
            'nome': usuario.nome, 
            'email': usuario.email, 
            'senha': usuario.senha, 
            'some_id': usuario.id
        })
        self.connection.commit()
        
        return usuario

   
    def excluirUsuario(self, id: int) -> Usuario:
        c = self.connection.cursor()
        sql = 'DELETE FROM usuario WHERE id = %s'
        c.execute(sql,[id])
        self.connection.commit()


#Liedson C. Abreu e Henrique da S. Pontes