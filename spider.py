import bs4
import requests

def add_to_dic(obj, dic):
    if obj in dic:
        dic[obj] = dic[obj]+1
    else:
        dic[obj] = 0
        
def recur(DIC, pages_visited, start_page):
    response = requests.get(start_page)
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
            
        paragraphs = html.select("p")
        for para in paragraphs:
            try:
                for j in para.find("a"):
                    add_to_dic(j,DIC)
            except:
                pass
       # recur(DIC, pages_visited, start_page)
    else:
        return 0


DIC = {}
pages_visited=[]
recur(DIC, pages_visited, "https://en.wikipedia.org/wiki/Philosophy")
print(DIC)






#while response is not None:
    #title = html.select("#firstHeading")[0].text
    #print(title)


 #   intro = '\n'.join([ para.text for para in paragraphs[0:5]])
   # print (intro)