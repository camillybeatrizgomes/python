from poligono import Poligono
from quadrado import Quadrado
from circulo import Circulo
from rich import print

def main():
    q = Quadrado(20)
    print(f"Um quadrado de lado {q.lado}cm tem perímetro de {q.perimetro()}cm")
    print(f"Um quadrado de lado {q.lado}cm tem área de {q.area()}cm²")

    c = Circulo(12)
    print(f"Um círculo de raio {c.raio}cm tem perímetro de {c.perimetro():.1f}cm")
    print(f"Um círculo de raio {c.raio}cm tem área de {c.area():.1f}cm²")

if __name__ == "__main__":
    main()

