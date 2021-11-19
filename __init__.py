from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time





class Instegram():
    index = 0
    ###Script to like all photoes of someone by name
    ###can swap multi accoutnts and scrol and like and add by name
    ### can add followers by fake accounts logiin and liking someone page 

    def __init__(self, username, pw,path): ##exalmple Username:Dima4560 Password:1234567 Path:https:/www.instagram.com/
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver_that_running = webdriver.Chrome(options=option, executable_path="D:\google_drive\chromedriver.exe")
        self.username = username
        self.pw = pw
        self.user_name_password = dict(zip(username, pw))
        self.path=path
        self.user_that_ruinng = None




    def run_web(self):##Finding the DNS of instegram
        driver=self.driver_that_running
        wait = WebDriverWait(driver, 5)
        run_web=driver.get(self.path)
        if self.user_that_ruinng == None:
            self.user_that_ruinng = {self.username[self.index]: self.pw[self.index]}
        for user, password in self.user_that_ruinng.items():
            time.sleep(3)
            log_in_username = driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(
                user)
            log_in_password = driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(
                password)
            log_in = driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        bool_1=self.is_element_exist_by_class_name("f5C5x")
        if bool_1 == True:
            move_front=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()


    def find_by_name(self,name): #####finding element by name....
        self.run_web()
        driver=self.driver_that_running
        wait = WebDriverWait(driver, 5)
        wait_until = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH,'//input[@type="text"]')))
        driver.find_element_by_xpath('//input[@type="text"]').send_keys(name)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"z556c")))
        driver.find_element_by_class_name("z556c").click()

        time.sleep(3)

    def log_out(self):
        driver = self.driver_that_running
        driver.get(self.path)
        wait_until = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')))
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div').click()


    def follow_account(self,name):
        self.find_by_name(name)
        driver=self.driver_that_running
        wait = WebDriverWait(driver, 5)
        wait_until = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='vBF20 _1OSdk']")))
        just_click=driver.find_element_by_xpath("//span[@class='vBF20 _1OSdk']").click()


    def get_list_of_possiable_accounts_for_now_running_account(self,set_time_scrolling_1=None,set_time_scrolling_2=None):
        self.run_web()
        driver = self.driver_that_running
        wait_until = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[text()="See All"]')))
        just_click = driver.find_element_by_xpath('//div[text()="See All"]').click()
        SCROLL_PAUSE_TIME = 0.5
        last_height = driver.execute_script("return document.body.scrollHeight")
        if set_time_scrolling_1 == None:
            set_time_scrolling_1 =  0
        if set_time_scrolling_2 == None:
            set_time_scrolling_2 = 10
        while set_time_scrolling_1 < set_time_scrolling_2:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            last_height = new_height
            time.sleep(1)
            set_time_scrolling_1=set_time_scrolling_1+1
        list_r=driver.find_elements_by_tag_name("a")
        list_of_people=[elem.get_attribute('title').strip('https://www.instagram.com/') for elem in list_r ]
        for name in list_of_people:
            if name != '':
                print(name)


    def like_all_pictures(self,name):
        self.find_by_name(name)
        driver=self.driver_that_running
        for i in range(1, 6):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        list_of_photos=driver.find_elements_by_tag_name("a")
        list_people=[elem.get_attribute('href') for elem in list_of_photos]
        for name in list_people:
            if '/p/' in name:
                driver.get(name)
                time.sleep(3)
                just_click = driver.find_element_by_xpath("//span[@class='fr66n']").click()


    def log_differnt_acoounts_and_like_many(self,name):
        driver = self.driver_that_running
        while self.index < len(self.username):
            self.user_that_ruinng = {self.username[self.index]: self.pw[self.index]}
            self.like_all_pictures(name)
            self.log_out()
            self.index+=1

    def is_element_exist_by_XPATH(self, text):
        browser = self.driver_that_running
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, text)))
            return True
        except TimeoutException:
            return False

    def is_element_exist_by_class_name(self,text):
        browser = self.driver_that_running
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, text)))
            return True
        except TimeoutException:
            return False

    def is_element_exist_by_text(self, text):
        browser = self.driver_that_running
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
            return True
        except TimeoutException:
            return False





