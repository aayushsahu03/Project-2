
# from collections import namedtuple
# n=int(input())
# sheet=namedtuple('sheet',input().split())
# marks=0
# for i in range(n):
#     row=sheet(",".join(input().split()))
#     marks+=int(row.MARKS)

# print(marks/n)

# inp=input().split()
# print(*inp) # unpacking tuples when using in this form

import os
from turtle import ScrolledCanvas
import pandas as pd
import re

df = pd.read_csv("D:\ISI\Placement\Student profiles\Student profiles.csv", usecols=[
                 'Student Name', 'Student ID  ( eg. DSTC-XXX)'])
df = df.iloc[:, 0].str.title().str.strip()
print(type(df))
df = df.sort_values(ascending=True)
names = df.values


def name_change():
    folder = "D:/test"
    for name in names:
        for fname in os.listdir(folder):
            if bool(re.search(name.lower().split()[0], fname.lower())):
                try:
                    src = f"{folder}/{fname}"
                    des = f"{folder}/{name}.pdf"
                    os.rename(src, des)
                except FileExistsError:
                    src = f"{folder}/{fname}"
                    des = f"{folder}/{name}-2.pdf"
                    os.rename(src, des)


name_change()
