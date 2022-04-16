
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
import requests
import urllib.request
import zipfile
import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings


def initialize_storage_account(storage_account_name, storage_account_key) -> None:
    try:  
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)
        
def upload_file_to_directory(name_file: str, directory_destination: str, file_system: str) -> None:
    try:

        file_system_client = service_client.get_file_system_client(file_system=f"{file_system}")

        directory_client = file_system_client.get_directory_client(f"{directory_destination}")
        
        file_client = directory_client.create_file(f"{name_file}")
        local_file = open(f"./{name_file}",'r', encoding="utf8", errors='ignore')
  
        file_contents = local_file.read()

        file_client.upload_data(file_contents, overwrite=True)
        
        os.remove(name_file)

    except Exception as e:
      print(e)