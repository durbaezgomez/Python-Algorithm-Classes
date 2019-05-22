import pickle

from btree_node import *


class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t

    def search(self, k, x=None):

        # k - szukana wartosc
        # x - opcjonalnie wezel od ktorego zaczac szukanie

        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                print("Znaleziono klucz {0} w ponizszym wezle:".format(k))
                print(str(x))
                return (x, i)
            elif x.leaf:
                print("Nie znaleziono klucza w zadnym wezle!")
                return None
            else:
                return self.search(k, x.c[i])
        else:
            return self.search(k, self.root)

    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:     # wezly sa pelne, trzeba rozdzielic
            s = BTreeNode()
            self.root = s
            s.c.insert(0, r)                    # dotychczasowy korzen jest 0-wym dzieckiem nowego korzenia s
            self._split_child(s, 0)             # podzial wezla s
            self._insert_nonfull(s, k)          # wstaw do nowego niepelnego wezla
        else:
            self._insert_nonfull(r, k)

    def _insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # wstawianie klucza
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # wstaw dziecko
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.c[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_nonfull(x.c[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)

        # przesun wszystkie dzieci x w prawo i wstaw z w miejscu i+1

        x.c.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        # klucze z sa na indeksach od t do 2t-1, wiec 0 <= y <= t-2

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        # children of z are t to 2t els of y.c
        # dzieci z sa od t do 2t,

        if not y.leaf:
            z.c = y.c[t:(2 * t)]
            y.c = y.c[0:(t - 1)]

    def __str__(self):
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.c])

    def writeToFile(self):

        r = self.root
        nodes = []
        nodes.append(r)
        nodes.extend([child for child in r.c])

        f = open("btree_data.dat", 'wb')

        for node in nodes:
            pickle.dump(node,f)
        f.close()

    def readTreeFromFile(self):

        f = open("btree_data.dat", 'r')
        while 1:
            try:
                node = pickle.load(f)
                print(node)
            except EOFError:
                break
        f.close()







