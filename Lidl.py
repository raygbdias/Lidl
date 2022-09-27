from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


html = urlopen("https://www.lidl.co.uk/our-products/pet" )
bs = BeautifulSoup(html, 'html.parser')
dados = bs.find_all("a", {'class':'ret-o-card__link nuc-a-anchor'})
#print(dados)

for i in dados:
    #print(i)
    preco = i.findChildren('span', {'class':'lidl-m-pricebox__price'})[0]
    produto = i.findChildren('h3', {'class': 'ret-o-card__headline'})[0]
    produto = produto.get_text()
    preco = preco.get_text()
    data = produto + preco 
    print(data)
