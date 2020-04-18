#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
from datetime import datetime
from modules.ConfigEngine import get_config, get_config_boolean


def get_days():
    containment_date = datetime(2020, 3, 17)  # Confinement
    today_date = datetime.today()

    number_of_days = str(today_date - containment_date)
    number_of_days = str([int(s) for s in number_of_days.split() if s.isdigit()])
    number_of_days = number_of_days.replace('[', '')
    number_of_days = number_of_days.replace(']', '')
    number_of_days = int(number_of_days) + 1  # Le confinement a débuté à midi.

    return str(number_of_days)

def check_time():
    if get_config_boolean('System', 'checkTime'):
        get_time_now = datetime.now().strftime("%H:%M")

        start_time = datetime.strptime(get_config('System', 'startTime'), '%H:%M')
        start_time = start_time.strftime('%H:%M')

        end_time = datetime.strptime(get_config('System', 'endTime'), '%H:%M')
        end_time = end_time.strftime('%H:%M')

        return start_time < get_time_now < end_time
    else:
        return True

def log_time():
    return "[" + datetime.now().strftime("%D %H:%M:%S") + "] "