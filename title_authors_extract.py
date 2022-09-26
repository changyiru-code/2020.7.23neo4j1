"""
file_name:title_authors_extract.py

说明：title_authors_extract.py是提取数据库joke库cnki_qikan表里的
里面的title author信息，存在csv文件里

"""

import pymysql
import csv


def connect():
    db = pymysql.connect(host='localhost', user='root', passwd='19980529', db='joke', charset='utf8')
    cusor = db.cursor()
    # 1读取全部字段
    sql = """select * from cnki_qikan"""
    cusor.execute(sql)
    # 获取所有结果
    results = cusor.fetchall()
    result = list(results)
    return result


def main():
    output_route = 'output\\'

    result = connect()

    header = ['title', 'authors']  # 数据列名
    list1 = []
    for i in result:
        authors = i[3].split(' ')
        for author in authors:
            dict1 = {}
            dict1['title'] = i[2]
            dict1['authors'] = author
            list1.append(dict1)
    print(list1)
    with open(output_route + "title_authors.csv", 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        writer.writeheader()  # 写入列名
        writer.writerows(list1)  # 写入数据

        # result_dict = []
        #
        # result_dict.append(i[2])
        # result_dict.append(i[3])
        # result_dict.append(i[4])
        # result_dict.append(i[5])
        # result_dict.append(i[6])
        # result_dict.append(i[8])
        # result1.append(result_dict)

main()


