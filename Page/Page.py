from Base.Base import Base
import Page

class Page(Base):
    """
        页面元素管理
        封装页面所有的元素
    """
    from selenium.webdriver.common.by import By

    """   
        百度首页
    """

    input_text_baidu_id = (By.ID, "kw")
    click_button_baidu_id = (By.ID, "su")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_text(self, text):
        self.send_keys(Page.input_text_baidu_id, text)
        self.click_element(Page.click_button_baidu_id)