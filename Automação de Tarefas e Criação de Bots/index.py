import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.3

# Open the browser
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

# Aceess the URL
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)

# Click on the username field
pyautogui.click(x=1840, y=410)
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.write('FASUNFAUSFNAOIMFIOAM')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# Import products list

products = pd.read_csv('./products.csv')

# Add products
for product in products.index:
    # Click on the id field
    pyautogui.click(x=1834, y=298)
    # Write the id name
    pyautogui.write(str(products.loc[product, 'codigo']))
    # Press tab to go to the brand field
    pyautogui.press('tab')
    # Write the brand name
    pyautogui.write(str(products.loc[product, 'marca']))
    # Press tab to go to the type field
    pyautogui.press('tab')
    # Write the type name
    pyautogui.write(str(products.loc[product, 'tipo']))
    # Press tab to go to the category field
    pyautogui.press('tab')
    # Write the category name
    pyautogui.write(str(products.loc[product, 'categoria']))
    # Press tab to go to the unit price field
    pyautogui.press('tab')
    # Write the unit price
    pyautogui.write(str(products.loc[product, 'preco_unitario']))
    # Press tab to go to the cost field
    pyautogui.press('tab')
    # Write the cost
    pyautogui.write(str(products.loc[product, 'custo']))
    # Press tab to go to the obs field
    pyautogui.press('tab')
    # Write the obs
    pyautogui.write('' if str(products.loc[product, 'obs']) == 'nan' else str(products.loc[product, 'obs']))
    # Press tab to go to the save button
    pyautogui.press('tab')
    # Press enter to save the product
    pyautogui.press('enter')
    # Scroll up to the top of the page
    pyautogui.scroll(5000)