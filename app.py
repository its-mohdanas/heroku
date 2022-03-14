from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
app = Flask(__name__)


path = 'D:\\Code\\WebDev\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(path)

scraped = []



@app.route('/scraped')
def scraper():
    return jsonify(scraped)

list1 = []

##############################################
@app.route('/scraped', methods=['POST'])
def add_scrap():
    website="https://www.papersdrop.com/"
    scrap = request.get_json()
    driver.get(website)
    links = driver.find_elements_by_tag_name('a')

    for link in links:
        lnk = link.get_attribute("href")
        list1.append(lnk)
    driver.close()

    dic1 = {"output": list1}
    return jsonify(dic1)

app.run()
