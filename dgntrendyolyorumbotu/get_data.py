from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def data(url):
    driver_path = "/chromedriver-win64/chromedriver.exe"

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Chrome'un yolu

    driver = webdriver.Chrome(
        options=chrome_options)  # Burada options parametresini kullanarak ChromeOptions'ı belirtiyoruz
    wait = WebDriverWait(driver, 10)

    driver.get(url)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='comment-text']")))
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='star-w']")))  # Yıldız elementlerinin yüklenmesini bekle

    comments_and_ratings = []

    # Bu dictionary, daha önce görülen yorumları depolamak için kullanılacak
    seen_comments = {}

    for _ in range(10):
        comments = driver.find_elements(By.XPATH, "//div[@class='comment-text']")
        stars = driver.find_elements(By.XPATH, "//div[@class='star-w']/div[contains(@class, 'full')]")

        for i in range(len(comments)):
            comment_text = comments[i].text
            star_rating = len(stars[i * 5:(i + 1) * 5]) / 5  # Her yorum için 5 yıldız varsayıyorum

            # Eğer bu yorum daha önce görüldüyse, atla
            if comment_text in seen_comments:
                continue

            # Yorumu işaretleyerek daha sonra kontrol etmek üzere gördüğümüz yorumları kaydedin
            seen_comments[comment_text] = True

            comments_and_ratings.append((comment_text, star_rating))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='comment-text']")))

    driver.quit()
    return comments_and_ratings
