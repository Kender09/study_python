class Binary:
    """Binary Search"""

    def binary_search(self, arg, target):
        head = 0
        tail = len(arg) - 1
        while head <= tail:
            center = (head + tail) // 2
            if arg[center] == target:
                return center
            else:
                if arg[center] < target:
                    head = center + 1
                else:
                    tail = center - 1
        return None

if __name__ == '__main__':
    binary = Binary()
    target = int(input())
    array = [11, 13, 15, 23, 42, 56]
    print(binary.binary_search(array, target))
