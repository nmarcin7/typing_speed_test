from selenium import webdriver

chrome_driver_path = "C:/DEV/chromedriver.exe" # CHOSE THE RIGHT PATH TO YOUR CHROMEDRIVE

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    url="https://typing-speed-test.aoeu.eu/?fbclid=IwAR3t1xbkpkgIxqjXMmhKuGsm_iy-tYEcmilyBE9WBE5SPxRRsLrJeQaBy4g")

words = driver.find_elements_by_css_selector(".nextword")
first_word = driver.find_element_by_css_selector(".currentword")

box = entry_box = driver.find_element_by_css_selector("#input")

one_line = [box.send_keys(i.text + " ") for i in words]




