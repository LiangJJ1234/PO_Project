import os, sys
sys.path.append(os.getcwd())


from base.base_driver import init_driver
from page.display_page import DisplayPage

class TestDisplay():

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)
        
        

    def test_display_input(self):
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_search_text("xxx")
        # 点击返回
        self.display_page.click_back()