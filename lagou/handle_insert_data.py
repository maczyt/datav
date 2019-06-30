from create_tables import LagouTable
from create_tables import Session
import time

class HandleLagouData(object):
  def __init__(self):
    # 实例化session
    self.mysql_session = Session()
    self.date = time.strftime('%Y-%m-%d', time.localtime())

  #数据的存储方法
  def insert_item(self,item):
    #今天
    date = time.strftime("%Y-%m-%d",time.localtime())
    #存储的数据结构
    data = LagouTable(
      #岗位ID
      positionID = item['positionId'],
      # 经度
      longitude=item['longitude'],
      # 纬度
      latitude=item['latitude'],
      # 岗位名称
      positionName=item['positionName'],
      # 工作年限
      workYear=item['workYear'],
      # 学历
      education=item['education'],
      # 岗位性质
      jobNature=item['jobNature'],
      # 公司类型
      financeStage=item['financeStage'],
      # 公司规模
      companySize=item['companySize'],
      # 业务方向
      industryField=item['industryField'],
      # 所在城市
      city=item['city'],
      # 岗位标签
      positionAdvantage=item['positionAdvantage'],
      # 公司简称
      companyShortName=item['companyShortName'],
      # 公司全称
      companyFullName=item['companyFullName'],
      # 公司所在区
      district=item['district'],
      # 公司福利标签
      companyLabelList=','.join(item['companyLabelList']),
      salary=item['salary'],
      # 抓取日期
      crawl_date=date
    )

    #在存储数据之前，先来查询一下表里是否有这条岗位信息
    query_result = self.mysql_session.query(LagouTable).filter(LagouTable.crawl_date==date,
                                                                LagouTable.positionID==item['positionId']).first()

    if query_result:
      pass
    else:
      #插入数据
      self.mysql_session.add(data)
      #提交数据到数据库
      self.mysql_session.commit()

lagou_mysql = HandleLagouData()