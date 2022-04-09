#from crypt import methods
from tkinter import messagebox
from pydoc import describe
from flask import Flask, render_template, request, redirect,flash
from flask_mysqldb import MySQL 
from config import config

#import mysql.connector, hashlib
from smtplib import SMTP
#from email.message import EmailMessage
from models.ModelUser import ModelUser

from models.entities.User import User
app = Flask(__name__)   
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_PORT']=3306
app.config['MYSQL_DB']='carta_virtual'
mysql = MySQL(app)

#video

# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         print(request.form)


#mio
@app.get("/")
def inicio():
    return render_template("index.html")

@app.route('/add_contact',  methods=['GET','POST'])
def add_contact():
    if request.method == 'POST':
        '''
       # cur = mysql.connection.cursor()
        user=User(0,request.form['email'],request.form['contrasena'])
       #user=User(0,request.form['nombre'],request.form['descripcion'],request.form['imagen'],request.form['celular'],request.form['direccion'],request.form['email'], request.form['confi_email'],request.form['contrasena'])
        logged_user =ModelUser.login(mysql,user)
        if logged_user != None:
            if logged_user.password:
                flash("acep")
                return render_template('iniciar_sesion.html')
            #  return redirect(url_for('home'))
            else:
                flash("inalid password...")
                return render_template('iniciar_sesion.html')
        else:
            flash("user no found")  
            return render_template('iniciar_sesion.html')
    else:
        return render_template('iniciar_sesion.html')
        '''
    nombre= request.form['nombre']
    descripcion=request.form['descripcion']
    imagen=request.form['imagen']
    celular=request.form['celular']
    direccion=request.form['direccion']
    email= request.form['email']
    confi_email= request.form['confi_email']
    contrasena= request.form['contrasena']
    
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO clientes (nombre,descripcion,imagen,celular,direccion,email,confi_email,contrasena) VALUES( %s, %s,%s,%s,%s,%s,%s )',
    (nombre, descripcion,imagen,celular,direccion,email,confi_email,contrasena))
    mysql.connection.commit()
    
    # messagebox.showinfo(message="El usuario ha sido registrado correctamente", title="Título")
# @app.route('/home')
# def home(): 
#     return render_template('home.html')
# def guardar(nombre,email,email2,contra,descripcion):
#     print(nombre)
#     print(email)
#     print(confi_email)
#     return 'received'

# def guardar(nombre,email,email2,contra,imagen):
#     print(nombre)
#     print(email)
#     #print(email2)
#     print(contra)
#     print(imagen)
    

#     contra_Encripted = hashlib.sha256(contra.encode())
#     print(contra_Encripted.hexdigest())
#     cursor.execute("INSERT INTO clientes(nombre,email,contraseña,imagen) VALUES (%s,%s,%s,%s)",(nombre,email,str(contra_Encripted.hexdigest(),imagen)))
#     db.commit()
#     cursor.close()
#     flash("Correo no concuerda")
        

# def buscar_usuario(nombre):
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM `clientes` WHERE email=%s"),(nombre)
#     usuario=cursor.fetchall()
#     return usuario
# def buscar_contra(contra):
#     contra_Encripted = hashlib.sha256(contra.encode())
#     print(contra_Encripted.hexdigest())
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM `clientes` WHERE contrasena=%s"),(str(contra_Encripted.hexdigest()))
#     contras = cursor.fetchall()
#     return contras


# app = Flask(__name__, template_folder = './templates' , static_folder = './templates' )
# app.secret_key="jhon"
# @app.get("/")
# def inicio():
#     return render_template("index.html")

# @app.post("/registro")
# def registro():
#    data=request.form
#    if data["email"]==data["email2"]:
#        msg = EmailMessage()
#        msg.set_content('Verificacion correo')
#        msg['Subject'] = 'Su cuenta se ha creado con exito'
#        msg['From'] = 'juanpuentes2020@itp.edu.co'
#        msg['To'] = data["email"]

#        username = 'juanpuentes2020@itp.edu.co'
#        password = '1002462375'

#        server = SMTP('smtp.gmail.com:587')
#        server.starttls()
#        server.login(username, password)
#        server.send_message(msg)
#        server.quit()

#        guardar(
#            nombre=data["nombre"],
#            email=data["email"],
#            email2=data["email2"],
#            contra=data["contra"],
#            imagen=data["imagen"])
           
#    else:
#        flash("es incorrecto")
#        print("es incorrecto")


#    return redirect("/ingreso")


# @app.route("/ingreso",methods=['GET','POST'])
# def ingreso():
#     return render_template("iniciar_sesion.html")

# app.route("/ingreso",methods=['GET','POST'])
# def inicios():
#     dato = request.form

#     user=buscar_usuario(
#         nombre=dato["usuario"]
#        )
#     contra=buscar_contra( contra=dato["contras"])

# if __name__== '_main_':
#     app.config.from_object(config['development'])
#     app.run(debug=True)


app.run(debug=True)
