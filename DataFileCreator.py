import csv

with open('customers', 'r') as f:
    customers = [line.strip() for line in f]

with open('supc', 'r') as f:
    supc = [line.strip() for line in f]

print(customers[0])

with open('dataSet.csv','w' , newline='') as csvfile:
    fieldsname=['customer','supc']
    writer = csv.DictWriter(csvfile,fieldnames=fieldsname)
    writer.writeheader()
    for i in range(200):
         writer.writerow({'customer':"\""+customers[i]+"\"",'supc':"\""+supc[i]+"\""})

print("complete")

