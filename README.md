# real-estate-scrapper
Project developed in python to scrap and analyze data obtained from real estate websites.

## How to Use:
Given the property link from "idealista.com" it prints in json format the following data: title, location, currency, price, initial price (if the current price is lower than the initial offer), description and date of update.

Example Output:
{
    "url": "https://www.idealista.com/inmueble/98776221/",
    "title": "Piso en venta en calle de Juan Bravo, 51",
    "location": "Lista, Madrid",
    "currency": "€",
    "price": 1950000,
    "pricedown": 2150000,
    "description": "Concepto Urbano presenta en exclusiva uno de los pisos más representativos actualmente disponibles en el prestigioso Barrio de Salamanca de Madrid./nSe trata de una vivienda exterior, en perfecto estado de conservación, ubicada en la tercera planta de un magnífico edificio situado en la milla de oro de la calle Juan Bravo de Madrid [...]",
    "updated": "18 de diciembre"
  }

