import bs4
import requests
import random
    
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def visit(page):
    r = requests.get(page)
    html = bs4.BeautifulSoup(r.content, 'html.parser') #parse page
    title = html.select("#firstHeading")[0].text
    title = title.replace(" ", "_")
    paragraphs = html.select("p")
    links = []
    nono1 = ":"; nono2 = "[update]"
    for para in paragraphs:
        linx = para.findAll('a')
        try:
            for i in linx:
                if (not hasNumbers("{}".format(i))) and ((nono1 or nono2) not in i):
                    i = i.get('title').replace(" ", "_")
                    links.append(i)
        except:
            pass
    return html, title, links

def write(file, line):
    f = open(file, "a")
    f.write(line)
    f.close()

def iterr(pages, start_page, index):
    #TOTAL_PAGES = 6257751
    MAX_PAGES = 1000000

    html, title, links = visit(start_page)
    
    write("pages_visited.txt", "{}\n".format(title))
    for i in links:
        write("master.txt", "{} {}\n".format(title,i))

    while index < MAX_PAGES:
        if index % 1000 == 0:
            print("------------index = {}------------".format(index))

        maxx = len(links)
        tries = 0
        while tries <= maxx:
            try: # html failure
                tries += 1
                if maxx>1:
                    j = links[random.randint(0,maxx-1)] # pick random page to go to
                else:
                    j = None
                if j not in pages and j is not None:
                    url = "https://en.wikipedia.org/wiki/{}".format(j)
                    index+=1
                    
                    html, title, links = visit(url)
                    write("pages_visited.txt", "{}\n".format(title))
                    for i in links:
                        write("master.txt", "{} {}\n".format(title,i))
                    pages.append(title) # track redirects instead of shown title
                    print("{}".format(title.replace("_", " ")))
                    
                #elif tries == maxx or maxx == 0: # if all pages have been visited or no links (say, just charts)
                else:
                    url = "https://en.wikipedia.org/wiki/Special:Random"
                    index+=1
                    
                    html, title, links = visit(url)
                    for i in links:
                        write("master.txt", "{} {}\n".format(title,i))
                    pages.append(title)
                    print("-{}".format(title.replace("_", " ")))
            except:
                pass
    print("finished")

pages = ["Philosophy"] # pages visited
try:
    fe = open("pages_visited.txt", "r")
    for line in fe:
        titlee = line.split()[0]
        pages.append(titlee)
    fe.close()
except:
    pass
#print(pages)
index = 1;
iterr(pages, "https://en.wikipedia.org/wiki/Philosophy", index)



#while response is not None:

#program improvements: huge slowdown mechanic, database stuff?
