from selenium import webdriver
import time
import re

def extract_phone_numbers(url):
    driver = webdriver.Chrome()  
    driver.get(url)
    time.sleep(2)  

    phone_numbers = set()  # Множество для хранения уникальных номеров

    phone_pattern = re.compile(r'\d{1}\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}')
    matches = phone_pattern.findall(driver.page_source)

    for match in matches:
        phone_numbers.add(match)

    for number in phone_numbers:
        print(number)

    driver.quit()

# Пример использования:
if __name__ == "__main__":
    extract_phone_numbers("https://hands.ru/company/about")
    extract_phone_numbers("https://repetitors.info")
