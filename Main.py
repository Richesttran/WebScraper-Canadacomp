
from canadaEgg import PriceFinder
item_detail = PriceFinder()
product_price=[]      # square brackets are lists the round ones are tupples
iterator=0
# put the item price and name into a list (i could have written and read at the same time but i did this for readability sake)

product_price=item_detail.findPriceOne("Wishlist.txt")

# open file as writable and readable
with open('ProductPrice.txt','r+') as file:
  for product in product_price:                    
    for line in file:                                        # iterate each product in the text file

      if line.find(product[0]) != -1:                      # check if it has an existing line

        if line.find(product[1]) != -1:
          print("no price change for the "+ product[0])
        else:
          file.writelines(product[0] + product[1]+"\n")            # overwrite the existing line with new price
        break
      elif not file.readline():                                     # check if at end of line
        file.write(product[0] + product[1]+"\n")                      # write the new line  
        break



          

print(product_price)