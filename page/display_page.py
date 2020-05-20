from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    # 显示按钮
    display_buttton = By.XPATH, "xpath"
    # 搜索按钮
    search_button = By.ID, "ID"
    # 搜索框
    input_text_view = By.ID, "ID"
    # 返回按钮
    back_button = By.CLASS_NAME, "class_name"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击显示（init里面可以去写已经确定的这个模块所有的前置功能）
        self.click_display()

    def click_display(self):
        self.click(self.display_buttton)

    def click_search(self):
        self.click(self.search_button)

    def input_search_text(self, text):
        self.input_text(self.input_text_view, text)

    def click_back(self):
        self.click(self.back_button)