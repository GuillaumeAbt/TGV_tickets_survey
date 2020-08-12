#!/usr/bin/python
#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from time import gmtime, strftime
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

dates=["12%2F12%2F2018","13%2F12%2F2018","14%2F12%2F2018","15%2F12%2F2018",\
     "16%2F12%2F2018","17%2F12%2F2018","18%2F12%2F2018","19%2F12%2F2018","20%2F12%2F2018","21%2F12%2F2018",\
     "22%2F12%2F2018","23%2F12%2F2018","24%2F12%2F2018","25%2F12%2F2018","26%2F12%2F2018","27%2F12%2F2018",\
     "28%2F12%2F2018","29%2F12%2F2018","30%2F12%2F2018","31%2F12%2F2018","01%2F01%2F2019","02%2F01%2F2019",\
     "03%2F01%2F2019","04%2F01%2F2019","05%2F01%2F2019","06%2F01%2F2019","07%2F01%2F2019","08%2F01%2F2019",\
     "09%2F01%2F2019","10%2F01%2F2019"]
while(True):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        with open('Paris-Rennes.csv', 'a') as writeFile:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--incognito")
                chrome_options.add_argument("headless")
                for date in dates:
                        driver.implicitly_wait(180)
                        driver.get("https://www.kelbillet.com/recherche/recherche-billet.php?depart=Paris&arrivee=Re$
                        time.sleep(10)
                        link=driver.find_element_by_css_selector(".resu.resu-1 .kb-search-result-content-more-res a")
                        source=driver.execute_script("return document.documentElement.outerHTML")
                        page_content = BeautifulSoup(source, "html.parser")
                        metas = page_content.find_all("li", {"class":"kb-search-result-content-offer ligne"})
                        liste_heure=[]
                        liste_nom=[]
                        for meta in metas:
                                h=meta.find("div",{"class":"heure"})
                                for nom in h.find_all("span"):
                                        liste_nom.append(nom.contents[0])
                                for  horaire in h.find_all("i"):
                                        liste_heure.append(horaire.contents[0])
                                try:
                                        if(int(meta.attrs['data-type-id'])==1 and "Paris" in liste_nom[0]):
                                        #print (str(strftime("%Y-%m-%d", gmtime()))+","+str(strftime("%H:%M:%S", gmt$
                                                writeFile.write(str(strftime("%Y-%m-%d", gmtime()))+","+str(strftime$
                                                writeFile.write("\n")
                                except:
                                        pass
                                liste_heure,liste_nom=[],[]

        writeFile.close()
        with open('Rennes-Paris.csv', 'a') as writeFile:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--incognito")
                chrome_options.add_argument("headless")
                for date in dates:
        #        print("Rennes->Paris")
#                print(date)
#                print("--------------")
                        driver.implicitly_wait(180)
                        driver.get("https://www.kelbillet.com/recherche/recherche-billet.php?depart=Rennes&arrivee=P$
                        time.sleep(10)

                        link=driver.find_element_by_css_selector(".resu.resu-1 .kb-search-result-content-more-res a")
                        source=driver.execute_script("return document.documentElement.outerHTML")
                        page_content = BeautifulSoup(source, "html.parser")
                        metas = page_content.find_all("li", {"class":"kb-search-result-content-offer ligne"})
                        liste_heure=[]
                        liste_nom=[]
                        for meta in metas:
                                h=meta.find("div",{"class":"heure"})
                                for nom in h.find_all("span"):
                                        liste_nom.append(nom.contents[0])
                                for  horaire in h.find_all("i"):
                                        liste_heure.append(horaire.contents[0])
  try:
                                        if(int(meta.attrs['data-type-id'])==1 and "Paris" in liste_nom[1]):
                                                #print (str(strftime("%Y-%m-%d", gmtime()))+","+str(strftime("%H:%M:$
                                                writeFile.write(str(strftime("%Y-%m-%d", gmtime()))+","+str(strftime$
                                                writeFile.write("\n")

                                except:
                                        pass
                                liste_heure,liste_nom=[],[]

        writeFile.close()

        driver.quit()
        time.sleep(3000)

display.stop()
