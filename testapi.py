from typing import Tuple, List
from math import log

# importing required libraries
import requests, json

def getrates():   
    base = "http://api.currencylayer.com/live?access_key=98c124bf7435efa765502126e4a3f026&"

    #base url
    curl1 = base+ "source=JMD&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl2 = base+ "source=USD&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl3 = base+ "source=CAD&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl4 = base+ "source=GBP&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl5 = base+ "source=EUR&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl6 = base+ "source=TTD&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl7 = base+ "source=KYD&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"
    curl8 = base+ "source=CHF&currencies=JMD,USD,CAD,GBP,EUR,TTD,KYD,CHF&format=1"

    req1 = requests.get(curl1)
    req2 = requests.get(curl2)
    req3 = requests.get(curl3)
    req4 = requests.get(curl4)
    req5 = requests.get(curl5)
    req6 = requests.get(curl6)
    req7 = requests.get(curl7)
    req8 = requests.get(curl8)

    r1 = req1.json()
    r2 = req2.json()
    r3 = req3.json()
    r4 = req4.json()
    r5 = req5.json()
    r6 = req6.json()
    r7 = req7.json()
    r8 = req8.json()

    rates = []
    rate1 = []
    rate2 = []
    rate3 = []
    rate4 = []
    rate5 = []
    rate6 = []
    rate7 = []
    rate8 = []

    for value in r1['quotes'].values():
        rate1.append(value)
        
    rates.append(rate1)

    for value in r2['quotes'].values():
        rate2.append(value)

    rates.append(rate2)

    for value in r3['quotes'].values():
        rate3.append(value)

    rates.append(rate3)

    for value in r4['quotes'].values():
        rate4.append(value)

    rates.append(rate4)

    for value in r5['quotes'].values():
        rate5.append(value)

    rates.append(rate5)

    for value in r6['quotes'].values():
        rate6.append(value)

    rates.append(rate6)

    for value in r7['quotes'].values():
        rate7.append(value)

    rates.append(rate7)

    for value in r8['quotes'].values():
        rate8.append(value)

    rates.append(rate8)

    print (rates)
    return (rates)















    
