import pyautogui
import time

#3 segundos para preparação
time.sleep(3); 

#Pressionar tecla Windows 
pyautogui.press('win'); 
time.sleep(1); 

#Digitar programa
pyautogui.write('youtube'); 
time.sleep(1); 

#Pressionar Enter
pyautogui.press('enter'); 
time.sleep(2); 

#Digitar texto
pyautogui.write('Automação finalizada!'); 