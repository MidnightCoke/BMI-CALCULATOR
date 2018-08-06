#!/usr/bin/env python
# -*- coding:utf8 -*-
import time

firstboy = float(input('boyunuz CM :'))
kilo = float(input('kilonuz KG :'))
boy = firstboy/100

ideal = kilo/boy**2
print('kutle indeksiniz')
print(ideal)

if ideal < 18.5 :

    print('Biraz kilo alsan pek fena olmaz. ')
    
elif ideal < 25 :

    print('kilonuz ideal. ')

elif ideal > 25 :

    print('fazla kilolarindan kurtulma zamani. ')

time.sleep(7)
