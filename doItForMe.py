import pyautogui
from selenium import webdriver
# print("Hello world!")

navegador = webdriver.Chrome()
navegador.get("https://weni.ai")
navegador.find_element_by_xpath('//*[@id="menu-item-35244"]/a')



# pyautogui.keyDown('alt') # mantém a tecla "alt" apertada
# pyautogui.press('tab') # pressiona a tecla "tab"
# pyautogui.keyUp('alt') # solta a tecla "alt"

# pyautogui.press('tab')