from flask import Flask, escape, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from faker import Faker
import csv
from collections import deque
import requests
 




    
app = Flask(__name__)



@app.route('/')
def home():
    return "Все норма ?" 



# ====111======================


@app.route('/requirements/')
def requ():
    with app.open_resource('requirements.txt', 'r') as f:
        file_content = f.read()
    return file_content





# ====111======================

faker = Faker()
@app.route('/generate-users/')
@app.route('/generate-users/<int:count>')
def gen(count=100):
    name = []
    email = []
    for _ in range(count):
        name.append(faker.name())
        email.append(faker.ascii_email())
    d = dict(zip(name, email))
    return d   


# =======333===================
all_weight = []
all_height = []
@app.route('/mean')
def mean():
    with open('hw.csv',"r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        headers = next(csv_reader)
        for row in csv_reader:
            if len(row) == 0:
                continue
            
            Index = row[0]
            Height = float(row[1])
            weight = float(row[2])
            all_weight.append(weight)
            all_height.append(Height)
        
   
            Len = len(all_weight)

            SumW = sum(all_weight)
            kg = SumW *0,453592
            averW = int(SumW / Len)

            SumH = sum(all_height)
            cm = SumH * 2.54 
            averH = int(SumH / Len)
 
            return (f'Average of weight is:  {averW} kg  and   Average of height is:  {averH} cm')
            



# ===============444===========

@app.route('/space/')
def cosmo():
    url = 'http://api.open-notify.org/astros.json'
    R = requests.get(url)
    k = R.json()['number']

    return (f'{k} космонавтов в настоящий момент')



if __name__ == '__main__':
    app.run()