import os
from re import S
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd

def case_law_results():

    print("Extracting case law results..")

    params = {
        "engine": "google_maps",
        "q": "ملاعب",
        "type": "search",
        "start": "0",
        "ll": "@26.4274657,50.1112348,14z",
        "api_key": "595a89814a7aec5c3bdb1c42d6fffdffc90ab61a6eb852f364e6f866531abce9"
    }
    # params = {
    #   "q": "ملاعب",
    #   "location": "Ad Dammam, Eastern Province, Saudi Arabia",
    #   "hl": "ar",
    #   "gl": "sa",
    #   "google_domain": "google.com.sa",
    #   "api_key": "595a89814a7aec5c3bdb1c42d6fffdffc90ab61a6eb852f364e6f866531abce9"
    # }
    search = GoogleSearch(params)

    results_data = []

    loop_is_true = True
    while loop_is_true:
      results = search.get_dict()

    #   print(results['serpapi_pagination']['current'])
    #   print(f"Currently extracting page №{results['serpapi_pagination']}..")
    #   print(results)

      for result in results["local_results"]:
        title = result["title"]
        result_type = result.get("type")

        try:
          phone = result["resources"][0]["title"]
        except: phone = None

        results_data.append({
          "position": result["position"] + 1,
          "result_type": result_type,
          "title": title,
          "phone": phone
        })
        # if i != 100 :
        #   i += 1
        #   search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        # else:
        #     loop_is_true = False
        if "next" in results["serpapi_pagination"]:
          search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
          loop_is_true = False

    return results_data


def save_case_law_results_to_csv():
    print("Waiting for case law results to save..")
    pd.DataFrame(data=case_law_results()).to_csv("google_scholar_case_law_results.csv", encoding="utf-8", index=False)

    print("Case Law Results Saved.")

save_case_law_results_to_csv()