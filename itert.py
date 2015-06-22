def iter_all_list(arg):
    comb_num = factorial(len(arg))
    all_list = [[0 for i in range(len(arg))] for j in range(comb_num)]
    ans_list = []
    ans_list.append(arg[0])
    for num in range(len(arg) - 1):
        save_arg = []
        save_arg.extend()



def factorial(n):
    for i in range(1, n):
        n *=i
    return n

if __name__ == '__main__':
    arr = [3, 2, 1]
    print iter_all_list(arr)
