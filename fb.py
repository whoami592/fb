from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver
driver = webdriver.Chrome()

# Navigate to Facebook's registration page
driver.get("https://www.facebook.com/r.php")

# Find the first name field and enter a name
first_name = driver.find_element_by_name("firstname")
first_name.send_keys("John")

# Find the last name field and enter a last name
last_name = driver.find_element_by_name("lastname")
last_name.send_keys("Doe")

# Find the email field and enter an email address
email = driver.find_element_by_name("reg_email__")
email.send_keys("john.doe@example.com")

# Find the confirm email field and enter the same email address
confirm_email = driver.find_element_by_name("reg_email_confirmation__")
confirm_email.send_keys("john.doe@example.com")

# Find the password field and enter a password
password = driver.find_element_by_name("reg_passwd__")
password.send_keys("password123")

# Select the month of birth
birth_month = driver.find_element_by_id("month")
birth_month.send_keys("Jan")

# Select the day of birth
birth_day = driver.find_element_by_id("day")
birth_day.send_keys("1")

# Select the year of birth
birth_year = driver.find_element_by_id("year")
birth_year.send_keys("1990")

# Select the gender
gender = driver.find_element_by_name("sex")
gender.click()

# Click the "Sign Up" button
sign_up_button = driver.find_element_by_name("websubmit")
sign_up_button.click()

# Wait for the page to load
time.sleep(5)

# Close the web driver
driver.quit()