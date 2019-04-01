# -*- coding: utf-8 -*-
import requests
import re
from time import sleep

class AddMoney():

    def __init__(self, cookie, uid, platform):
        self.cookie = cookie
        self.platform = platform
        self.uid = uid
        self.headers2 = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN',
        'Host': 'staging.authorize.zb.mi.srv',
        'Cookie': self.cookie,
        'Content-Type':'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control':'max-age=0',
        }

        self.user_data = {
        'applyer':'yibin',
        'applyReason':'测试',
        'uuid':self.uid,
        'money':'5000000',
        'platform': self.platform,
        'msg':'',
        'rechargeCode':'',
        }

    def get_key(self):
        send_data_url = "http://staging.authorize.zb.mi.srv/payment/direct-gemgiving/uploadGivingListMobile"
        req = requests.post(send_data_url, data=self.user_data, headers=self.headers2)
        key = re.findall('<font color=red>(.*)</td>', str(req.text))[0].strip()

        return key
    def get_giveld(self):
        giveid_url = "http://staging.authorize.zb.mi.srv/payment/direct-gemgiving/list?"
        req2 = requests.get(giveid_url, headers=self.headers2)
        giveid = re.findall('<a href="#" class="id">(.*)</a>', str(req2.text))[0]

        return giveid
    def add_money(self):
        add_url = "http://staging.authorize.zb.mi.srv/payment/direct-gemgiving/start"
        add_data = {
        'key': self.get_key(),
        'giveId': self.get_giveld(),
        }
        req3 = requests.post(add_url, data=add_data, headers=self.headers2)

        return req3.text
    def add_more_money(self, n):
        vale = 0
        for i in range(int(n)):
            result = self.add_money()
            if result == "OK":
                # print("第%s条添加完毕！总计添加金额: %s 元" % (i+1, 10000*(i+1)))
                vale += 1
                yield "第%s条添加完毕！总计添加金额: %s 元" % (i+1, 10000*(i+1))
            else:
                # print("第%s条添加失败！" % (i+1))
                yield "第%s条添加失败！" % (i+1)
        if vale == int(n):
            yield "充值成功！"

if __name__ == '__main__':
    cool = 'email.cookie=QfZiSvx5jzE7v25X99HhfkQ1SF+ekpeVP1UkwSLvXtw=; language.cookie=English; JSESSIONID=aaajtb3yURFTi5xgcCMEw'
    a = AddMoney(cool, '17216', 2).add_money()
    print(a)



