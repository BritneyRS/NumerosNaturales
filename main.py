class CalculadoraMCD:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_mcd(self):
        """
        Método para calcular el máximo común divisor (MCD) de dos números enteros.

        :return: Máximo común divisor (MCD) de num1 y num2
        """
        a = self.num1
        b = self.num2
        while b != 0:
            a, b = b, a % b
        return a


# Solicitar entrada al usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD(num1, num2)

# Calcular el MCD utilizando el método de la clase y mostrar el resultado
mcd = calculadora.calcular_mcd()
print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")
