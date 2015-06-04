class Selection:
    """select sort """

    def selectionSort(self, array):
        for i in range(len(array) - 1):
            k = i + 1
            index_min = i
            while k < len(array):
                if array[k] < array[index_min]:
                    index_min = k
                k += 1
            array[i], array[index_min] = array[index_min], array[i]
        return array

if __name__ == '__main__':
    array = [16, 63, 15, 23, 42, 56]
    select = Selection()
    ans = select.selectionSort(array)
    print(ans)
