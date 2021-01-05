# -*- coding:utf-8 -*-
import random
import time
import xlrd
import requests
import datetime
import re
from collections import OrderedDict
from urllib3 import encode_multipart_formdata
import string
from requests_toolbelt import MultipartEncoder
from lxml import etree
from time import sleep
from selenium import webdriver
import os
import json




def Post_bug():
    r = requests.session()
    #获取你的redminebug地址
    url1 = r.get('url')
    #获取你的cookies
    url_cookie = url1.cookies.get_dict()
    #获取提交bug的token在页面中
    get_token = re.findall(r'<meta name="csrf-token" content="(.*)"', url1.text)
    header = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/84.0.4147.125Safari/537.36',
        'origin': 'url',
        'referer': 'url',
        'content-type': 'url'
    }
    data = {
        'utf8': '✓',
        'authenticity_token': get_token[0],
        'back_url': 'url',
        'username': 'user',
        'password': pwd,
        'login': '登录',
    }
    r1 = r.post('url',
                data=data,
                headers=header)

    day_today = datetime.date.today()

   
    r3 = r.get('url',headers=header)
    etree_page = etree.HTML(r3.text)
    #获取提交bugtoken
    token_value =etree_page.xpath('//*[@id="issue-form"]/input[2]/@value')
    # print(token_value)
    #获得表格内容第一行为标题，第二行为内容
    wb1 = xlrd.open_workbook(r'path')
    table = wb1.sheets()[0]
    for i in range(1,table.nrows):
        if i < table.nrows:
            title2 = table.row_values(i,0)
            print(title2)
        else:
            break
        header1 = {
            'x-csrf-token': token_value[0],
            'content-type': 'application/octet-stream',
            'referer': 'https://redmineurl/projects/web_test/issues/new',
            'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/84.0.4147.135Safari/537.36'

        }
        #使用表单from-data方式提交bug
        m = MultipartEncoder(
            fields={
                'utf8': '✓',
                'authenticity_token': token_value[0],
                'form_update_triggered_by': '',
                'issue[is_private]': '0',
                'issue[tracker_id]': '1',
                'issue[subject]': title2[0],
                'issue[description]': title2[1],
                'issue[status_id]': '1',
                'was_default_status': '1',
                'issue[priority_id]': '4',
                'issue[assigned_to_id]': '892',
                ' issue[parent_issue_id]': '',
                'issue[start_date]': f"{time.strftime('%Y-%m-%d', time.localtime(time.time()))}",
                'issue[due_date]': '',
                'issue[estimated_hours]': '',
                'issue[done_ratio]': '0',
                'issue[custom_field_values][1]': 'Definitely(100%)',
                'issue[custom_field_values][2]': '0',
                'issue[custom_field_values][3]': 'VIP0',
                'issue[custom_field_values][4]': '',
                'issue[custom_field_values][5]': '',
                'issue[custom_field_values][8]': '',
                'attachments[1][filename]': '',
                'attachments[1][description]':'',
                'attachments[dummy][file]': '(binary)',
                'issue[watcher_user_ids][]': '',
                'commit': '创建'
            },
            #提交bug的时候需要有一个随机的加密码
            boundary=f'----WebKitFormBoundary{"".join(random.sample(string.ascii_letters + string.digits, 16))}'
        )
        header2 = {
            'content-type': m.content_type,

        }

        r4 = r.post('https://redminurl/projects/web_test/issues', data=m,
                    headers=header2)
        print(r4.request.body)
        if r4.status_code == 200:
            print("bug提交完成")
        else:
            print('Fail')
        sleep(3)
    # webscan = webdriver.Chrome
        # with open("text.html", "w")as f:
        #     f.write(r4.text)






if __name__ == '__main__':
    Post_bug()
