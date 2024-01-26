baseDatos={} 

#Funcion que registra user

def registrarUser(db):
  nombre= input("Ingrese su nombre: ")
  contrasena= input("Ingrese su contrasena: ")

  baseDatos[nombre]= contrasena

  #Funcion que realiza registro
registrarUser(baseDatos)
print(baseDatos)

#Funcion que imprime los elementos de la lista
def mostrarLista(baseDatos):
  print(f"Los elementos registrados hasta el momento son: {baseDatos}" )

mostrarLista(baseDatos)

#Funcion que verifica que la contrasena de un user es correcta

def funcionLog(baseDatos):
  clave_buscada= input("ingrese su nombre de usuario: ")

  if clave_buscada in baseDatos:
    if baseDatos[clave_buscada] == input("Ingrese su contrasena: "):
      print("Has iniciado sesion")
    else:
      print("Contrasena Incorrecta")

funcionLog(baseDatos)

#Conectar Drive
#from google.colab import drive
#drive.mount('/content/drive')

#%cd '/content/drive/MyDrive/CoderHouse/Python/ArchivosTxt'
#!ls

#Generar TXT en drive con el diccionario

def almacenarBD(baseDatos):
  file = open("./archivo.txt","w")
  #convierto el diccionario en string para poder guardarlo en el txt
  baseSt= str(baseDatos)
  file.write(baseSt)
  file.close()

almacenarBD(baseDatos)

#Donde se crea el archivo
#https://drive.google.com/drive/folders/1fePMsvl_IKg8Ajc4R5B6A_Z8rvD8KG-n?usp=sharing