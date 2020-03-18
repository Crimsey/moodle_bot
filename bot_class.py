#By SpicyCurry13
import sys,time,datetime
from selenium import webdriver
from secret import username,password
from courses_with_dates import courses

#represents simple bot to connect to your courses
class MoodleBot():
    def __init__(self,browser=""):
        if browser == "firefox":
            self.browser = webdriver.Firefox()
        elif browser == "chrome":
            self.browser = webdriver.Chrome()
        elif browser == "opera":
            self.browser = webdriver.Opera()
        else:
            print("Nie podano przegladarki zainstalowanego webdrivera. Podaj go w argumencie (firefox, chrome, opera)")
            exit()
    
    def login(self):
        #open moodle login page
        self.browser.get("https://moodle.cs.pollub.pl/")

        #find login and passowrd input tags
        login_username = self.browser.find_element_by_id("login_username")
        login_password = self.browser.find_element_by_id("login_password")
        #find submit btn
        submit_btn = self.browser.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div/section[2]/aside/section[1]/div/div/form/div[4]/input")

        #fill in username, passowrd and click btn to confirm
        login_username.send_keys(username)
        login_password.send_keys(password)
        submit_btn.click()

    def make_dic(self):
        self.browser.get("https://moodle.cs.pollub.pl/?redirect=0")

        #get list of your courses from Main Page
        elements = self.browser.find_elements_by_css_selector("h3.coursename a")

        #open or creates file to save your courses
        my_courses_file = open("my_courses.py","w")
        
        #save them into my_courses.py file as dict
        my_courses_file.write('my_courses = {\n')
        
        
        for element in elements:
            key = element.text
            val = element.get_attribute("href")
            line = "\""+key+"\":\""+val+"\",\n"
            
            my_courses_file.write(line)
        
        my_courses_file.write('}\n')
        
        #close file
        my_courses_file.close()

    def get_to_course(self):
        today = datetime.datetime.now()
        #today = datetime.datetime(2020,3,18,12,15)

        #get todays weekday
        todays_weekday = today.weekday()
        today_hour = today.hour
        today_mins = today.minute
        
        #get todays time of a day as minutes
        today_hour_in_mins = today_hour*60 + today_mins
        
        for key in courses:
            course_link = courses[key][0]
            course_weekday = courses[key][1]
            course_hour = courses[key][2]
            
            #parse course time from string to time struct
            t = time.strptime(course_hour,"%H:%M")         
            #count minutes of given time of a day
            course_hour_in_mins = t.tm_hour * 60 + t.tm_min
            
            #find and open latest course from dict (courses_with_dates.py)
            if course_weekday == todays_weekday and today_hour_in_mins > course_hour_in_mins:
                self.browser.get(course_link)
                break
        


