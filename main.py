from engine import askForCurrency, collectAmount, convertCurrency
import time as t

print("Welcome to the KurrencKonvrtr:\n")

t.sleep(1)

baseCurrency = askForCurrency("base")

print()
targetCurrency =  askForCurrency("target")

print()
amount = collectAmount(baseCurrency, targetCurrency)



result = round(convertCurrency(baseCurrency, targetCurrency, amount), 4)
print()
print(f"{baseCurrency}{amount} = {targetCurrency}{result}")
