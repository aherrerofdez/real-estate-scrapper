import httpx
import asyncio
import json
import re

from parsel import Selector
from typing import Dict, List
from typing_extensions import TypedDict
from datetime import date


# -------------------------------------------------
# Property Data
# -------------------------------------------------

# Establish persistent HTTPX session with browser-like headers to avoid blocking
BASE_HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.124 Safari/537.36",
    "accept-language": "es-ES;es"
}
session = httpx.AsyncClient(headers=BASE_HEADERS, follow_redirects=True)

# TO-DO check other data to be retrieved and analyzed
# Add price per square meter and community expenses
# Add property owner contact details: phone and name
class PropertyResult(TypedDict):
    url: str
    title: str
    location: Dict[str, str]
    currency: str
    price: int
    initialprice: int
    downpercentage: str
    description: str
    updated: str
    features: Dict[str, List[str]]
    images: Dict[str, List[str]]
    plans: List[str]
    housingdevelopment: bool


def parse_property(response: httpx.Response) -> PropertyResult:
    """parse Idealista.com property page"""
    # Load response's HTML tree for parsing:
    selector = Selector(text=response.text)
    css = lambda x: selector.css(x).get("").strip()
    css_all = lambda x: selector.css(x).getall()

    data = {}
    # Meta data
    data['url'] = str(response.url)

    # Basic information
    data['title'] = css("h1 .main-info__title-main::text")
    location = css(".main-info__title-minor::text").split(", ")
    data['location'] = {"city": location[1], "zone": location[0]}
    data['currency'] = css(".info-data-price::text")
    data['price'] = int(css(".info-data-price span::text").replace(".", ""))
    if css(".pricedown_price::text"):
        data['initialprice'] = int(css(".pricedown_price::text").replace(".", "").replace("€", ""))
        data['downpercentage'] = css(".pricedown_icon::text")
    # Avoid duplicated text description if there's more than one listing belonging to the same housing development
    data['description'] = css_all(".comment p")[0].replace("<p>", "").replace("</p>", "").replace("<br>", "/n").strip()
    date_listing_update = css(".stats-text::text").split(" el ")[-1].split(" de ")
    # Date Format: DD-MM-YYYY
    date_today = date.today().strftime("%d-%m-%Y")
    current_month = int(date_today.split("-")[1])
    months_dictionary = {'enero': "01", 'febrero': "02", 'marzo': "03", 'abril': "04", 'mayo': "05", 'junio': "06",
                         'julio': "07", 'agosto': "08", 'septiembre': "09", 'octubre': "10", 'noviembre': "11", 'diciembre': "12"}
    if current_month >= int(months_dictionary[date_listing_update[1]]):
        data['updated'] = date_listing_update[0] + "-" + months_dictionary[date_listing_update[1]] + "-" + date_today.split("-")[2]
    else:
        data['updated'] = date_listing_update[0] + "-" + months_dictionary[date_listing_update[1]] + "-" + str(int(date_today.split("-")[2]) - 1)
    if css(".item-ribbon::text"):
        data['housingdevelopment'] = True
    else:
        data['housingdevelopment'] = False

    # Features
    data['features'] = {}
    #  first we extract each feature block like "Basic Features" or "Amenities"
    for feature_type_list in css_all(".details-property_features ul"):
        index =  css_all(".details-property_features ul").index(feature_type_list)
        feature_label = css_all(".details-property-h3::text")[index]
        features_list_raw = feature_type_list.split("</li>")
        features_list = []
        for feature in features_list_raw:
            if "\n" in feature:
                feature = feature.replace("\n", "")
            if "<ul>" in feature:
                feature = feature.replace("<ul>", "")
            if "</ul>" in feature:
                feature = feature.replace("</ul>", "")
            if "<span>" in feature and "</span>" in feature:
                feature = feature.split("<span>")[1].split("</span>")[0]
            if feature != "":
                features_list.append(feature.replace("<li>", ""))
        data['features'][feature_label] = features_list


    data['images'] = {}
    images_raw_data = re.findall("fullScreenGalleryPics\s*:\s*(\[.+?\]),", response.text)[0]
    images_data = images_raw_data[1:-1].split("},")
    for img in images_data:
        index = images_data.index(img)
        if img[-1] != "}":
            new_img_data = img + "}"
        if ':' in new_img_data:
            if '":' in new_img_data:
                images_data[index] = new_img_data.replace('":', ':')
            images_data[index] = images_data[index].replace(':', '":').replace('":/', ':/')
        new_img_data = images_data[index]
        if ',' in new_img_data:
            if ',"' in new_img_data:
                images_data[index] = new_img_data.replace(',"', ',')
            images_data[index] = images_data[index].replace(',', ',"').replace('," ', ', ')
        if ',"WEB_DETAIL' in images_data[index]:
            images_data[index] = images_data[index].replace(',"WEB_DETAIL', '')
        if images_data[index][1] != '"':
            images_data[index] = '{"' + images_data[index][1:]
    
    data['plans'] = []
    image_tags = []
    for img_data in images_data:
        img_data_json = json.loads(img_data)
        if img_data_json['isPlan']:
            data['plans'].append(img_data_json['imageDataService'])
            continue
        if img_data_json['tag'] not in image_tags:
            image_tags.append(img_data_json['tag'])
            data['images'][img_data_json['tag']] = []
        
        for tag in image_tags:
            images_by_tag_list = data['images'][tag]
            if tag == img_data_json['tag']:
                if img_data_json['imageDataService'] not in images_by_tag_list:
                    images_by_tag_list.append(img_data_json['imageDataService'])
                data['images'][tag] = images_by_tag_list

    
    return data


async def scrape_properties(urls: List[str]) -> List[PropertyResult]:
    """Scrape Idealista.com properties"""
    properties = []
    to_scrape = [session.get(url) for url in urls]
    for response in to_scrape:
        response = await response
        if response.status_code != 200:
            print(f"can't scrape property: {response.url}")
            continue
        properties.append(parse_property(response))
    return properties



# -------------------------------------------------
# Main
# -------------------------------------------------
async def execute_main():
    urls = ["https://www.idealista.com/inmueble/98776221/",
            "https://www.idealista.com/inmueble/99776484/"]
    data = await scrape_properties(urls)
    print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(execute_main())
