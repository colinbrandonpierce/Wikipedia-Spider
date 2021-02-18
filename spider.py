import bs4
import requests
import random

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def add_to_dic(obj, dic):
    if obj in dic:
        dic[obj] = dic[obj]+1
    else:
        dic[obj] = 0
        
def recur(dic, pages, start_page):
    response = requests.get(start_page)
    html = bs4.BeautifulSoup(response.text, 'html.parser')
        
    #title = html.select("#firstHeading")[0].text
        
    #add_to_dic(title, dic)
    #print(dic)
            
    paragraphs = html.select("p")
    for para in paragraphs:
        try:
            for i in para.find("a"):
                if not hasNumbers("{}".format(i)):
                    pages.append(i)
                    add_to_dic(i, dic)
        except:
            pass

    j = pages[random.randint(0,len(pages))]
    url = "https://en.wikipedia.org/wiki/{}".format(j.replace(" ", "_"))
    try:
        print("visiting page: {}".format(j))
        recur(dic, pages, url)           
    except:
        j = pages[random.randint(0,len(pages))]
        url = "https://en.wikipedia.org/wiki/{}".format(j.replace(" ", "_"))
        print("visiting page: {}".format(j))
        recur(dic, pages, url)


DIC = {"Philosophy":1}
pages = []
recur(DIC, pages, "https://en.wikipedia.org/wiki/Philosophy")



#while response is not None:
