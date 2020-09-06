import csv
from py2neo import Graph, Node, Relationship
graph = Graph("http://localhost:7474", username="neo4j", password='19980529')
#csv 读取
csv_file=csv.reader(open('D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\yanzheng.csv','r',encoding='utf-8'))
print(csv_file)  #打印出来的csv_file只是一个对象的模型
# for line in csv_file:
#     if len(line)!=0:  #如果列表为空，则不能用列表索引，否则会出错，所以需要去掉空列表，方法是：判断列表的长度，若长度为0，则去掉，否则不去掉。
#
#         # continue
#         print(line) #遍历打印，得到模型的数据

#去掉第一行的代码
csv_list=list(csv_file)
for i in range(1,len(csv_list)): #len(csv_list)
    if len(csv_list[i]) != 0:
        print(csv_list[i])
        # 创建题目实体节点
        Title = Node('题目', Title_name=csv_list[i][0])
        # 创建作者实体节点
        Author = Node('作者', Author_name=csv_list[i][1])
        # 创建关键词实体节点
        Keywords = Node('关键词', Keywords_name=csv_list[i][2])
        # 创建学校实体节点
        Institute = Node('学校', Institute_name=csv_list[i][3])
        # 创建摘要实体节点
        # Abstract = Node('摘要', Abstract_content=csv_list[i][4])
        # 创建实体关系类型节点
        r1 = Relationship(Title, '题目的作者', Author)
        r2 = Relationship(Title, '题目的关键词', Keywords)
        r3 = Relationship(Author, '作者学校', Institute)
        # r4 = Relationship(Title, '题目的摘要', Abstract)
        # 在图形数据库中创建实体和关系
        graph.create(Title)
        graph.create(Author)
        graph.create(Keywords)
        graph.create(Institute)
        # graph.create(Abstract)
        graph.merge(r1)
        graph.merge(r2)
        graph.merge(r3)
        # graph.merge(r4)


# #csv 写入
# stu1 = ['marry',26]
# stu2 = ['bob',23]
# #打开文件，追加a
# out = open('Stu_csv.csv','a', newline='')
# #设定写入模式
# csv_write = csv.writer(out,dialect='excel')
# #写入具体内容
# csv_write.writerow(stu1)
# csv_write.writerow(stu2)
# print ("write over")
# #如果从excel读取数据，存到csv文件，则设一个循环，读一条数据，存一次


