import matplotlib.pyplot as plt
import numpy as np
import csv

journals = []
categories = []
draw_data = []

class journal:
    def __init__(self, name, category):
        self.total_cities = [-1, -1, -1, -1, -1, -1]
        self.IFs = [-1, -1, -1, -1, -1, -1]
        self.name = name
        self.category = category

    def add_data(self ,cities, IF, year):
        match year:
            case "2019":
                self.total_cities[0] = cities
                self.IFs[0] = IF
            case "2020":
                self.total_cities[1] = cities
                self.IFs[1] = IF
            case "2021":
                self.total_cities[2] = cities
                self.IFs[2] = IF
            case "2022":
                self.total_cities[3] = cities
                self.IFs[3] = IF
            case "2023":
                self.total_cities[4] = cities
                self.IFs[4] = IF
            case "2024":
                self.total_cities[5] = cities
                self.IFs[5] = IF

def file_IO(input_database):
    #開檔
    file = open(f"{input_database}(2019~2024).csv", encoding = "utf-8")
    reader = csv.reader(file)

    #讀檔
    for row in reader:
        if len(journals) == 0:
            journal1 = journal(row[7], row[8])
            journal1.add_data(row[0], row[1], row[14])
            journals.append(journal1)
            continue

        find = False
        for j in journals:                                        
            if j.name == row[7] and j.category == row[8]:
                j.add_data(row[0], row[1], row[14])
                find = True
                break

        if find == False:
            journal1 = journal(row[7], row[8])
            journal1.add_data(row[0], row[1], row[14])
            journals.append(journal1)

def draw_line_chart():
    x = [2019, 2020, 2021, 2022, 2023, 2024]
    y = []

    for line in draw_data:
        print(line.name)
        y = line.total_cities
        plt.plot(x, y)
        y = []
    plt.show()

def choose_category():
    for j in journals:
        if j.category not in categories:
            categories.append(j.category)
    
    for i in range(0, len(categories), 1):
        print(f"{(i+1)}. {categories[i]}")

    input_category = input("Please input the category: ")

    for j in journals:
        if j.category == input_category:
            draw_data.append(j)

def choose_journals():
    while True:
        input_journal = input("Please input the journal(Enter -1 to end): ")

        if input_journal == "-1":
            break

        for j in journals:
            if j.name == input_journal:
                draw_data.append(j)

def choose_all():
    123

def option():
    print("1.比對個別期刊\n2.比對領域內所有期刊\n3.比對所有期刊")
    input_option = input("Please input the option: ")

    match input_option:
        case "1":
            choose_journals()
            draw_line_chart()
        case "2":
            choose_category()
            draw_line_chart()
        case "3":
            choose_all()
            draw_line_chart()
        case _:
            print("sorry, there's no any options like that")

##### main ####

input_database = input("Please input the database: ")
file_IO(input_database)
option()