from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'iPhone'
CURRENCY = '₹'
MIN_PRICE = '40000'
MAX_PRICE = '100000'
FILTERS = {
    'min' : MIN_PRICE,
    'max' : MAX_PRICE
}

BASE_URL = 'https://www.amazon.in/'

def get_Chrome_Driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

