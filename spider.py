import bs4
import requests
import random
#import os

# try: # start from fresh file
#     os.remove("master.txt")
# except:
#     pass
    
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def recur(pages, start_page, index):
    #TOTAL_PAGES = 6257751

    r = requests.get(start_page) # pull page
    html = bs4.BeautifulSoup(r.content, 'html.parser') #parse page
    title = html.select("#firstHeading")[0].text
    
    links = [] # links on page
    paragraphs = html.select("p")
    for para in paragraphs:
        linx = para.findAll('a')
        try:
            for i in linx:
                if not hasNumbers("{}".format(i)) and i != "[update]":
                    links.append(i.get('title').replace(" ", "_"))
                    f = open("master.txt", "a")
                    f.write("{} {}\n".format(title.replace(" ", "_"), i.get('title').replace(" ", "_")))
                    f.close()
        except:
            pass
        
    #if index != TOTAL_PAGES: # if visited everything (SHOULD BE A BIG SLOWDOWN MECHANIC INSTEAD)
    sentinel = 0
    while sentinel == 0:
        maxx = len(links)
        tries = 0
        
        j = links[random.randint(0,len(links))] # pick random page to go to (cant do more than one at a time apparently)
        try:
            tries += 1
            if j not in pages:
                url = "https://en.wikipedia.org/wiki/{}".format(j)
                print("{}".format(j))
                pages.append(j) # track redirects instead of page titles
                index+=1
                recur( pages, url, index)    
                sentinel = 1 # just in case you can
            elif tries == maxx or maxx == 0: # if all pages have been visited or no links (say, just charts)
                url = "https://en.wikipedia.org/wiki/Special:Random"
                print("------------visiting random page------------")
                index+=1
                recur( pages, url, index)
        except:
            pass

pages = ["Philosophy"] # pages visited
try:
    fe = open("master.txt", "r")
    for line in fe:
        titlee = line.split()[0]
        if titlee not in pages:
            pages.append(titlee)
    fe.close()
except:
    pass
print(pages)
index = 1;
recur(pages, "https://en.wikipedia.org/wiki/Philosophy", index)



#while response is not None:

#program improvements: huge slowdown mechanic, database stuff?
