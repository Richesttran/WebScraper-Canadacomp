
from selenium import webdriver
from selenium.webdriver.common.by import By
from canadaEgg import PriceFinder
hi = PriceFinder()
print(hi.findPriceOne("https://www.canadacomputers.com/product_info.php?cPath=4_64&item_id=226995"))
