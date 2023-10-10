import pandas as pd
import numpy as np

df_original = pd.read_csv('Cleaned.csv')

columns = [
    'International ID',
    'Storm Names',
    'Date and Time',
    'Grade',
    'Latitude of the Center',
    'Longitude of the Center',
    'Central Pressure',
    'Maximum sustained wind speed',
    'Direction of the longest radius of 50kt winds or greater',
    'Longest radius of 50kt winds or greater',
    'Shortest radius of 50kt winds or greater',
    'Direction of the longest radius of 30kt winds or greater',
    'Longest radius of 30kt winds or greater'
]

na_count = df_original[columns].isna().sum()

columns_to_drop = [
    'Maximum sustained wind speed',
    'Direction of the longest radius of 50kt winds or greater',
    'Longest radius of 50kt winds or greater',
    'Shortest radius of 50kt winds or greater',
    'Direction of the longest radius of 30kt winds or greater',
    'Longest radius of 30kt winds or greater'
]

df = df_original.drop(columns_to_drop, axis =1)

import streamlit as st
from matplotlib import pyplot as plt

td = len(df[df.Grade == 'Tropical Depression (TD)'].count(axis=1))
ts = len(df[df.Grade == 'Tropical Storm (TS)'].count(axis=1))
sts = len(df[df.Grade == 'Severe Tropical Storm (STS)'].count(axis=1))
ty = len(df[df.Grade == 'Typhoon (TY)'].count(axis=1))
l = len(df[df.Grade == 'Extra-tropical Cyclone (L)'].count(axis=1))

grade_ocurrence = [td, ts, sts, ty, l]

grade = ['Tropical Depression (TD)',
    'Tropical Storm (TS)',
    'Severe Tropical Storm (STS)',
    'Typhoon (TY)',
    'Extra-tropical Cyclone (L)']

data_ocurrence = pd.DataFrame(grade_ocurrence,grade)

st.bar_chart(data_ocurrence)

datetime_ocurrence = df.loc[:,'Date and Time']
grades = df.loc[:,'Grade']

grade_per_datetime = pd.DataFrame(datetime_ocurrence,grades)

st.line_chart(grade_per_datetime)