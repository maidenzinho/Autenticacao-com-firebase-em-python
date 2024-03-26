import pyrebase

firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL": ""
}

# Inicializa o FireBase
firebase = pyrebase.initialize_app(firebaseConfig)

# API de autenticação do firebase que configuramos
auth = firebase.auth()

user = input("Digite seu email: ")
password = input("Digite sua senha com pelo menos 8 caracteres : ")

if len(password) < 8:
  print("Sua senha precisa de pelo menos 8 caracteres")

esp = '!@#$%&*()'
mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
min = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

var1 = False
for char1 in esp:
 if char1 in password:
  var1 = True

var2 = False
for char2 in mai:
 if char2 in password:
  var2 = True

var3 = False
for char3 in min:
 if char3 in password:
  var3 = True

var4 = False
for char4 in num:
 if char4 in password:
  var4 = True

if (var1 == True and var2 == True and var3 == True and var4 == True):
    status = auth.create_user_with_email_and_password(user, password)
    print(f"Resultado: {status}")

else:
    print(f"Você precisa digita pelo menos uma letra maiúscula, uma minúscula, um número e um caracter especial {esp}")
