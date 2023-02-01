# Cotação de moedas
import httpx
from lista import moedas

print(f"{moedas}\n")

base_currency = input("Digite a moeda de base: ").upper()
currency = input("Digite a moeda desejada: ").upper()

# BUSCA VALORES DE MOEDAS NA API PUBLICA
response = httpx.get(
    url=f'https://api.exchangerate.host/latest?base={base_currency}'
).json()

currency_data = response['rates']

print(f'1 {base_currency} vale {currency_data.get(currency)} {currency}')

