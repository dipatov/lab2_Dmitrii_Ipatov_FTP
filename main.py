from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import logging

authorizer = DummyAuthorizer()
authorizer.add_user('admin', '00000', 'FTP', perm="elradfmwMT")
authorizer.add_user('dmitriip99', 'qwerty', 'FTP/dmitriip99', perm="elradfmwMT")
authorizer.add_user('not_dima', 'ytrewq', 'FTP/not_dima', perm="elradfmwMT")
authorizer.add_user('dummy', '12345', 'FTP/dummy', perm="elradfmwMT")
authorizer.add_anonymous('FTP/anon', perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'Welcome to FTP-server'
handler.passive_ports = range(60000, 65535)
handler.active_dtp
handler.timeout = 600
handler.log_prefix = 'XXX [%(username)s]@%(remote_ip)s'
logging.basicConfig(level=logging.INFO)

server = ThreadedFTPServer(('141.8.151.149', '41234'), handler)
server.max_cons = 50
server.max_cons_per_ip = 5
server.serve_forever()
