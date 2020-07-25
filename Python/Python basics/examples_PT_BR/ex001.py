nome = input("Qual teu nome? ")
print(nome)
print("Oi {}, seja bem vindo!".format(nome))

#varias entradas de uma vez só

name, age, phone = input("Enter your name, Age, Percentage separated by space: ").split()
print("User Details: ", name, age, phone)