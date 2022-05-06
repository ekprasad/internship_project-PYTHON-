import requests
from bs4 import BeautifulSoup as bs
from random import choice
def get_proxy():
    url= "https://free-proxy-list.net/"
    proxie=[] #to srore proxy
    soup= bs(requests.get(url).content,"html.parser")
    for row in soup.find("table", attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds=row.find_all("td")
        try:
            ip=tds[0].text.strip()
            port=tds[1].text.strip()
            proxie.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxie
print(get_proxy())
url ="http://httpbin.org/ip"
proxies=get_proxy()
working_proxy=[]
for i in range(10):
   # print("Request Number:" + str(i+1))
    proxy=proxies[i]
    #proxy=get_random_proxy(proxies)
    print(f"using {proxy}...")
    try:
        r=requests.get(url,proxies={"http":proxy,"https":proxy},timeout=3)
        print(r.status_code)
        if r.status_code==200:
            working_proxy.append(proxy)
            
    except:
        pass
print(working_proxy)
current_proxy=choice(working_proxy)
stock_list=["RELIANCE","NMDC","BPCL"]
for stock_name in stock_list:
#stock_name="RELIANCE"
    #print(current_proxy)
        rl_link=requests.get(f"https://www.screener.in/company/{stock_name}/consolidated/")#,proxies={"http":current_proxy,"https":current_proxy})
        soup1 = bs(rl_link.content,"html.parser")
    #for i in stock_list:
        name = soup1.find("div", class_="flex-row flex-wrap flex-align-center flex-grow").h1.text
        print(name)
        price=soup1.find("div",class_="flex flex-align-center").span.text
        time=soup1.find("div",class_="ink-600 font-size-11 font-weight-500").text.split()

print(price)
print(' '.join(time))

rl_data=soup1.find("div",class_="company-ratios").find_all('li')
    
stock_dict={}
stock_dict["name"]=stock_name
    #current_date
    
for data in rl_data:
        
        label = data.find("span", class_="name").text.strip()
        val=data.find("span",class_="number").text.strip()
        stock_dict[label]=val
print(stock_dict)  

