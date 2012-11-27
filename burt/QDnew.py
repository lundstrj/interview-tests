# -*- coding: utf-8 -*-
#!/usr/bin/python
# 
# By: Johan Lundström 20/4/2011
# e-mail: lundstrom.se@gmail.com
# 
# Give it a a list of tuples like this: [(a,b),(a,c),(f,c)]
# and it will generate a "tree like" dictionary that looks like this:
#       a  f
#      / \/
#     b  c
# or: {'a': {'c': {}, 'b': {}}, 'f': {'c': {}}}

import sys

class QDtree(object):
  tree = {}
  tuples_base = [('a', 'b'), ('a', 'c'), ('f', 'c'), ('c', 'd')]
  tuples_visited = []
  tuples_left = [('a', 'b'), ('a', 'c'), ('f', 'c'), ('c', 'd')]  
  
  def main(self, tuples):
    for tuple in self.tuples_left:
      self.make_tree(self.tree, tuple[0], new_root=True)
      print 'visited', self.tuples_visited
    print self.tree
  
  def make_tree(self, tree, root, new_root=False):
    print '0', tree
    children_of_root = self.get_children(root)
    print 'root', root
    print 'children', children_of_root
    for child in children_of_root:
      self.fake_tree_search(self.tree, root, child, add=True, new_root=new_root)
      if new_root: self.tuples_visited.append((root, child))
      new_root = False
      print '1',tree
      if tree.has_key(root): print '2',tree[root]
      
    res = self.fake_tree_search(tree, root, None, add=False)
    if res:
      for child in res:
        print '6 root', root
        print '6 child', child
        self.tuples_visited.append((root, child))
        self.make_tree(tree, child)
    else:
      print '5 root', root
      print '5 tree', tree
      raw_input("have a look")
      for tuple in self.tuples_visited:
        if tuple in self.tuples_left: self.tuples_left.remove(tuple)
        
  def fake_tree_search(self, tree, node, child, add=True, new_root=False):
    if tree=={} or new_root: 
      if add: 
        tree[node]={child:{}}
        return
    #tree = self.tree
    keys = tree.keys()
    for key in keys:
      res = self.fake_tree_search_subtree(tree[key], node, child, add=add, new_root=new_root)
      if res:
        return res
    return
      
  def fake_tree_search_subtree(self, tree, node, child, add=True, new_root=False):
    if tree=={} or new_root: 
      if add: 
        tree[node]={child:{}}
        return
    if tree == {}: # Todo: make this work
      pass
      #tree = self.tree
    keys = tree.keys()
    print 'keytree', tree
    print 'keys', keys
    for key in keys:
      if key == node:
        if add: 
          tree[node][child]={}
          print 'after', tree
          return
        return tree[node]
      return self.fake_tree_search(tree[key], node, child, add=add)
  
  def get_children(self, node):
    ret = []
    for tuple in self.tuples_base: 
      if node == tuple[0]: ret.append(tuple[1])
    return ret
      

if __name__ == "__main__":
  t = QDtree()
  #t.main([['a', 'b'], ['a', 'c'], ['f', 'c'], ['c', 'd']])
  #t.main([['a', 'b'], ['f', 'c'], ['a', 'c'], ['c', 'd']])
  #t.main([['c', 'd'], ['f', 'c'], ['a', 'c'], ['a', 'b']])
  #t.main([['f', 'c'], ['c', 'd'], ['a', 'c'], ['a', 'b']])
  t.main([['f', 'c'], ['c', 'd'], ['a', 'c'], ['a', 'b']])
  #t.main([['x', 't'], ['a', 'c'], ['t', 'c'], ['t', 'd'], ['q', 'd'], ['c', 'z'], ['c', 'o']])

