from time import sleep
from selenium.webdriver.common.by import By


def go_to_home_page(driver):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Discounts').click()


def go_to_all_products_from_menu(driver):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'All Products').click()


def go_to_category_furniture_from_menu(driver):
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Categories")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Furniture")]').click()


def go_to_category_electronics_from_menu(driver):
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Categories")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Electronics")]').click()


def go_to_seller_structube_from_menu(driver):
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Sellers")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Structube")]').click()


def go_to_seller_bestbuy_from_menu(driver):
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"Sellers")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"BestBuy")]').click()


def go_to_all_products_page_from_home_page_direct_link(driver):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Go to products').click()


def go_to_category_furniture_from_home_page_direct_link(driver):
    sleep(1)
    driver.find_element(By.ID, 'furnitureDirectLink').click()


def go_to_category_electronics_from_home_page_direct_link(driver):
    sleep(1)
    driver.find_element(By.ID, 'electronicsDirectLink').click()


def go_to_all_products_and_check_furniture_in_filters(driver):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'All Products').click()
    driver.find_element(By.ID, 'label-furniture').click()


def go_to_all_products_and_check_electronics_in_filters(driver):
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'All Products').click()
    driver.find_element(By.ID, 'label-electronics').click()


def set_sort_by_price_low_to_high(driver):
    driver.find_element(By.LINK_TEXT, 'Go to products').click()
    sleep(1)
    driver.find_element(By.NAME, 'sorting').click()
    sleep(1)
    driver.find_element(By.XPATH, '//option[@value = "price,asc"]').click()


def set_sort_by_price_high_to_low(driver):
    driver.find_element(By.LINK_TEXT, 'Go to products').click()
    sleep(1)
    driver.find_element(By.NAME, 'sorting').click()
    sleep(1)
    driver.find_element(By.XPATH, '//option[@value = "price,desc"]').click()


def click_next_page_button(driver):
    sleep(1)
    driver.find_element(By.XPATH,
                        '//ul[@class="pagination justify-content-center justify-content-lg-end"]'
                        '//a[contains(.,"next")]').click()


def is_disabled(driver):
    sleep(1)
    disabled = driver.find_element(By.XPATH,
                                   '//ul[@class="pagination justify-content-center justify-content-lg-end"]'
                                   '//a[contains(.,"next")]').get_attribute('aria-disabled')
    return disabled
