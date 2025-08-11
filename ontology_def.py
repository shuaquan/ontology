
import networkx as nx
from gremlin_python.structure.graph import Graph
from gremlin_python.process.traversal import T, Cardinality
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

"""
定义: 
    task: 任务, 就是一个要具体干的活, 可以是人干, 也可以是AI干
    包含具体的: 
        data(数据结构定义): task自生包含的数据
        logic(逻辑定义, 即执行逻辑): task的执行逻辑
        input: 任务的输入, 可以是一组数据, 也可以是一个数据结构 
        output: 任务的输出, 可以是一组数据, 也可以是一个数据结构  
        action(动作定义) , 以及产生 output 后的 action(动作定义) 

构造场景, 内容包含: 
1, 两个创值阶段:  create_value_stage_1, create_value_stage_2 
2, 每个创值阶段, 两个供应能力:  supply_ability_1, supply_ability_2, supply_ability_3, supply_ability_4 
3, 每个供应能力, 两个创值事项:  create_value_item_1, create_value_item_2, create_value_item_3, create_value_item_4  
4, 每个创值事项, 两个任务:  task_1, task_2, task_3, task_4  
5, 每个任务, 包含具体的: 
    data(数据结构定义), 
    logic(逻辑定义, 即执行逻辑), 
    input, 
    output, 
    action(动作定义) , 以及产生 output 后的 action(动作定义) 
"""
# 创建一个简单的图
g = nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_edge(1, 2)

# 使用 Gremlin 来演示连接（假设一个架构）
# 这里假设连接到一个 Gremlin Server（需配置），或使用类似于 TinkerPop 的图结构

# placeholder for actual connection
# conn = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
# g = Graph().traversal().with_remote(conn)

# print nodes and edges
print("Nodes:", g.nodes())
print("Edges:", g.edges())

# 关闭连接
# conn.close()