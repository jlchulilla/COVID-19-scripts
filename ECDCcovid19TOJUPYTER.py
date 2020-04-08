import pandas as pd
import numpy as np
from datetime import datetime

#source = https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

def descargatablaecdc(url):
    pd.options.mode.chained_assignment = None  # elimina aviso innecesario
    hoy = datetime.today().strftime("%d%m%Y")

    mundo = pd.read_csv(url)
    mundo.to_csv('ECDC' + hoy + '.csv')
    mundo['date'] = pd.to_datetime((mundo.year*10000+mundo.month*100+mundo.day).apply(str),format='%Y%m%d')

    dt = mundo[['date','deaths','cases','countriesAndTerritories', 'popData2018']]
    dt['DperHab'] = dt['deaths']/dt['popData2018']
    
    presalida = pd.pivot_table(dt.loc[(dt['countriesAndTerritories']=='Spain') | (dt['countriesAndTerritories']=='Italy') | (dt['countriesAndTerritories']=='Germany') | (dt['countriesAndTerritories']=='France') |  (dt['countriesAndTerritories']=='United_Kingdom') | (dt['countriesAndTerritories']=='Portugal') | (dt['countriesAndTerritories']=='Netherlands') | (dt['countriesAndTerritories']=='Iran') | (dt['countriesAndTerritories']=='China') | (dt['countriesAndTerritories']=='South_Korea')], index = ['date'], values=['deaths','cases','DperHab'], columns = 'countriesAndTerritories', aggfunc=np.sum, fill_value = 0)
    
    salida = presalida.reindex(axis = 1, level = 1, labels = ['Spain','Italy','Germany','France','United_Kingdom','Portugal','Netherlands','Iran','China','South_Korea'])
    
    
    salida.to_excel('ECDC' + hoy + '.xlsx')
    salida.cumsum().to_excel('agregados_ECDC' + hoy + '.xlsx')
    
    return()
descargatablaecdc('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
