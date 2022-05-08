from bs4 import BeautifulSoup
import requests
from time import sleep
import sys

import winsound


arg = sys.argv

checkTime = 8

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

gpu3090Tistore = "https://tw.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090+Ti" # url of the store, no touchy
GPU3090Tiname = "GeForce RTX 3090 Ti"

gpu3090store = "https://tw.evga.com/products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3090" # url of the store, no touchy
GPU3090name = "GeForce RTX 3090"

gpu3080Tistore = "https://tw.evga.com/Products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080+Ti" # url of the store, no touchy
GPU3080Tiname = "GeForce RTX 3080 Ti"

gpu308012store = "https://tw.evga.com/Products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080+12GB" # url of the store, no touchy
GPU308012name = "GeForce RTX 3080 12GB"

gpu3080store = "https://tw.evga.com/Products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3080" # url of the store, no touchy
GPU3080name = "GeForce RTX 3080"

gpu3070Tistore = "https://tw.evga.com/Products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070+Ti" # url of the store, no touchy
GPU3070Tiname = "GeForce RTX 3070 Ti"

gpu3070store = "https://tw.evga.com/products/productlist.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070" # url of the store, no touchy
GPU3070name = "GeForce RTX 3070"

gpu3060Tistore = "https://tw.evga.com/Products/ProductList.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3060+Ti" # url of the store, no touchy
GPU3060Tiname = "GeForce RTX 3060 Ti"

gpu3060store = "https://tw.evga.com/Products/Product.aspx?pn=12G-P5-3657-KR" # url of the store, no touchy
GPU3060name = "GeForce RTX 3060"

class CheckGPUs:
    def gpu3090Ti():
        site = requests.get(gpu3090Tistore, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl5_pnlgPriceFinal').get_text()
        getGPUPrice2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl6_pnlgPriceFinal').get_text()
        getGPUPrice3 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl7_pnlgPriceFinal').get_text()


        getGPUCart1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl5_pnlAddCart')
        getGPUCart2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl6_pnlAddCart')
        getGPUCart3 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl4_ctrl7_pnlAddCart')


        if (getGPUCart1 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice1} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        elif (getGPUCart2 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice2} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        elif (getGPUCart3 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice3} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        else :
            print(f"[*] {GPU3090name} Carts do not appear")
            sleep(checkTime)

    def gpu3090():
        site = requests.get(gpu3090store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl7_ctrl9_pnlgPriceFinal').get_text()
        getGPUPrice2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl10_ctrl13_pnlgPriceFinal').get_text()


        getGPUCart1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl7_ctrl9_pnlAddCart')
        getGPUCart2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl10_ctrl13_pnlAddCart')


        if (getGPUCart1 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice1} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        elif (getGPUCart2 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice2} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        elif (getGPUCart3 != None):
            print(f"[*] {GPU3090name} Can Add cart!!!")
            print(f"[+] {GPU3090name} : {getGPUPrice3} | {gpu3090store}")
            print(f"[+] {gpu3090store}")
            Beeper()
        else :
            print(f"[*] {GPU3090name} Carts do not appear")
            sleep(checkTime)

    def gpu3080():
        site = requests.get(gpu3080store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl7_ctrl9_pnlgPriceFinal').get_text()
        getGPUPrice2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl11_ctrl15_pnlgPriceFinal').get_text()


        getGPUCart1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl7_ctrl9_pnlAddCart')
        getGPUCart2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl11_ctrl15_pnlAddCart')


        if (getGPUCart1 != None):
            print(f"[*] {GPU3080name} Can Add cart!!!")
            print(f"[+] {GPU3080name} : {getGPUPrice1} | {gpu3080store}")
            print(f"[+] {gpu3080store}")
            Beeper()
        elif (getGPUCart2 != None):
            print(f"[*] {GPU3080name} Can Add cart!!!")
            print(f"[+] {GPU3080name} : {getGPUPrice2} | {gpu3080store}")
            print(f"[+] {gpu3080store}")
            Beeper()
        else :
            print(f"[*] {GPU3080name} Carts do not appear")
            sleep(checkTime)

    def gpu3070():
        site = requests.get(gpu3070store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl0_ctrl1_pnlgPriceFinal').get_text()
        getGPUPrice2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl3_ctrl6_pnlgPriceFinal').get_text()
        getGPUPrice3 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl8_ctrl9_pnlgPriceFinal').get_text()

        getGPUCart1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl0_ctrl3_pnlAddCart')
        getGPUCart2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl3_ctrl6_pnlAddCart')
        getGPUCart3 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl8_ctrl9_pnlAddCart')

        if (getGPUCart1 != None):
            print(f"[*] {GPU3070name} Can Add cart!!!")
            print(f"[+] {GPU3070name} : {getGPUPrice1} | {gpu3070store}")
            print(f"[+] {gpu3070store}")
            Beeper()
        elif (getGPUCart2 != None):
            print(f"[*] {GPU3070name} Can Add cart!!!")
            print(f"[+] {GPU3070name} : {getGPUPrice2} | {gpu3070store}")
            print(f"[+] {gpu3070store}")
            Beeper()
        elif (getGPUCart3 != None):
            print(f"[*] {GPU3070name} Can Add cart!!!")
            print(f"[+] {GPU3070name} : {getGPUPrice3} | {gpu3070store}")
            print(f"[+] {gpu3070store}")
            Beeper()
        else :
            print(f"[*] {GPU3070name} Carts do not appear")
            sleep(checkTime)

    def gpu3060Ti():
        site = requests.get(gpu3060Tistore, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl0_ctrl3_pnlgPriceFinal').get_text()
        getGPUPrice2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl5_ctrl7_pnlgPriceFinal').get_text()

        getGPUCart1 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl0_ctrl3_pnlAddCart')
        getGPUCart2 = soup.find(id='ctl00_LFrame_prdList_rlvProdGridView_ctrl5_ctrl7_pnlAddCart')

        if (getGPUCart1 != None):
            print(f"[*] {GPU3060Tiname} Can Add cart!!!")
            print(f"[+] {GPU3060Tiname} : {getGPUPrice1} | {gpu3060Tistore}")
            print(f"[+] {gpu3060Tistore}")
            Beeper()
        elif (getGPUCart2 != None):
            print(f"[*] {GPU3060Tiname} Can Add cart!!!")
            print(f"[+] {GPU3060Tiname} : {getGPUPrice2} | {gpu3060Tistore}")
            print(f"[+] {gpu3060Tistore}")
            Beeper()
        else :
            print(f"[*] {GPU3060Tiname} Carts do not appear")
            sleep(checkTime)

    def gpu3060():
        site = requests.get(gpu3060store, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        getGPUPrice = soup.find(id='ctl00_LFrame_lblPrice').get_text()

        getGPUCart = soup.find(id='ctl00_LFrame_pnlBuy')

        if (getGPUCart != None):
            print(f"[*] {GPU3060name} Can Add cart!!!")
            print(f"[+] {GPU3060name} : {getGPUPrice} | {gpu3060store}")
            print(f"[+] {gpu3060store}")
            Beeper()
        else :
            print(f"[*] {GPU3060name} Carts does not appear")
            sleep(checkTime)

def Beeper():
    winsound.Beep(600,500)
    winsound.Beep(600,500)
    winsound.Beep(600,1000)

def sysarg():
    if (arg[1] == "3090"):
        Check3090Evga()
    elif (arg[1] == "3080"):
        Check3080Evga()
    elif (arg[1] == "3070"):
        Check3070Evga()
    elif (arg[1] == "3060Ti"):
        Check3060TiEvga()
    elif (arg[1] == "3060"):
        Check3060Evga()
    elif (arg[1] == "gpus"):
        print("\n---- GPU List ----\nGeForce RTX 3090\nGeForce RTX 3080\nGeForce RTX 3070\nGeForce RTX 3060")
        print("-" * 18)
    else:
        print("That GPU isnt added.")
        sys.exit()

def Check3090TiEvga():
    print("\n")
    while True:
        CheckGPUs.gpu3090Ti()

def Check3090Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3090()

def Check3080Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3080()
        
def Check3070Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3070()

def Check3060TiEvga():
    print("\n")
    while True:
        CheckGPUs.gpu3060Ti()

def Check3060Evga():
    print("\n")
    while True:
        CheckGPUs.gpu3060()

sysarg()
