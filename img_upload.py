# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import xlrd

class Upload_Img():
    #页面登录
    def get_html(self,account,pwd):
        self.acocunt = account
        self.pwd = pwd
        self.driver = webdriver.Firefox()
        self.driver.get('https://redmineurl/projects/web_test/issues')
        self.driver.maximize_window()
        sleep(3)
        if self.driver.find_element_by_name('login'):
            self.driver.find_element_by_id('username').send_keys(self.acocunt)
            sleep(5)
            self.driver.find_element_by_id('password').send_keys(self.pwd)
            sleep(5)
            self.driver.find_element_by_name('login').click()
            sleep(5)
            print('登录成功')
        else:
            print('该页面非登录页面')
    #寻找bug，进行上传图片
    def get_project_id(self):
        self.wb1 = xlrd.open_workbook(r'filepath.xls')
        table = self.wb1.sheets()[0]
        print('你需要上传的图片数量：'+str(table.nrows))
        for i in range(1, table.nrows):
            if i < table.nrows:
                #获取表格中bug的project_id
                id = table.cell(i,0).value
                # 获取表格中bug相对应需要上传的文件位置
                file_path = table.cell(i, 1).value

                if i+1 > table.nrows:
                    self.driver.close()
                    print('你的bug已经提交完毕了')

                else:
                    #判断上一个BUG的project_id是不是与现在提交的一样
                    if id == table.cell(i-1,0).value:
                        #判断需要提交多少个bug
                        if table.nrows-1 < 2:
                            #寻找bug
                            self.driver.find_element_by_xpath(f'//*[@id="issue-{id}"]/td[2]').click()
                            sleep(5)
                            #点击编辑按钮
                            self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
                            sleep(5)
                            #上传文件
                            self.upload = self.driver.find_element_by_xpath('//*[@id="new-attachments"]/span/span[2]/input')
                            self.upload.send_keys(file_path)
                            sleep(5)
                            self.driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
                            sleep(5)
                            print('编号：'+str(id)+'第1个文件上传成功')
                        # 判断需要提交多少个bug
                        elif table.nrows-1 >= 2:
                                self.driver.get('https://redmineurl/projects/web_test/issues')
                                sleep(5)
                                self.driver.find_element_by_xpath(f'//*[@id="issue-{id}"]/td[2]').click()
                                sleep(5)
                                self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
                                sleep(5)
                                self.upload = self.driver.find_element_by_xpath('//*[@id="new-attachments"]/span/span[2]/input')
                                self.upload.send_keys(file_path)
                                sleep(5)
                                self.driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
                                sleep(5)
                                self.driver.get('https://redmineurl/projects/web_test/issues')
                                sleep(1)
                                print('编号：'+str(id)+'第' + str(i) + '个文件上传成功')
                        else:
                            print('编号：'+str(id)+'第' + str(i) + '个文件上传失败')
                            continue
                    else:
                        self.driver.get('https://redmineurl/projects/web_test/issues')
                        self.driver.find_element_by_xpath(f'//*[@id="issue-{id}"]/td[2]').click()
                        sleep(5)
                        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
                        sleep(5)
                        self.upload = self.driver.find_element_by_xpath('//*[@id="new-attachments"]/span/span[2]/input')
                        self.upload.send_keys(file_path)
                        sleep(1)
                        print('编号：' + str(id) + '第' + str(i) + '个文件上传成功')
                        if table.nrows - i < 2:
                            sleep(5)
                            self.upload = self.driver.find_element_by_xpath('//*[@id="new-attachments"]/span/span[2]/input')
                            self.upload.send_keys(file_path)
                            sleep(5)
                            self.driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
                            sleep(5)
                            print('编号：'+str(id)+'第1个文件上传成功')

                        elif table.nrows - i >= 2:
                            self.driver.get('https://redmineurl/projects/web_test/issues')
                            sleep(5)
                            self.driver.find_element_by_xpath(f'//*[@id="issue-{id}"]/td[2]').click()
                            sleep(5)
                            self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
                            sleep(5)
                            self.upload = self.driver.find_element_by_xpath('//*[@id="new-attachments"]/span/span[2]/input')
                            self.upload.send_keys(file_path)
                            sleep(5)
                            self.driver.find_element_by_xpath('//*[@id="issue-form"]/input[6]').click()
                            sleep(5)
                            self.driver.get('https://redmineurl/projects/web_test/issues')
                            sleep(1)
                            print('编号：'+str(id)+'第' + str(i) + '个文件上传成功')
                        else:
                            print('编号：'+str(id)+'第' + str(i) + '个文件上传失败')
                            continue
            else:
                break



start1 = Upload_Img()
start1.get_html('user','pwd')
start1.get_project_id()
