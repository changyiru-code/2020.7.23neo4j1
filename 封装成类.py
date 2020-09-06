#该代码正确，可以合并节点
import csv
from py2neo import Graph,Node,Relationship
class keshi(object):
    def __init__(self):
        pass
    def duqu(self):
        graph = Graph("http://localhost:7474", username="neo4j", password='19980529')

        # csv 读取
        csv_file1 = csv.reader(open(
            'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\作者.csv',
            'r', encoding='utf-8'))
        print(csv_file1)  # 打印出来的csv_file1只是一个对象的模型
        csv_file2 = csv.reader(open(
            'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\关键词.csv',
            'r', encoding='utf-8'))
        print(csv_file2)  # 打印出来的csv_file2只是一个对象的模型
        csv_file3 = csv.reader(open(
            'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\Bug.csv',
            'r', encoding='utf-8'))
        print(csv_file3)  # 打印出来的csv_file3只是一个对象的模型
        csv_file4 = csv.reader(open(
            'D:\\常艺茹的文档\\研究生期间的资料\\知识图谱\\Vulnerability-Knowledge-Graph-master\\Vulnerability-Knowledge-Graph-master\\漏洞demo\\output.csv',
            'r', encoding='utf-8'))
        print(csv_file4)  # 打印出来的csv_file1只是一个对象的模型
        return csv_file1, graph, csv_file2, csv_file3, csv_file4
class Create(object):
    def __init__(self, csv_file1, graph, csv_file2, csv_file3, csv_file4):
        self.csv_file1 = csv_file1
        self.graph = graph
        self.csv_file2 = csv_file2
        self.csv_file3 = csv_file3
        self.csv_file4 = csv_file4
    # 读取第一个文件
    def file1(self):
        csv_list1 = list(self.csv_file1)
        for i in range(1, len(csv_list1)):  # len(csv_list)
            if len(csv_list1[i]) != 0:
                print(csv_list1[i])
                # 创建题目实体节点
                Title = Node('title', Title_name=csv_list1[i][0])
                # 在数据库中创建节点
                self.graph.merge(Title, 'title', 'Title_name')
                # 创建作者实体节点
                Author = Node('author', Author_name=csv_list1[i][1])
                # 在数据库中创建节点
                self.graph.merge(Author, 'author', "Author_name")
                # 创建学校实体节点
                Institute = Node('institute', Institute_name=csv_list1[i][2])
                # 在数据库中创建节点
                self.graph.merge(Institute, 'institute', "Institute_name")
                # 创建实体关系类型节点
                author_of = Relationship.type("author_of")
                institute_of = Relationship.type("institute_of")
                # 在图形数据库中创建实体和关系
                self.graph.merge(author_of(Title, Author), "title", "Title_name")
                self.graph.merge(institute_of(Author, Institute), "title", "Title_name")

    # 读取第二个文件
    def file2(self):
        csv_list2 = list(self.csv_file2)
        for i in range(1, len(csv_list2)):  # len(csv_list)
            if len(csv_list2[i]) != 0:
                print(csv_list2[i])
                # 题目实体节点已经存在，无需创建
                Title = Node('title', Title_name=csv_list2[i][0])
                # 创建关键词实体节点
                Keywords = Node('keywords', Keywords_name=csv_list2[i][1])
                # 在数据库中创建节点
                self.graph.merge(Keywords, 'keywords', "Keywords_name")
                # 创建实体关系类型节点
                keywords_of = Relationship.type("keywords_of")
                # 在图形数据库中创建实体和关系
                self.graph.merge(keywords_of(Title, Keywords), "title", "Title_name")

    # 读取第三个文件
    def file3(self):
        csv_list3 = list(self.csv_file3)
        for i in range(1, len(csv_list3)):  # len(csv_list)
            if len(csv_list3[i]) != 0:
                print(csv_list3[i])
                # 创建题目实体节点
                Title = Node('title', Title_name=csv_list3[i][0], Abstract_content=csv_list3[i][4])
                self.graph.merge(Title, 'title', 'Title_name')

    # 读取第四个文件
    def file4(self):
        csv_list4 = list(self.csv_file4)
        for i in range(1, len(csv_list4)):  # len(csv_list)
            if len(csv_list4[i]) != 0:
                print(csv_list4[i])
                # 创建实体1节点
                entity1 = Node('entity1', entity_1=csv_list4[i][0])
                # 在数据库中创建节点
                self.graph.merge(entity1, 'entity1', "entity_1")
                # 创建实体2节点
                entity2 = Node('entity2', entity_2=csv_list4[i][2])
                self.graph.merge(entity2, 'entity2', "entity_2")
                rel = Relationship.type(csv_list4[i][1])
                # 在图形数据库中创建实体和关系
                self.graph.merge(rel(entity1, entity2), "entity1", "entity_1")
    def yunxing(self):
        gql1 = 'MATCH (a:entity1),(b:entity2)  where (a.entity_1 = b.entity_2 and id(a) <> id(b))  call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node;'
        gql2 = 'MATCH (a:entity1),(b:title)  where (a.entity_1 = b.Title_name and id(a) <> id(b)) call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node'
        gql3 = 'MATCH (a:entity1),(b:keywords)  where (a.entity_1 = b.Keywords_name and id(a) <> id(b))  call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node;'
        gql4 = 'MATCH (a:entity2),(b:title)  where (a.entity_2 = b.Title_name and id(a) <> id(b)) call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node'
        gql5 = 'MATCH (a:entity2),(b:keywords)  where (a.entity_2 = b.Keywords_name and id(a) <> id(b)) call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node'
        gql6 = 'MATCH (a:title),(b:keywords)  where (a.Title_name = b.Keywords_name and id(a) <> id(b)) call apoc.refactor.mergeNodes([a,b]) YIELD node  RETURN node'
        self.graph.run(gql1)
        self.graph.run(gql2)
        self.graph.run(gql3)
        self.graph.run(gql4)
        self.graph.run(gql5)
        self.graph.run(gql6)

def main():
    y=keshi()
    csv_file1, graph, csv_file2, csv_file3, csv_file4=y.duqu()
    x=Create(csv_file1, graph, csv_file2, csv_file3, csv_file4)
    x.file1()
    x.file2()
    x.file3()
    x.file4()
    x.yunxing()


main()
