# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:19:06 2017

@author: Administrator
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')#链接数据库，没有就创建
c = conn.cursor()#创建游标
conn.execute('drop table if exists company') #如果存在这个表就删掉
c.execute('''create table company
          (title text,
          link text,
          category text,
          num text,
          city text,
          time time,
          jobduties text,
          jobrequirement text
          );''') #建表
conn.commit() #保存
item = ["24548-综艺商业制片人","http://hr.tencent.com/position_detail.php?id=33369&keywords=&tid=0&lid=0","产品/项目类", "2","北京", "2017-10-16","负责节目招商变现，统筹规划节目售卖库存及售卖策略； 能根据品牌诉求与品类特点，提供植入营销方案，支持销售提案； 全程跟进节目策划及录制，保证客户权益落实，维护客户合作满意度； 有效沟通，面向客户、协同部门及合作团队等，解决项目进程的问题。", "热爱综艺节目，具备3年以上节目制片经验，能够独立运行项目，包括项目的研发及执行； 一定程度了解客户营销需求，有一定广告行业经验者优先； 具备良好的客户服务意识及沟通能力，良好的逻辑思维及策划能力，项目的统筹与协调能力； 精通PPT，Excel等Office软件，有一定英语沟通能力为佳。"]
insql = 'insert into company values(?,?,?,?,?,?,?,?)'
c.execute(insql,(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
#插入数据
conn.commit()#保存
c.execute("insert into company values ("'a''b''c''d''e''f''g''h'")")
c.execute('''CREATE TABLE master2 (
        type TEXT,
        name TEXT,
        tbl_name TEXT,
        rootpage INTEGER,
        sql TEXT
        );''')
c.execute("select name from sqlite_master where type = 'table'")
c.fetchall()

selsql = 'select * from company' #c查找出company表中的所有数据
df = pd.read_sql(selsql,conn) #将查找出的数据加载成DataFrame

df.to_sql('company',conn,if_exists='fail')#将DataFrame的数据写入数据库campany表
#if_exists='fail'如果表存在，则什么都不做，‘replace’覆盖 ‘append’追加

comm = sqlite3.connect(r'D:\Anaconda\test\tencent\test.db')

