# coding=utf-8
# python2中运行
import re
import urllib2

# 1 收集数据
myUrl = "http://www.xicidaili.com/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(myUrl, headers=headers)
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()
# print len(myPage)

# 2 处理数据（筛选）
str = r'''<tr class=".*?">\n    <td.+?</td>\n    <td>(.+?)</td>\n    <td>(.+?)</td>\n    <td>(.+?)</td>\n    <td class="country">.+?</td>\n    <td>(.+?)</td>\n      <td>.+?</td>\n    <td>.+?</td>\n  </tr>'''
p = re.compile(str)
matchs = p.findall(myPage)
# print len(matchs)

# 3 输出数据
th_title = "%6s\t%20s\t%9s\t%10s\t%14s" % ('序号', 'ip', '端口', '类型', '所在地')
print th_title
for i, item in enumerate(matchs):
    print "%4s\t%16s\t%6s\t%8s\t%s" % (i, item[0], item[1], item[3], item[2])
