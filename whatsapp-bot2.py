from random import betavariate
from bs4 import BeautifulSoup
import requests, pyautogui, time

def bot_spam(url, tag):
    time.sleep(20)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)
    print(html)
    
    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press('enter')
        
bot_spam('https://aminoapps.com/c/walkersbramino/page/blog/shrek-2-roteiro-completo-pt-br/bLNZ_lfoumGbqVdpZYxL5B5JEREDJz1bE', 'p')