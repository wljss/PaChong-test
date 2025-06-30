from bs4 import BeautifulSoup
import requests
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36"}#修改请求头，伪装成浏览器

for start_num in range(0,250,25):
    response =requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=head) #f表示格式化，start_num是确定爬第几页/从第几个开始爬
    content=response.text
    soup=BeautifulSoup(content,"html.parser")
    all_titles = soup.findAll("span",attrs={"class":"title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:#这个是因为豆瓣电影原名前有“/”，这样做就不用打印原名了
            print(title_string)