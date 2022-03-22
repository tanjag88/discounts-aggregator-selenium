import discountAggregatorMethods as methods
from baseDiscountAggreagator import BaseDiscountAggregatorTests
import websiteURLs as urls


class NavigationTestCases(BaseDiscountAggregatorTests):

    @classmethod
    def test_go_to_home_page(cls):
        print('---- Go to home page ----')
        methods.go_to_home_page(cls.driver)
        assert cls.driver.current_url == urls.baseUrl
        print(f'URl: {cls.driver.current_url}')
        print('You are back on home page!')

    @classmethod
    def test_go_to_all_products_from_menu(cls):
        print('---- Go to all products from menu ----')
        methods.go_to_all_products_from_menu(cls.driver)
        assert cls.driver.current_url == urls.allProducts_url
        print(f'URl: {cls.driver.current_url}')
        print('You are on all products page!')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_category_furniture_from_menu(cls):
        print('---- Click on categories and select furniture ----')
        methods.go_to_category_furniture_from_menu(cls.driver)
        assert cls.driver.current_url == urls.categoryFurniture_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_category_electronics_from_menu(cls):
        print('---- Click on categories and select electronics ----')
        methods.go_to_category_electronics_from_menu(cls.driver)
        assert cls.driver.current_url == urls.categoryElectronics_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_seller_structube_from_menu(cls):
        print('---- Click on sellers and select Structube ----')
        methods.go_to_seller_structube_from_menu(cls.driver)
        assert cls.driver.current_url == urls.sellerStructube_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_seller_bestbuy_from_menu(cls):
        print('---- Click on sellers and select BestBuy ----')
        methods.go_to_seller_bestbuy_from_menu(cls.driver)
        assert cls.driver.current_url == urls.sellerBestBuy_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_all_products_page_from_home_page_direct_link(cls):
        print("---- Click on 'Go to products' link! ----")
        methods.go_to_all_products_page_from_home_page_direct_link(cls.driver)
        assert cls.driver.current_url == urls.allProducts_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_category_furniture_from_home_page_direct_link(cls):
        print("---- Click on 'FURNITURE' link! ----")
        methods.go_to_category_furniture_from_home_page_direct_link(cls.driver)
        assert cls.driver.current_url == urls.categoryFurniture_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)

    @classmethod
    def test_go_to_category_electronics_from_home_page_direct_link(cls):
        print("---- Click on 'ELECTRONICS' link! ----")
        methods.go_to_category_electronics_from_home_page_direct_link(cls.driver)
        assert cls.driver.current_url == urls.categoryElectronics_url
        print(f'URl: {cls.driver.current_url}')
        methods.go_to_home_page(cls.driver)
