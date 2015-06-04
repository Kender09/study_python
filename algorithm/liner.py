class Liner:
    """Liner Search"""

    args = []

    def __init__(self, array):
        self.args = array

    def liner_search(self, target):
        for i in self.args:
            if i == target:
                return i
        return None

if __name__ == '__main__':
    liner = Liner([4, 2, 3, 5, 1])
    target = int(input())
    print(liner.liner_search(target))
