from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from secrets import username, password


class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def login(self):
        self.driver.get('https://www.instagram.com/')

        sleep(2)

        login_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        login_link.click()

        sleep(2)

        username_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        username_in.send_keys(username)

        passw_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        passw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        login_btn.click()

        sleep(2)

        notNow_btn = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]')
        notNow_btn.click()

        sleep(2)

    def first_search(self):
        search = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        search.click()

        search_in = bot.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_in.send_keys('#motoadventure')
        sleep(2)
        list_item = bot.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

        list_item.click()


if __name__ == "__main__":
    bot = InstaBot()
    bot.login()
