import os
from re import S
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd
import pyfiglet



def scrap_results():
    name = pyfiglet.figlet_format("Hey-Bandar")
    welcome = pyfiglet.figlet_format("Welcome-to Google-Map Scraping!")
    print(name)
    print(welcome)
    word_term = input("Please enter word term to search on Google Map")
    address = input("Please enter the address")

    print("Extracting case law results..")

    params = {
        "engine": "google_maps",
        "q": word_term,
        "type": "search",
        "start": "0",
        "ll": f"@{address}",
        "api_key": "dc6b3115d8f60c154a001daa6c17cb9a0fc65b8a9ab6bbf9b78895ebd7e7ecce"
    }
 
 
    search = GoogleSearch(params)

    results_data = []

    loop_is_true = True
    while loop_is_true:

      results = search.get_dict()
      if "local_results" in results:
        for result in results["local_results"]:
          title = result["title"]
          result_type = result.get("type")
          try:
            phone = result["phone"]
          except: 
            phone = None
          results_data.append({
            "result_type": result_type,
            "title": title,
            "phone": phone
          })
          
        if "next" in results["serpapi_pagination"]:
          search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
          loop_is_true = False
      else: 
          loop_is_true = False

    return results_data


def save_to_csv():
    print("Waiting to save..")
    pd.DataFrame(data=scrap_results()).to_csv("google_map_scrapping.csv", encoding="utf-8-sig", index=False)
    done = pyfiglet.figlet_format("Done")
    print(done)

save_to_csv()
