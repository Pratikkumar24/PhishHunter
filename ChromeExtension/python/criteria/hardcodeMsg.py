from module.Module import *

# url ="https://vip-l82.work/sb/?th=#1609078595595"

class HardCode_Scanner:
    def __init__(self, url):
        self.session = requests.Session()
        self.target_url = url
        self.chrome_options = webdriver.ChromeOptions()
        self.completeUrl()

    def completeUrl(self):
        if not re.match('(?:http|ftp|https)://', self.target_url):
            self.target_url = 'https://{}'.format(self.target_url)   
  
    def check_Hardcode(self):
        try:
            response = self.session.get(self.target_url)
        except Exception:
            return 'X'

        regex = r" Share it until the blue bar is full|Share until the blue bar is full"
        return re.search(regex,(response.content).decode(errors="ignore"))

    

def SCAN(url):
    target_url = url
    scan = HardCode_Scanner(target_url)
    
    result = scan.check_Hardcode()                      #Scanning hardcode

    if result == 'X':
        return("Page not Found!!!")
         
    elif result:
        return("Suspecion Increased!!!")
    else:
        return("Found Nothing!!")

def domainExtractor(url):                                                # domain extrater for the certificate scanning input
    result = tldextract.extract(url)
    return result.registered_domain