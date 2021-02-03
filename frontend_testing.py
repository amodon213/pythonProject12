from selenium import webdriver

try:
    driver = webdriver.Chrome(executable_path="/Users/alexz/Downloads/chromedriver")
    driver.get("http://127.0.0.1:5001/users/123")
    get_name = driver.find_element_by_id('user').text
    print(get_name)
except:
    print("FAILED TO CONNECT")
finally:
    driver.quit()


