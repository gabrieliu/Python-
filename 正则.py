import requests
import re
import xlwt

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
        av_number = re.findall(r'o/.*?\?f',html)
        for i in range(len(up_names)):
            up_name = re.split(r'">|</', up_names[i])[1]
            video_title = video_titles[i].split('"')[1]
            avnum =  av_number[i].strip('o/?f')
            ilt.append([up_name,video_title,avnum])
    except:
        print(" ")

def printGoodsList(ilt):
    tplt="{0:^10}\t{1:{4}^10}\t{2:{4}^30}\t{3:{4}^30}"
    print(tplt.format("序号","up主","视频名称","AV号",chr(12288)))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1],g[2],chr(12288)))

def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
    f.save(file_path)

def main():
    word = "美食作家王刚R"
    page = 4
    start_url= "https://search.bilibili.com/all?keyword=" + word
    infoList = []
    filepath = "C://Users//jsrgl//Desktop//1.xls"
    for i in range(page):
        try:
            url = start_url +"&order=click&duration=0&tids_1=0"+ "&page=" + str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
        print(str(i+1)+"/"+str(page)+" pages are finished")
    printGoodsList(infoList)
    data_write(filepath,infoList)
main()