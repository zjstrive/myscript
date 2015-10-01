'''
Created on Sep 6, 2015

@author: jie
'''
import requests
import sys

WEB_URL = 'http://www.csdn.net/'


def run():
    try:
        page = requests.get(WEB_URL)
        if page.status_code == 200 and page.content.decode("utf-8").find('<title>CSDN.NET - 全球最大中文IT社区，为IT专业技术人员提供最全面的信息传播和服务平台</title>') >= 0:
            print("CSDN is working great :)")
        else:
            print("It looks like CSDN is having trouble, some one please take a look at it")
            sys.exit(-1)
    except:
        print("It looks like CSDN is having trouble, some one please take a look at it")
        sys.exit(-1)


if __name__ == '__main__':
    run()
