from criteria.hardcodeMsg import SCAN, domainExtractor
from plyer import notification
from module.colour import color

def start(url): 
    try:
        point = SCAN(url)
        domain_name = domainExtractor(url)
        if "Suspecion" in point:
            suspecion = '80'
        else:
            suspecion = '10'
        msg ="DOMAIN := " + domain_name +"\nRESULT := "+ point +"\nDANGER := "+suspecion+"%"
    except Exception:
        msg = "Error Occured(tryAgain)"

    if domain_name == "":
        msg = "Please Select a link!!"

    notification.notify( 
                app_icon  = "icon128.ico",
                title = "PhishHunter", 
                message= msg, 
                timeout=3
        ) 


    return(point)

# url = "https://vip-l82.work/sb/?th=#1609078595595"
# start(url)
