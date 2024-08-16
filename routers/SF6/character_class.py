from bs4 import BeautifulSoup
import requests
import json
import asyncio
import aiohttp

'''
In this module, we're building a web scraper, to use on the Super Combo Wiki of SF6, to extract the frame data of the 20 characters in the game so far.
In order to do that, I'll use the builder method, because, while it is true that most characters have the same components to their moveset,
'Chun-Li', has an extra stance that requires an extra subdictionary, and also, the frame data for everyone is different, so the instances of the 'Character' class
aren't built equally
'''

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
        normal_names = ''
        command_normals = ''
        tgt_combos = ''
        throw_data = ''
        drv_sys = ''
        specials = ''
        supers = ''
        taunts = ''
        phase = ['Startup', 'Active', 'Recovery', 'Cancel', 'Damage', 'Guard', 'On Hit', 'On Block']
        move_types = ['normals', 'command_normals', 'target_combos', 'throws', 'drive_system', 'special_moves', 'super_arts', 'taunts', 'serenity_stream']

        #move names and framedata
        nom_data = []
        name_data = []
        frame_data = []
        frame_obj = {}

        group_size = 8
        character_framedata = {}
        

        if fetched_info:
            soup = BeautifulSoup(fetched_info, 'lxml')
            normals = soup.find('section', attrs={'id':'section-collapsible-1'})
            command_normals = soup.find('section', attrs={'id':'section-collapsible-2'})
            target_combos = soup.find('section', attrs={'id':'section-collapsible-3'})
            throws = soup.find('section', attrs={'id':'section-collapsible-4'})
            drive_system = soup.find('section', attrs={'id':'section-collapsible-5'})
            special_moves = soup.find('section', attrs={'id':'section-collapsible-6'})
            super_arts = soup.find('section', attrs={'id':'section-collapsible-7'})
            taunts = soup.find('section', attrs={'id':'section-collapsible-8'})
            
            move_types_var = [normals, command_normals, target_combos, throws, drive_system, special_moves, super_arts, taunts]
            
            if self.name.lower() == 'chun-li':
                serenity_stream = soup.find('section', attrs={'id':'section-collapsible-4'}) 
                throws = soup.find('section', attrs={'id':'section-collapsible-5'})
                drive_system = soup.find('section', attrs={'id':'section-collapsible-6'})
                special_moves = soup.find('section', attrs={'id':'section-collapsible-7'})
                super_arts = soup.find('section', attrs={'id':'section-collapsible-8'})
                taunts = soup.find('section', attrs={'id':'section-collapsible-9'})

                move_types_var = [normals, command_normals, target_combos, throws, drive_system, special_moves, super_arts, taunts, serenity_stream]
            
                
            else:
                pass
            
#We're gonna run a loop to collect the information

            for move_t, move_src in zip(move_types, move_types_var):
                
                frame_obj[move_t] = {}
                     
                if move_src:
                   info_divs = move_src.find_all('div', class_='movedata-flex-framedata-name-item movedata-flex-framedata-name-item-middle') 
                   
                
                #Loop to get the name and nomenclature of each move
                     
                for move in info_divs:
                    
                    move_nom_div = move.find('div', attrs={'style':''})
                    if move_nom_div:
                        nom_data.append(move_nom_div.text.strip())
                    
                    move_name_div = move.find('div', attrs={'style':"font-size:80%"})
                    if move_name_div:
                        name_data.append(move_name_div.text.strip())
                        
                #get frame data of moves       
                
                framedata_div = move_src.find_all('div', class_='movedata-flex-framedata-table')
    
                for framedata in framedata_div:
                    find_move_table = framedata.find('table', class_='wikitable citizen-table-nowrap')
                    find_move_data = find_move_table.find_all('td', attrs={'style':'text-align:center;'})
                    for i, data in enumerate(find_move_data):
                        
                        if i % group_size == 0:
                            current_group = []

                        current_group.append(data.text.replace('\n',''))

                        if (i + 1) % group_size == 0 or i == len(find_move_data) - 1:
                            frame_data.append(current_group)
               
            
                for first_key, second_key, value in zip(name_data, nom_data, frame_data):
                    
                    if move_t == 'special_moves':
                        if second_key.endswith('LP') or second_key.endswith('LK') == True:
                            first_key = f'L_{first_key}'
                        elif second_key.endswith('MP') or second_key.endswith('MK') == True:
                            first_key = f'M_{first_key}'
                        elif second_key.endswith('HP') or second_key.endswith('HK') == True:
                            first_key = f'H_{first_key}'
                        elif second_key.endswith('PP') or second_key.endswith('KK') == True:
                            first_key = f'EX_{first_key}'
                                        
                    if first_key not in frame_obj[move_t]:
                        frame_obj[move_t][first_key] = {}
                    if second_key not in frame_obj[move_t][first_key]:
                        frame_obj[move_t][first_key][second_key] = {}

                    for i in range(8):
                        sub_phase = f'{phase[i]}'
                        sub_value = f'{value[i]}' 
                        frame_obj[move_t][first_key][second_key][sub_phase] = sub_value

                character_framedata.update(frame_obj)
                name_data = []
                nom_data = []
                frame_obj = {}
            

        self.framedata = character_framedata
        return self.framedata
    
    # Finally we create a function that awaits for the scraper to finish and it returns the dictionary with all of the character's info
    
    async def get_framedata(self):
        await self.character_scrape()
        return self.framedata
    

#use this to check if the scraper is working properly

'''
new_char = Character('ryu', 'https://wiki.supercombo.gg/w/Street_Fighter_6/Ryu').get_framedata()
print(json.dumps(asyncio.run(new_char), indent=3))
'''