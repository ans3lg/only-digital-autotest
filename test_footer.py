from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_footer_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://only.digital/")
    driver.maximize_window()

    footer = driver.find_elements(By.TAG_NAME, "footer")
    assert len(footer) > 0, "Футер не найден на странице"

    try:
        driver.find_element(By.CSS_SELECTOR, "footer a[href*='vk.com']")
        driver.find_element(By.CSS_SELECTOR, "footer a[href*='t.me']")
        driver.find_element(By.CSS_SELECTOR, "footer a[href^='mailto:']")

        print("Все элементы футера успешно найдены!")
    except:
        assert False, "Некоторые элементы футера отсутствуют"

    driver.quit()


if __name__ == "__main__":
    test_footer_elements()
