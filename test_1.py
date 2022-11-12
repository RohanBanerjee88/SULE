# Raw Package
import numpy as np
import pandas as pd

from nsepython import *

from bsedata.bse import BSE
from tabulate import tabulate

from data_1 import *

print('*********************************100%***************************************')
print("****************************************************************************")
print("******************************* S U L E ************************************")
print("------------------------------Instructions----------------------------------")
print("1. If you want to see NSE and BSE exchange values of TATA or RELIANCE or INFOSYS or ZOMATO or TCS just follow normal procedure")
print("2. If you want to see list of all stock exchange value type 'LUCKY' ")
print("4. If difference value is negative then Buy BSE and Sell NSE and vice versa")

b = BSE()

data = {'TATAMOTORS': '500570', 'RELIANCE': '500325', 'INFOSYS': '500209', 'ZOMATO': '543320', 'TCS': '532540'}
st_1 = ['TATA', 'tata', 'Tata']
st_2 = ['Reliance', 'RELIANCE', 'reliance']
st_3 = ['kpitech', 'KPITECH', 'Kpitech']
st_4 = ['Zomato', 'Zomato', 'zomato']
st_5 = ['TCS', 'tcs', 'Tcs']
all_st = ['LUCKY']


nst = "Current Value at NSE: "
bst = "Current Value at BSE: "

user = input("Enter your stock name for indian market: ")


def stocks(w):
    stc_diff = []
    for i in st_1:
        if user == i:
            q = b.getQuote(list(data.values())[0])
            result_1 = (nst, nse_eq(list(data.keys())[0])['priceInfo']['lastPrice'],
                        bst, list(q.values())[1])
            d = float(nse_eq(list(data.keys())[0])['priceInfo']['lastPrice'])
            f = float(list(q.values())[1])
            dif_1 = d - f
            print("------------------------ TATA MOTORS STOCK LISTING ----------------------")
            if dif_1 < 0:
                res = -dif_1
                r_1 = stc_diff.append(int(res))
                print(result_1, res)
                print(dif_1, r_1)
            else:
                print(result_1, dif_1)
    else:
        pass
    for j in st_2:
        if user == j:
            q = b.getQuote(list(data.values())[1])
            result_2 = (nst, nse_eq(list(data.keys())[1])['priceInfo']['lastPrice'],
                        bst, list(q.values())[1])
            d = float(nse_eq(list(data.keys())[1])['priceInfo']['lastPrice'])
            f = float(list(q.values())[1])
            dif_2 = d - f
            print("------------------ RELIANCE STOCK LISTING ---------------------------")
            if dif_2 < 0:
                res_2 = -dif_2
                print(result_2, res_2)
            else:
                print(result_2, dif_2)
    else:
        pass
    for k in st_3:
        if user == k:
            q = b.getQuote(list(data.values())[2])
            result_3 = (nst, nse_eq(list(data.keys())[2])['priceInfo']['lastPrice'],
                        bst, list(q.values())[1])
            d = float(nse_eq(list(data.keys())[2])['priceInfo']['lastPrice'])
            f = float(list(q.values())[1])
            dif_3 = d - f
            print("--------------------- INFOSYS STOCK LISTING -------------------------")
            if dif_3 < 0:
                res_3 = -dif_3
                print(result_3, res_3)
            else:
                print(result_3, dif_3)
    else:
        pass
    for f in st_4:
        if user == f:
            q = b.getQuote(list(data.values())[3])
            result_4 = (nst, nse_eq(list(data.keys())[3])['priceInfo']['lastPrice'],
                        bst, list(q.values())[1])
            d = float(nse_eq(list(data.keys())[3])['priceInfo']['lastPrice'])
            f = float(list(q.values())[1])
            dif_4 = d - f
            print("-------------------- ZOMATO STOCK LISTING --------------------")
            if dif_4 < 0:
                res_4 = -dif_4
                print(result_4, res_4)
            else:
                print(result_4, dif_4)
    else:
        pass
    for h in st_5:
        if user == h:
            q = b.getQuote(list(data.values())[4])
            result_5 = (nst, nse_eq(list(data.keys())[4])['priceInfo']['lastPrice'],
                        bst, list(q.values())[1])
            d = float(nse_eq(list(data.keys())[4])['priceInfo']['lastPrice'])
            f = float(list(q.values())[1])
            dif_5 = d - f
            print("--------------- TCS STOCK LISTING --------------")
            if dif_5 < 0:
                res_5 = -dif_5
                print(result_5, res_5)
            else:
                print(result_5, dif_5)
    for _ in all_st:
        if user == 'LUCKY':
            print(final)
        else:
            pass
    else:
        pass


stocks(user)
