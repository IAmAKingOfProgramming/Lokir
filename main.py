from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import urllib.request
from bs4 import BeautifulSoup
#from flask_sslify import SSLify


app = Flask(__name__)
#sslify = SSLify(app)


URL = 'https://api.telegram.org/bot564565047:AAE_6dyDlkYhlXJ3hGfdkCCnXKdgdGi-6b4/'


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    find = soup.find('div', class_="itemBody")
    for pow in find.find_all('div', class_="itemFullText"):
        tablish = pow.find_all("table")
        monday = tablish[0]
        tuesday = tablish[1]
        wednesday = tablish[2]
        thorsday = tablish[3]
        friday = tablish[4]
        pon = ('Пари на понеділок:\n')
        i = 0
        for row in monday.find_all('tr')[1:]:
            cols = row.find_all('td')
            table1 = cols[0].text.strip()
            table2 = cols[1].text.strip()
            table3 = cols[2].text.strip()
            table4 = cols[3].text.strip()
            monday[i] = ("Час: |" + table1 + " |  № пари: (" + table2 + ") Назва пари та викладач: |" + table3 + "| Кабінет: |" + table4 + "|")
            i = i+1
        vt = ('\nПари на вівторок:\n')
        i = 0
        for row in tuesday.find_all('tr')[1:]:
            cols = row.find_all('td')
            table1 = cols[0].text.strip()
            table2 = cols[1].text.strip()
            table3 = cols[2].text.strip()
            table4 = cols[3].text.strip()

            tuesday[i] = ("Час: |" + table1 + " |  № пари: (" + table2 + ") Назва пари та викладач: |" + table3 + "| Кабінет: |" + table4 + "|")
            i = i+1
        sr = ('\nПари на середу:\n')
        i = 0
        for row in wednesday.find_all('tr')[1:]:
            cols = row.find_all('td')
            table1 = cols[0].text.strip()
            table2 = cols[1].text.strip()
            table3 = cols[2].text.strip()
            table4 = cols[3].text.strip()
            wednesday[i] = ("Час: |" + table1 + " |  № пари: (" + table2 + ") Назва пари та викладач: |" + table3 + "| Кабінет: |" + table4 + "|")
            i = i+1
        cht = ('\nПари на четверг:\n')
        i = 0
        for row in thorsday.find_all('tr')[1:]:
            cols = row.find_all('td')
            table1 = cols[0].text.strip()
            table2 = cols[1].text.strip()
            table3 = cols[2].text.strip()
            table4 = cols[3].text.strip()
            thorsday[i] = ("Час: |" + table1 + " |  № пари: (" + table2 + ") Назва пари та викладач: |" + table3 + "| Кабінет: |" + table4 + "|")
            i = i+1
        pt = ("\nПари на п'ятницю:")
        i = 0
        for row in friday.find_all('tr')[1:]:
            cols = row.find_all('td')
            table1 = cols[0].text.strip()
            table2 = cols[1].text.strip()
            table3 = cols[2].text.strip()
            table4 = cols[3].text.strip()
            friday[i] = ("Час: |" + table1 + " |  № пари: (" + table2 + ") Назва пари та викладач: |" + table3 + "| Кабінет: |" + table4 + "|")
            i = i+1
        pari = pon + '\n' + monday[0] + '\n' + monday[1] + '\n' + monday[2] + '\n' + monday[3] + '\n' + vt + '\n' + \
tuesday[0] + '\n' + tuesday[1] + '\n' + tuesday[2] + '\n' + tuesday[3] + '\n' + sr + '\n' + wednesday[
                   0] + '\n' + wednesday[1] + '\n' + wednesday[2] + '\n' + wednesday[3] + '\n' + cht + '\n' + thorsday[
                   0] + '\n' + thorsday[1] + '\n' + thorsday[2] + '\n' + thorsday[3] + '\n' + pt + '\n' + friday[0] + '\n' + \
               friday[1] + '\n' + friday[2] + '\n' + '\n' + friday[3]
        return pari


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return


def send_photo(chat_id, text):
    url = URL + 'sendPhoto'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def send_location(chat_id, latitude, longitude):
    url = URL + 'sendLocation'
    answer = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}
    r = requests.post(url, json=answer)
    return r.json()


def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


class Nachalniki: #Класс
    prizv = ""
    name = ""
    po_batkovi = ""
    posada = ""

    def __init__(self, prizv, name, po_batkovi, posada): #Коноструктор с параметром
        self.prizv = prizv
        self.name = name
        self.po_batkovi = po_batkovi
        self.posada = posada

class Others(Nachalniki): #Наследование
    Moz_ker_insh_nach = ""
    def __init__(self, prizv, name, po_batkovi, posada, Moz_ker_insh_nach): #Перегрузка методов
        self.prizv = prizv
        self.name = name
        self.po_batkovi = po_batkovi
        self.posada = posada
        self.Moz_ker_insh_nach = Moz_ker_insh_nach

Zamistnik = Others("Косенко ", "Дмитро", " Сергійович", "Замістник директора", True)
Director = Others("Майстренко", " Наталія ", "Миколаївна", "Директор", True)



class Zav(Nachalniki): #Наследование
    __kurs = "" #Инкапсуляция


Sovgir = Zav("Совгир ", "Людмила", " Миколаївна", "Завідуюча відділенням")
Sovgir.kurs = "другий, третій, четвертий"

Vasiletc = Zav("Василець", " Тетяна ", "Олександрівна", "Завідуюча відділенням")
Vasiletc.kurs = "перший"

Zhmud = Zav("Жмуд", " Надія ", " Олександрівна", "Завідуюча відділенням")
Zhmud.kurs = "другий, третій, четвертий (Професійна освіта)"


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        message = message.lower()
        if 'добрий' in message or 'прив' in message or 'доброго' in message or 'здравств' in message or 'добрый' in message:
            send_message(chat_id, text='Доброго дня' + ' ' + r['message']['from']['first_name'])
        elif 'допомога' in message or 'помошь' in message:
            send_message(chat_id, text='Привіт, Мене звуть Куратор. \n Я можу відповісти на питання стосовно технікуму та навчання. \n Основні питання, які можуть виникати у вас, я відвів в окремому меню. \n Просто відкрийте випадаюче меню та оберіть питання, яке вас цікавить \n Також ви можете спілкуватися зі мною за допомогою звичайної клавіатури звичним способом. \n Приємного спілкування 😉 ')
        elif 'python' in message and 'мануал' in message:
            send_message(chat_id, text=("Ось відмінний сайт для розробників на Python: " + '\n' + " https://tproger.ru/tag/python/"))
        elif 'дела' in message or 'справи' in message or 'как ты' in message or 'что ты там' in message:
            send_message(chat_id, text='Все добре,чим можу допомогти?')
        elif 'звуть' in message or 'зовут' in message or 'звати' in message or 'имя' in message or "ім'я" in message:
            send_message(chat_id, text="моє ім'я - Куратар v1.1")
        elif 'возраст' in message or 'лет' in message or 'років' in message or 'вік' in message:
            send_message(chat_id, text='Це надто особисте питання')
        elif 'локация' in message or 'адрес' in message or 'нахождение' in message or 'знаходження' in message or 'карт' in message or 'локація' in message:
            send_location(chat_id, latitude='51.224849650919865', longitude='33.2270427122603')
        elif 'пар' in message or 'рассписание' in message or 'розклад' in message:
            send_message(chat_id, text='В якій групі ви навчаєтесь?')
        elif '711' in message:
            send_message(chat_id, text=parse(urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/1-kurs/item/226-711.html')))
        elif '711' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/1-kurs/item/226-711.html')))
        elif '511' in message or '611' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/1-kurs/item/225-511-611.html')))
        elif '311' in message or '911' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/1-kurs/item/224-311-911.html')))
        elif '111' in message or '811' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/1-kurs/item/223-111-811.html')))
        elif '621' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/711-621.html')))
        elif '921' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/238-921.html')))
        elif '821' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/237-821.html')))
        elif '721' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/236-721.html')))
        elif '702' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/235-702.html')))
        elif '521' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/233-521.html')))
        elif '421' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/232-421.html')))
        elif '322' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/231-322.html')))
        elif '321' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/230-321.html')))
        elif '221' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/229-221.html')))
        elif '122' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/228-122.html')))
        elif '121' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/k2-3/k2-categories/k2-1column/item/227-121.html')))
        elif '931' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/250-931.html')))
        elif '831' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/249-831.html')))
        elif '731' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/248-731.html')))
        elif '703' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/247-703.html')))
        elif '631' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/246-631.html')))
        elif '531' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/245-531.html')))
        elif '431' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/244-431.html')))
        elif '332' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/243-332.html')))
        elif '331' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/242-331.html')))
        elif '231' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/241-231.html')))
        elif '132' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/240-132.html')))
        elif '131' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/239-131.html')))
        elif '132' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/3-kurs/item/240-132.html')))
        elif '741' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/4-kurs/item/253-741.html')))
        elif '342' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/4-kurs/item/252-342.html')))
        elif '142' in message:
            send_message(chat_id, text=parse(
                urllib.request.urlopen('http://kipt.sumdu.edu.ua/navchannia/rozklad-zaniat/4-kurs/item/251-142.html')))
        elif 'замен' in message or 'замін' in message:
            url = "http://kipt.sumdu.edu.ua/images/foto/krutu/x300518.jpg.pagespeed.ic.8hvFsnze7-.webp"
            img = urllib.request.urlopen(url).read()
            out = open("img.jpg", "wb")
            out.write(img)
            out.close()
            send_photo(chat_id, text='')
        elif "де" in message and "знах" in message or "где" in message  \
                and "наход" in message:
            send_message(chat_id, text=" - Відділ кадрів знаходиться на другому поверсі, кабінет № ... ")
            send_message(chat_id, text=" - Профком знаходиться на ... поверсі, кабінет № ... ")
            send_message(chat_id, text=" - Студентський парламент знаходиться на ... поверсі, кабінет № ... ")
            send_message(chat_id, text=" - Бухгалтерія знаходиться на другому поверсі, кабінет № ... ")
        elif "зав" in message and "відд" in message or "зав" in message \
                and "отдел" in message:
            send_message(chat_id, text="На якому курсі ви навчаєтесь? \n Чи є ви студентом проф освіти (так або ні)")
        elif "1" in message and "так" in message  \
                or "1" in message and "да" in message  \
                or "2" in message and "так" in message  \
                or "2" in message and "да" in message  \
                or "3" in message and "так" in message  \
                or "3" in message and "да" in message  \
                or "пер" in message and "так" in message  \
                or "пер" in message and "да" in message  \
                or "втор" in message and "так" in message  \
                or "втор" in message and "да" in message  \
                or "други" in message and "так" in message  \
                or"други" in message and "да" in message  \
                or "трет" in message and "так" in message  \
                or "трет" in message and "да" in message :
            send_message(chat_id, text="Ваш зав відділенням:" + Nachalniki.Zhmud.prizv + Nachalniki.Zhmud.name + Nachalniki.Zhmud.po_batkovi)
        elif "2" in message and "ні" in message \
                or "2" in message and "нет" in message  \
                or "3" in message and "ні" in message  \
                or "3" in message and "нет" in message  \
                or "4" in message and "ні" in message  \
                or "4" in message and "нет" in message  \
                or "втор" in message and "ні" in message  \
                or "втор" in message and "нет" in message  \
                or "други" in message and "ні" in message  \
                or "други" in message and "нет" in message  \
                or "трет" in message and "ні" in message \
                or "трет" in message and "нет" in message  \
                or "чет" in message and "ні" in message  \
                or "чет" in message and "нет" in message:
            send_message(chat_id, text="Ваш зав відділенням: " + Nachalniki.Sovgir.prizv + Nachalniki.Sovgir.name + Nachalniki.Sovgir.po_batkovi)
        elif "1" in message and "ні" in message  \
                or "1" in message and "нет" in message  \
                or "пер" in message and "ні" in message  \
                or "пер" in message and "нет" in message :
            send_message(chat_id, text="Ваш зав відділенням: " + Nachalniki.Vasiletc.prizv + Nachalniki.Vasiletc.name + Nachalniki.Vasiletc.po_batkovi)
        elif "директ" in message :
            send_message(chat_id, text="Наш " + Nachalniki.Director.posada + ": " + Nachalniki.Director.prizv + Nachalniki.Director.name + Nachalniki.Director.po_batkovi)
        elif "зам" in message:
            send_message(chat_id, text=Nachalniki.Zamistnik.posada + ": " + Nachalniki.Zamistnik.prizv + Nachalniki.Zamistnik.name + Nachalniki.Zamistnik.po_batkovi)
        else:
            send_message(chat_id, text="Це не стосується навчатьного процесу")
        write_json(r)
        return jsonify(r)


if __name__ == '__main__':
    app.run()
