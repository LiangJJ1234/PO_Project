import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetworkPage(BaseAction):

    # 更多按钮
    more_button = By.XPATH, "xpath路径"
    # 移动网络
    network_button = By.XPATH, "xpath路径"
    # 网络首选项按钮
    network_first_button = By.XPATH, "xpath路径"
    # 2g网络按钮
    network_2g_button = By.XPATH, "xpath路径"
    # 3g网络按钮
    network_3g_button = By.XPATH, "xpath路径"

    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(self.network_button)

    def click_first_network(self):
        self.click(self.network_first_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)