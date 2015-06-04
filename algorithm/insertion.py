class Insertion:
    """insertion sort """

    def insertionSort(self, array):
        i = 1
        while i < len(array):
            tmp = array[i]
            print array
            k = i
            while array[k-1] > tmp and k > 0:
                array[k] = array[k-1]
                k -= 1
            array[k] = tmp
            i += 1
        return array

if __name__ == '__main__':
    array = [16, 63, 15, 23, 42, 56]
    obj = Insertion()
    ans = obj.insertionSort(array)
    print(ans)
