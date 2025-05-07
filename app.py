from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
base_url = 'https://zh.moegirl.org.cn'


def search(month, day):
    r = requests.get(
        base_url + f'/Category:{month}%E6%9C%88{day}%E6%97%A5')
    soup = BeautifulSoup(r.content, features='lxml')
    s = soup.find('div', {'class': 'mw-category'})
    links = s.find_all('a')
    result = []
    for link in links:
        result.append([base_url + link['href'], link['title']])

    return result


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return render_template('main.html', profiles=search(request.values['month'], request.values['day']))
    return render_template('main.html', profiles=[])
