# Real Estate Scrapper
Project developed in python to scrap and analyze data obtained from real estate websites (i.e. "idealista.com").

### Important Note:
The code currently assumes that the links for the properties provided are in Spanish.
The python version used is 3.10.5.

### Requirements:
- httpx: the version used is 0.23.2 -->
```pip install httpx```

- parsel: the version used is 1.7.0 -->
```pip install parsel```

---

## How to Use:
Given the property link from "idealista.com" it prints in json format the following data:
- Listing's title
- Property's location, divided into city and zone
- Price and currency
- Initial price (if the current price is lower than the initial offer) and percentage difference between initial price and current price
- Description and comments from the property owner
- Last date when the listing was updated, in the format of "DD-MM-YYYY"
- If it belongs to a housing development or not.

### Example Output:
```
  {
    "url": "https://www.idealista.com/inmueble/98776221/",
    "title": "Piso en venta en calle de Juan Bravo, 51",
    "location": {
      "city": "Madrid",
      "zone": "Lista"
    },
    "currency": "€",
    "price": 1950000,
    "initialprice": 2150000,
    "downpercentage": "9%",
    "description": "Concepto Urbano presenta en exclusiva uno de los pisos más representativos [...]",
    "updated": "18-12-2022",
    "housingdevelopment": false
  }
```

