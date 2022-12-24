import json


with open("jsonFile.json", 'r') as jf:
    ratesTable = json.load(jf)



def askForCurrency(kind):
    currency =  input(f"Enter the 3 letter symbol of your {kind} currency\n eg. GHS for Ghana Cedis: ").upper()

    currencyFound = currency in ratesTable.keys()

    while currencyFound == False:
        print(f"\n\nSorry! {currency} not found...\nTry again.")
        currency =  input(f"\nEnter the 3 letter symbol of your {kind} currency\n eg. GHS for Ghana Cedis: ").upper()

        if currency in ratesTable.keys():
            currencyFound = True

        

    return currency

# baseCurrency = askForCurrency("base")
# print()
# targetCurrency =  askForCurrency("target")




def collectAmount(baseCurrency, targetCurrency):
    amount = input(f"How many {baseCurrency}s do you want to convert to {targetCurrency}: ")



    amountIsValid = isaNumber(amount)

    while amountIsValid == False:
        
        print(f"{amount} is not a number!\nTry again...\n")

        amount = input(f"How many {baseCurrency}s do you want to convert to {targetCurrency}: ")

        if isaNumber(amount):
            amountIsValid = True
        
    return amount


# amount = collectAmount(baseCurrency, targetCurrency)



def convertCurrency(baseCurrency, targetCurrency, amount):
    baseCurrency = float(ratesTable[baseCurrency])
    targetCurrency = float(ratesTable[targetCurrency])
    amount = float(amount)
 
    rateOfConvertion = targetCurrency / baseCurrency

    convertedAmount = amount * rateOfConvertion

    return convertedAmount

# result = round(convertCurrency(baseCurrency, targetCurrency, amount), 4)

# print(f"{baseCurrency}{amount} = {targetCurrency}{result}")



def isaNumber(something):
    verdict = True;

    for i in something:
        if i.isdigit():
            verdict = True
        else:
            verdict = False
            break
    return verdict
    