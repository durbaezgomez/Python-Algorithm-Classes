from rbnode import rbnode


class rbtree(object):
    def __init__(self, create_node=rbnode):

        self._nil = create_node(key=None)
        self._root = self.nil
        self._create_node = create_node

    root = property(fget=lambda self: self._root)
    nil = property(fget=lambda self: self._nil)

    def search(self, key, x=None):

        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x=None):

        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x=None):

        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, key):
        self.insert_node(self._create_node(key=key))

    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.p.red:                      #jesli ojciec czerwony
            if z.p == z.p.p.left:           #jesli ojciec jest lewym synem
                y = z.p.p.right             #y = wuj (lewy)
                if y.red:                   #jesli wuj jest czerwony
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:                       #jesli wuj jest czarny
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:                           #jesli ojciec jest prawym synem
                y = z.p.p.left              #y = wuj (prawy)
                if y.red:                   #jesli wuj jest czerwony
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:                       #jesli wuj jest czarny
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False              #root znow czarny, jesli sie to zmienilo

    def _left_rotate(self, x):
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y

    def _right_rotate(self, y):
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x


def minimalDepth(item):

    leftDepth = 0
    if item.left != None:
        leftDepth = minimalDepth(item.left)

    rightDepth = 0
    if item.right != None:
        rightDepth = minimalDepth(item.right)

    if leftDepth > rightDepth:
        return rightDepth + 1

    elif rightDepth >= leftDepth:
        return leftDepth + 1


def maximalDepth(item):

    leftDepth = 0
    if item.left != None:
        leftDepth = maximalDepth(item.left)

    rightDepth = 0
    if item.right != None:
        rightDepth = maximalDepth(item.right)

    if leftDepth > rightDepth:
        return leftDepth + 1

    elif rightDepth >= leftDepth:
        return rightDepth + 1


def countRed(item):
    if item == None:
        return 0
    redCount=0
    if item.red:
        redCount=1
    return countRed(item.left)+countRed(item.right)+redCount


def print_out(tree, item, level):
    if item != tree.nil:
        if item.drawn == False:
            print(nodeClr(tree, item))
        if item.left != None and item.right != None:
            level += 1
            print(nodeClr(tree, item.left)),
            print(nodeClr(tree, item.right))
            # print("LEVEL "+str(level))
            print_out(tree, item.left,level)
            print_out(tree, item.right,level)
        elif item.left != None and item.right == None:
            level += 1
            print(nodeClr(tree, item.left)),
            # print("LEVEL "+str(level))
            print_out(tree, item.left,level)
        elif item.left == None and item.right != None:
            level += 1
            print(nodeClr(tree,item.right))
            # print("LEVEL "+str(level))
            print_out(tree, item.right,level)



def nodeClr(tree, item):
    item.drawn = True
    if item != tree.nil:
        if item.red:
            s = str(item.key) + "R"
        else:
            s = str(item.key)
    else:
        s="_"
    return s


def drukujost(tree, item, l, p, poziom):
    srodek = (l + p) / 2
    if (item == tree.nil):
        return
    wydruk[poziom][srodek] = '*'


def drukujwew(tree,item, l, p, poziom):
    srodek = (l + p) / 2
    if item == tree.nil:
        return
    if item.red == False:
        s = str(item.key)
        dl = len(s)
    else:
        s = str(item.key)+"R"
        dl = len(s)
    # print("DL: "+str(dl))
    # print("S: "+s)
    for i in range(dl):
        wydruk[poziom][srodek - dl / 2 + i] = s[i]
    if ++poziom < IL_POZ:
        drukujwew(tree, item.left, l, srodek, poziom)
        drukujwew(tree, item.right, srodek+1, p, poziom)
    else:
        drukujost(tree, item.left, l, srodek, poziom)
        drukujost(tree, item.right, srodek+1, p, poziom)


def drukuj(tree):
    for i in range(IL_POZ):
        for j in range(SZER_EKR):
            wydruk[i][j] = ' '
    drukujwew(tree, tree.root, 0, SZER_EKR, 0)
    for i in range(IL_POZ):
        for j in range(SZER_EKR):
            print(wydruk[i][j])
    print("\n")


IL_POZ = 50
SZER_EKR = 80
wydruk = [[0 for x in range(SZER_EKR)] for y in range(IL_POZ)]

# test
t1 = rbtree()
t2 = rbtree()
for key in (1,2,3,4,5):
    t1.insert_key(key)

# print(minimalDepth(t.root))
# print(maximalDepth(t.root))
# print(countRed(t.root))
# print("\n")

# Moja metoda wypisywania, nie dziala do konca prawidlowo
print_out(t1, t1.root, 0)

# metoda z materialow od Pana Profesora, niepoprawiona wersja w Pythonie (problem z sprintf)
# drukuj(t1)

