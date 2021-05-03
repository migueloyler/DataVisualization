import csv
import json

#json_list = []
json_dict = {}
json_arr = []
with open("ufo_data_us_cleaned_v2.csv", mode="r") as ufo_data:
    reader = csv.reader(ufo_data)
    next(reader)
    for date, city, state, shape, duration, posted, city_lower, lat, lng in reader:
        if date == '' or state == '' or shape == '':
            continue
        print(date)
        if '/' not in date.split()[0] or len(date.split()[0]) < 5:
            print("NOT INCLUDING^^^")
            continue
        year = date.split()[0][-2:]
        if int(year) >= 22 and int(year) <= 99:
            year =  "19" + year
        else:
            year = "20" + year

        year = int(year)

        

        if year in json_dict:

            if state in json_dict[year]:

                if shape in json_dict[year][state]:

                    json_dict[year][state][shape] += 1

                else:

                    json_dict[year][state][shape] = 1

            else:
                json_dict[year][state] = {}
                json_dict[year][state][shape] = 1



        else:


            json_dict[year] = {}
            json_dict[year][state] = {}
            json_dict[year][state][shape] = 1

json_arr = []
for year, yeardata in json_dict.items():
    new_dict = {}
    new_dict['year'] = year
    new_dict['yeardata'] = []
    for state,statedata in json_dict[year].items():
        new_dict2 = {}
        new_dict2['state'] = state
        new_dict2['statedata'] = []
        for shape, frequency in json_dict[year][state].items():
            new_dict2['statedata'].append({'shape': shape, 'frequency': json_dict[year][state][shape]})
        new_dict['yeardata'].append(new_dict2)
    json_arr.append(new_dict)
#json = json.dumps(json_dict)
with open("mig_data.json" , "w") as outfile:
    json.dump(json_arr, outfile)