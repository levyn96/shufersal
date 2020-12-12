from selenium import webdriver


def get_example():
    file = open('groceries_list_example.txt', 'r')
    groceries_list = eval(file.readline())

    return groceries_list


def add_to_cart(groceries_list):
    first = True
    # Using Chrome to access web
    driver = webdriver.Chrome()
    try:
        for product in groceries_list:
            # Open the website
            try:
                driver.get('https://www.shufersal.co.il/online/he/search?text={}'.format(product))
                driver.maximize_window()
                # convert to list view
                list_button = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/button/i")
                list_button.click()
                # add to cart
                add_to_cart_button = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/ul/li[1]/section/ul/li[1]/div[1]/div[4]/button[1]") # /html/body/main/div[2]/div[2]/div[2]/ul/li[1]/section/ul/li[1]/div[1]/div[4]/button[1]
                # clicking the button in a different way. see reference here:
                # https://stackoverflow.com/questions/48665001/can-not-click-on-a-element-elementclickinterceptedexception-in-splinter-selen
                driver.execute_script("arguments[0].click();", add_to_cart_button)
                # webdriver.ActionChains(driver).move_to_element(add_to_cart_button).click(add_to_cart_button).perform()
                if first:
                    first = False
                    input("exit the prompt window on the site and press enter here")
            except:
                pass
    except Exception as e:
         print(e)

    finally:
        input("to close press enter")
        driver.close()


if __name__ == '__main__':
    groceries = get_example()
    print(groceries)
    add_to_cart(groceries)
