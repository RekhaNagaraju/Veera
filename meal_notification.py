from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import schedule
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def send_notification():
chrome_options=Options();
chrome_options.add_experimental_option('detach', True)
service_obj=Service("/Users/Rekha/Desktop/driver/chromedriver.exe");
driver=webdriver.Chrome(service=service_obj,options=chrome_options)
driver.get("https://prodapi.veerahealth.com/cron/meal-picture-notification");
#print(driver.current_url())
message=driver.find_element(By.XPATH,"//pre").text
breakfast=schedule.every().day.at("09:00").do(send_notification);
if is_number(message):
    print("The result is a number:notification are sending for the breakfast", message)
else:
    print("The result is not a number:notification are not sending for the breakfast", message)

lunch =schedule.every().day.at("01:00").do(send_notification);
if is_number(message):
    print("The result is a number:notification are sending for the lunch", message)
else:
    print("The result is not a number:notification are not sending for the lunch", message)

dinner=schedule.every().day.at("20:00").do(send_notification);
if is_number(message):
print("The result is a number:notification are sending for the dinner", message)
else:
    print("The result is not a number:notification are not sending for the dinner", message)



driver.quit();
