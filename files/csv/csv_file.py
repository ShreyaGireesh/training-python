import csv

data = [['Comapany', 'Owner'],
        ['Alphabet','Sundar Pichai'],
        ['Amazon','Jeff Bezos']]
file_name='company.csv'
with open(file_name, 'w', newline ='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open(file_name, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)


more_data = [['ABC', 'John'],
            ['KJU', 'Sam']]

with open(file_name, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(more_data)
print("\nafter appending...")
with open(file_name, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)