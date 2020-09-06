#修改zhr的读取output.csv文件的代码
#1、所有实体节点都放一个标签下面
import csv
from py2neo import Graph,Node,Relationship

#读取第一个文件
def file1(csv_file1,graph):
    csv_list1 = list(csv_file1)
    for i in range(1, len(csv_list1)):  # len(csv_list)
        if len(csv_list1[i]) != 0:
            print(csv_list1[i])
            # 创建实体1节点
            entity1 = Node('entity1', entity_1=csv_list1[i][0])
            # 在数据库中创建节点
            graph.merge(entity1, 'entity1', 'entity_1')
            # 创建实体2节点
            entity2 = Node('entity1', entity_1=csv_list1[i][2])
            # 在数据库中创建节点
            graph.merge(entity2, 'entity1', "entity_1")
            # 创建实体关系类型节点
            rel = Relationship.type(csv_list1[i][1])
            # 在图形数据库中创建实体和关系
            graph.merge(rel(entity1, entity2),"entity1", "entity_1")

def main():
    graph = Graph("http://localhost:7474", username="neo4j", password='19980529')
    # csv 读取
    csv_file1 = csv.reader(open(
        'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\output1.csv',
        'r', encoding='utf-8'))
    print(csv_file1)  # 打印出来的csv_file1只是一个对象的模型
    file1(csv_file1, graph)
main()

# #2.1一个实体的全部标签建完后，再建另一个实体的标签，同时创建实体间的关系
# import csv
# from py2neo import Graph,Node,Relationship,NodeMatcher
# def MatchNode1(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_1": csv_list1[i][0]}
#     m_n = "_.entity_1=" + "\'" + m_attrs['entity_1'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
# #查询节点作者是否存在
# def MatchNode2(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_2": csv_list1[i][2]}
#     m_n = "_.entity_1=" + "\'" + m_attrs['entity_2'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
# def MatchNode3(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_1": csv_list1[i][0]}
#     m_n = "_.entity_2=" + "\'" + m_attrs['entity_2'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
#
# #读取第一个文件
# def file1(csv_file1,graph):
#     csv_list1 = list(csv_file1)
#     for i in range(1, len(csv_list1)):  # len(csv_list)
#         if len(csv_list1[i]) != 0:
#             print(csv_list1[i])
#             # 创建实体1节点
#             entity1 = Node('entity1', entity_1=csv_list1[i][0])
#             # 在数据库中创建节点
#             reValue1 = MatchNode1(graph, 'entity1', {"entity_1": csv_list1[i][0]})
#             print(reValue1)
#             if reValue1 is None:
#                 # 在数据库中创建节点
#                 graph.merge(entity1, 'entity1', "entity_1")
#     for i in range(1, len(csv_list1)):  # len(csv_list)
#         if len(csv_list1[i]) != 0:
#             print(csv_list1[i])
#             # 创建实体2节点
#             entity2 = Node('entity2', entity_2=csv_list1[i][2])
#             reValue2 = MatchNode2(graph, 'entity1', {"entity_2": csv_list1[i][2]})
#             print(reValue2)
#             entity1 = Node('entity1', entity_1=csv_list1[i][0])
#             if reValue2 is None:
#                 reValue3 = MatchNode3(graph, 'entity2', {"entity_2": csv_list1[i][2]})
#                 print(reValue3)
#                 if reValue3 is None:
#                     # 在数据库中创建节点
#                     graph.merge(entity2, 'entity2', "entity_2")
#                     reValue2 = entity2
#                 else:
#                     reValue2 = reValue3
#             rel = Relationship.type(csv_list1[i][1])
#             # 在图形数据库中创建实体和关系
#             graph.merge(rel(entity1, reValue2),"entity1", "entity_1")
#
#
# def main():
#     graph = Graph("http://localhost:7474", username="neo4j", password='19980529')
#     # csv 读取
#     csv_file1 = csv.reader(open(
#         'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\output1.csv',
#         'r', encoding='utf-8'))
#     print(csv_file1)  # 打印出来的csv_file1只是一个对象的模型
#     file1(csv_file1, graph)
# main()


# #2.2一个实体的全部标签建完后，再建另一个实体的标签，同时创建实体间的关系，
# #2.2与2.1效果一样
# import csv
# from py2neo import Graph,Node,Relationship,NodeMatcher
# def MatchNode1(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_1": csv_list1[i][0]}
#     m_n = "_.entity_1=" + "\'" + m_attrs['entity_1'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
# #查询节点作者是否存在
# def MatchNode2(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_2": csv_list1[i][2]}
#     m_n = "_.entity_1=" + "\'" + m_attrs['entity_2'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
# def MatchNode3(m_graph,m_label,m_attrs):#graph, 'entity1', {"entity_1": csv_list1[i][0]}
#     m_n = "_.entity_2=" + "\'" + m_attrs['entity_2'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
#
# #读取第一个文件
# def file1(csv_file1,graph):
#     csv_list1 = list(csv_file1)
#     for i in range(1, len(csv_list1)):  # len(csv_list)
#         if len(csv_list1[i]) != 0:
#             print(csv_list1[i])
#             # 创建实体1节点
#             entity1 = Node('entity1', entity_1=csv_list1[i][0])
#             # 在数据库中创建节点
#             reValue1 = MatchNode1(graph, 'entity1', {"entity_1": csv_list1[i][0]})
#             print(reValue1)
#             if reValue1 is None:
#                 # 在数据库中创建节点
#                 graph.merge(entity1, 'entity1', "entity_1")
#     for i in range(1, len(csv_list1)):  # len(csv_list)
#         if len(csv_list1[i]) != 0:
#             print(csv_list1[i])
#             # 创建实体2节点
#             entity2 = Node('entity2', entity_2=csv_list1[i][2])
#             reValue2 = MatchNode2(graph, 'entity1', {"entity_2": csv_list1[i][2]})
#             print(reValue2)
#             entity1 = Node('entity1', entity_1=csv_list1[i][0])
#             if reValue2 is None:
#                 # 在数据库中创建节点
#                 graph.merge(entity2, 'entity2', "entity_2")
#                 reValue2 = entity2
#             rel = Relationship.type(csv_list1[i][1])
#             # 在图形数据库中创建实体和关系
#             graph.merge(rel(entity1, reValue2),"entity1", "entity_1")
#
#
# def main():
#     graph = Graph("http://localhost:7474", username="neo4j", password='19980529')
#     # csv 读取
#     csv_file1 = csv.reader(open(
#         'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\output1.csv',
#         'r', encoding='utf-8'))
#     print(csv_file1)  # 打印出来的csv_file1只是一个对象的模型
#     file1(csv_file1, graph)
# main()
