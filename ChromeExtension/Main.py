import requests
import re,html
import tldextract
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url ="https://vip-l82.work/sb/?th=#1609078595595"

class HardCode_Scanner:
    def __init__(self, url):
        self.session = requests.Session()
        self.target_url = url
        self.chrome_options = webdriver.ChromeOptions()
    
    def check_Hardcode(self):
        try:
            response = self.session.get(self.target_url)
        except Exception:
            response = '404'
        if '404' in str(response):
            return 'X'
        else:
            regex = r" Share it until the blue bar is full|Share until the blue bar is full"
            return re.search(regex,(response.content).decode(errors="ignore"))

class CertificateScanner(HardCode_Scanner): #use of inheritance
    def __init__(self,CS_url):
        super().__init__(CS_url) #inherit the methods and all from parents
        self.sslUrl = CS_url

    def addagruments(self):
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("--log-level=3")
        # self.chrome_options.headless = True
        self.open_browser()

    def open_browser(self):                                                     
        self.driver = webdriver.Chrome(options = self.chrome_options)

    def digicert(self): 
        self.driver.get('https://www.google.com/')    
        searchBox = self.driver.find_element_by_name("q").send_keys("Try" + Keys.RETURN)
        return 1

    def certificateScan(self):
        self.addagruments()                                                   # adding the arguments for webdriver
        errorCount=0
        if not self.digicert():
            errorCount = errorCount+1
        return errorCount

    def domainExtractor(self):                                                # domain extrater for the certificate scanning input
        result = tldextract.extract(self.sslUrl)
        return result.registered_domain

def start(url):
    target_url = url
    scan = CertificateScanner(target_url)

    result = scan.check_Hardcode()                      #Scanning hardcode

    if result == 'X':
        return("Page not Found!!! (check your internet connection) (point 0)")
         
    elif result:
        return("Match Found!! Should be rejected (point 1)")
    else:
        return("Found Nothing!! (point 0)")

    # domain_name = scan.domainExtractor()                #extracting domain name
    # print("\n The Domain Name: "+ str(domain_name))


    validity = scan.certificateScan()                   #certificate scanning
    print("\nThe Validity:"+ str(validity))

