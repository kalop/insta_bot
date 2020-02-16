from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from secrets import username, password
from random import randint
from hashtags import hashtags

# https://gist.github.com/tacomonster/555bceef3d14673810f625edd000c112

WAIT_TIME = randint(2, 5)


class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def _getLink(self, link):
        self.driver.get(link)
        sleep(WAIT_TIME)
        self.action = ActionChains(self.driver)

    def login(self):
        try:
            self._getLink('https://www.instagram.com/')

            login_link = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
            login_link.click()

            sleep(WAIT_TIME)

            username_in = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            username_in.send_keys(username)

            passw_in = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            passw_in.send_keys(password)

            login_btn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
            login_btn.click()

            sleep(WAIT_TIME)

            notNow_btn = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]')
            notNow_btn.click()

            sleep(WAIT_TIME)

        except Exception as error:
            print(str(error))
            return False
        return True

    def hashtag_search(self, hashtag):
        search = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        sleep(WAIT_TIME)
        search.click()

        search_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_in.send_keys(hashtag)
        sleep(WAIT_TIME)
        list_item = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

        list_item.click()

    def go_to_hashtag_link(self, hashtag):
        self._getLink('https://www.instagram.com/explore/tags/%s/' % hashtag)

    def get_pics(self):
        pic_hrefs = []
        for _ in range(1, 7):
            try:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                sleep(WAIT_TIME)
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue
        return pic_hrefs

    def close_window(self):
        cross = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[3]/button')
        cross.click()

    def like_pic_from_link(self, link):
        self._getLink(link)
        pic = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[1]/div')
        self.action.double_click(pic).perform()
        sleep(WAIT_TIME)

    def perform_hashtag(self, hashtag):
        self.go_to_hashtag_link(hashtag)
        pics = self.get_pics()
        for link in pics:
            try:
                self.like_pic_from_link(link)
                # self.perform_profile()
            except Exception as e:
                print(str(e))
                continue

    def perform_profile(self):
        pass

    def load_hashtags(self):
        for hashtag in hashtags:
            self.perform_hashtag(hashtag)
            sleep(10)


if __name__ == "__main__":
    bot = InstaBot()
    while not bot.login():
        print('trying to login...')

    bot.load_hashtags()
