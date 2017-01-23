import csv
import copy
import json
data = []

with open('raw.csv') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        data.append({})
        for k, v in row.items():
            if k == "Row Labels":
                data[len(data) - 1][k] = str(v).replace("'","").replace('"',"")
            else:
                try:
                    data[len(data) - 1][k] = int(v)
                except:
                    data[len(data) - 1][k] = str(v)
                    #continue
year_data = []
causes = ['OTHER', 'TOTAL SUDDEN DEATHS', 'SUDDEN DEATHS(HEART ATTACKS)', 'TOTAL FIRE', 'OTHER RAILWAY ACCIDENTS', 'DROWNING',
            #'TOTAL POISONING', 'TOTAL FALLS', 'EPILEPTIC FITS/GIDDINESS', 'INFLUENCE OF ALCOHOL', 'ELECTROCUTION', 'SNAKE BITE/ANIMAL BITE', 'FOOD POISIONING/ACCIDENTAL INTAKE OF INSECTICIDES ETC.',
            'ABORTIONS/CHILD BIRTH', 'TOTAL DROWNING', 'FIRE-ARMS', 'GAS CYLINDER/STOVE BURST']

for i in data:
    if i['YEAR'] == 2002:
        if i['CAUSE'] in causes:
            year_data.append(i)

keys = year_data[0].keys()
with open('output.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(year_data)
