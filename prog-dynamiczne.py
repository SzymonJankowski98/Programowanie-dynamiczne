

file = open("dane.txt", "r")
line = file.readline().split(" ")
AMOUNT = int(line[0])
CAPACITY = int(line[1])

tab = []
for i in range(AMOUNT):
    line = file.readline().split(" ")
    tab.append([int(line[0]), int(line[1])])


class Pd:
    def __init__(self, c, tab):
        self.result_tab = []
        self.c = c
        self.tab = tab
        self.pd()
        self.result()

    def pd(self):
        self.result_tab.append([])
        for k in range(self.c + 1):
            self.result_tab[0].append(0)
        for i in range(len(self.tab)):
            self.result_tab.append([])
            for j in range(self.c + 1):
                if j == 0:
                    self.result_tab[i + 1].append(0)
                elif self.tab[i][1] > j:
                    self.result_tab[i + 1].append(self.result_tab[i][j])
                else:
                    x = max(self.result_tab[i][j], self.result_tab[i][j - self.tab[i][1]] + self.tab[i][0])
                    self.result_tab[i + 1].append(x)
    def result(self):
        res = []
        i = len(self.result_tab) - 1
        j = len(self.result_tab[0]) - 1
        while i > 0 and j > 0:
            while self.result_tab[i][j] == self.result_tab[i-1][j] and i > 1:
                i -= 1
            res.append(i)
            j -= self.tab[i - 1][1]
            i -= 1
        print(res)


def brute_force(c, tab, value = 0, weight = 0, used = [], i = 0):
    if weight <= c:
        if i < len(tab):
            value1, used_tab1 = brute_force(c, tab, value + tab[i][0], weight + tab[i][1], used + [i + 1], i + 1)
            value2, used_tab2 = brute_force(c, tab, value, weight, used, i + 1)
            if value1 > value2:
                return value1, used_tab1
            else:
                return value2, used_tab2
        else:
            return value, used
    else:
        return 0, used


x = Pd(CAPACITY, tab)
print(brute_force(CAPACITY, tab))