%matplotlib widget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# if you want dynamic plots, start with %matplotlib widget

#source = https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

def descargatablaecdc(url):

    hoy = datetime.today().strftime("%d%m%Y")

    mundo = pd.read_csv(url)
    mundo.to_csv('ECDC' + hoy + '.csv')
    
    mundo['date'] = pd.to_datetime((mundo.year*10000+mundo.month*100+mundo.day).apply(str),format='%Y%m%d')

    dt = mundo[['date','deaths','cases','countriesAndTerritories']]

    presalida = pd.pivot_table(dt.loc[(dt['countriesAndTerritories']=='Spain') | (dt['countriesAndTerritories']=='Italy') | (dt['countriesAndTerritories']=='Germany') | (dt['countriesAndTerritories']=='France') |  (dt['countriesAndTerritories']=='United_Kingdom') | (dt['countriesAndTerritories']=='Portugal') | (dt['countriesAndTerritories']=='Netherlands') | (dt['countriesAndTerritories']=='Iran') | (dt['countriesAndTerritories']=='China') | (dt['countriesAndTerritories']=='South_Korea')], index = ['date'], values=['deaths','cases'], columns = 'countriesAndTerritories', aggfunc=np.sum, fill_value = 0)
    precasosspait = pd.pivot_table(dt.loc[(dt['countriesAndTerritories']=='Spain') | (dt['countriesAndTerritories']=='Netherlands')| (dt['countriesAndTerritories']=='Italy') ], index = ['date'], values=['cases'], columns = 'countriesAndTerritories', aggfunc=np.sum, fill_value = 0)
    prefallecspait= pd.pivot_table(dt.loc[(dt['countriesAndTerritories']=='Spain') | (dt['countriesAndTerritories']=='Netherlands')| (dt['countriesAndTerritories']=='Italy') ], index = ['date'], values=['deaths'], columns = 'countriesAndTerritories', aggfunc=np.sum, fill_value = 0)

    salida = presalida.reindex(axis = 1, level = 1, labels = ['Spain','Italy','Germany','France','United_Kingdom','Portugal','Netherlands','Iran','China','South_Korea'])
    casosspait = precasosspait.reindex(axis = 1, level = 1, labels = ['Spain','Italy','Netherlands'])
    fallecspait = prefallecspait.reindex(axis = 1, level = 1, labels = ['Spain','Italy','Netherlands'])


    salida.to_excel('ECDC' + hoy + '.xlsx')
    
    plt.rcParams["figure.figsize"] = (8,5)
    
    casosspait.plot()#(xticks=casosspait.index)#(xticks='day')
    plt.ylabel('casos España e Italia');
    fallecspait.plot()
    plt.ylabel('fallecimientos España e Italia');
    return()



descargatablaecdc('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')

