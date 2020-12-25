# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess
import os

def getlinks():
    allLinkFiles = list()
    driver = webdriver.Chrome("D:\\Github\\Python\\ChangeProperties\\PNTT\\chromedriver.exe")
    # to maximize the browser window
    driver.minimize_window()
    driver.get("https://truyenaudio.org/kiem-hiep/nghe-truyen/pham-nhan-tu-tien-truyen-tien-hiep.html")

    print("**************************************************************************************")
    print("                                 GETLINK...")
    print("**************************************************************************************")

    click = driver.find_elements_by_class_name("download-item")
    path = "D:\\Github\\Python\\ChangeProperties\\PNTT\\test.sh"

    if os.path.exists(path):
        os.remove(path)
    f = open((path), "a")
    f.write("#!/bin/bash\n\n\n")

    pause = 200
    for i in range(200, 466):
        if i == (pause + 5):
            f.write("echo -p \"---------------> PAUSED <--------------------\"\n")
            pause += 5
        temp = click[i].get_attribute("href")
        f.write("start \"" + temp + "\"\n")
        allLinkFiles.append(temp)
    f.close()

    print("**************************************************************************************")
    print("                                 Done")
    print("**************************************************************************************")
    return allLinkFiles