import json
from time import sleep
from selenium.webdriver.common.by import By
from baseDiscountAggreagator import BaseDiscountAggregatorTests
import discountAggregatorMethods as methods

with open('tests/productsData.json', 'r') as f:
    data = json.load(f)
products = data['products']
furniture_products_names = [x["name"] for x in products if x["category"] == 'furniture']
electronics_product_names = [x["name"] for x in products if x["category"] == 'electronics']
sofa_products = [x["name"] for x in products if "sofa" in x["name"]]
prices_ascending = sorted([x['price'] for x in products])
prices_descending = sorted([x['price'] for x in products], reverse=True)


class FiltersTestCases(BaseDiscountAggregatorTests):

    @classmethod
    def test_furniture_filter_is_selected_when_is_selected_from_menu(cls):
        print('---- Check if furniture checkbox is selected, when category furniture is selected from menu! ----')
        methods.go_to_category_furniture_from_menu(cls.driver)
        sleep(1)
        assert cls.driver.find_element(By.XPATH, '//input[@id="furniture"]').is_selected()
        print('Yes, "furniture" is checked, when selected from menu!')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_furniture_filter_is_checked_when_is_selected_from_home_page_direct_link(cls):
        print('---- Check if furniture checkbox is selected, when category furniture is selected from home '
              'page direct link! ----')
        methods.go_to_category_furniture_from_home_page_direct_link(cls.driver)
        sleep(1)
        assert cls.driver.find_element(By.XPATH, '//input[@id="furniture"]').is_selected()
        print('Yes, "furniture" is checked, when selected from home page direct link!')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_all_furniture_products_are_displayed_when_furniture_filter_is_selected(cls):
        print('---- Check if all furniture products are displayed when furniture filter is selected! ----')
        methods.go_to_all_products_and_check_furniture_in_filters(cls.driver)
        for p in furniture_products_names:
            sleep(1)
            assert cls.driver.find_element(By.LINK_TEXT, p)
        sleep(1)
        print(f"All furniture products are displayed: {furniture_products_names}")
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_electronics_filter_is_checked_when_is_selected_from_menu(cls):
        print('---- Check if electronics checkbox is selected, when category electronics is selected from menu! ----')
        methods.go_to_category_electronics_from_menu(cls.driver)
        sleep(1)
        assert cls.driver.find_element(By.XPATH, '//input[@id="electronics"]').is_selected()
        print('Yes, "electronics" is checked, when selected from menu!')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_electronics_filter_is_checked_when_is_selected_from_home_page_direct_link(cls):
        print('---- Check if electronics checkbox is selected, when electronics furniture is selected from home '
              'page direct link! ----')
        methods.go_to_category_electronics_from_home_page_direct_link(cls.driver)
        sleep(1)
        assert cls.driver.find_element(By.XPATH, '//input[@id="electronics"]').is_selected()
        print('Yes, "electronics" is checked, when selected from home page direct link!')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_all_electronics_products_are_displayed_when_electronics_filter_is_selected(cls):
        print('---- Check if all electronics products are displayed when electronics filter is selected! ----')
        methods.go_to_all_products_and_check_electronics_in_filters(cls.driver)
        for p in electronics_product_names:
            sleep(1)
            assert cls.driver.find_element(By.LINK_TEXT, p)
        sleep(1)
        print(f"All electronics products are displayed: {electronics_product_names}")
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_search_for_sofa_from_home_page(cls):
        cls.driver.find_element(By.ID, 'search_filter').send_keys('sofa')
        sleep(1)
        cls.driver.find_element(By.XPATH, '//button[contains(.,"Search")]').click()
        if len(sofa_products) > 0:
            for p in sofa_products:
                sleep(1)
                assert cls.driver.find_element(By.LINK_TEXT, p)
            print(f'Sofa products found and displayed: {sofa_products}')
        else:
            print('No sofa products found')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_search_for_sofa_from_products_page(cls):
        methods.go_to_all_products_from_menu(cls.driver)
        sleep(1)
        cls.driver.find_element(By.ID, 'search_filter').send_keys('sofa')
        sleep(1)
        cls.driver.find_element(By.XPATH, '//button[contains(.,"Search")]').click()
        if len(sofa_products) > 0:
            for p in sofa_products:
                sleep(1)
                assert cls.driver.find_element(By.LINK_TEXT, p)
            print(f'Sofa products found and displayed: {sofa_products}')
        else:
            print('No sofa products found')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_set_sort_by_price_low_to_high(cls):
        prices_list = []
        methods.set_sort_by_price_low_to_high(cls.driver)
        sleep(1)
        prices_page_1 = cls.driver.find_elements(By.XPATH, '//p[@class = "small text-muted"]')

        for price in prices_page_1:
            lp = len(price.text)
            prices_list.append(int(price.text[1:lp]))

        while methods.is_disabled(cls.driver) == 'false':
            methods.click_next_page_button(cls.driver)
            current_page_prices = cls.driver.find_elements(By.XPATH, '//p[@class = "small text-muted"]')

            for price in current_page_prices:
                lp = len(price.text)
                prices_list.append(int(price.text[1:lp]))

        assert prices_list == prices_ascending
        print('Products are sorted low to high price!')
        print(f"List of prices returned, if sorting is low to high: {prices_list}")
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_set_sort_by_price_high_to_low(cls):
        prices_list = []
        methods.set_sort_by_price_high_to_low(cls.driver)
        sleep(1)
        prices_page_1 = cls.driver.find_elements(By.XPATH, '//p[@class = "small text-muted"]')

        for price in prices_page_1:
            lp = len(price.text)
            prices_list.append(int(price.text[1:lp]))

        while methods.is_disabled(cls.driver) == 'false':
            methods.click_next_page_button(cls.driver)
            current_page_prices = cls.driver.find_elements(By.XPATH, '//p[@class = "small text-muted"]')

            for price in current_page_prices:
                lp = len(price.text)
                prices_list.append(int(price.text[1:lp]))
        assert prices_list == prices_descending
        print('Products are sorted high to low price!')
        print(f"List of prices returned, if sorting is high to low: {prices_list}")
        methods.go_to_home_page(cls.driver)
