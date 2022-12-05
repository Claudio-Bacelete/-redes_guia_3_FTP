from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Press the green button in the gutter to run the script.
authorizer = DummyAuthorizer()
authorizer.add_user("teste", "1234", 'C:/Users/chcbe/Desktop/Puc Minas/Projetos/Java/redes_guia_3/src/main/java/com/redes/redes/Logs')
authorizer.add_anonymous('C:/Users/chcbe/Desktop/Puc Minas/Projetos/Java/redes_guia_3/src/main/java/com/redes/redes/Logs')
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()