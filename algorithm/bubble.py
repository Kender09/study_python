class Bubble:
    """bubble sort """

    def bubbleSort(self, array):
        k = 0
        while k < (len(array) - 1):
            i = len(array) - 1
            while k < i:
                if array[i-1] > array[i]:
                    array[i-1], array[i] = array[i], array[i-1]
                i -= 1
            k += 1
        return array

if __name__ == '__main__':
    array = [16, 63, 15, 23, 42, 56]
    obj = Bubble()
    ans = obj.bubbleSort(array)
    print(ans)
