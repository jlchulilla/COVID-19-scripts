# COVID-19-scripts
COVID-19 scripts

## Introduction (EN)

This project is a simple repository of python scripts related with COVID-19 data. Since most of data sources are not tabular or aren't formatted properly, here I plan to upload small and simple scripts for help with that problem. Courtesy of www.onlineandoffline.com

If you have not used python before, you need to take some previous steps. If you use Linux or MacOS X, python comes by default. If you use windows, you have to download python. A tutorial about it: https://justcodeit.io/aprende-a-instalar-python-en-tu-ordenador/

Personally, I recommend Windows Subsystem Linux because in a linux environment there are some advantages to work with python, and with WSL you have the best of both worlds: your usual windows environment and a linux console. Instructions to download it: https://docs.microsoft.com/es-es/windows/wsl/install-win10

All the scripts to be published here are created in python3. In windows it is not a problem, but in linux we will have to install or update python3 separately.

In order to use more than the python base, we will need access to your libraries. For that, the best option is Pip. To install it in windows: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/ ; to install it in a Debian derivative: `$sudo apt-get install python3-pip`

IMPORTANT: TO ADD MODULES TO PYTHON3, IN LINUX YOU HAVE TO USE PIP3. IN WINDOWS, IF WE HAVE ONLY INSTALLED PYTHON, PIP

Then, to install pandas, in windows or linux the command is: `$pip3 install pandas` (`pip install pandas` in windows). The same applies to `numpy`, `jupyter`, `matplotlib` and `datetime`. 

## Introducción (ES)
Este proyecto es un simple almacén de scripts python creados para tratar los datos sobre el COVID-19. Dado que la mayoría de las fuentes no se ofrecen para ser descargadas de forma tabulada, o dado que las tablas no se ofrecen en formatos, el objetivo es ir subiendo scripts que ayuden a ahorrar tiempo a los que quieran acceder a los datos. Cortesía de www.onlineandoffline.com

Si no ha empleado python anteriormente, necesitas dar algunos pasos previos. Si empleas Linux o MacOS X, python viene por defecto. Si empleas windows, tienes que descargar python. Un tutorial al respecto: https://justcodeit.io/aprende-a-instalar-python-en-tu-ordenador/

Personalmente, recomiendo Windows Subsystem Linux porque en un entorno linux hay algunas ventajas para trabajar con python, y con WSL se tiene lo mejor de los dos mundos: tu entorno windows habitual y una consola linux. Instrucciones para descargarlo: https://docs.microsoft.com/es-es/windows/wsl/install-win10

Todos los scripts que se van a publicar aquí están creados en python3. En windows no es un problema, pero en linux tendremos que instalar o actualizar python3 por separado.

Para poder emplear algo más que la base de python, necesitaremos acceso a sus bibliotecas. Para eso, la mejor opción es Pip. Para instalarla en windows: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/ ; para instalarla en un derivado de Debian: `$sudo apt-get install python3-pip`

IMPORTANTE: PARA AÑADIR MÓDULOS A PYTHON3, EN LINUX HAY QUE EMPLEAR PIP3. EN WINDOWS, SI SOLO HEMOS INSTALADO PYTHON, BASTA CON PIP

Después, para instalar pandas, en windows o linux el comando es: `$pip3 install pandas (pip install pandas en windows)`. Lo mismo aplica para `numpy`, `jupyter`, `matplotlib` y `datetime` . 

## Contact (EN)
If you have any questions, please contact us using github, at twitter.com/Poliorcetes or www.linkedin.com/in/jlchulilla/

## Contacto (ES)
Si tiene alguna duda, contacte con nosotros usando github, a twitter.com/Poliorcetes o a www.linkedin.com/in/jlchulilla/

## ECDCtables.py (EN)
This script, based on Pandas, downloads from the ECDC (https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide) a `.csv` file with the updated data of daily cases and deaths due to the COVID-19 pandemic. It downloads it as csv raw data in the directory where we have installed the script, normalizing the file name to the date of the day.

Then, it selects only the fields that interest us (and that we can change at our convenience), generate a pivot table, ordering the data by date and nation.

Finally, it reorders the nations for a previous project we have underway. You can use that for the order you need. It ends up generating an excel file by normalizing the file name to the date of the day.

## ECDCtables.py (ES)
Este script, basado en Pandas, descarga del ECDC (https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide) un archivo `.csv` con los datos actualizados de casos y de fallecimientos diarios debido a la pandemia de COVID-19. Lo descarga en bruto en el directorio donde tengamos instalado el script, normalizando el nombre de archivo a la fecha del día.

A continuación, selecciona sólo los campos que nos interesan (y que podemos cambiar a nuestra conveniencia), genera una tabla pivot (dinámica para los usuarios de excel, benditas localizaciones de Microsoft a español que rompen con los términos usados internacionalmente) ordenando los datos por fecha y nación.

Después, reordena las naciones para un proyecto previo que tenemos en marcha. Se puede aprovechar para el orden que necesite cada uno. Acaba generando un archivo excel normalizando el nombre de archivo a la fecha del día.

## ECDCcovid19TOJUPYTER.ipynb (EN)
`EDCcovid19TOJUPYTER.ipynb` is the transformation of ECDCTables into jupiter notebooks. It adds two extra tables to represent in real time the evolution of the selected metrics. Example:

![](https://i.imgur.com/chVzcnx.png)

## ECDCcovid19TOJUPYTER.ipynb (ES)
`ECDCcovid19TOJUPYTER.ipynb` es la transformación de ECDCTables en cuaderno jupyter. Añade dos tablas extra para representar en tiempo real la evolución de las métricas seleccionadas. Ejemplo:

![](https://i.imgur.com/chVzcnx.png)
