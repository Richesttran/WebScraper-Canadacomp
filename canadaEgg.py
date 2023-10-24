
from selenium import webdriver
from selenium.webdriver.common.by import By
class PriceFinder:
  def remove_dolla(string):
    if "$" in string: 
      modifiedstring=string.replace("$","")
    
      return modifiedstring

  #new change testasdasd
  def findPrice(self):
    driver = webdriver.Chrome()

    driver.get("https://www.canadacomputers.com/product_info.php?cPath=4_64&item_id=226995")  # Replace with the URL of the web page

    meta_element = driver.find_element(By.CSS_SELECTOR, 'meta[name="price"]')

    canada_value = meta_element.get_attribute("content")

    driver.get("https://www.newegg.ca/amd-ryzen-7-7700x-ryzen-7-7000-series/p/N82E16819113768?Item=N82E16819113768")  # Replace with the URL of the web page

    li_element = driver.find_element(By.CSS_SELECTOR, 'li.price-current')
    newegg_value = li_element.text

    canada_result = float(self.remove_dolla(canada_value))
    newegg_result = float(remove_dolla(newegg_value))

    print("Price for canada computers:", canada_value, " new egg price ",newegg_value )
    if canada_result>newegg_result:
      print("canada computer is the better deal",canada_value)
    elif canada_result<newegg_result:
      print("newegg is the better deal",newegg_value)
    else:
      print("They are the same :(")
    driver.quit()

