import json
import requests

def fetch_apps_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["apps"]

def combine_sources(urls):
    combined_apps = []
    for url in urls:
        apps = fetch_apps_from_url(url)
        combined_apps.extend(apps)
    return combined_apps

def write_to_json_file(apps, name, identifier, subtitle, description, iconURL, website, tintColor, filename="apps.json"):
    data = {
        "name": name,
        "identifier": identifier, 
        "subtitle": subtitle,
        "description": description,
        "iconURL": iconURL,
        "website": website,
        "tintColor": tintColor,
        "apps": apps
    }
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

name = "Balackburn Source"
identifier = "com.balackburn.source"
subtitle = "Balackburn's Github Projects"
description = "This source contains Balackburn's Github Projects"
iconURL = "https://balackburn.github.io/images/balackburn_icon.png"
website = "https://balackburn.github.io/"  
tintColor = "#62c855"

urls = [
    "https://raw.githubusercontent.com/Balackburn/YTLitePlusAltstore/main/apps.json",
    "https://raw.githubusercontent.com/Balackburn/Apollo/main/apps.json",
    "https://raw.githubusercontent.com/Balackburn/Winston/main/apps.json",
]

combined_apps = combine_sources(urls)

write_to_json_file(combined_apps, name, identifier, subtitle, description, iconURL, website, tintColor)