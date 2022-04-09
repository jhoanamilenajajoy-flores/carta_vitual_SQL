from werkzeug.security import check_password_hash, generate_password_hash

#self para hacer refercia al propio objeto

class User():
    def _init_(self,id, email,contrasena) -> None:    
  #  def _init_(self,id, nombre, descripcion, imagen, celular, direccion,email, confi_email, contrasena) -> None:
        self.id =id
     #   self.nombre=nombre
    #    self.descripcion=descripcion
      #  self.imagen=imagen
      #  self.celular=celular
       # self.direccion=direccion
        self.email=email
       # self.confi_email=confi_email
        self.contrasena=contrasena

    @classmethod
    def check_contra(self,hashed_password,contrasena):
        return check_password_hash(hashed_password, contrasena)

print(generate_password_hash("12345"))