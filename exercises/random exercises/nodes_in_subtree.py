from collections import defaultdict

class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

def dfs(root, s, countMap):
  charCountMap = defaultdict(int)
  charCountMap[s[root.val-1]] = 1
  
  for child in root.children:
    d = dfs(child, s, countMap)
    for key, val in d.items():
      charCountMap[key] += val
      
  countMap[root.val] = charCountMap
  return charCountMap

def count_of_nodes(root, queries, s):
  res = []
  cntMap = defaultdict(int)
  dfs(root, s, cntMap)
  print(cntMap)
  for start_idx, query_val in queries:
    res.append(cntMap[start_idx][query_val])
  return res

n_2 ,q_2 = 7, 3 
s_2 = "abaacab"
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [(1, 'a'),(2, 'b'),(3, 'a')]
output_2 = count_of_nodes(root_2, queries_2, s_2)