#!/usr/bin/python3
"""Import the requests library"""
import requests


url = 'http://158.69.76.135/level0.php'

for i in range(0, 1004):
    data = {"id": "4297", "holdthedoor": "Enviar"}
    result = requests.post(url, data=data)
