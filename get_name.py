
def hello(name):
    """
    Pide el nombre del usuario y lo muestra con un saludo personalizado
    """
    print(f"Hola {name} como has estado?")

if __name__ == "__main__":
    n = input("Dime tu nombre: ")
    hello(n)