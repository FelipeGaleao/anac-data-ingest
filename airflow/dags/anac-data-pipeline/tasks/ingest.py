

from distutils.command.upload import upload
import os, sys
import zipfile
import urllib.request

sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
from common import azureadls

from airflow.hooks.base_hook import BaseHook
connection = BaseHook.get_connection("AZURE_STORAGE_CONNECTION")

def ingest_file_from_anac(year: int, month: int) -> None:
    if(month < 10):
        month = str("0" + str(month))
    
    get_download_file(year, month)
    extract_file(f"basica{year}-{month}.zip")
    upload_file(year, month)
    
    
def upload_file(year: int, month: int) -> None:
    """ function to upload file to Azure Datalake

    Args:
        year (int): year of file
        month (int): month of file
    """
    azureadls.initialize_storage_account(connection.login, connection.password)
    azureadls.upload_file_to_directory(f"basica{year}-{month}.txt", f"RAW/{year}", 'anac')
       
def get_download_file(year: int, month: int) -> None:
    """ function to download file that contains data statistical about air traffic in Brazil from ANAC website

    Args:
        year (int): year of file (2000-2022)
        month (int): month of file (1-12)
    """
    file_link_url = f"https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/envio-de-informacoes/microdados/basica{year}-{month}.zip"
    name_file = file_link_url[97:]
    try:
        urllib.request.urlretrieve(file_link_url, name_file)
        print(f"{name_file} was downloaded with success!")
    except ValueError:
        print(ValueError)
        print(f"{name_file} wasnt downloaded! Something was happened!")
        
def extract_file(name_file: str) -> None:
    """ function to extract file downloaded from ANAC web site to get .txt file that contains data.

    Args:
        name_file (str): name of file downloaded from ANAC website
    """ 
    with zipfile.ZipFile(name_file, 'r') as zip_ref:
        zip_ref.extractall(f'.')
        os.remove(name_file)