import requests
from bs4 import BeautifulSoup
import pandas as pd

def export_csv(data):
    """
    Exportar a csv los datos capturados
    """
    df = pd.DataFrame(data)
    df.to_csv("datos.csv", index=False)


def web_scraping():
    """
    web scraping a pagina de fake jobs
    """
    data = {"Cargo":[], "Locacion":[]}
    url = "https://realpython.github.io/fake-jobs/"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    #obtenemos el cargo y el pais del mismo
    jobs = soup.find("div", attrs={"id": "ResultsContainer"}).find_all("div", attrs={"class": "column is-half"})
    
    for job in jobs:
        position = job.find("div", attrs={"class": "media-content"}).find("h2").get_text().strip()

        Location = job.find("div", attrs={"class": "content"}).find("p", attrs={"class": "location"}).get_text().strip()

        data["Cargo"].append(position)
        data["Locacion"].append(Location)
    
    return data

data = web_scraping()
export_csv(data)