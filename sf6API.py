from bs4 import BeautifulSoup
import requests
import textwrap

html_text = requests.get('https://wiki.supercombo.gg/w/Street_Fighter_6/Chun-Li').text
soup = BeautifulSoup(html_text, 'lxml')
move_names = soup.find_all('div', attrs= {'class': 'movedata-flex-framedata-name'})
table = soup.find_all('table', class_='wikitable citizen-table-nowrap')

#Lo siguiente es modificar la funcion para que segun el personaje me de la data. Es decir, hay que volverlo un metodo

def find_move_names(move_names):
    if move_names:
        name_data = []
        for move in move_names:
            divs = move.find('div')
            names = [div.get_text(strip=True) for div in divs]
            name_data.extend(names)
        print(name_data[0])
        
        if name_data:
            return [name_data[0]]
        else: 
            return None
    else:
        print('Move not found')

find_move_names(move_names[0])


def find_framedata(table):
    if table:
        for row in table.find_all('tr'):
            row_data = [td.get_text(strip=True) for td in row.find_all('td')]
        print(row_data)
        return row_data
    else:
        print('Table not found')
find_framedata(table[0])




