import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
df = pd.read_csv('/content/drive/MyDrive/Colab_Notebooks/datasets/student_performance.csv')
df.head()
df.shape
df.info()
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

factor = "Motivation_Level"
target = "Exam_Score"
groups = [group[target].values for name, group in final_data.groupby(factor)]
group_names = final_data[factor].unique()

##darshan commit(first)->
factor = "Motivation_Level"
target = "Exam_Score"
groups = [group[target].values for name, group in final_data.groupby(factor)]
group_names = final_data[factor].unique()

##darshan commit(second)->
group_means = [np.mean(g) for g in groups]
overall_mean = np.mean(np.concatenate(groups))
n_i = [len(g) for g in groups]
k = len(groups)
N = sum(n_i)
# SSB
SSB = sum(n_i[i] * (group_means[i] - overall_mean)**2 for i in range(k))
# SSW
SSW = sum(sum((x - group_means[i])**2 for x in groups[i]) for i in range(k))
# Degrees of freedom
df_between = k - 1
df_within = N - k
# MS
MSB = SSB / df_between
MSW = SSW / df_within
# F
F_stat, p_value = f_oneway(*groups)
print("SSB:", SSB)
print("SSW:", SSW)
print("MSB:", MSB)
print("MSW:", MSW)
print("F-statistic:", F_stat)
print("p-value:", p_value)






