from py2neo import Node,Relationship,Graph,NodeMatcher,RelationshipMatcher
#数据库
graph=Graph('http://localhost:7474/',username='neo4j',password='19980529')
#创建节点
def CreateNode(m_graph,m_label,m_attrs):
    m_n="_.name="+"\'"+m_attrs['name']+"\'"
    matcher=NodeMatcher(m_graph)
    re_value=matcher.match(m_label).where(m_n).first()
    #print(re_value)
    if re_value is None:
        m_node=Node(m_label,**m_attrs)
        #在数据库中创建节点
        n=m_graph.create(m_node)
        return n
    return None
label1='stock'
attrs1={"name":"招商银行","code":"600036"}
label2='securitiesExchange'
attrs2={"name":"上海证券交易所"}
CreateNode(graph,label1,attrs1)
CreateNode(graph,label2,attrs2)

# #查询节点是否存在的方法
# def MatchNode(m_graph,m_label,m_attrs):
#     m_n = "_.name=" + "\'" + m_attrs['name'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
#
# #创建两个节点的关系，如果节点不存在，不创建关系
# def CreateRelationship(m_graph,m_label1,m_attrs1,m_label2,m_attrs2,m_r_name):
#     reValue1=MatchNode(m_graph,m_label1,m_attrs1)
#     reValue2 = MatchNode(m_graph,m_label2,m_attrs2)
#     if reValue1 is None or reValue2 is None:
#         return False
#     m_r=Relationship(reValue1,m_r_name,reValue2)
#     n=graph.create(m_r)
#     return n
# label1='stock'
# attrs1={"name":"招商银行","code":"600036"}
# label2='securitiesExchange'
# attrs2={"name":"上海证券交易所"}
# m_r_name="证券交易所"
# CreateRelationship(graph,label1,attrs1,label2,attrs2,m_r_name)

# #查询节点，按照ID查询，没有则返回None
# def MatchNodeById(m_graph,m_id):
#     matcher = NodeMatcher(m_graph)
#     re_value=matcher.get(m_id)
#     return re_value
#
# #查询节点，按照name查询，没有则返回None
# def MatchNode(m_graph,m_label,m_attrs):
#     m_n = "_.name=" + "\'" + m_attrs['name'] + "\'"
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label).where(m_n).first()
#     return re_value
#
# #查询节点，按照标签查询标签下的所有节点，没有则返回None
# def MatchNodeByLabel(m_graph,m_label):
#     matcher = NodeMatcher(m_graph)
#     re_value = matcher.match(m_label)
#     return re_value



