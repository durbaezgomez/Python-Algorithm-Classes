#  'A' - angle 'L' - left 'U' - up


class LCS:

    def __init__(self,s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.n = len(s1)
        self.m = len(s2)
        self.C = [[0 for x in range(self.n+2)] for y in range(self.m+2)]
        self.X = [['' for x in range(self.n+2)] for y in range(self.m+2)]
        self.LCS = []


    def initialize(self):
        for i in range(0,self.m+2):
            for j in range(0,self.n+2):
                self.X[i][j] = ''

        for i in range(self.m+2):
            self.C[i][0] = 0
            for j in range(self.n+2):
                self.C[0][j] = 0

    def fillTable(self):
        self.initialize()
        for i in range(2,self.m+2):
            for j in range(2,self.n+2):
                if self.s1[j-2] == self.s2[i-2]:
                    self.C[i][j] = self.C[i-1][j-1] + 1
                    self.X[i][j] = 'A'
                else:
                    self.C[i][j] = max(self.C[i-1][j], self.C[i][j-1])
                    if max(self.C[i-1][j], self.C[i][j-1]) == self.C[i-1][j]:
                        self.X[i][j] = 'U'
                    else:
                        self.X[i][j] = 'L'

    def printSeries(self):
        print('TWORZE TABELE: \n')
        s = ''
        for i in range(self.m+2):
            for j in range(self.n+2):
                if i == 0 and j == 0:
                    s += '{:5}'.format('*')
                elif i + j == 1:
                    s += '{:5}'.format('0')
                elif i == 0 and j > 1:
                    s += '{:5}'.format(str(self.s1[j-2]))
                elif j == 0 and i > 1:
                    s += '{:5}'.format(str(self.s2[i-2]))
                else:
                    if self.X[i][j] == 'A':
                        s += '{:5}'.format('\\' + str(self.C[i][j]))
                    elif self.X[i][j] == 'L':
                        s += '{:5}'.format('-' + str(self.C[i][j]))
                    elif self.X[i][j] == 'U':
                        s += '{:5}'.format('|' + str(self.C[i][j]))
                    else:
                        s += '{:5}'.format(str(self.C[i][j]))

            s += '\n\n'
        print(s)

    def findLCS(self):
        self.fillTable()
        self.printSeries()
        self.retLCS(self.m+1, self.n+1)

    def retLCS(self, x, y):
        if x == 1 or y == 1:
            self.LCS.reverse()
            print(self.LCS)
            return
        if self.X[x][y] == 'A':
            self.LCS.append(self.s1[y-2])
            self.retLCS(x-1,y-1)
        elif self.X[x][y] == 'U':
            self.retLCS(x-1,y)
        else:
            self.retLCS(x,y-1)


s1 = 'aabb'
s2 = 'abasa'

lcs1 = LCS(s1, s2)
lcs1.findLCS()