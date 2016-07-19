#Website I have scrapped: http://www.chicagoreader.com/chicago/best-of-chicago-2011/BestOf?oid=4100483

from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html,"lxml")

# I have used the Food and drinks section of the BOC list as section_url
def get_category_links(section_url):
    soup = make_soup(section_url)
    #search the <dl> element with boccat class and store  that section variable boccat
    boccat = soup.find("dl","boccat")
    #performing a list comprehension
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

#coming to http://www.chicagoreader.com/chicago/best-chef/BestOf?oid=4088191

def get_category_winner(category_url):
    soup = make_soup(category_url)
    #this will find the string within <h1 class="headline"> and store it in category
    category = soup.find("h1","headline").string
    #Performing list comprehension
    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"Category": category,
            "category Url": category_url,
            "Winner": winner,
            "Runners Up": runners_up}

if __name__ == '__main__':
    food_n_drink = ("http://www.chicagoreader.com/chicago/"
                    "best-of-chicago-2011-food-drink/BestOf?oid=4106228")

    categories = get_category_links(food_n_drink)

    data = []#list to store our dictionaries
    for category in categories:
        winner = get_category_winner(category)
        data.append(winner)
        print data




