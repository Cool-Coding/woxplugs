# encoding=utf8
import requests
from bs4 import BeautifulSoup
from wox import Wox


# 用户写的Python类必须继承Wox类 https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
# 这里的Wox基类做了一些工作，简化了与Wox通信的步骤。
class Main(Wox):

    def request(self, url):
        heads = {}
        heads['User-Agent'] = 'Mozilla/5.0 ' \
                      '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                      '(KHTML, like Gecko) Version/5.1 Safari/534.50'
        return requests.get(url,headers = heads)

    # 必须有一个query方法，用户执行查询的时候会自动调用query方法
    def query(self, key):
        url = 'http://www.iciba.com/'+key
        r = self.request(url)
        bs = BeautifulSoup(r.text,features="html.parser")

        results = []
        for i in bs.select("ul .clearfix"):
            text = i.text.replace('\n', '')
            subtext = ''
            if len(text) > 50:
                subtext = text[50:]
                text = text[0:50]

            results.append({
              "Title": text,
              "SubTitle": subtext,
              "IcoPath": "Images/app.ico"
            })
        f = open("E:/out.txt",'w')
        for i in results:
            f.write(i.get("Title"))
            
        return results


# 以下代码是必须的
if __name__ == "__main__":
    Main()