import requests
def convert_currency(amount, from_currency, to_currency):
    base_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(base_url)
    data = response.json()
    conversion_rate = data['rates'][to_currency] / data['rates'][from_currency]
    converted_amount = amount * conversion_rate
    return round(converted_amount, 2)
print(convert_currency(100,"rupee","dollor"))