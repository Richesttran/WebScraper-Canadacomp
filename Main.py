
from canadaEgg import PriceFinder
item_detail = PriceFinder()
with open('Wishlist.txt','r') as file:
  for line in file:
   print(item_detail.findPriceOne(line.strip()))
