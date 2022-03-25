import os
from re import S
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd


def case_law_results():
    word_term = input("Please enter word term to search on Google Map")
    address = input("Please enter the address")

    print("Extracting case law results..")

    params = {
        "engine": "google_maps",
        "q": word_term,
        "type": "search",
        "start": "0",
        "ll": f"@{address}",
        "api_key": "595a89814a7aec5c3bdb1c42d6fffdffc90ab61a6eb852f364e6f866531abce9"
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


def save_case_law_results_to_csv():
    print("Waiting for case law results to save..")
    pd.DataFrame(data=case_law_results()).to_csv("google_scholar_case_law_results.csv", encoding="utf-8-sig", index=False)

    print("Case Law Results Saved.")

save_case_law_results_to_csv()