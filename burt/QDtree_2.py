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
  true_roots = []
  
  def main(self, tuples):
    
    self.tuples_left = tuples
    self.tuples_base = tuples
    self.true_root_list()
    for tuple in self.tuples_left:
      self.make_tree(self.tree, tuple[0], new_root=True)
      print 'tuples left', self.tuples_left
      print 'visited visited', self.tuples_visited
    all_roots = self.tree.keys()
    print "truth!",self.true_roots
    for root in all_roots:
      if root not in self.true_roots:
        del self.tree[root]
    print self.tree
  
  def make_tree(self, tree, root, new_root=False):
    print 'tree 1:', self.tree
    print 'root 1:', root
    print 'newr 1:', new_root
    
    if self.tree == {} or (new_root and not self.root_in_tree(root)):
      print "adding new root:", root
      self.tree[root] = {} # Base case
    if tree.has_key(root): pass
      
    children = self.get_children(root)
    for child in children:
      print "adding   ", root, child
      print "self.tree", self.tree
      print "tree     ", tree
      if new_root and self.root_in_tree(root):
        print 'Adding to visited 1:', (root,child)
        self.tuples_visited.append((root,child))
      else:
        tree[root][child]={}
        print 'Adding to visited 2:', (root,child)
        self.tuples_visited.append((root,child))
        #self.make_tree(tree[root][child], child, new_root=False)
        self.make_tree(tree[root], child, new_root=False)
    for tuple in self.tuples_visited:
        if tuple in self.tuples_left: 
          print "removing", tuple
          self.tuples_left.remove(tuple)
  
  def root_in_tree(self, root):
    for tuple in self.tuples_visited:
      #if tuple[0] == root or tuple[1] == root:
      if tuple[1] == root:
        return True
    return False
    
  def true_root_list(self):
    for tuple in self.tuples_base:
      found = False
      root = tuple[0]
      for tuple_2 in self.tuples_base:
        if tuple_2[1] == root:
          print "rootbreak", root
          found = True
          break
      if not found:  self.true_roots.append(root)
        
  
  def fake_tree_search(self):
    pass
  def fake_tree_search_subtree(self):
    pass
  
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
  t.main([['f', 'c'], ['c', 'd'], ['a', 'c'], ['a', 'b'], ['x', 'a']])
  #t.main([['x', 't'], ['a', 'c'], ['t', 'c'], ['t', 'd'], ['q', 'd'], ['c', 'z'], ['c', 'o']])

