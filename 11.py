import time
print("==========================time模块====================================",end='\n')
now_time = time.strftime('%m%d%H%M%S', time.localtime())
print(now_time)
print(time.localtime(),type(time.localtime()))


#:推迟指定的时间运行，单位为秒
# time.sleep()

# datetime模块
# datetime.time():生成一个时间对象。这个时间可以由我们来设置，默认都是0(这个类只针对时间)
import datetime
print("==========================datetime.time====================================",end='\n')
t = datetime.time(23, 20, 2, 2)
print(t)  # 输出的时间23:20:02.000002
print(t.hour)  # 时23
print(t.minute)  # 分20
print(t.second)  # 秒2
print(t.microsecond)  # 毫秒2
print("==========================datetime.date====================================",end='\n')
# datetime.date():生成一个日期对象。这个日期要由我们来设置，(这个类只针对日期)
t = datetime.date(2023,2,1)

#获取今天的时间
today = datetime.date.today()
print(today)
