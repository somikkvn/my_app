from django.shortcuts import render

import csv

def open_csv():
    # відкриваємо файл для читання
    with open('static/data/data.csv', 'r') as csv_file:
        # створюємо об'єкт csv.reader
        reader = csv.reader(csv_file)

        # ітеруємося по рядках файлу
        for row in reader:
            # виводимо значення у кожному стовпці рядка
            print(row[0], row[1], row[2])


def index(requests):
    return render(requests, 'bases/index.html')

def type(requests):
    return render(requests, 'bases/type.html')

def offers(requests):
    return render(requests, 'bases/offers.html')

def functional(requests):
    return render(requests, 'bases/functional.html')

def contact(requests):
    return render(requests, 'bases/contact.html')