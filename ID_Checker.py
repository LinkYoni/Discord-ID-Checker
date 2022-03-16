import requests
import os
import colorama
from colorama import Fore, Style
from datetime import datetime
from getpass import getpass
import shutil

colorama.init()

def clear():
	os.system('cls')
clear()

token = '' #a bot token

headers={"Authorization": f"Bot {token}"}

default = ''' 
{0}{2}  ___ ____{1}     ____ _               _             
{0}{2} |_ _|  _ \ {1}  / ___| |__   ___  ___| | _____ _ __ 
{0}{2}  | || | | |{1} | |   | '_ \ / _ \/ __| |/ / _ \ '__|
{0}{2}  | || |_| |{1} | |___| | | |  __/ (__|   <  __/ |
{0}{2} |___|____/{1}   \____|_| |_|\___|\___|_|\_\___|_|

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.CYAN, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #default

correct = '''
{0}{2}  ___ ____{1}     ____ _               _             
{0}{2} |_ _|  _ \ {1}  / ___| |__   ___  ___| | _____ _ __ 
{0}{2}  | || | | |{1} | |   | '_ \ / _ \/ __| |/ / _ \ '__|
{0}{2}  | || |_| |{1} | |___| | | |  __/ (__|   <  __/ |
{0}{2} |___|____/{1}   \____|_| |_|\___|\___|_|\_\___|_|

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.GREEN, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #correct

fail = '''
{0}{2}  ___ ____{1}     ____ _               _             
{0}{2} |_ _|  _ \ {1}  / ___| |__   ___  ___| | _____ _ __ 
{0}{2}  | || | | |{1} | |   | '_ \ / _ \/ __| |/ / _ \ '__|
{0}{2}  | || |_| |{1} | |___| | | |  __/ (__|   <  __/ |
{0}{2} |___|____/{1}   \____|_| |_|\___|\___|_|\_\___|_|

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #fail

default_txt = ''' 
  ___ ____     ____ _               _             
 |_ _|  _ \   / ___| |__   ___  ___| | _____ _ __ 
  | || | | | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
  | || |_| | | |___| | | |  __/ (__|   <  __/ |
 |___|____/   \____|_| |_|\___|\___|_|\_\___|_|

 Coded by $ Yøni ⁶⁹ 🚬#0003

''' #default for txt

print(default)

res = requests.get(f'https://discordapp.com/api/v6/users/@me', headers=headers) #check if the given token is valid

if res.status_code == 200:
	user_id_input = input(f'{Fore.RED} [-] {Fore.RESET}ID: ')

	res = requests.get(f'https://discordapp.com/api/v6/users/{user_id_input}', headers=headers)
	res_json = res.json()

	if res.status_code == 200:
		clear()
		print(correct)
		user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
		discriminator = res_json["discriminator"]
		user_id = res_json['id']
		avatar_id = res_json['avatar']
		avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}'
		avatar = f"{avatar_url}.gif?size=1024" if requests.get(f'{avatar_url}.gif', headers=headers).status_code == 200 else f"{avatar_url}.png?size=1024"
		banner_id = res_json['banner']
		banner_url = f'https://cdn.discordapp.com/banners/{user_id}/{banner_id}'
		banner = f"{banner_url}.gif?size=1024" if requests.get(f'{banner_url}.gif', headers=headers).status_code == 200 else f"{banner_url}.png?size=1024"
		banner_color = res_json['banner_color']
		creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
		flags = res_json['public_flags']

		badges = []

		badges2 = {
			1 << 0:  'Discord Employee',
			1 << 1:  'Partnered Server Owner',
			1 << 2:  'HypeSquad Events',
			1 << 3:  'Bug Hunter Level 1',
			1 << 6:  'House Bravery',
			1 << 7:  'House Brilliance',
			1 << 8:  'House Balance',
			1 << 9:  'Early Supporter',
			1 << 10: 'Team User',
			1 << 12: 'System',
			1 << 14: 'Bug Hunter Level 2',
			1 << 16: 'Verified Bot',
			1 << 17: 'Early Verified Bot Developer',
			1 << 18: 'Certified Moderator'
		}

		user_badges = []

		for badge_flag, badge_name in badges2.items():
			if flags & badge_flag == badge_flag:
				user_badges.append(badge_name)

		x = discriminator
		last_num = int(x[3:])

		if last_num == 0 or last_num == 5:
			ava_def = '0'
		elif last_num == 1 or last_num == 6:
			ava_def = '1'
		elif last_num == 2 or last_num == 7:
			ava_def = '2'
		elif last_num == 3 or last_num == 8:
			ava_def = '3'
		elif last_num == 4 or last_num == 9:
			ava_def = '4'
		else:
			pass

		print(f''' ╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
 ┊ {Fore.RED}-> {Fore.YELLOW}Name: {Fore.RESET}{user_name}
 ┊ {Fore.RED}-> {Fore.YELLOW}ID: {Fore.RESET}{user_id}
 ┊ {Fore.RED}-> {Fore.YELLOW}Avatar: {Fore.RESET}{avatar if avatar_id != None else f'https://cdn.discordapp.com/embed/avatars/{ava_def}.png'}
 ┊ {Fore.RED}-> {Fore.YELLOW}Banner: {Fore.RESET}{banner if banner_id != None else "X"}
 ┊ {Fore.RED}-> {Fore.YELLOW}Banner Color: {Fore.RESET}{banner_color if banner_color != None else "Default"}
 ┊ {Fore.RED}-> {Fore.YELLOW}Creation Date: {Fore.RESET}{creation_date}
 ┊ {Fore.RED}-> {Fore.YELLOW}Badges: {Fore.RESET}{', '.join(user_badges) if user_badges != [] else "X"}
 ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯''')

		try:
			os.mkdir("Results")
		except:
			pass
		os.chdir("Results")

		date = datetime.now()
		os.mkdir(f"{user_id}_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}")
		directorio = (f"{user_id}_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}")
		os.chdir(directorio)

		info_txt = f''' ╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
 ┊ -> Name: {user_name}
 ┊ -> ID: {user_id}
 ┊ -> Avatar: {avatar if avatar_id != None else f'https://cdn.discordapp.com/embed/avatars/{ava_def}.png'}
 ┊ -> Banner: {banner if banner_id != None else "X"}
 ┊ -> Banner Color: {banner_color if banner_color != None else "Default"}
 ┊ -> Creation Date: {creation_date}
 ┊ -> Badges: {', '.join(user_badges) if user_badges != [] else "X"}
 ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯'''

		with open('Info.txt', "w", encoding="utf-8") as file:
			file.write(default_txt)
			file.write(info_txt)
		file.close()

		if avatar_id != None:
			image_url = f'{avatar_url}.gif' if requests.get(f'{avatar_url}.gif', headers=headers).status_code == 200 else f'{avatar_url}.png'
			filename = image_url.split("/")[-1]

			r = requests.get(image_url, stream = True)

			with open(filename,'wb') as f:
				shutil.copyfileobj(r.raw, f)
		else:
			image_url = f'https://cdn.discordapp.com/embed/avatars/{ava_def}.png'
			filename = image_url.split("/")[-1]

			r = requests.get(image_url, stream = True)

			with open(filename,'wb') as f:
				shutil.copyfileobj(r.raw, f)
		if banner_id != None:
			image_url = f'{banner_url}.gif' if requests.get(f'{banner_url}.gif', headers=headers).status_code == 200 else f'{banner_url}.png'
			filename = image_url.split("/")[-1]

			r = requests.get(image_url, stream = True)

			with open(filename,'wb') as f:
				shutil.copyfileobj(r.raw, f)
	else:
		clear()
		print(fail)
		print(f'{Fore.RED} [-] {Fore.RESET}Invalid ID (ID {Fore.RED}{user_id_input}{Fore.RESET} does not correspond to a user)\n')

elif res.status_code == 401:
	clear()
	print(fail)
	print(f'{Fore.RED} [-] {Fore.RESET}Invalid Token\n')

getpass("") # prevent from typing at the end
