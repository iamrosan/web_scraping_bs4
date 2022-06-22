# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.pararius.com/apartments/nederland?ac=1'

# pageContent = requests.get(url)
# # print(pageContent)

# coup = BeautifulSoup(pageContent.content, 'html.parser')
# # print(coup)
# itemDiv = coup.find('Div', class_='listing-search-item listing-search-item--list listing-search-item--featured')
# print(itemDiv)
# item1 = itemDiv.find('div', class_='c3e8SH')
# print(item1)

from bs4 import BeautifulSoup
import requests
from csv import writer

header = ['Title','Price']
url = 'https://www.sastodeal.com/catalogsearch/result/?q=trimmer'

pageContent = requests.get(url)
# print(pageContent)

coup = BeautifulSoup(pageContent.content, 'html.parser')
# print(coup)
itemDiv = coup.find('ol', class_='products list items product-items')
# print(itemDiv)

items = itemDiv.find_all('li', class_='item product product-item')
with open('trimmerSastoDeal.csv','w') as f:
    write = writer(f)
    write.writerow(header)
# print(item1)
    for item in items:
        divBox = item.find('div',class_='product-item-info')
        item1Title = divBox.find('strong', class_="product name product-item-name").text
        # print(item1Title)

        priceDiv = itemDiv.find('div', class_='price-box price-final_price')
        price = priceDiv.find('span', class_='price').text[2:]

        if ',' in price:
            actualPrice = price.replace(',','')
            if int(actualPrice) > 1000 :
                detail = [item1Title,actualPrice]
                write.writerow(detail)
        # if price < 'रू 1,000':
                print(f"""
                Product Name: {item1Title}
                price: {actualPrice}

                """)
