from bs4 import BeautifulSoup
#from bs4.element import has_attr
import requests
import json
import asyncio
import aiohttp

def move_family_identifier(move_t, old_move, new_move):
    
 # Case 1: Moves belong to the same family by the first three characters
    if new_move[:3] == old_move[:3]:
        return True
    
    # Case 2: Special handling for '22' motions
    if '22' in old_move or '22' in new_move:
        return new_move[:2] == old_move[:2]
    
    # Case 3: Air-based special moves ('j.')
    if move_t == 'special_moves' and ('j.' in old_move or 'j.' in new_move):
        return new_move[:4] == old_move[:4]
    
    # Case 4: Follow-up moves always belong to the same family
    if 'Follow-up' in old_move:
        return True

    # Default case: No match
    return False
    
    
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
        
        index_tracker = 0
        move_index = 0
        regular_move_tracker = []
        version_move_tracker = []
        nomenclature = ''
        copy = []
        copy_obj = {}

        #move names and framedata
        move_simple_data = []
        move_version_data = []
        name_data = []
        regular_name_data = []
        version_name_data = []
        
        #2b moves
        
        twob_moves = {
            'normals': {
                'striking_assault' : {
                    'versions': []
                    },
                'slashing_assault': {
                    'versions': []
                    },
                'severing_assault': {
                    'versions': []
                    },
                'multistrike_protocol': { 
                    'versions': []
                    }
                },
                
            'unique_action': {
                'evasive_maneuver': {
                    'versions': []
                    },
                'grab_pod': {
                    'versions':[]
                    }
            }
        }
        
        frame_obj = {}
        character_framedata = {}

        for type in move_types:
            character_framedata[type] = {} 
        
       
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
                #print(index_tracker)
                move_info = move_src.find_all('div', class_='frameDataGridRow')
                move_names = move_src.find_all('span', class_='mw-headline')
                
                frame_obj = {}
                name_data = []

                # Collect move names and clean them
                for name in move_names:
                    if name['id'] in ['Air_Normals', 'Ground_Normals', 'Dash_Normals']:
                        continue
                    
                    else:
                        
                        name_parent = name.find_parent('h4') or name.find_parent('h3')
                        
                        if name_parent:
                            
                            attack_container = name_parent.find_next_sibling('div', class_='attack-container')
                            
                            
                            if attack_container:
                                attack_info = attack_container.find('div', class_='attack-info')
                                
                                
                                if attack_info:
                                    framedatagrid = attack_info.find('div', class_='frameDataGrid')
                                    
                                    
                                    if framedatagrid:
                                        col_column_checker = framedatagrid.find('div')
                                        
                                        if 'colCount-8' in col_column_checker['class']:
                                            name_data.append((name['id'].lower().replace('-', '_'), '8cols'))
                                            regular_name_data.append((name['id'].lower().replace('-', '_'), '8cols'))
                                        elif 'colCount-9' in col_column_checker['class']:
                                            name_data.append((name['id'].lower().replace('-', '_'), '9cols'))
                                            version_name_data.append((name['id'].lower().replace('-', '_'), '9cols'))
                                        else:
                                            print('No name info collected, we are dead') 
                               
                character_framedata[move_t] = {name: {} for name, flag in name_data}
                
                for move in move_info:
                    move_info_divs = move.find_all('div')
                    
                    if 'colCount-4' in move['class'] or 'colCount-3' in move['class']:
                        continue
                    
                    else:
                        
                        if any('colCount-8' in class_name for class_name in move['class']):
                            
                            move_simple_data.append([data_cell.text.strip() for data_cell in move_info_divs])
                            regular_move_tracker.append(move_index)
                            move_index += 1
                            
                        
                        elif any('colCount-9' in class_name for class_name in move['class']):
                        
                            version_move_tracker.append(move_index)
                            move_version_data.append([data_cell.text.strip() for data_cell in move_info_divs])
                            #print(f'''version move: {move_version_data}''')
                            move_index += 1
                           
                if self.name == '2B':
                    for m in move_version_data:
                        
                        move_nom = m[0]
                        
                        twob_obj = {
                            move_nom :{
                                'damage': m[1],
                                'guard': m[2],
                                'startup': m[3],
                                'active': m[4],
                                'recovery': m[5],
                                'on-block': m[6],
                                'on-hit': m[7],
                                'invul': m[8]
                                
                            }
                            }
                        if move_t == 'normals' and m[0].startswith('5L') and '~' not in  m[0]:                  
                            twob_moves['normals']['striking_assault']['versions'].append(twob_obj)
                        elif move_t == 'normals' and m[0].startswith('5M') and '~' not in  m[0]:                  
                            twob_moves['normals']['slashing_assault']['versions'].append(twob_obj)
                        elif move_t == 'normals' and m[0].startswith('5H') and '~' not in  m[0]:                  
                            twob_moves['normals']['severing_assault']['versions'].append(twob_obj)
                        elif move_t == 'normals' and '~' in  m[0]:                  
                            twob_moves['normals']['multistrike_protocol']['versions'].append(twob_obj)
                        elif move_t == 'unique_action' and 'U' in m[0]:
                            twob_moves['unique_action']['evasive_maneuver']['versions'].append(twob_obj)
                        else:
                            twob_moves['unique_action']['grab_pod']['versions'].append(twob_obj)
                            
                        twob_obj = {}
                            
                #print(json.dumps(twob_moves, indent=3))     
                                    
                                 
                                                        
                for (simple_name, _), simple_move, in zip(regular_name_data, move_simple_data):
                    #print(f'name: {simple_name}: data: {simple_move}')
                    
                    frame_obj = {
                                    'damage': simple_move[0],
                                    'guard': simple_move[1],
                                    'startup': simple_move[2],
                                    'active': simple_move[3],
                                    'recovery': simple_move[4],
                                    'on-block': simple_move[5],
                                    'on-hit': simple_move[6],
                                    'invul': simple_move[7]
                                }
                           
                    character_framedata[move_t][simple_name] = frame_obj      
                    frame_obj = {}  
                    
                
                for ver_name, _ in version_name_data:
                    
                    if 'versions' not in character_framedata[move_t].get(ver_name, {}):
                        character_framedata[move_t][ver_name]['versions'] = []
                        
                   
                    while move_version_data:
                        print(f'''{move_version_data}
                              
                              ''')
                        
                        element = move_version_data.pop(0)
                        version_key = element[0]
                        
                        if nomenclature == '':
                            nomenclature = version_key
                        print(version_key)
                        print(nomenclature)
                        
                        if '[' in version_key[:3]:
                            pass
                        
                        elif nomenclature[:3] != version_key[:3]:
                            
                            copy = element[:]
                            print(f'this is a copy: {copy}')
                            nomenclature = version_key
                            break #try changing this break to...
                        
                        if copy != []:
                            
                            copy_key = copy[0]
                            
                            copy_obj = {
                            copy_key: {
                                'damage': copy[0],
                                'guard': copy[1],
                                'startup': copy[2],
                                'active': copy[3],
                                'recovery': copy[4],
                                'on-block': copy[5],
                                'on-hit': copy[6],
                                'invul': copy[7]
                                }
                            }
                        
                            character_framedata[move_t][ver_name]['versions'].append(copy_obj)
                            copy_key = ''
                            copy_obj = {}
                            copy = []
                            #here
                        
                        version_obj = {
                            version_key: {
                                'damage': element[1],
                                'guard': element[2],
                                'startup': element[3],
                                'active': element[4],
                                'recovery': element[5],
                                'on-block': element[6],
                                'on-hit': element[7],
                                'invul': element[8]
                                }
                            }
                        
                        character_framedata[move_t][ver_name]['versions'].append(version_obj)
                        version_key = ''
                        version_obj = {}
                        
                        
                    if self.name == '2B':
                        if twob_moves[move_t]:
                            character_framedata[move_t][ver_name] = twob_moves[move_t][ver_name]  
                        else:
                            pass
                    
                        
                        
                    
                regular_name_data = []
                version_name_data = []            
                version_move_tracker = [] 
                regular_move_tracker= [] 
                move_simple_data = []
                move_version_data = []
                nomenclature = ''
                               
                move_index = 0        
                index_tracker += 1       
                
     
        character_framedata_json = json.dumps(character_framedata, indent=3)
        character_framedata_corrected = character_framedata_json.replace('\\u00d7', '×')
        print(character_framedata_corrected)
        self.framedata = character_framedata
        return self.framedata
    
    # Finally we create a function that awaits for the scraper to finish and it returns the dictionary with all of the character's info
    
    async def get_framedata(self):
        await self.character_scrape()
        return self.framedata
    

#use this to check if the scraper is working properly


new_char = Character('Avatar_Belial', 'https://www.dustloop.com/w/GBVSR/Avatar_Belial').character_scrape()
asyncio.run(new_char)
