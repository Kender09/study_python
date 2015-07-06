class Knapsack():
    """docstring for knapsack"""
    def __init__(self, weight_list, value_list, memo_date):
        self.weight_list = weight_list
        self.value_list = value_list
        self.memo_date = memo_date

    def rec(self, i, j):
        if self.memo_date[i][j] >= 0:
            return self.memo_date[i][j]
        if i == len(self.value_list):
            res = 0
        elif j < self.weight_list[i]:
            res = self.rec(i + 1, j)
        else:
            res = max(self.rec(i+1, j), self.rec(i + 1, j - self.weight_list[i]) + self.value_list[i])
        self.memo_date[i][j] = res
        return res

if __name__ == '__main__':
    """
    ex input)
        4
        2 3
        1 2
        3 4
        2 2
        5
    """
    size = int(input())
    weight_list = []
    value_list = []
    for i in range(size):
        w, v = map(int, input().split())
        weight_list.append(w)
        value_list.append(v)
    W = int(input())
    dp = [[-1 for i in range(W + 1)] for i in range(size + 1)]
    knapsack = Knapsack(weight_list, value_list, dp)
    print(knapsack.rec(0, W))
