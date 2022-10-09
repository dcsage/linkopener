import asyncio
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from colorama import init as colorama_init

colorama_init()

print(f'''{Fore.LIGHTGREEN_EX}
██╗░░░░░██╗███╗░░██╗██╗░░██╗  ░█████╗░██████╗░███████╗███╗░░██╗███████╗██████╗░
██║░░░░░██║████╗░██║██║░██╔╝  ██╔══██╗██╔══██╗██╔════╝████╗░██║██╔════╝██╔══██╗
██║░░░░░██║██╔██╗██║█████═╝░  ██║░░██║██████╔╝█████╗░░██╔██╗██║█████╗░░██████╔╝
██║░░░░░██║██║╚████║██╔═██╗░  ██║░░██║██╔═══╝░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗
███████╗██║██║░╚███║██║░╚██╗  ╚█████╔╝██║░░░░░███████╗██║░╚███║███████╗██║░░██║
╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝{Fore.CYAN}''')

print(" ")
print(" ")

yesorno = input('''  [X]    Start Opening Links (y/n) : ''')



async def openlinks():
    a = 0
    opts = Options()
    link_file = open('links.txt','r')
    lines = link_file.readlines()
    for line in lines:
        linkk = line.strip()
        a = a + 1
        print(f'''  [|]    Link gotten ({a} / {len(lines)})''')
        browser = Chrome(options=opts)
        browser.minimize_window()
        browser.get(f'{linkk}')
        print(f'''  [|]    Link Loaded ({a} / {len(lines)})''')
        await asyncio.sleep(1)
        print(f'''  [|]    Link Visited ({a} / {len(lines)})''')
        browser.quit()
        await asyncio.sleep(1)
    print("")
    print(f'''  [|]    All Links Visited.''')
    await asyncio.sleep(10000)

if yesorno == 'y' or yesorno == 'Y':
    asyncio.run(openlinks())
else:
    pass
