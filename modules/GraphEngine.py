#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import pygal.maps.fr
from pygal.style import Style
import cairosvg

import matplotlib.image as image
import matplotlib.cbook as cbook

from modules.ConfigEngine import get_config
import os
import requests
import json
import datetime
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib

matplotlib.matplotlib_fname()
'/etc/matplotlibrc'
matplotlib.use('Agg')

directory = os.path.join(os.path.dirname(__file__), '../')
current_time = datetime.datetime.now()


def make_local_graph():
    days = []
    total_cases = []
    hospitalization_cases = []
    severe_cases = []
    dead_cases = []
    recovered_cases = []
    sick_cases = []

    with open(directory + 'data/graphData.txt', 'r') as csv_file:
        plots = csv.reader(csv_file, delimiter=',')
        for row in plots:
            days.append(int(row[0]))
            total_cases.append(int(row[1]))
            hospitalization_cases.append(int(row[2]))
            severe_cases.append(int(row[3]))
            dead_cases.append(int(row[4]))
            recovered_cases.append(int(row[5]))
            sick_cases.append(int(row[1]) - (int(row[4]) + int(row[5])))

    plt.style.use('seaborn-talk')

    # plt.plot(totalCases, label=u'Cas totaux confirmés', marker='o',color = 'darkorange', linewidth = 4)

    plt.plot(sick_cases, label=u'Population activement malade',
             marker='o', color='darkorange', linewidth=4)

    plt.plot(hospitalization_cases, label=u'Population activement hospitalisée', marker='o', color='indianred',
             linewidth=4)

    plt.plot(severe_cases, label=u"Population en réanimation",
             marker='o', color='maroon', linewidth=4)

    plt.plot(recovered_cases, label=u'Population guérie',
             marker='o', color='yellowgreen', linewidth=4)

    plt.plot(dead_cases, label=u"Population décédée",
             marker='o', color='dimgray', linewidth=4)

    plt.tick_params(axis='both', labelsize=15)

    ax = plt.axes()
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.ylabel(u'Twitter - @' + get_config('TwitterAPI',
                                           'account_name') + '\n', style='italic', fontsize=8)
    plt.xlabel(u'Jours à partir du confinement: Mardi 17 Mars 2020',
               fontsize=12, style='italic')
    plt.title(u'AVANCÉE DU COVID-19 EN FRANCE\n(' +
              current_time.strftime("%d") + u' Mai 2020)', fontweight='bold')
    plt.legend(prop={'size': 11}, labelspacing=1.1)
    plt.grid(color='grey', linestyle='solid', linewidth=0.5)

    plt.savefig(directory + 'data/localGraph.png', format='png', dpi=200)
    if not os.path.isdir('/var/www/html/covid19/data/' + datetime.datetime.now().strftime("%d-%m-%Y")):
        os.makedirs('/var/www/html/covid19/data/' +
                    datetime.datetime.now().strftime("%d-%m-%Y"))
    plt.savefig('/var/www/html/covid19/data/' + datetime.datetime.now().strftime(
        "%d-%m-%Y") + '/localGraph.png', format='png', dpi=200)

    return  # Le laisser sinon risque de duplication de légende


def sort(d, order):
    return [d[k] for k in sorted(order, key=order.get, reverse=True)]


def make_world_graph():
    worldometers_api = requests.get(
        "https://coronavirus-19-api.herokuapp.com/countries")
    worldometers_data = worldometers_api.json()
    line_count = len(worldometers_data)

    with open(directory + 'data/todayGouvData.json') as data:
        data = json.load(data)
        cas_confirmes = data['casConfirmes']
        total_deces = data['totalDeces']
        cas_gueris = data['casGueris']

    total_cases = {}
    dead_cases = {}
    recovered_cases = {}

    for i in range(line_count):
        if worldometers_data[i]['country'] == 'USA':
            x = i

    for i in range(x, x + int(get_config('GraphConfig', 'countryView'))):
        if not worldometers_data[i]['country'] == 'France':
            try:
                total_cases.update(
                    {str(worldometers_data[i]['country']): int(worldometers_data[i]['cases'])})
            except:
                total_cases.update({str(worldometers_data[i]['country']): 0})

            try:
                dead_cases.update(
                    {str(worldometers_data[i]['country']): int(worldometers_data[i]['deaths'])})
            except:
                dead_cases.update({str(worldometers_data[i]['country']): 0})

            try:
                recovered_cases.update(
                    {str(worldometers_data[i]['country']): int(worldometers_data[i]['recovered'])})
            except:
                recovered_cases.update(
                    {str(worldometers_data[i]['country']): 0})

        try:
            if 0 <= i <= int(get_config('GraphConfig', 'countryView')):
                total_cases.update({'France': cas_confirmes})
                dead_cases.update({'France': total_deces})
                recovered_cases.update({'France': cas_gueris})
        except:
            pass

    total_cases = {k: v for k, v in sorted(
        total_cases.items(), key=lambda item: item[1], reverse=True)}
    countries = list(total_cases.keys())

    for a in range(0, int(get_config('GraphConfig', 'countryView'))):
        countries = [sub.replace(countries[a], get_config(
            'TraductionGraph', countries[a])) for sub in countries]

    graph_labels = countries
    total_cases_formated = list(total_cases.values())
    total_deaths_formated = list(sort(dead_cases, total_cases))
    total_recovered_formated = list(sort(recovered_cases, total_cases))

    plt.style.use('seaborn-talk')

    x = np.arange(len(graph_labels))
    width = 0.275

    fig, ax = plt.subplots()
    ax_total = ax.bar(x + width / 2, total_cases_formated, width,
                      label=u'Population touchée', color='indianred')
    ax_recovered = ax.bar(x - width / 2, total_recovered_formated,
                          width, label=u'Population guérie', color='yellowgreen')
    ax_deaths = ax.bar(x - width / 2, total_deaths_formated,
                       width, label=u'Population décédée', color='dimgray')

    ax.set_xticks(x)
    ax.set_xticklabels(graph_labels, rotation=35, size=9.2,
                       backgroundcolor='dimgray', color='white')

    # plt.legend(prop={'size': 15}, labelspacing=5)
    plt.ylabel(u'Twitter - @' + get_config('TwitterAPI',
                                           'account_name') + '\n', style='italic', fontsize=8)
    ax.legend()
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    def add_label(rects, size):
        for rect in rects:
            height = rect.get_height()
            if height == 0:
                break
            else:
                ax.annotate('{0:,}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 1.5),
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=size, style='italic')

    add_label(ax_total, 10)
    # add_label(ax_recovered, 7)
    # add_label(ax_deaths, 6)

    plt.grid(color='grey', linestyle='solid', linewidth=0.1)
    plt.title(u'AVANCÉE DU COVID-19 DANS LE MONDE\n(' +
              current_time.strftime("%d") + u' Mai 2020)', fontweight='bold')
    plt.savefig(directory + 'data/worldGraph.png', format='png', dpi=200)
    if not os.path.isdir('/var/www/html/covid19/data/' + datetime.datetime.now().strftime("%d-%m-%Y")):
        os.makedirs('/var/www/html/covid19/data/' +
                    datetime.datetime.now().strftime("%d-%m-%Y"))
    plt.savefig('/var/www/html/covid19/data/' + datetime.datetime.now().strftime(
        "%d-%m-%Y") + '/worldGraph.png', format='png', dpi=200)

    return


def make_hospital_departements_map():
    data = {}

    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    gouv_data = requests.get(
        "https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.json")
    gouv_data = gouv_data.json()

    count_lines = len(gouv_data)

    try:
        for i in range(count_lines):
            if str(gouv_data[i]['date']) == today_date:
                # print(str(python_obj[i]['code']))
                dep_code = "DEP-" in (str(gouv_data[i]['code']))
                if dep_code:
                    dep_code = str(gouv_data[i]['code']).replace('DEP-', "")
                    data[str(dep_code)] = int(gouv_data[i]['hospitalises'])
    except:
        pass

    custom_style = Style(background='#FFFFFF', label_font_size=5,
                         title_font_size=20, title_font_family='jsp',
                         colors=('#cc0000', '#ffe6e6'))  # MOINs -> FORTE COULEUR

    fr_chart = pygal.maps.fr.Departments(style=custom_style, show_legend=False)
    fr_chart.title = '\nConcentration de la population hospitalisée en France\n[' + current_time.strftime(
        "%d") + u' Mai 2020]'
    fr_chart.add(today_date, data)
    fr_chart.render_to_png(directory + 'data/departements_hospital_map.png', dpi=1000)
    fr_chart.render_to_png(
        '/var/www/html/covid19/data/' + datetime.datetime.now().strftime("%d-%m-%Y") + 'departements_hospital_map.png',
        dpi=1000)

    return


def make_gueris_departements_map():
    today_data = {}
    yesterday_data = {}

    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday_date = (datetime.datetime.strptime(today_date, "%Y-%m-%d") - datetime.timedelta(days=1)).strftime(
        "%Y-%m-%d")

    gouv_data = requests.get(
        "https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.json")
    gouv_data = gouv_data.json()

    count = len(gouv_data)
    count_lines = len(gouv_data)

    try:
        for i in range(count_lines):
            if str(gouv_data[i]['date']) == today_date:
                # print(str(python_obj[i]['code']))
                dep_code = "DEP-" in (str(gouv_data[i]['code']))
                if dep_code:
                    dep_code = str(gouv_data[i]['code']).replace('DEP-', "")
                    today_data[str(dep_code)] = int(gouv_data[i]['gueris'])
    except:
        pass

    try:
        for i in range(count_lines):
            if str(gouv_data[i]['date']) == yesterday_date:
                # print(str(python_obj[i]['code']))
                dep_code = "DEP-" in (str(gouv_data[i]['code']))
                if dep_code:
                    dep_code = str(gouv_data[i]['code']).replace('DEP-', "")
                    yesterday_data[str(dep_code)] = int(gouv_data[i]['gueris'])
    except:
        pass

    final_data = {key: today_data[key] - yesterday_data.get(key, 0) for key in today_data}

    custom_style = Style(background='#FFFFFF', label_font_size=5,
                         title_font_size=20, title_font_family='jsp',
                         colors=('#00b300', '#ccffcc'))  # COULEUR CLAIRE, COULEUR FONCÉE

    fr_chart = pygal.maps.fr.Departments(style=custom_style, show_legend=False)
    fr_chart.title = '\nConcentration de nouveaux guéris en France\n[' + current_time.strftime("%d") + u' Mai 2020]'
    fr_chart.add(today_date, final_data)
    fr_chart.render_to_png(directory + 'data/departements_gueris_map.png', dpi=1000)
    fr_chart.render_to_png('/var/www/html/covid19/data/' + datetime.datetime.now().strftime(
        "%d-%m-%Y") + 'departements_gueris_map.png', dpi=1000)

    return


def save_data_graph(total_cases, sick_cases, severe_cases, dead_cases, recovered_cases):
    data_graph = open(directory + 'data/graphData.txt', 'a')
    data_graph.write(
        "0," + str(total_cases) + "," + str(sick_cases) + "," + str(severe_cases) + "," + str(dead_cases) + "," + str(
            recovered_cases) + "\n")
    data_graph.close()
