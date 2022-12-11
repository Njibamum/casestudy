import re

import requests
import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/link/")
async def return_value(url: str, output: str):
    # url_option
    # output_option
    # reference https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
    html = requests.get(url)
    bsoup_object = BeautifulSoup(html.text, "lxml")
    a_tag = bsoup_object.findAll(
        'a', attrs={'href': re.compile("^https://")})
    if output == "stdout":
        l = []
        for a in a_tag:
            l.append(a['href'])
        return l
    elif output == "json":
        test = {}
        for a in a_tag:
            u = str(a['href']).split(".com/")
            base = u[0]
            if base not in test.keys():
                if not len(u) > 1:
                    test[base] = ['/']
                else:
                    test[base] = [u[1]]
            else:
                if not len(u) > 1:
                    test[base].append('/')
                else:
                    test[base].append(u[1])

        return test


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
    # http://0.0.0.0:8080/link/?url=https://www.geeksforgeeks.org&output=stdout
