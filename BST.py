'''非递归构建有序符号表
使用两个平行列表：键列表和值列表，位置对应：键列表中对应位置值列表中的值
'''
class Node(object):
    def __init__(self):
        self.key=None
        self.value=None
        self.lchild=None
        self.rchild=None
        self.N=None
class BST(object):
    def __init__(self):
        self.root=None
    #判断某个键是否存在于二叉树中
    def __contains__(self, key):
        return self._bstsearch(self.root,key) is not None
    def _bstsearch(self,sub_tree,key):
        if sub_tree is None:
            return None
        elif sub_tree.key > key:
            return self._bstsearch(sub_tree.lchild,key)
        elif sub_tree.key<key:
            return self._bstsearch(sub_tree.rchild,key)
        else:
            return sub_tree
    #非递归向树中插入结点
    def _putWithOutRecur(self,sub_tree,key,value):
        #判断是插入左子树-1还是右子树1
        left_or_right=0
        #判断根节点是否为空，非空情况下插入
        while sub_tree is not None:
            root=sub_tree
            if sub_tree.key==key:
                sub_tree.value=value
                return
            elif sub_tree.key<key:
                sub_tree=sub_tree.rchild
                left_or_right=1
            else :
                sub_tree=sub_tree.lchild
                left_or_right=-1
        if left_or_right==1:
            root.rchild=Node(key,value)
        else:
            root.lchild=Node(key,value)
        #统计结点数
        self._plusN(key)
    #结点计数
    def _plusN(self,key):
        sub_tree=self.root
        while sub_tree.key is not key:
            sub_tree.N+=1
            if sub_tree.key<key:
                sub_tree=sub_tree.rchild
            else:
                sub_tree=sub_tree.lchild
    #查询
    def get(self,sub_tree,key):
        return self._getOutRecur(sub_tree,key)
    def _getOutRecur(self,sub_tree,key):
        while sub_tree.key is not None:
            if sub_tree.key==key:
                return
            elif sub_tree.key<key:
                sub_tree=sub_tree.rchild
            else:
                sub_tree=sub_tree.lchild
        return None
    def size(self,sub_tree=-1):
        if sub_tree==-1:
            if self.root is None:
                return 0
            else:
                return self.root.N
        elif sub_tree is None:
            return 0
        else:
            return sub_tree.N
    #递归实现最小键
    def min(self):
        if self.root is None:return None
        return self._min(self.root).key
    def _min(self,sub_tree):
        if sub_tree.lchild is None:return sub_tree
        else:return self._min(sub_tree.lchild)
    #递归实现最大键
    def max(self):
        if self.root is None:return None
        return self._max(self.root).key
    def _max(self,sub_tree):
        if sub_tree.lchild is None:return sub_tree
        else:return self._max(sub_tree.rchild)
    #递归实现向上取整和向下取整
    #给定的键key小于二叉查找树的根节点的键，小于等于key的最大键floor(key)一定在根结点的左子树中
    #只有当根节点右子树中存在小于等于key的结点时，小于等于key的最大键才会出现在右子树中，否则根结点就是小于等于key的最大键
    def floor(self,key):
        if self.root is None:return None
        result=self._floor(self.root,key)
        return None if result is None else result.key
    def _floor(self,sub_tree,key):
        if sub_tree is None:return None
        if sub_tree.key==key:return sub_tree
        elif sub_tree.key>key:
            return sub_tree(sub_tree.lchild,key)
        else:
            temp=self.__floor(sub_tree.rchild,key)
            return sub_tree if temp is None else temp
    #找到排名为k的键
    def select(self,k):
        if self.root is None:return None
        if k<0 or k>self.size()-1:
            raise ValueError('{0} is out of range:(0,{1})'.format(k,self.size()-1))
        else:
            return self._select(self.root,k)
    def _select(self,sub_tree,k):
        t=0 if sub_tree.lchild is None else sub_tree.lchild.N
        if t>k:
            return self._select(sub_tree.lchild,k)
        elif t<k:
            return self._select(sub_tree.rchild,k-t-1)
        else:
            return sub_tree
    #返回给定键的排名
    def rank(self,key):
        if self.root is None:return None
        return self._rank(self.root,key)
    def _rank(self,sub_tree,key):
        if sub_tree is None:return 0
        if sub_tree.key==key:
            return self.size(sub_tree.lchild)
        elif sub_tree.key > key:
            return self._rank(sub_tree.lchild,key)
        else:
            return self._rank(sub_tree.rchild)+self.size(sub_tree.lchild)+1























