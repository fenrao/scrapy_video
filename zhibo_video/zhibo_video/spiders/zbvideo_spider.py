import scrapy
import json
import re
import requests
from ..items import ZhiboVideoItem

class zbVideoSpider(scrapy.Spider):
     name = "zhibo"
     def start_requests(self):
         self.data = {'app': 'api',
                 'mod': 'Login',
                 'act': 'login',
                 'device': 'SM-G955N',
                 'udid': '484520b9d7191359',
                 'version': '3.8',
                 'uname': '', 			#先下载app注册账号
                 'upwd': '',			#输入账号密码
                 'oauth_token': '',
                 'oauth_token_secret': '',

                 }
         loginurl = 'https://www.shengbenbang.cn/index.php?app=' + self.data['app'] + '&mod=' + self.data['mod'] + '&act=' + self.data[
             'act'] + '&device=' + self.data['device'] + '&udid=' + self.data['udid'] + '&version=' + self.data[
                        'version'] + '&uname=' + self.data['uname'] + '&upwd=' + self.data['upwd']
         self.header = {
             'Content-Length': '0',
             'Host': 'www.shengbenbang.cn',
             'Connection': 'Keep-Alive',
             'User-Agent': 'okhttp/3.10.0',
         }
         yield  scrapy.FormRequest(url=loginurl,headers=self.header,callback=self.parse_login)

     def parse_login(self,response):
         postdata = json.loads(response.text)
         self.data['oauth_token'] = postdata['data']['oauth_token']
         print(self.data['oauth_token'])
         self.data['oauth_token_secret'] = postdata['data']['oauth_token_secret']
         print( self.data['oauth_token_secret'])
         self.data['mod'] = 'Video'
         self.data['act'] = 'videoList'
         self.data['orderBy'] = 'default'
         self. data['pType'] = 1
         self. data['cateId'] = 0
         self.data['page'] = 1
         self. data['page'] = 60  # 获取每页视频数 直接设置为最大
         url =[ 'https://www.shengbenbang.cn/index.php?app=api&mod=Video&act=videoList&device=SM-G955N&udid=484520b9d7191359&version=3.8&oauth_token=6b79dfc96c9a42d558400aa65c98887e&oauth_token_secret=389111ed1e099c72ad9447f6d63182a4&orderBy=default&pType=0&cateId=8&page=1&count=60','https://www.shengbenbang.cn/index.php?app=api&mod=Video&act=videoList&device=SM-G955N&udid=484520b9d7191359&version=3.8&oauth_token=6b79dfc96c9a42d558400aa65c98887e&oauth_token_secret=389111ed1e099c72ad9447f6d63182a4&orderBy=default&pType=0&cateId=0&page=1&count=60']
         for i in url:
            yield scrapy.Request(url=i,callback=self.parse_list, headers=self.header,dont_filter=True)#dont_filter=True不去重

     def parse_list(self,response):
             list = json.loads(response.text)
             #print(list)
             video_title = [i['video_title'] for i in list['data']]
             video_id = [i['id'] for i in list['data']]

             self.data['act']='getCatalog'
             url='https://www.shengbenbang.cn/?app='+self.data['app']+'&mod='+self.data['mod']+'&act=getCatalog&device=SM-G955N&udid=484520b9d7191359&version=3.8&oauth_token='+self.data['oauth_token']+'&oauth_token_secret='+self.data['oauth_token_secret']+'&id='
             for i in range(len(video_title)):
                 yield scrapy.Request(url=url+str(video_id[i]),headers=self.header,callback=self.parse_video, dont_filter=True,meta={'title':video_title[i]})



     def parse_video(self, response):

            jj=json.loads(response.text)
            print(response.meta.get('title'))
            video_url=[]
            video_title=[]
            for data in jj['data']:

                    for child in data['child']:
                        try:
                            video_url.append(child['video_address'])
                            video_title.append(child['title'])
                        except Exception as e:
                            video_url.append('########')
                            video_title.append(child['title'])

            item=ZhiboVideoItem()
            item['title'] = response.meta.get('title')
  
            yield item
            item['title']=[]
            for i in range(0,len(video_url)):
                item['video_title']=video_title[i]
                item['video_url']=video_url[i]
                yield  item
           
