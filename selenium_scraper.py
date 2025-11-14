"""
selenium_scraper.py
Simple scraper to collect issue titles from a GitHub repo page's Issues tab.


Prerequisites:
- Chrome browser
- Chromedriver in PATH (matching your Chrome version) or specify path to driver
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time




def scrape_issues(repo_url, headless=True, max_items=50):
chrome_options = Options()
if headless:
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--no-sandbox')


# If chromedriver is in PATH, Service() without args is fine. Otherwise set executable_path
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)


try:
driver.get(repo_url.rstrip('/') + '/issues')
time.sleep(3)
issue_elems = driver.find_elements(By.CSS_SELECTOR, 'a.Link--primary')
issues = []
for elem in issue_elems[:max_items]:
text = elem.text.strip()
if text:
issues.append(text)
return issues
finally:
driver.quit()




if __name__ == '__main__':
repo = input('Enter repository URL (e.g. https://github.com/microsoft/vscode): ').strip()
issues = scrape_issues(repo, headless=True, max_items=30)
print('\nScraped issues:')
for i, t in enumerate(issues, 1):
print(f"{i}. {t}")
