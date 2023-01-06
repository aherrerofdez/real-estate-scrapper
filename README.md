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
- If it belongs to a housing development or not
- Features such as basic features of the property, the building and its energy certificate

### Example Output*:
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
    "description": "Concepto Urbano presenta en exclusiva uno de los pisos más representativos [...].",
    "updated": "18-12-2022",
    "housingdevelopment": false,
    "features": {
      "Características básicas": [
        "268 m² construidos",
        "4 habitaciones",
        "5 baños",
        "Terraza",
        "Balcón",
        "Plaza de garaje incluida en el precio",
        "Segunda mano/buen estado",
        "Armarios empotrados",
        "Trastero",
        "Calefacción central"
      ],
      "Edificio": [
        "Planta 3ª exterior",
        "Con ascensor"
      ],
      "Equipamiento": [
        "Aire acondicionado"
      ],
      "Certificado energético": [
        "En trámite"
      ]
    },
    "images": {
      "Estancia": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/0d/87/32/1025229898.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/f8/24/ec/1025229989.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/b7/db/03/1025230009.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/57/be/c1/1025230006.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/ea/70/81/1025230034.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/8a/db/2e/1025230018.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/ed/da/8e/1025229991.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/2f/64/ff/1025230023.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/b9/e7/7d/1025230014.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/63/33/f8/1025229981.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/df/07/a7/1025230019.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/07/ae/86/1025229902.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/b9/a7/b3/1025230024.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/ca/df/d7/1025230010.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/ec/21/28/1025229901.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/3a/25/67/1025230029.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/74/ae/97/1025230016.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/3d/5e/ee/1025230013.jpg"
      ],
      "Foto": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/58/55/d6/1025230000.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/a0/10/e8/1025229900.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/6b/34/71/1025230002.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/de/b2/91/1025229982.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/02/8f/bc/1025230015.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/c0/d5/96/1025230028.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/33/6d/2f/1025229980.jpg"
      ],
      "Baño": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/2a/be/81/1025230026.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/26/fe/16/1025230008.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/6f/12/15/1025230017.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/b5/e5/c8/1025230012.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/99/2e/3c/1025230011.jpg"
      ],
      "Pasillo": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/3c/55/2e/1025230020.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/1b/e4/79/1025230027.jpg"
      ],
      "Cocina": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/1c/7d/41/1025230033.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/55/63/4e/1025229979.jpg"
      ],
      "Terraza": [
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/1e/c8/8d/1025229992.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/1f/d1/41/1025230025.jpg",
        "https://img3.idealista.com/blur/WEB_DETAIL/0/id.pro.es.image.master/dc/0b/27/1025229899.jpg"
      ]
    },
    "plans": []
  }
```

*This example has no floor plan available in the listing. Therefore, it is empty. However, if the listing has a floor plan available, a link to the image is added, similarly to the images.