from datetime import datetime
import json
import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
file_path = os.path.join(base_dir,"techpages/fixtures/")

def fetch_testimonies_from_files():
    with open(file_path+"testimonies.json","r") as output_file:
        datas = json.load(output_file)
    
    new_datas = []
    for data in datas:
        date_format = "%Y-%m-%d %H:%M:%S"
        formatted_date = datetime.strptime(data["date"], date_format)
        data_obj = {}
        data_obj["fullname"] = "{0} {1}".format(data["lastname"], data["firstname"])
        data_obj["message"] = data["message"]
        data_obj["date"] = "{0}-{1}-{2}".format(formatted_date.year, formatted_date.month, formatted_date.day)
        new_datas.append(data_obj)
    return new_datas