def calcular(numero1, operador, numero2):
	"""Realiza una operacion basica y devuelve el resultado."""
	if operador == "+":
		return numero1 + numero2
	if operador == "-":
		return numero1 - numero2
	if operador == "*":
		return numero1 * numero2
	if operador == "/":
		if numero2 == 0:
			raise ValueError("No se puede dividir entre cero.")
		return numero1 / numero2
	raise ValueError("Operador no valido.")


def main():
	print("Calculadora basica")
	print("Operaciones disponibles: +, -, *, /")
	print("Escribe 'salir' como operador para terminar.")

	while True:
		try:
			entrada = input("Primer numero: ").strip()
			if entrada.lower() == "salir":
				print("Hasta luego.")
				break

			numero1 = float(entrada)
			operador = input("Operacion: ").strip()

			if operador.lower() == "salir":
				print("Hasta luego.")
				break

			numero2 = float(input("Segundo numero: "))
			resultado = calcular(numero1, operador, numero2)
			print(f"Resultado: {resultado:g}")
		except ValueError as error:
			print(f"Error: {error}")


if __name__ == "__main__":
	main()
