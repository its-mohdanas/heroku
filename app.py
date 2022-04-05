from flask import Flask, request, jsonify, render_template, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
app = Flask(__name__)

path = 'D:\\Code\\WebDev\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(path)

scraped = []
# @app.route('/scraped1')
# def scraper():
#     # return jsonify(scraped)
#     return render_template('index.html')

list1 = []

##############################################
@app.route('/', methods=['GET'])
def add_scrap():
    website="https://www.papersdrop.com/"

    driver.get(website)
    links = driver.find_elements_by_tag_name('a')

    for link in links:
        lnk = link.get_attribute("href")
        list1.append(lnk)
    driver.close()

    dic1 = {"output": list1}
    # return jsonify(dic1)
    print(jsonify(dic1))
    # print(list1)
    return render_template('index.html', dic1 = dic1)

app.run(debug=True)
