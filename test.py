import matplotlib.pyplot as plt
import csv

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

journals = []

#開檔
file = open("JCR_AHCI(2019~2024).csv", encoding = "utf-8")
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
            
#繪圖
x = [2019, 2020, 2021, 2022, 2023, 2024]
y = []

for i in range(6):
    print(journals[0].total_cities[i])
    y.append(journals[0].total_cities[i])

plt.plot(x, y)
plt.show()