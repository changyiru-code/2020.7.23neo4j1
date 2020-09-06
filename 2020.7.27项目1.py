import csv
from py2neo import Graph,Node,Relationship,NodeMatcher
graph = Graph("http://localhost:7474", username="neo4j", password='19980529')
#csv 读取
csv_file1=csv.reader(open('D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\作者.csv','r',encoding='utf-8'))
print(csv_file1)  #打印出来的csv_file1只是一个对象的模型
csv_file2=csv.reader(open('D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\关键词.csv','r',encoding='utf-8'))
print(csv_file2)  #打印出来的csv_file2只是一个对象的模型
csv_file3=csv.reader(open('D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\Bug.csv','r',encoding='utf-8'))
print(csv_file3)  #打印出来的csv_file3只是一个对象的模型

#查询节点题目是否存在
def MatchNode1(m_graph,m_label,m_attrs):
    m_n = "_.Title_name=" + "\'" + m_attrs['Title_name'] + "\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    return re_value
#查询节点作者是否存在
def MatchNode2(m_graph,m_label,m_attrs):
    m_n = "_.Author_name=" + "\'" + m_attrs['Author_name'] + "\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    return re_value

#查询节点学校是否存在
def MatchNode3(m_graph,m_label,m_attrs):
    m_n = "_.Institute_name=" + "\'" + m_attrs['Institute_name'] + "\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    return re_value


#读取第一个文件
csv_list1=list(csv_file1)
for i in range(1,len(csv_list1)): #len(csv_list)
    if len(csv_list1[i]) != 0:
        print(csv_list1[i])
        Title = Node('题目', Title_name=csv_list1[i][0])
        Author = Node('作者', Author_name=csv_list1[i][1])
        Institute = Node('学校', Institute_name=csv_list1[i][2])
        # 创建题目实体节点
        reValue1=MatchNode1(graph,'题目',{"Title_name":csv_list1[i][0]})
        if reValue1 is None:
            # 在数据库中创建节点
            graph.create(Title)
        # 创建作者实体节点
        reValue2=MatchNode2(graph,'作者',{"Author_name":csv_list1[i][1]})
        if reValue2 is None:
            # 在数据库中创建节点
            graph.create(Author)
        # 创建学校实体节点
        reValue3=MatchNode3(graph,'学校',{"Institute_name":csv_list1[i][2]})
        if reValue3 is None:
            # 在数据库中创建节点
            graph.create(Institute)
        # 创建实体关系类型节点
        r1 = Relationship(Title, 'author_of', Author)
        r2 = Relationship(Author, 'institute_of', Institute)
        # 在图形数据库中创建实体和关系
        graph.create(r1)
        graph.create(r2)

# #读取第二个文件
# csv_list2=list(csv_file2)
# for i in range(1,len(csv_list2)): #len(csv_list)
#     if len(csv_list2[i]) != 0:
#         print(csv_list2[i])
#         # 创建题目实体节点
#         # Title = Node('题目', Title_name=csv_list2[i][0])
# #读取第三个文件
# csv_list3=list(csv_file3)
# for i in range(1,len(csv_list3)): #len(csv_list)
#     if len(csv_list3[i]) != 0:
#         print(csv_list3[i])
#         # 创建题目实体节点
#         # Title = Node('题目', Title_name=csv_list3[i][0])
