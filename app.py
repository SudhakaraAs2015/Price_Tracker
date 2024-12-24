import requests
from bs4 import BeautifulSoup


products_to_track=[

    {
        "product_url":"https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-Storage/dp/B07HGJKDQL?ref_=Oct_s9_apbd_orecs_hd_bw_b1yBwdz&pf_rd_r=55ER8G6AQWTCQRMB1Q3V&pf_rd_p=94baa1a4-2f06-554d-82db-8b9866e02276&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1805560031&tag=coa_in-21",
        "name": "Samsung M31",
        "target_price" : 16000,
    },
     {
        "product_url":"https://www.amazon.in/Test-Exclusive-668/dp/B07HGH88GL/ref=psdc_1805560031_t1_B07HGJKDQL",
        "name": "Samsung M21 6GB 128RAM",
        "target_price" : 16000,
    },
     {
        "product_url":"https://www.amazon.in/Test-Exclusive-553/dp/B0784D7NFQ/ref=sr_1_12?crid=2RE70JAZ07V4M&dchild=1&keywords=redmi+note+9&qid=1599449618&s=electronics&sprefix=redmi+%2Celectronics%2C-1&sr=1-12",
        "name": "Redmi Note 9 Pro",
        "target_price" : 17000,
    },
]

def give_product_price(URL):
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    page = requests.get(URL,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if(product_price==None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()


result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
     product_price_returned = give_product_price(every_product.get("product_url"))
     print(product_price_returned+ "-" +every_product.get('name'))
     
    my_product_price = product_price_returned[2:]
    my_product_price = my_product_price.replace(',','')
    my_product_price = int(float(my_product_price))
    
    print(my_product_price)
    
    if my_product_price < every_product.get('target_price'):
        print("Available at your price")
        result_file.write(every_product.get('name')+ '- \t' + "Available at target price" + "Current Price -" + str(my_product_price) + "\n")
        
    else:
        print("Still at current price")
        

finally:
    result_file.close()
