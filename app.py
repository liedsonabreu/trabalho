from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.Table import Table

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)

usuario = Usuario()
usuario.nome  ='José'
usuario.email = 'email@teste.com.br'
usuario.senha = 'senha'
print(dao.inserirUsuario(usuario))

usuario = Usuario()
usuario.id = 25
usuario.nome = 'Tião'
usuario.email = 'jose@teste.com.br'
usuario.senha = 'jose123'
print(dao.alterarUsuario(usuario))

usuario = Usuario()
print(dao.excluirUsuario(usuario))

# lista = dao.selecionarUsuarios()
# tela = Table(lista)
