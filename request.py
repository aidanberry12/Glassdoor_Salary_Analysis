# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:20:06 2020

@author: aidan
"""



import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400})

print(r.json())