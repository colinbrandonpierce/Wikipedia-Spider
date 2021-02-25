import bs4
import requests
import random
import pickle

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def add_to_dic(obj, links, dic, flag):
    if flag == 0: # if a link
        if obj in dic:
            dic[obj[0]] = dic[obj[0]]+1#, dic[obj[1]]]
        else:
            dic[obj] = [0, 0]
    else: # if main page
        try:
            dic[obj] = [dic[obj[0]], links]
        except:
            dic[obj] = [0, links]
            #print("------------new entry------------") # never visited nor added to dictionary
        
        
def recur(dic, pages, start_page, index):
    index += 1
    response = requests.get(start_page) # pull page
    html = bs4.BeautifulSoup(response.text, 'html.parser') #parse page
    title = html.select("#firstHeading")[0].text
    pages.append(title.lower())
    
    
    links = [] # links on page
    paragraphs = html.select("p")
    for para in paragraphs:
        try:
            for i in para.find("a"):
                if not hasNumbers("{}".format(i)):
                    links.append(i)
                    add_to_dic(i, links, dic, 0)
        except:
            pass
        
    add_to_dic(title, links, dic, 1) 
        
    if  index % 100 == 0: # update master file
        f = open("master.pkl", "wb") # NEEDS WORK
        pickle.dump(dic,f)
        f.close()
        print("------------UPDATED------------")
        print("------------index = {}------------".format(index))
    
    sentinel = 0
    while sentinel == 0:
        maxx = len(links)
        tries = 0
        
        j = links[random.randint(0,len(links))] # pick random page to go to (cant do more than one at a time apparantly)
        try:
            tries += 1
            if j.lower() not in pages:
                url = "https://en.wikipedia.org/wiki/{}".format(j.replace(" ", "_"))
                print("{}".format(j))
                recur(dic, pages, url, index)    
                sentinel = 1 # just in case you can heh
            elif tries == maxx: # if all pages have been visited
                url = "https://en.wikipedia.org/wiki/Special:Random"
                print("------------visiting random page------------")
                recur(dic, pages, url, index)
            #else:
            #    print("page visited! = {}".format(j))

        except:
            pass


DIC = {} # run LOAD PICKLE HERE
pages = [] # pages visited
index = 0;
recur(DIC, pages, "https://en.wikipedia.org/wiki/Philosophy", index)



#while response is not None:
#title = html.select("#firstHeading")[0].text
 #add_to_dic(title, dic)
    #print(dic)
    
    #    if  index == 100:
#        print(dic)
#        index = 0