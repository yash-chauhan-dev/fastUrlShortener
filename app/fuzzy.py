import uuid

import urllib3
from fastapi import Request

from app import config, db, models


def generate_fuzzy_url(request: Request, data: models.URL):
    settings = config.Settings()
    host_name = settings.app_host

    original_url = data.url

    if check_for_valid_url(original_url):
        uid = str(uuid.uuid1())[:8]
        fuzzy_url = host_name + uid
        data_json = {
            "fuzzy_url": fuzzy_url,
            "original_url": original_url
        }
        ret_val = db.save_document(request, data_json)
        return ret_val

    else:
        return {
            "error": "Please enter valid URL!"
        }


def check_for_valid_url(url):
    http = urllib3.PoolManager()
    try:
        ret_val = http.request('GET', url)
        if ret_val.status == 200:
            return True
    except Exception:
        return False


def list_fuzzy_url(request: Request):
    list_of_documents = db.list_documents(request)
    return {
        "message": "success",
        "data": list_of_documents
    }


def redirect_fuzzy_url():
    pass
