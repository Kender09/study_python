class Quick:
    """quick sort """

    def quickSort(self, array):
        print array
        if len(array) <= 1:
            return array
        return self.quickSort([lt for lt in array[1:] if lt < array[0]]) + array[0:1] + self.quickSort([ge for ge in array[1:] if ge >= array[0]])

    def qSort(self, array):
        print("q: ", array)
        if len(array) <= 1:
            return array
        pivot = array[0]
        smaller = [x for x in array[1:] if x < pivot]
        larger = [x for x in array[1:] if x >= pivot]

        return self.qSort(smaller) + [pivot] + self.qSort(larger)

if __name__ == '__main__':
    array = [16, 63, 15, 23, 42, 56]
    obj = Quick()
    ans = obj.qSort(array)
    print(ans)
