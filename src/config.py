from distutils.command.config import config
from distutils.debug import DEBUG


class Config:
    SECRET_KEY ="mile"#llave privada nos sirve para manejar datos de sesion.. envio de mensajes 

#conexion base de datos
class DevelopmentConfig(Config):#clas e heredada
    DEBUG =True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_PORT=3306
    MYSQL_DB='carta_virtual'

config={
    'development': DevelopmentConfig
}