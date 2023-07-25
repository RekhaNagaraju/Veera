from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# current dateTime
now = datetime.now()
# convert to time String
time = now.strftime("%H:%M")
print('Time String:', time)

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def send_notification():
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    service_obj = Service("/Users/Rekha/Desktop/driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    #for getting the url
    driver.get("https://prodapi.veerahealth.com/cron/meal-picture-notification")
    #for obtaining xpath and stored the value
    message = driver.find_element(By.XPATH, "//pre").text

    if time == "09:00":
        if is_number(message):
            print("The result is a number: notification is sending for breakfast", message)
        else:
            print("The result is not a number: notification is not sending for breakfast", message)
            print("breakfast")
    elif time == "13:00":
        if is_number(message):
            print("The result is a number: notification is sending for lunch", message)
        else:
            print("The result is not a number: notification is not sending for lunch", message)
            print("lunch")
    elif time == "20:00":
        if is_number(message):
            print("The result is a number: notification is sending for dinner", message)
        else:
            print("The result is not a number: notification is not sending for dinner", message)
            print("dinner")
    else:
        print("notification is not sending")

# Call the function to execute the logic
send_notification()
