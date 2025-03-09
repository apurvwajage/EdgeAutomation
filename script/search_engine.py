import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from wonderwords import RandomWord

# Path to Edge WebDriver
EDGE_DRIVER_PATH = "C:\\WebDrivers\\msedgedriver.exe"
service = Service(EDGE_DRIVER_PATH)

# Set up Edge options to evade detection
options = Options()
options.add_argument("--headless")  # Enable headless mode
options.add_argument("--disable-gpu")  # Disable GPU (required for headless mode on Windows)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent automation detection
options.add_argument("--window-size=1920,1080")  # Set a default window size

# Initialize WebDriver for Edge
driver = webdriver.Edge(service=service, options=options)

# Remove navigator.webdriver flag
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Initialize RandomWord generator
rw = RandomWord()

try:
    # Open Bing
    driver.get("https://www.bing.com")
    time.sleep(random.uniform(3, 6))  # Randomized delay

    # Perform multiple searches using random words
    for _ in range(32):
        word_count = random.randint(1, 3)  # Random number of words (1-3)
        search_word = " ".join([rw.word() for _ in range(word_count)])

        print(f"Searching for: {search_word}")

        # Locate the search bar
        search_box = driver.find_element("name", "q")
        search_box.clear()
        search_box.send_keys(search_word)
        search_box.send_keys(Keys.RETURN)

        # Simulate slight human scrolling
        time.sleep(random.uniform(2, 5))
        driver.execute_script(f"window.scrollBy(0, {random.randint(100, 500)})")

        time.sleep(random.uniform(10, 30))  # Random wait for search results

finally:
    driver.quit()
