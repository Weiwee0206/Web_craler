from ast import Num
from importlib.resources import path
from pprint import pprint
from telnetlib import SE
#from matplotlib.pyplot import text
#import youtube_dl
import requests
import re
from bs4 import BeautifulSoup
import json
import yt_dlp


def Download_video(Result, Video_Num):  ###
    for i in range(Video_Num):
        youtube_url = "https://www.youtube.com/watch?v=" + Result["Video_ID (" + str(i + 1) + ")"] + "&ab_channel=" + \
                      Result["Channel_ID (" + str(i + 1) + ")"]
        # Result["Video_ID ("+i+")"]
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(youtube_url, download=True)

    return 0


def Search_Video_Id(YT_Data_API, Video_Num, SearchKeyword):  # 搜尋頁面的影片標題、影片ID、頻道ID
    Search_path = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + SearchKeyword + "&key=" + YT_Data_API + "&type=video&maxResults=" + str(
        Video_Num)
    video_info = {}  # 存放資訊到字典
    res = requests.get(url=Search_path)
    data_json = json.loads(res.text)
    f = open(SearchKeyword + "_Search.json", "w", encoding='UTF-8')
    f.write(res.text
            )
    f.close()
    for i in range(Video_Num):
        video_info["Video_Title (" + str(i + 1) + ")"] = data_json['items'][i]['snippet']['title']
        print("第" + str(i + 1) + "部影片標題 :" + data_json['items'][i]['snippet']['title'])

        video_info["Video_ID (" + str(i + 1) + ")"] = data_json['items'][i]['id']['videoId']
        print("第" + str(i + 1) + "部影片 ID :" + data_json['items'][i]['id']['videoId'])

        video_info["Channel_ID (" + str(i + 1) + ")"] = data_json['items'][i]['snippet']['channelId']
        print("第" + str(i + 1) + "部頻道 ID :" + data_json['items'][i]['snippet']['channelId'])

    return video_info  # 回傳字典


def Write_Video_Info(Result, Video_Num, SearchKeyword):  # 寫入TXT
    f = open(SearchKeyword + "_Search.txt", "w", encoding='UTF-8')  ####
    for i in range(Video_Num):
        f.write("Title : " + Result["Video_Title (" + str(i + 1) + ")"] + "\n")
        f.write("VideoID : " + Result["Video_ID (" + str(i + 1) + ")"] + "\n")
        f.write("ChannelID : " + Result["Channel_ID (" + str(i + 1) + ")"] + "\n\n")
    f.close()
    return 0


if __name__ == '__main__':
    print("請輸入關鍵字 : ")
    SearchKeyword = input()  # input() #搜尋關鍵字
    print("請輸入搜尋影片數量 : ")
    Video_Num = 50  # 影片數量
    YT_Data_API = 'AIzaSyC74YHsxBkMDH86jP_imXmod5MQA-RNZ24'  # Youtube_Data_API
    SearchVideo_Path = ('https://www.youtube.com/results?search_query=' + SearchKeyword)  # 搜尋頁面連結

    # res = requests.get(url = Search_path)
    # data_json = json.loads(res.text)
    Result = Search_Video_Id(YT_Data_API, int(Video_Num), SearchKeyword)  # 抓取搜尋頁面資料
    Write_Video_Info(Result, int(Video_Num), SearchKeyword)  # 寫入txt檔

    Download_video(Result, Video_Num)
