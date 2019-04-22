from flask import Flask, render_template, redirect, request
from random import randint
from time import gmtime, strftime
app = Flask(__name__)

money = 0
log = []


@app.route('/')
def index():
    global money
    return render_template('index.html', money=money, log=log)


@app.route('/process_money', methods=['POST'])
def process_money():
    location = request.form['location']
    gold = evaluate_gold[location]()
    update_log(gold, location)
    return redirect('/')


def new_log_entry(gold, location):
    return {
            "gold": gold,
            "location": location,
            "time": strftime("%Y/%m/%d %H:%M %p", gmtime())
            }


def update_log(gold, location):
    global money
    money += gold
    log.insert(0, new_log_entry(gold,location))


def farm(): return randint(10, 20)
def cave(): return randint(5, 10)
def house(): return randint(2, 5)
def casino(): return randint(-50, 50)


evaluate_gold = {"farm": farm, "cave": cave, "house": house, "casino": casino}

if __name__ == '__main__':
    app.run(debug=True)
