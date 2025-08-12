
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

"""

class ability_tianyancha():
    """
    调用天眼查接口
    """
    ability_name = "天眼查"
    ability_description = """
        调用天眼查接口, 查询一个企业的基本信息, 包括企业名称, 企业地址, 企业注册资本, 企业成立时间, 企业法人, 企业联系方式等
        基本产品, 行业分类, 联系电话等
    """
    
    # 输入, 企业行业分类
    input = {
        "industry_classification": "行业分类"
    }
    
    # 输出 为一个list
    output = {
        "company_name": "企业名称",
        "company_address": "企业地址",
        "company_register_capital": "企业注册资本",
        "company_establishment_time": "企业成立时间",
        "company_legal_person": "企业法人",
        "company_contact": "企业联系方式"
    }
    
    def _do_sth(self):
        """
        调用天眼查, 批量根据行业分类, 获取企业信息
        """
        pass
    
class task_tianyancha: 
    '''
     专家 OR 大模型 确定需要使用 天眼查 能力, 来获取企业信息
    '''
    task_name = "天眼查"
    task_description = """
        专家 OR 大模型 确定需要使用 天眼查 能力, 来获取企业信息
    """
     
    # 输入, 企业行业分类
    input = {
       "industry_classification": "行业分类"
    }
     
    # 输出 为一个list
    output = {
        "company_name": "企业名称",
        "company_address": "企业地址",
        "company_register_capital": "企业注册资本",
    }
     
    def _logic(self):
        """
        始终天眼查能力, 来查行业客户, 并将结果存放在 output中
        task 就是纯干活, 结果说话, 没有所谓的action
        """
        pass
     
class task_tianyancha_sort:
    '''
    对天眼查结果进行排序 
    '''
    task_name = "天眼查排序"
    task_description = """
        对天眼查结果进行排序 
    """
    
    # 输入, 天眼查结果  
    input = {
        "tianyancha_result": "天眼查结果"
    }
    
    # 输出, 排序后的结果
    output = {
        "sorted_result": "排序后的结果"
    }
    
    def _logic(self):
        """
        对天眼查结果进行排序 
        """
        pass
    
class event_ai_clue: 
    '''
    线索挖掘事件
    事件和任务的区别: 
        事件: 是创值事件, 是创值事件的触发条件, 事件产生action
        任务: 是创值事件的执行者, 是创值事件的执行者, 任务产生结果, 是否产生action, 由上层事件来决定
    '''
    event_name = "线索挖掘"
    event_description = """
        1, 线索挖掘创值事件, 根据行业分类, 获取企业信息
        2, 对线索进行排序
    """
    
    status = "success"
    
    # data为专家需要在打造的时候, 输入的参数
    # input 为事件运行时, 输入的参数
    
    # 此处事件包含的参数
    # 1, 行业分类
    # 2, 排序方式
    # 3, 返回结果数量
    data = {
        "industry_classification": "行业分类",
        "sort_type": "排序方式",
        "return_num": "返回结果数量"
    }
    
    # 事件运行时, 输入的参数
    input = {
        "industry_classification": "行业分类"
    }
    
    
    def _logic(self):
        """
        查天眼查, 并进行排序
        """
        
        task_tianyancha = task_tianyancha()
        task_tianyancha.input = self.input
        task_tianyancha.logic()
        
        task_tianyancha_sort = task_tianyancha_sort()
        task_tianyancha_sort.input = task_tianyancha.output
        task_tianyancha_sort.logic()
        
        list_task = [task_tianyancha, task_tianyancha_sort]
        
        # 执行任务
        for task in list_task:
            task.logic()
            
        # 判断任务是否执行成功
        for task in list_task:
            if task.output is None:
                self.status = "failed"
                break
            
        self.status = "success"
    
    def _action(self):
        """
        事件产生action, 通知上层引擎. 
        """
        if self.status == "success":
            pass
        else:
            pass
    

class event_ai_touch:
    '''
    线索触达事件
    '''
    event_name = "线索触达"
    event_description = """
        线索触达事件, 根据线索, 进行触达
    """
    
# 创建一个简单的图
obj_event_ai_clue = event_ai_clue()
obj_event_ai_touch = event_ai_touch()

g = nx.Graph()
g.add_node(obj_event_ai_clue)
g.add_node(obj_event_ai_touch)

# add_edge由上层引擎来决定
g.add_edge(obj_event_ai_clue, obj_event_ai_touch)



# 这里假设连接到一个 Gremlin Server（需配置），或使用类似于 TinkerPop 的图结构

# placeholder for actual connection
# conn = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
# g = Graph().traversal().with_remote(conn)

# print nodes and edges
print("Nodes:", g.nodes())
print("Edges:", g.edges())

# 关闭连接
# conn.close()