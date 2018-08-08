from Page.Page import Page
from selenium import webdriver
from Base.read_data import Op_Data
import pytest, sys, os, allure
sys.path.append(os.getcwd())

def get_data():
    # 读取返回数据
    data_list = []
    data = Op_Data("data.yml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o, i.get(o).get("text"), i.get(o).get("tag")))
    return data_list

class Test_baidu():

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.url = "http://www.baidu.com/"

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="测试用例")
    @pytest.mark.parametrize("case_num,text, tag", get_data())
    def test_login_page(self, case_num, text, tag):
        """

        :param case_num: 用例编号
        :param text: 输入测试数据
        :param tag: 1 标记成功
        :return:
        """
        page = Page(self.driver, self.url)
        page.open()

        allure.attach("用例编号", "{}".format(case_num))

        page.input_text(text)
