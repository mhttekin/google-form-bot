import random, time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def emailer():
    names = [
        "james", "mary", "michael", "patricia", "robert", "jennifer",
        "john", "linda", "david", "elizabeth", "william", "barbara",
        "richard", "susan", "joseph", "jessica", "thomas", "karen",
        "christopher", "sarah", "charles", "lisa", "daniel", "nancy",
        "matthew", "sandra", "anthony", "betty", "mark", "ashley",
        "donald", "emily", "steven", "kimberly", "andrew", "margaret",
        "paul", "donna", "joshua", "michelle", "kenneth", "carol",
        "kevin", "amanda", "brian", "melissa", "timothy", "deborah",
        "ronald", "stephanie", "george", "rebecca", "jason", "sharon",
        "edward", "laura", "jeffrey", "cynthia"
    ]
    
    surnames = [
        "smith", "jones", "williams", "taylor", "brown", "davies", "evans", "wilson", 
        "thomas", "johnson", "roberts", "robinson", "thompson", "wright", "walker", "white", 
        "edwards", "hughes", "green", "hall", "lewis", "harris", "clarke", "patel", "jackson", 
        "wood", "turner", "martin", "cooper", "hill", "ward", "morris", "moore", "clark", 
        "lee", "king", "baker", "harrison", "morgan", "allen", "james", "scott", "phillips", 
        "watson", "davis", "parker", "price", "bennett", "young", "griffiths", "mitchell", 
        "kelly", "cook", "carter", "richardson", "bailey", "collins", "bell", "shaw", "murphy", 
        "miller", "cox", "richards", "khan", "marshall", "anderson", "simpson", "ellis", "adams", 
        "singh", "begum", "wilkinson", "foster", "chapman", "powell", "webb", "rogers", "gray", 
        "mason", "ali", "hunt", "hussain", "campbell", "matthews", "owen", "palmer", "holmes", 
        "mills", "barnes", "knight", "lloyd", "butler", "russell", "barker"
    ]
    midle = [".", ""]
    last = ["12","23", "11", "1", "", "", "1"]
    mail = ["@outlook.com", "@gmail.com", "@hotmail.com"]
    
    return random.choice(names) + random.choice(midle) + random.choice(surnames) + random.choice(last) + random.choice(mail)

class init_bot():
    def __init__(self):
        path = "/opt/homebrew/bin/geckodriver"
        service = Service(path)
        self.driver = webdriver.Firefox(service=service)

class fetch_response(init_bot):

    def positive(self):
        driver = self.driver
        url = 'https://docs.google.com/forms/d/1A9SO-gEKoeWQiO5kp7W89a5ZnFXkBXCO_rUn-aCYv30/viewform?edit_requested=true#responses'
        driver.get(url)
        
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @type='text' and not(@aria-hidden)]")))
        email_input.click()
        email_input.send_keys(emailer())

        time.sleep(3)

        c1 = int(random.random() * 4)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '18-25')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '26 - 35')]"))).click()
        elif c1 == 2:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '36 - 45')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '46+')]"))).click()
            
        time.sleep(3)

        c1 = int(random.random() * 4)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Male')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Female')]"))).click()
        elif c1 == 2:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Non-bnary')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Prefer not to say')]"))).click()
 
        time.sleep(3)

        c1 = int(random.random() * 4)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Very interested')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Somewhat interested')]"))).click()
        elif c1 == 2:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Not very interested')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Not interested at all')]"))).click()
 
        time.sleep(3)

        c1 = int(random.random() * 5)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Always')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Most of the time')]"))).click()
        elif c1 == 2:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sometimes')]"))).click()
        elif c1 == 3:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Rarely')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Never')]"))).click()
        
        time.sleep(3)
        
        c1 = int(random.random() * 2)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sundresses')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sandals')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Light - weight cotton T - shirts')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Shorts')]"))).click()

        time.sleep(3)

        c1 = int(random.random() * 2)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Woolen sweaters')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Coats')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Boots')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Coats')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Boots')]"))).click()

        time.sleep(3)

        c1 = int(random.random() * 3)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Layering')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Wearing light jackets')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Wearing long - sleeved shirts without jackets')]"))).click()

        time.sleep(3)

        c1 = int(random.random() * 5)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Daily')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Weekly')]"))).click()
        elif c1 == 2:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Monthly')]"))).click()
        elif c1 == 3:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Rarely')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Never')]"))).click()

        time.sleep(3)

        c1 = int(random.random() * 2)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Instagram')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'TikTok')]"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Pinterest')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Facebook')]"))).click()

        time.sleep(3)

        c1 = int(random.random() * 3)
        if c1 == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Professional fashion influencers')]"))).click()
        elif c1 == 1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Friends and family')]"))).click()
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'A combination of both')]"))).click()

        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Yes')]"))).click()
        
        time.sleep(3)

        if c1 == 0:
            c1 = int(random.random() * 2)
            if c1 == 0:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'User reviews of clothing items for different weather conditions')]"))).click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Integration with local weather forecasts')]"))).click()
            else:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'The ability to create and share your own weather - appropriate outfit collections')]"))).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Submit')]"))).click()

        driver.quit()

for i in range(35):
    bot = fetch_response()
    bot.positive()
    print(i)
            
