import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.flipkart.com/apple-iphone-16-pro-max-black-titanium-512-gb/p/itmb63439b8f1383?pid=MOBH4DQFQR3BH2VT&lid=LSTMOBH4DQFQR3BH2VTHEFSV3&marketplace=FLIPKART&q=i+phone+16+pro+max&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_ps&fm=productRecommendation%2Fsimilar&iid=a669a6d7-c92a-4dcd-8d21-f5deab764599.MOBH4DQFQR3BH2VT.SEARCH&ppt=pp&ppn=pp&ssid=bhwmvjqxog0000001736419700459&qH=62177aa31210ee2e",
        "name": "I phone 16 Pro Max Black",
        "target_price":100000,
    },
    {
        "product_url": "https://www.flipkart.com/apple-iphone-16-pro-black-titanium-128-gb/p/itm12f97adb4c5ed?pid=MOBH4DQFVXNS5ZJH&lid=LSTMOBH4DQFVXNS5ZJHBZDANB&marketplace=FLIPKART&q=i+phone+16+pro&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=48b5c39a-36c2-432d-a511-8e46fcbb7372.MOBH4DQFVXNS5ZJH.SEARCH&ppt=sp&ppn=sp&ssid=b8nar94f1c0000001736419725204&qH=3ba41052be06fa8c",
        "name": "I phone 16 Pro Black",
        "target_price":130000,
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN/ref=sr_1_3?crid=3SV3V2L6ZJOHQ&dib=eyJ2IjoiMSJ9.ffRO-Sv2k0eXWrxGcHbapUr-7yBJq4ursX1vybpqLssWPSYT79WdkAB0g4NUNLHBhu6RCw_O1mkz6aaKmwx3JxwBP_fOiInXnTUny2jHdZNkHpv1sK203gACayrX1qWY4Z79ihZywvLKhgjJEoQMqm68WReIQimZQJVOlssmyeTer5mqIiN299hbvlEzHdZlljPx23aQt9xc47Hkva4ViahRZny7hd0K1jNTRP_4o0o.V7GQCRYs4XFtDLEfECoq6QZmWc0lWNbK7FDxpDFcJGc&dib_tag=se&keywords=samsung+s24+ultra+5g+mobile&nsdOptOutParam=true&qid=1736423890&sprefix=sa%2Caps%2C213&sr=8-3",
        "name": "Samsung Galaxy S24 Ultra",
        "target_price":110000,
    }
]

def give_product_price(URL):
    headers = {
        "User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(class_='Nx9bqj CxhGGd')

    if product_price == None:
        product_price = soup.find(class_='a-price-whole')

    return product_price.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + "-" + every_product.get('name'))

        # Slice and clean the price value
        product_price_str = product_price_returned[1:]  # Remove currency symbol
        product_price_str = product_price_str.replace(',', '')  # Remove commas
        my_product_price = int(float(product_price_str))  # Convert to integer

        print(my_product_price)

        # Check if the price is below the target price
        if my_product_price < every_product.get("target_price"):
            print("Available at Your Required Price")
            result_file.write(f"{every_product.get('name')}\tAvailable at Your Target Price\tCurrent Price: {my_product_price}\n")
        else:
            print("Still at Current Price")
            result_file.write(f"{every_product.get('name')}\tStill at Current Price\tCurrent Price: {my_product_price}\n")
    
finally:
    result_file.close()
