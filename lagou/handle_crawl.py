import requests
import re
import time
import json
import multiprocessing
from handle_insert_data import lagou_mysql

class Handle(object):
  def __init__(self):
    # 使用session保存cookie信息
    self.session = requests.session()
    self.header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    self.city_list = ""

  # 获取全国城市列表
  def handle_city(self):
    city_search = re.compile(r'zhaopin/">(.*?)</a>')
    city_url = "https://www.lagou.com/jobs/allCity.html"
    city_result = self.handle_request(method="GET",url=city_url)
    self.city_list = city_search.findall(city_result)
    self.session.cookies.clear()

  # 获取某城市的工作
  def handle_city_job(self, city):
    print('爬取city:%s'%city)
    # first_request_url = "https://www.lagou.com/jobs/list_python?px=default&city=%s#filterBox"%city
    first_request_url = "https://www.lagou.com/jobs/list_web前端?px=default&city=%s#filterBox"%city
    
    first_response = self.handle_request(method="GET", url=first_request_url, info=city)
    total_page_search = re.compile(r'totalNum(?:.*?)">(\d+)</span>')
    try:
      total_page = total_page_search.search(first_response).group(1)
    except:
      return
    else:
      for i in range(1, int(total_page) + 1):
        data = {
          "pn": i,
          "kd": "web前端"
        }
        page_url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false"%city
        # referer_url = "https://www.lagou.com/jobs/list_python?px=default&city=%s"%city
        referer_url = "https://www.lagou.com/jobs/list_web前端?px=default&city=%s"%city        
       
        # referer需要encode
        self.header['Referer'] = referer_url.encode()
        response = self.handle_request(method="POST", url=page_url, data=data, info=city)
        data = json.loads(response)
        job_list = data['content']['positionResult']['result']
        for job in job_list:
          lagou_mysql.insert_item(job)

  def handle_get_proxy(self):
    response = requests.get('http://118.24.52.95:5010/get/')
    return response.text
  def handle_delete_proxy(self, proxy):
    response = requests.get('http://118.24.52.95:5010/delete/?proxy=%s'%proxy)

  def handle_request(self, method, url, data=None, info=None):
    while True:
      # 加入动态代理
      proxyinfo = self.handle_get_proxy()
      proxy = {
        "http": "http://%s"%proxyinfo,
      }
      try:
        if method == 'GET':
          response = self.session.get(url=url,headers=self.header,timeout=6,proxies=proxy)
        elif method == 'POST':
          response = self.session.post(url=url,headers=self.header,data=data,timeout=6,proxies=proxy)
      except:
        # 需要清理cookie信息
        self.session.cookies.clear()
        # 重新获取cookie信息
        first_request_url = "https://www.lagou.com/jobs/list_web前端?px=default&city=%s#filterBox"%info
        # first_request_url = "https://www.lagou.com/jobs/list_python?px=default&city=%s#filterBox"%info
        self.handle_request(method="GET",url=first_request_url)
        self.handle_delete_proxy(proxy=proxyinfo)
        # 睡眠10s
        time.sleep(10)
        continue
      response.encoding = 'utf-8'

      if '频繁' in response.text:
        print(response.text)
        # 需要清理cookie信息
        self.session.cookies.clear()
        # 重新获取cookie信息
        # first_request_url = "https://www.lagou.com/jobs/list_python?px=default&city=%s#filterBox"%info
        first_request_url = "https://www.lagou.com/jobs/list_web前端?px=default&city=%s#filterBox"%info
        self.handle_request(method="GET",url=first_request_url)
        self.handle_delete_proxy(proxy=proxyinfo)
        # 睡眠10s
        time.sleep(10)
        continue
      return response.text

if __name__ == '__main__':
  h = Handle()
  h.handle_city()
  # 创建进程池
  pool = multiprocessing.Pool(2)

  for city in h.city_list:
    pool.apply_async(h.handle_city_job, args=(city,))
  # 关闭进程池
  pool.close()
  pool.join()