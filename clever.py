import requests
import json as js
import sys
import numpy as np
import math



access_token = 'DEMO_TOKEN'
header = {'Authorization' : 'Bearer {}'.format(access_token)}

url = "https://api.clever.com"

sections_uri = '/v1.2/sections'

students_per_section = []



# Returns number of students per section
def cal_total_students_per_section(section):
    return len(section)

# gets all sections with default API call
def get_sections():
    response = requests.get('{}/{}'.format(url, sections_uri), headers=header)
    return js.loads(response.text)

# calculates sum of all students in all sections
def cal_avg_students():
    sections = get_sections()
    data_sections = sections["data"]
    for d in data_sections:
        num_student = cal_total_students_per_section(d['data']['students'])
        students_per_section.append(num_student)

    # converting list to numpy array to calculate mean   
    arr = np.array(students_per_section)

    return len(data_sections), arr.mean()
    



if len(sys.argv) == 2:
    access_token = sys.argv[1]
    sections, avg_students = cal_avg_students()
    print("Total number of Sections: ", sections)
    print("Average number of Students per Section: " +  str(avg_students) + " " + u"\u2248" + " " + str(math.ceil(avg_students)))

elif len(sys.argv) == 1:
    sections, avg_students = cal_avg_students()
    print("Total number of Sections: ", sections)
    print("Average number of Students per Section: " +  str(avg_students) + " " + u"\u2248" + " " + str(math.ceil(avg_students)))
else:
    print("usage: python clever.py with default token")
    print("usage: python clever.py <ACCESS_TOKEN> with custom token")





