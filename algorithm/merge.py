class Merge:
    """merge sort """

    def mSort(self, array):
        print("Splitting ", array)
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        l_array = self.mSort(array[:mid])
        r_array = self.mSort(array[mid:])

        return self.marge(l_array, r_array)

    def marge(self, l_array, r_array):
        marge_array = []
        l_index = 0
        r_index = 0

        while len(l_array) > l_index and len(r_array) > r_index:
            if l_array[l_index] <= r_array[r_index]:
                marge_array.append(l_array[l_index])
                l_index += 1
            else:
                marge_array.append(r_array[r_index])
                r_index += 1

        if l_array[l_index:]:
            marge_array.extend(l_array[l_index:])
        if r_array[r_index:]:
            marge_array.extend(r_array[r_index:])

        print("Merging ", marge_array)
        return marge_array


if __name__ == '__main__':
    array = [16, 63, 15, 23, 42, 56]
    obj = Merge()
    ans = obj.mSort(array)
    print(ans)
