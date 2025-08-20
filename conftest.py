import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import shutil
import os

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")  # можно отключить для отладки
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    chromedriver_path = os.getenv("CHROMEDRIVER_PATH", shutil.which("chromedriver"))
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()
