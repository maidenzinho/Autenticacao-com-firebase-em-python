# Autenticação com FireBase em Python
# Importar pyrebase no PyCharm:

### Settings

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003553.png">

### Pesquise "interpreter">Clique em "python interpreter">Clique em "+"

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003559.png">

### Pesquise "pyrebase4" e instale-o

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003606.png?raw=true">

### Agora é só fechar e clicar em "OK"

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003613.png">

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003619.png">

### Colocar seus dados do Firebase como nos passos abaixo:

### 1 - abra firebase.google.com e entre em sua conta!

### 2 - Crie seu projeto

<img src="https://github.com/maidenzinho/Autenticacao-com-firebase-em-python/blob/main/Captura%20de%20tela%202024-03-26%20000133.png">

### 3 - Crie um projeto

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000144.png">

### 4 - Dê o nome

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000156.png">

### 5 - Desmarque o Google Analytics

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000208.png">

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000305.png">

### 6 - Selecione Web APP

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000313.png">

### 7 - Dê o nome

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000321.png">

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000343.png">

### 8 - Copie esse código e substitua pelos seus dados do Firebase

```
firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL": ""
}
```

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20003628.png">

### 9 - Selecione "Authentication"

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000402.png">

### 10 - Selecione Email/Senha

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000416.png">

### 11 - Ative a opção Email/Senha

<img src="https://github.com/maidenzinho/imagens/blob/main/Captura%20de%20tela%202024-03-26%20000423.png">

### 12 - Copie o código que está no repositório ou abaixo

```
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
```
