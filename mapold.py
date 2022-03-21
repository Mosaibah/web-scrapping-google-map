import os
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd

def case_law_results():
    params = {
        "engine": "google_maps",
        "q": "ملاعب",
        "type": "search",
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

    result_data = []

    loop_is_true = True
    while loop_is_true:
        results = search.get_dict()
        # print(results)





        
        for result in results["local_results"]:
            title = {result['title']}
            try:
                phone = {result['phone']}
            except: phone = None
            result_type = result.get("type")
        
        
            # if something is None it will return an empty {} dict()

            result_data.append({
                "page_number": results['serpapi_pagination']['current'],
                "position": result["position"] + 1,
                "result_type": result_type,
                "title": title,
                "phone": phone,
                })
            if next page is not present -> exit the while loop.
            if "next" in results["serpapi_pagination"]:
                search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
            else:
                loop_is_true = False
return result_data


def save_case_law_results_to_csv():
    print("Waiting for الملاعب results to save..")
    pd.DataFrame(data=case_law_results()).to_csv("google_scholar_case_law_results.csv", encoding="utf-8", index=False)


    print("Case Law Results Saved.")

save_case_law_results_to_csv()