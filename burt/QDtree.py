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
  debug = False
  intact = False
  test_data = [[['a', 'b'], ['a', 'c'], ['f', 'c'], ['c', 'd']], 
               [['a', 'b'], ['f', 'c'], ['a', 'c'], ['c', 'd']],
               [['c', 'd'], ['f', 'c'], ['a', 'c'], ['a', 'b']],
               [['f', 'c'], ['c', 'd'], ['a', 'c'], ['a', 'b']]]
  test_data = [[['x', 't'], ['a', 'c'], ['t', 'c'], ['t', 'd'], ['q', 'd'], ['c', 'z'], ['c', 'o']],
               [['a', 'c'], ['x', 't'], ['t', 'c'], ['t', 'd'], ['q', 'd'], ['c', 'z'], ['c', 'o']]]
  test_res = {'a': {'b': {}, 'c': {'d': {}}}, 'f': {'c': {'d': {}}}}
  test_res = {'a': {'c': {'z': {}}}, 'x': {'t': {'c': {'z': {}}}}, 'c': {'z': {}, 'o': {}}, 'q': {'d': {}}, 't': {'c': {'z': {}}, 'd': {}}}
  tree = {}
  
  def test(self):
    if self.debug: print "Starting test"
    for test_data_set in self.test_data:
      self.tree = {}
      for test_dt in test_data_set:
        if self.debug: print "before", self.tree
        self.make_tree(self.tree, test_dt)
        if self.debug: print "after ", self.tree
      result = self.test_res == self.tree
      print "Input data:%s\nfinal:   %s\nexpected:%s\nSelf test OK:%s" % (
            test_data_set, self.tree, self.test_res,result)
    return result
  
  def main(self, base_tree, tuples):
    self.tree = base_tree
    if self.debug: print "Starting main"
    for tuple in tuples:
      self.make_tree(self.tree, tuple)
    print 'result:',self.tree
    if self.debug: print "Terminating main"
  
  def make_tree(self, tree, tuple):
    parent = tuple[0] 
    child = tuple[1]
    if tree == {}:                      # Base case
      self.tree[parent]={child:{}}
      if self.debug: print "l1",tree
      if self.intact: raw_input('leaf 1\n')
      return tree
    elif tree.has_key(parent):          # Hit!
      tree[parent][child]={}
      if self.intact: raw_input('hit  2\n')
      return tree
    elif tree.has_key(child):           # add parent Up one level here!
      if self.debug: print "child",child
      if self.debug: print "parent",parent
      if self.debug: print "b1",tree,'||', self.tree
      tree[parent] = {}
      tree[parent][child] = tree[child]
      #self.tree[parent] = {child:tree[child]}# ERROR!
      
      if self.debug: print "b2",tree,'||', self.tree
      if tree[parent].has_key(child): del tree[child] # Ugly hack
      if self.debug: print "b3",tree ,'||', self.tree
      if self.intact: raw_input('parent\n')
      return tree

    else:
      if self.intact: raw_input('loop 1\n')
      for key in tree.keys():
        if self.debug: print "looking in", tree[key], "for", tuple
        self.make_tree(tree[key], tuple)
  
if __name__ == "__main__":
  arg = sys.argv
  if "-h" in arg or "-help" in arg:
    print "Usage: \n -v (verbose)\n -b <base_tree>\n -t <tuples>\n -h (help)"\
          " -T (self test mode)\n -i (interactive mode)\n\n"\
          "For instance:\n> python QDTree.py -t [('a', 'b'), ('a', 'c'), "\
          "('f', 'c'), ('c', 'd')]"
  else:  
    base_tree = {}
    if "-b" in arg: 
      base_tree = arg[arg.index("-b")+1]
      base_tree = eval(base_tree)
    tuples = []
    if "-t" in arg: 
      tuples = arg[arg.index("-t")+1]
      tuples = eval(tuples)
    t = QDtree()
    t.debug = "-v" in arg
    t.intact = "-i" in arg
    if "-T" in arg: t.test()
    else: t.main(base_tree, tuples)
