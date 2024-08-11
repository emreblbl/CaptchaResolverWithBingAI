# import the required library
from seleniumbase import Driver
import requests
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# create a Driver instance with undetected_chromedriver (uc) and headless mode
driver = Driver(uc=True, headless=False)

# # navigate to the specified URL
# driver.get("https://ita-schengen.idata.com.tr/tr")

# driver.sleep(1)

# # Select the image element with alt attribute 'CAPTCHA Resmi'
# captcha_image = driver.find_element('img[alt="CAPTCHA Resmi"]')


# # Optionally, print the src attribute of the image to verify
# print("CAPTCHA image src:", captcha_image.get_attribute('src'))

# # Extract the Base64 data from the URI
# base64_data = captcha_image.get_attribute('src').split(',')[1]

# # Decode the Base64 data
# image_data = base64.b64decode(base64_data)

# # Write the image data to a file
# with open('output_image.png', 'wb') as file:
#     file.write(image_data)

# print("Image saved successfully.")


# Now navigate to Bing Chat
driver.get("https://www.bing.com/chat?form=CONVRD")

shadow_root_1 = driver.find_element(By.CLASS_NAME, 'cib-serp-main').shadow_root
shadow_root_2 = shadow_root_1.find_element(By.CSS_SELECTOR, 'cib-action-bar').shadow_root
shadow_root_3 = shadow_root_2.find_element(By.CSS_SELECTOR, 'cib-text-input').shadow_root

textarea = shadow_root_3.find_element(By.ID, 'searchbox')
textarea.send_keys("Which number did you see?")
textarea.send_keys("output_image.png")
textarea.send_keys(Keys.RETURN)
print("Text entered successfully.")


driver.sleep(4)
driver.quit()
