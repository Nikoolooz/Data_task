import pandas as pd
from matplotlib import pyplot as plt
from src.model.data import Data
from src.data_processing import count_data_by_segment_type, count_data_by_answer, \
    count_percentage, total_count_by_answer, total_count_by_segment_type
sample_data = pd.read_csv("./data/WhatsgoodlyData-10.csv")

data_list = []
for i in sample_data.values:
    data_list.append(Data(i[0], i[1], i[2], i[3], int(i[4]), float(i[5])))


data_by_segment_type = count_data_by_segment_type(data_list)
data_by_answer = count_data_by_answer(data_list)

data_count_percentage = count_percentage(data_list, "Mobile", "Mobile respondents", "Instagram")

data_count_by_answer = total_count_by_answer(data_list)
data_count_by_segment_type = total_count_by_segment_type(data_list)



answers = ['Facebook', 'Instagram', 'Linkedin', 'Snapchat' ]
segment_type = ['Mobile','Web','Gender','University','Custom']

# Plotting by social media
fig, ax = plt.subplots(figsize=(8,4))
explode = (0, 0, 0, 0.1)
ax.pie(data_count_by_answer, labels=answers, autopct='%0.1f%%', explode=explode, shadow=True, startangle=90)
ax.axis('equal')
ax.legend(answers, title='Social Media', loc='upper right', labelcolor = 'blue')
ax.set_title('Respondent choice of social media', font = 'times new roman', size = 16, color='blue')
plt.show()

#Plotting by segment type
fig_1, ax = plt.subplots(figsize=(8,4))
explode_1 = (0, 0, 0, 0, 0.1)
ax.pie(data_count_by_segment_type, labels=segment_type, autopct='%0.1f%%', explode=explode_1, shadow=True, startangle=90)
ax.axis('equal')
ax.legend(segment_type, title='Respondents', loc='upper right', labelcolor = 'blue')
ax.set_title('Segment type', font = 'times new roman', size = 16, color='blue')
plt.show()