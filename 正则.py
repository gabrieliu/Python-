import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def parsePage(ilt,html):
    try:
        up_names = re.findall(r'up-name">.*?</a>',html)
        video_titles = re.findall(r'<a title=\".*?\"',html)
        for i in range(len(up_names)):
            up_name = re.split(r'">|</', up_names[i])[1]
            video_title = video_titles[i].split('"')[1]
            ilt.append([up_name,video_title])
    except:
        print(" ")

def printGoodsList(ilt):
    tplt="{0:^10}\t{1:{3}^10}\t{2:{3}^16}"
    print(tplt.format("序号","up主","视频名称",chr(12288)))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1],chr(12288)))

def main():
    word = "莓可"
    page = 4
    start_url= "https://search.bilibili.com/all?keyword=" + word
    infoList = []
    for i in range(page):
        try:
            url = start_url + "&page=" + str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
        print(str(i)+"/"+str(page)+" pages are finished")
    printGoodsList(infoList)
main()