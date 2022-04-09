from .entities.User import User


class ModelUser():
    @classmethod
    def login(self,mysql,email):#email user

        try:
             cur=mysql.connection.cursor()
             #row 1 2 3 4 ....
         #    sql="""SELECT id, nombre,descripcion,imagen,celular,direccion,email,confi_email,contrasena
             sql="""SELECT id, email,contrasena FROM  clientes  WHERE email = '{}'""".format(email.email)

 #   son ddevueltos como una dupla los cuales puedo acceder utilizando las posiciones
             cur.execute(sql)
             row=cur.fectchone()
             if row  != None:
                 email=User(row[0],row[1],User.check_contra(row[2],email.contrasena,))
                 return email
             else:
                 return None

        except Exception as ex:
            raise Exception(ex) 