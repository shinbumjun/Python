from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
ss1 = soup.select("#tabCont01 > ul > li > a > dl > dt")
ss2 = soup.select("#tabCont01 > ul > li> a > p.money > strong")
cn = list()
price = list()
for s in ss1:
    if s.string != None:
        cn.append(s.string)
for p in ss2:
    if p.string != None:
        tmp = p.text.strip()
        tmp = tmp.replace(',','')
        price.append(int(tmp))

df = pd.DataFrame({'상품명': cn, '가격': price})
print(df['가격'].mean())
print(df['가격'].std())
