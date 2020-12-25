# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess
import os
import download

def getlinks():
    allLinkFiles = list()
    driver = webdriver.Chrome(download.saveFile() + "\\IDE\\chromedriver.exe")
    # to maximize the browser window
    driver.minimize_window()
    driver.get("https://truyenaudio.org/kiem-hiep/nghe-truyen/pham-nhan-tu-tien-truyen-tien-hiep.html")

    print("**************************************************************************************")
    print("                                 GETLINK...")
    print("**************************************************************************************")

    click = driver.find_elements_by_class_name("download-item")
    path = download.saveFile() + "\\src\\test.sh"

    if os.path.exists(path):
        os.remove(path)
    f = open((path), "a")
    f.write("#!/bin/bash\n\n\n")

    pause = 200
    for i in range(200, 466):
        
        if i == (pause + 5):
            f.write("echo -p \"---------------> PAUSED <--------------------\"\n")
            pause += 5
            os.system("pause")
        temp = click[i].get_attribute("href")
        f.write("start \"" + temp + "\"\n")
        download.downloadLink(temp)
        allLinkFiles.append(temp)
    f.close()

    print("**************************************************************************************")
    print("                                 Done")
    print("**************************************************************************************")
    return allLinkFiles