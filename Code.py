import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
df = pd.read_csv('/content/drive/MyDrive/Colab_Notebooks/datasets/student_performance.csv')
df.head()
data = df[['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Motivation_Level', 'Exam_Score']]
data.head()
data['Sleep_Category'] = pd.cut(
    data['Sleep_Hours'],
    bins=[0,4,7,10],
    labels=['Low','Medium','High']
)
data['Study_Level'] = pd.cut(
    data['Hours_Studied'],
    bins=[0,21,42,70],
    labels=['Low','Medium','High']
)
data['Attendance_Level'] = pd.cut(
    data['Attendance'],
    bins=[0,60,80,100],
    labels=['Low','Medium','High']
)
final_data = data.drop(['Hours_Studied', 'Attendance', 'Sleep_Hours'], axis=1)