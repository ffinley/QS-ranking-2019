import requests
import json
import xlwt

# 从network的xhr文件中发现json文件的url
url='https://www.topuniversities.com/sites/default/files/qs-rankings-data/397863.txt?_=1548401405177'

# 将字典数据转换为数组
def parser_page(json):
    if json:
        items = json.get('data')
        for i in range(len(items)):
            item = items[i]
            QSrank = {}
            if "=" in item['rank_display']:
                rk_str = str(item['rank_display']).split('=')[-1]
                QSrank['rank_display'] = rk_str
            else:
                QSrank['rank_display'] = item['rank_display']
            QSrank['title'] = item['title']
            QSrank['region'] = item['region']
            QSrank['score'] = item['score']
            yield QSrank

def main():
    cont = requests.get(url)
    json = cont.json()   # json数据类型为dict

    results = parser_page(json)

    # 创建excel表
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet')

    # 写入表头
    headings = ['Rank','Title','Region','Score']
    m = 0
    for heading in headings:
        worksheet.write(0,m, heading)
        m = m+1


    # 写入内容
    i = 1
    for result in results:
        m = 0
        for item in result:
            worksheet.write(i,m,result[item])  # 取值而非键
            m = m+1
        i = i+1

    # 在后面填写保存路径
    workbook.save(r'C:\Users\xxx\Desktop\QSrank.xls')

    #导出txt文档
    # for result in results:
    #     with open(r'C:\Users\徐智勇\Desktop\QSrank.txt', 'a', encoding='utf-8') as f:
    #         f.write('{:10}{:50}{:^88}{:>}\n'.format(result['rank_display'], result['title'], result['region'],
    #                                                 result['score']))
    #         f.close()

main()