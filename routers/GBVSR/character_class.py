from bs4 import BeautifulSoup
#from bs4.element import has_attr
import requests
import json
import asyncio
import aiohttp


class Character:
    
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.htmltext = None
        self.framedata = None
    
    async def set_htmltext(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    print(f'Successful response')
                    html_text = await response.text()
                    self.htmltext = html_text
                    return self.htmltext
                else:
                    print(f"Failed to fetch data for {self.name}. Status Code: {response.status}")
                    return None
        
    async def character_scrape(self):
        
        fetched_info = await self.set_htmltext()
        
        soup = ''
        normals = ''
        unique_action = ''
        universal_mechanics = ''
        special_moves = ''
        ultimate_skills = ''
        skybound_art = ''
        super_skybound_art = ''
        data = ['version', 'damage', 'guard', 'startup', 'active', 'recovery', 'on-block', 'on-hit', 'invul']
        move_types = ['normals', 'unique_action', 'universal_mechanics', 'special_moves', 'ultimate_skills', 'skybound_art', 'super_skybound_art']

        #move names and framedata
        move_data = []
        name_data = []
        
        frame_obj = {
                    'damage': '',
                    'guard': '',
                    'startup': '',
                    'active': '',
                    'recovery': '',
                    'on-block': '',
                    'on-hit': '',
                    'invul': ''
        }

        character_framedata = {}
        

        if fetched_info:
            soup = BeautifulSoup(fetched_info, 'lxml')
            normals = soup.find('section', attrs={'id':'citizen-section-2'})
            unique_action = soup.find('section', attrs={'id':'citizen-section-3'})
            universal_mechanics = soup.find('section', attrs={'id':'citizen-section-4'})
            special_moves = soup.find('section', attrs={'id':'citizen-section-5'})
            ultimate_skills = soup.find('section', attrs={'id':'citizen-section-6'})
            skybound_art = soup.find('section', attrs={'id':'citizen-section-7'})
            super_skybound_art = soup.find('section', attrs={'id':'citizen-section-8'})
            
            move_types_var = [normals, unique_action, universal_mechanics, special_moves, ultimate_skills, skybound_art, super_skybound_art]
            
#We're gonna run a loop to collect the information


            for move_t, move_src in zip(move_types, move_types_var):
                    
                move_info = move_src.find('div', class_='frameDataGridRow')
                move_names = move_src.find_all('span', class_ ='mw-headline')
                
                frame_obj[move_t] = {}
                #print(move_info)
                
                for name in move_names:
                    if name['id'] == 'Air_Normals':
                        continue
                    else:
                        name_data.append(name['id'])
                        print(name['id'])
                        
                        print(name_data)
                #name_data = []
                
                '''
                for move in move_names:
                    move_info_divs = move.find_all('div')
                    #print(move_info_divs)
                '''    
                '''
                    for i, data_cell in enumerate(move_info_divs[:9], start=1): 
                        move_data.append(data_cell.text.strip())
                        print(move_data)    
                        if len(move_data) == 8:
                            frame_obj[move_t] = {
                            'damage': move_data[0],
                            'guard': move_data[1],
                            'startup': move_data[2],
                            'active': move_data[3],
                            'recovery': move_data[4],
                            'on-block': move_data[5],
                            'on-hit': move_data[6],
                            'invul': move_data[7]
                            }   
                            
                
                                #print(json.dumps(frame_obj, indent=3)) 
                '''
                '''
                character_framedata.update(frame_obj)
                name_data = []
                nom_data = []
                frame_obj = {}
                '''
                

        self.framedata = character_framedata
        return self.framedata
    
    # Finally we create a function that awaits for the scraper to finish and it returns the dictionary with all of the character's info
    
    async def get_framedata(self):
        await self.character_scrape()
        return self.framedata
    

#use this to check if the scraper is working properly


new_char = Character('2b', 'https://www.dustloop.com/w/GBVSR/2B').character_scrape()
asyncio.run(new_char)
