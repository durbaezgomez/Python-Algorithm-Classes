class BTreeNode(object):

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.c = []


    def __str__(self):

        if self.leaf:
            return "Wezel-lisc z {0} kluczami:\n\tK:{1}\n\n".format(len(self.keys), self.keys)
        else:
            s = "Wezel z {0} kluczami i {1} dziecmi:  \n\tK:{2}\n".format(len(self.keys), len(self.c),self.keys)
            return s