# Real Estate Scrapper
Project developed in python to scrap and analyze data obtained from real estate websites (i.e. "idealista.com")

---

## How to Use:
Given the property link from "idealista.com" it prints in json format the following data:
- Listing's title
- Property's location
- Price currency
- Price
- Initial price (if the current price is lower than the initial offer)
- Description and comments from the property owner
- Last date when the listing was updated.

### Example Output:
```
  {
    "url": "https://www.idealista.com/inmueble/98776221/",
    "title": "Piso en venta en calle de Juan Bravo, 51",
    "location": "Lista, Madrid",
    "currency": "€",
    "price": 1950000,
    "initialprice": 2150000,
    "description": "Concepto Urbano presenta en exclusiva uno de los pisos más representativos [...]",
    "updated": "18 de diciembre"
  }
```

