from transportes import *

def main():
    distancia = 8
    entrega = Drone(distancia)
    print(f"Frete de {type(entrega).__name__} em {distancia} Km = {entrega.calcularFrete()}")

if __name__ == "__main__":
    main()