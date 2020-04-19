#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
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

    # plt.ylabel(u'Graphique généré le ' + currentDT.strftime("%d-%m-%Y %H:%M:%S") + ' Par @COVID_France', fontsize = 7)
    plt.xlabel(u'Jours à partir du confinement: Mardi 17 Mars 2020',
               fontsize=12, style='italic')
    plt.title(u'AVANCÉE DU COVID-19 EN FRANCE\n(' +
              current_time.strftime("%d") + u' Avril 2020)', fontweight='bold')
    plt.legend(prop={'size': 11}, labelspacing=1.1)
    plt.grid(color='grey', linestyle='solid', linewidth=0.5)

    plt.savefig(directory + 'data/localGraph.png', format='png', dpi=200)

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
            if i >= 0 and i <= int(get_config('GraphConfig', 'countryView')):
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
    ax_total = ax.bar(x + width/2, total_cases_formated, width,
                      label=u'Population touchée', color='indianred')
    ax_recovered = ax.bar(x - width/2, total_recovered_formated,
                          width, label=u'Population guérie', color='yellowgreen')
    ax_deaths = ax.bar(x - width/2, total_deaths_formated,
                       width, label=u'Population décédée', color='dimgray')

    ax.set_xticks(x)
    ax.set_xticklabels(graph_labels, rotation=35, size=9.2,
                       backgroundcolor='dimgray', color='white')
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
    #add_label(ax_recovered, 7)
    #add_label(ax_deaths, 6)

    plt.grid(color='grey', linestyle='solid', linewidth=0.1)
    plt.title(u'AVANCÉE DU COVID-19 DANS LE MONDE\n(' +
              current_time.strftime("%d") + u' Avril 2020)', fontweight='bold')
    plt.savefig(directory + 'data/worldGraph.png', format='png', dpi=200)

    return


def save_data_graph(total_cases, sick_cases, severe_cases, dead_cases, recovered_cases):
    data_graph = open(directory + 'data/graphData.txt', 'a')
    data_graph.write(
        "0," + str(total_cases) + "," + str(sick_cases) + "," + str(severe_cases) + "," + str(dead_cases) + "," + str(
            recovered_cases) + "\n")
    data_graph.close()