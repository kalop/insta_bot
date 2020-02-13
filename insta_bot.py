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

        sleep(3)

        notNow_btn = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]')
        notNow_btn.click()

        sleep(3)

    def hashtag_search(self, hashtag):
        search = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        sleep(2)
        search.click()

        search_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_in.send_keys(hashtag)
        sleep(2)
        list_item = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

        list_item.click()

    def go_to_hashtag_link(self, hashtag):
        self.driver.get(
            'https://www.instagram.com/explore/tags/%s/' % hashtag)
        sleep(2)

    def get_pics(self):
        pic_hrefs = []
        for i in range(1, 3):
            try:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
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

    def like_pic(self):
        pic = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[2]')
        self.action.double_click(pic).perform()
        sleep(2)


if __name__ == "__main__":
    bot = InstaBot()
    bot.login()
    bot.go_to_hashtag_link('motoadventure')
    bot.scroll_down()
    # bot.like_pic()
    # bot.click_next_pic()
    # bot.like_pic()
    # bot.click_next_pic()
    # bot.like_pic()
    # bot.go_to_hashtag_link('motorcycle')
    # bot.open_first_pic()
    # bot.like_pic()
    # bot.click_next_pic()
    # bot.like_pic()
    # bot.click_next_pic()
    # bot.like_pic()
