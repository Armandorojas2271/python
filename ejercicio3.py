def calcular_imc(peso, altura):
    return peso / altura ** 2

def interpretar_imc(imc):
    return "Bajo peso" if imc < 18.5 else "Normal" if 18.5 <= imc < 24.9 else "Sobrepeso" if 25 <= imc < 29.9 else "Obesidad"

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

resultado_imc = calcular_imc(peso, altura)
categoria_imc = interpretar_imc(resultado_imc)

print(f"\nTu IMC es: {resultado_imc:.2f}")
print(f"Categoría de IMC: {categoria_imc}")