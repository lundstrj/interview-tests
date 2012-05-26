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
 
  def main(self, base_tree, tuples):
    self.tree = base_tree
    for tuple in tuples:
      self.make_tree(self.tree, tuple)
    print self.tree
  
  def make_tree(self, tree, tuple):
    parent = tuple[0] 
    child = tuple[1]
    if tree == {}:                            # Base case
      self.tree[parent]={child:{}}
      return tree
    elif tree.has_key(child):                 # add parent Up one level here!
      self.tree[parent] = {child:tree[child]}
      if self.tree.has_key(child): del self.tree[child] # Ugly hack
      return tree
    elif tree.has_key(parent):                # Hit!
      tree[parent][child]={}
      return tree
    else: 
      for key in tree.keys(): 
        self.make_tree(tree[key], tuple)

if __name__ == "__main__":
  t = QDtree()
  t.main({}, [['a', 'b'], ['a', 'c'], ['f', 'c'], ['c', 'd']])
  t.main({}, [['a', 'b'], ['f', 'c'], ['a', 'c'], ['c', 'd']])
  t.main({}, [['c', 'd'], ['f', 'c'], ['a', 'c'], ['a', 'b']])
  t.main({}, [['f', 'c'], ['c', 'd'], ['a', 'c'], ['a', 'b']])
  t.main({}, [['x', 't'], ['a', 'c'], ['t', 'c'], ['t', 'd'], ['q', 'd'], ['c', 'z'], ['c', 'o']])

