#import library
#%%
import  pandas as pd
import requests
from bs4 import BeautifulSoup

# get url object
#%%
url = 'https://www.worldometers.info/coronavirus/'

# create object page
#%%
page = requests.get(url)
print(page)

# get information web
#%%
soup = BeautifulSoup(page.text,'lxml')
print(soup)

# get information taq table 
#%%
tabel = soup.find('table', id='main_table_countries_today')
print(tabel)


# get name column taq th
#%%
headers = []
for i in tabel.find_all('th'):
    judul = i.text
    headers.append(judul)
    
headers[13] = 'Tests/1M pop'

# create dataframe 
#%%
data = pd.DataFrame(columns=headers)

# fill data frame
#%%
for j in tabel.find_all('tr')[1:]:
    data_baris = j.find_all('td')
    baris = [tr.text for tr in data_baris]
    panjang = len(data)
    data.loc[panjang] = baris
    
    
# drop data no use
#%%
data.drop(data.index[0:7], inplace=True)

data.drop(data.index[222:229], inplace=True)

data.reset_index(inplace=True,drop=True)

# drop column #
#%%
data.drop('#',inplace=True, axis=1)

# export to cvs
#%%
data.to_csv('data_covid.csv', index=False)

# open file csv
#%%
new_data = pd.read_csv('data_covid.csv')

