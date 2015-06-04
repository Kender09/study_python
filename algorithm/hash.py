class Hash:
    """Hash Search"""

    arrayH = []
    numH = 0

    def __init__(self, num):
        self.arrayH = [0] * num
        self.numH = num

    def hashSrore(self, array1):
        k = 0
        for i in array1:
            k = i % self.numH
            while True:
                if self.arrayH[k] == 0:
                    self.arrayH[k] = i
                    break
                else:
                    k = (k + 1) % self.numH
        return self.arrayH

    def hashSearch(self, num, array):
        k = num % self.numH
        while array[k] != 0:
            if array[k] != num:
                return k
            else:
                k = (k+1) % self.numH
        return None

if __name__ == '__main__':
    from pprint import pprint
    hash_test = Hash(11)
    target = int(input())
    array = [12, 13, 15, 23, 42, 56]
    hash_arr = hash_test.hashSrore(array)
    pprint(hash_arr)
    ans = hash_test.hashSearch(target, hash_arr)
    print(ans)
