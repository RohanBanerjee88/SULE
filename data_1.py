from nsepython import *

from bsedata.bse import BSE

from tabulate import tabulate

b = BSE()

tata_nse = float(nse_eq("TATAMOTORS")['priceInfo']['lastPrice'])
tata_bse = b.getQuote('500570')
reliance_nse = float(nse_eq("RELIANCE")['priceInfo']['lastPrice'])
reliance_bse = b.getQuote('500325')
infosys_nse = float(nse_eq("INFY")['priceInfo']['lastPrice'])
infosys_bse = b.getQuote('500209')
zomato_nse = float(nse_eq("ZOMATO")['priceInfo']['lastPrice'])
zomato_bse = b.getQuote('543320')
tcs_nse = float(nse_eq("TCS")['priceInfo']['lastPrice'])
tcs_bse = b.getQuote('532540')

f = float(list(tata_bse.values())[1])
f_2 = float(list(reliance_bse.values())[1])
f_3 = float(list(infosys_bse.values())[1])
f_4 = float(list(zomato_bse.values())[1])
f_5 = float(list(tcs_bse.values())[1])

diff_1 = tata_nse - f
diff_2 = reliance_nse - f_2
diff_3 = infosys_nse - f_3
diff_4 = zomato_nse - f_4
diff_5 = tcs_nse - f_5

mod_1 = -diff_1
mod_2 = -diff_2
mod_3 = -diff_3
mod_4 = -diff_4
mod_5 = -diff_5

label = [{'TATA': mod_1}, {'RELIANCE': mod_2}, {'INFOSYS': mod_3}, {'ZOMATA': mod_4}, {'TCS': mod_5}]
modu = [mod_1, mod_2, mod_3, mod_4, mod_5]
modu_2 = mod_1, mod_2, mod_3, mod_4, mod_5
r_modu = sorted(modu)
max_value = max(r_modu)


final_table = {'STOCK NAME': ['TATAMOTORS', 'RELIANCE', 'INFOSYS', 'ZOMATO', 'TCS'],
               'NSE VALUE': [tata_nse, reliance_nse, infosys_nse, zomato_nse, tcs_nse],
               'BSE VALUE': [f, f_2, f_3, f_4, f_5],
               'VALUE DIFFERENCE': [mod_1, mod_2, mod_3, mod_4, mod_5]}

final = tabulate(final_table, headers='keys', tablefmt='fancy_grid')

