import bs4, requests, os

os.system('cls' if os.name == 'nt' else 'clear')

def search(word,news):
    search_news ={}
    for i in news.keys():
        if i.find(word) !=-1:
            search_news[i] = news[i]
    for i in news.values():
        if i.find(word) !=-1:
            k = list(news.keys())
            search_news[k[list(news.values()).index(i)]]=i
    if len(search_news)==0:
        return 'No record found'
    else:
        return search_news

print('Scrapping...........')   
res = requests.get(
    'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen', headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
main_news = soup.select('div > article > h3 > a')
#print(len(main_news))
c=0
news={}
for i in range(len(main_news)):
    #if main_news[i].text.startswith('Corona'):
    sub_news = soup.select('div:nth-child('+str(i+1)+') > div > div.SbNwzf > article:nth-child(1) > h4 > a')
    #print(main_news[i].text)
    c += 1  
    try:
        sub_news[0].text
        news[main_news[i].text] = sub_news[0].text
    except:
        news[main_news[i].text] = ''

    
print(news,'\nTotal news = ',c,'\n---------------------------\n')
print('searched word news are -\n',search(input('Enter words to search '),news))

