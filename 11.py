# #1、重新读取数据库cnki，将作者字段里的\xa0 不间断空白符去掉，重新存入数据库cnki_qikan
# import pymysql
# def insert_db(data):
#     db = pymysql.connect(host='localhost', user='root', passwd='19980529', db='joke', charset='utf8')  # db为所使用的数据库
#     cusor = db.cursor()     # (发布者,正文,点赞数,转发数,评论数,发布时间)
#     # sql1='create table cnki_qikan(id int primary key auto_increment,url varchar(200),title varchar(200),author varchar(200),abstract text,keywords varchar(200),source varchar(200),leixing varchar(200),publishTime varchar(200),shumu int)'
#     sql2 = """INSERT INTO cnki_qikan(url,title,author,abstract,keywords,source,leixing,publishTime,shumu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#     try:
#         # cusor.execute(sql1)
#         cusor.execute(sql2, data)  # sql执行
#         db.commit()  # 提交到数据库
#     except Exception as e:  # 获取报错信息
#         print(e)
#     db.close()
#
# def main():
#     db = pymysql.connect(host='localhost', user='root', passwd='19980529', db='joke', charset='utf8')
#     cusor = db.cursor()
#     # 1读取全部字段
#     sql = """select * from cnki"""
#     cusor.execute(sql)
#     # 获取所有结果
#     results = cusor.fetchall()
#     result = list(results)
#
#     result1=[]
#     for i in result:
#         result_dict = []
#
#         result_dict.append(i[1])
#         result_dict.append(i[2])
#
#         if len(i[3])==0 or len(i[3])==1:
#             result_dict.append(0)
#         else:
#             l1=[]
#             for n in i[3].split(' ')[::2]:  # 将作者字段里的\xa0 不间断空白符去掉
#                 out = "".join(n.split())
#                 l1.append(out)
#             result_dict.append(' '.join(l1))
#
#         result_dict.append(i[4])
#         result_dict.append(i[5])
#         result_dict.append(i[6])
#         result_dict.append(i[7])
#         result_dict.append(i[8])
#         result_dict.append(i[9])
#         result1.append(result_dict)
#     # print(result1)
#     for i in result1:
#         insert_db(i)
#     # insert_db()
#
# main()


#2、重新读取数据库cnki_paper，将作者字段里的\xa0 不间断空白符去掉，重新存入数据库cnki_paper1
import pymysql
def insert_db(data):
    db = pymysql.connect(host='localhost', user='root', passwd='19980529', db='joke', charset='utf8')  # db为所使用的数据库
    cusor = db.cursor()     # (发布者,正文,点赞数,转发数,评论数,发布时间)
    # sql1='create table cnki_paper1(id int primary key auto_increment,url varchar(200),title varchar(200),author varchar(200),abstract text,keywords varchar(200),source varchar(200),leixing varchar(200),publishTime varchar(200),shumu int)'
    sql2 = """INSERT INTO cnki_paper1(url,title,author,abstract,keywords,source,leixing,publishTime,shumu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        # cusor.execute(sql1)
        cusor.execute(sql2, data)  # sql执行
        db.commit()  # 提交到数据库
    except Exception as e:  # 获取报错信息
        print(e)
    db.close()

def main():
    db = pymysql.connect(host='localhost', user='root', passwd='19980529', db='joke', charset='utf8')
    cusor = db.cursor()
    # 1读取全部字段
    sql = """select * from cnki_paper"""
    cusor.execute(sql)
    # 获取所有结果
    results = cusor.fetchall()
    result = list(results)

    result1=[]
    for i in result:
        result_dict = []

        result_dict.append(i[1])
        result_dict.append(i[2])

        if len(i[3])==0 or len(i[3])==1:
            result_dict.append(0)
        else:
            l1=[]
            for n in i[3].split(' ')[::2]:  # 将作者字段里的\xa0 不间断空白符去掉
                out = "".join(n.split())
                l1.append(out)
            result_dict.append(' '.join(l1))

        result_dict.append(i[4])
        result_dict.append(i[5])
        result_dict.append(i[6])
        result_dict.append(i[7])
        result_dict.append(i[8])
        result_dict.append(i[9])
        result1.append(result_dict)
    # print(result1)
    for i in result1:
        insert_db(i)
    # insert_db()

main()
