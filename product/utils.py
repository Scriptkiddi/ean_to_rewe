__author__ = 'fritz'
import requests
import os
from bs4 import BeautifulSoup
import json
import urllib
from .models import Product, Price, Ean

def send_simple_message(sender, to, subject, text):
    return requests.post(
        os.environ['eantorewe_mailgun_link'],
        auth=("api", os.environ['eantorewe_mailgun_api_key']),
        data={"from": sender,
              "to": to,
              "subject": subject,
              "text": text})


def get_rewe_price_for_product(nan):
    products = crawl_rewe(nan)
    if len(products) == 1:
        return products[0].get("price")

def crawl_rewe(query):
    query = urllib.parse.quote(query)
    r = requests.get("https://shop.rewe.de/productList?search={}".format(query))
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        scripts = soup.find_all("script")

        for script in scripts:
            if "pageData" in script.text:
                content = script
                break

        content = json.loads(content.contents[0][20:-2])
    return content.get('products')


def gather_information(ean):
    r = requests.get("http://www.codecheck.info/product.search?q={}".format(ean))
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        name = soup.find("h1").text.strip()
        image_url = "http://www.codecheck.info/{}".format(soup.find_all("span", class_="cc-image s1 hf")[0].find("img"))
        rewe_results = crawl_rewe(name)
        products = []
        prices = []
        eans = []
        for product in rewe_results:
            nan = rewe_results[0].get('id')
            pro = Product(nan=nan, name=name)
            products.append(pro)
            price = rewe_results[0].get('price')
            prices.append(Price(product=pro, price=price))
            eans.append(Ean(product=pro, ean=ean))
        return (products, prices, eans)



