# never use print in the python script to debug use icecream library to debug or print any statement it will give you more information

from icecream import ic

ic("Python snake hacking")


cre_dict = {'John' : {'country' : ['India' , 'Paris', 'America', 'Switzerland']}, 'Rock': {'country': ['America', 'India', 'Finland', 'Brazil']}}


ic(cre_dict)

# print(cre_dict)

# def price(product_1, product_2):
#     summing = product_1 + product_2

#     ic(f"price of product 1 is {product_1} and product 2 is {product_2} and the total amount you have to pay is {summing}")
#     return summing

# def main():
#     chair_price = int(input("Price of the first? "))

#     text_book_price = int(input("Price of the second? "))

#     ic(price(chair_price, text_book_price))