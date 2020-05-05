# %%
import urllib

import requests

import googlesearch
import interruptingcow
import pandas as pd
import tika
from bs4 import BeautifulSoup
from library import start

# %% # Import list of Texas school districts
# We will eventually want to use a national dataset of districts
# Texas dataset from:
# https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/download/DownloadData.html
districts = pd.read_csv(os.path.join(start.dir_path + 'DREF.dat'))
districts = districts[['DISTRICT', 'DISTNAME', 'CNTYNAME', 'DFLCHART']]
districts = districts.loc[districts['DFLCHART'] == "N"] # drop charters
rename_var_dict = {'DISTRICT': 'distcode', 'DISTNAME': 'district', 
'CNTYNAME': 'county'}
districts = districts[list(rename_var_dict.keys())]
districts = districts.rename(index=str, columns=rename_var_dict)
districts.head()

# %%

# Random sample of 15 districts from proof of concept
districts = districts.sample(5, random_state=672)
districts