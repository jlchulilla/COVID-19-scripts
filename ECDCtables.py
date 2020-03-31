import pandas as pd
from datetime import datetime

#source = https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

def descargatablaecdc(url):

    hoy = datetime.today().strftime("%d%m%Y")

    mundo = pd.read_csv(url)
    mundo.to_csv('ECDC' + hoy + '.csv')

    dt = mundo[['dateRep','day', 'month', 'year','deaths','cases','countriesAndTerritories']]

    presalida = pd.pivot_table(dt.loc[(dt['countriesAndTerritories']=='Spain') | (dt['countriesAndTerritories']=='Italy') | (dt['countriesAndTerritories']=='Germany') | (dt['countriesAndTerritories']=='France') |  (dt['countriesAndTerritories']=='United_Kingdom') | (dt['countriesAndTerritories']=='Portugal') | (dt['countriesAndTerritories']=='Netherlands') | (dt['countriesAndTerritories']=='Iran') | (dt['countriesAndTerritories']=='China') | (dt['countriesAndTerritories']=='South_Korea')], index = ['year','month','day'], values=['deaths','cases'], columns = 'countriesAndTerritories', fill_value = 0)

    salida = presalida.reindex(axis = 1, level = 1, labels = ['Spain','Italy','Germany','France','United_Kingdom','Portugal','Netherlands','Iran','China','South_Korea'])

    salida.to_excel('ECDC' + hoy + '.xlsx')
    return()

descargatablaecdc('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
