# -*- coding: utf-8 -*-
更新所有数据
db.urllist.update({"status":3},{'$set':{"status":0}},false,true)
第一个false是设置数据不存在时，是否新增
第二个是设置更新所有
http://blog.csdn.net/mlz_2/article/details/46545081

默认是64位浮点型数值，对于整形可以使用NumberInt类或NumberLong类 db.xxx.insert({age:NumberInt("26"))

