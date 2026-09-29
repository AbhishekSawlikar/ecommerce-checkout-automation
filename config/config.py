import os

BASE_URL = "http://www.automationpractice.pl/index.php"
EXPLICIT_WAIT = 15
GRID_URL = os.getenv("SELENIUM_GRID_URL", "http://localhost:4444/wd/hub")