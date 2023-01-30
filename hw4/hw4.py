import numpy as np


class Problem1:
    @staticmethod
    def generateGameMap(n, m, minPoint=0, maxPoint=100):
        return np.random.randint(minPoint, maxPoint, size=(n, m))

    @staticmethod
    def findBestRoute(gameMap, i=0, j=0):
        n, m = gameMap.shape

        if n == i and m == j:
            return ([], [])

        south = ([], [])
        east = ([], [])

        if i + 1 < n:
            south = Problem1.findBestRoute(gameMap, i + 1, j)

        if j + 1 < m:
            east = Problem1.findBestRoute(gameMap, i, j + 1)

        if sum(south[0]) > sum(east[0]):
            return ([gameMap[i, j]] + south[0], [(i, j)] + south[1])
        else:
            return ([gameMap[i, j]] + east[0], [(i, j)] + east[1])

    @staticmethod
    def findAndPrintBestRoute(gameMap, i=0, j=0):
        points, route = Problem1.findBestRoute(gameMap)

        print(
            f"Best route: {' -> '.join(map(lambda r: f'A{1 + r[0]}B{1 + r[1]}', route))}"
        )
        print(f"Points: {' + '.join(map(str, points))} = {sum(points)}")

    @staticmethod
    def driverFunction():
        print("---===Problem 1===---")
        print()
        print("Enter n:")
        n = int(input())
        print()
        print("Enter m:")
        m = int(input())

        gameMap = Problem1.generateGameMap(n, m)

        print()
        print(f"{n=}, {m=}")
        print("Game map:")
        print(gameMap)
        print()

        Problem1.findAndPrintBestRoute(gameMap)
        print()


class Problem2:
    @staticmethod
    def generateArray(n, minValue, maxValue):
        return np.random.randint(minValue, maxValue, size=(n,))

    @staticmethod
    def getMedianHelper(arr, n, even):
        arrLength = len(arr)

        pivot = arr.pop(np.random.randint(0, arrLength))

        less = []
        greater = []

        for value in arr:
            if value < pivot:
                less.append(value)
            else:
                greater.append(value)

        lessLength = len(less)

        if n == lessLength:
            if even:
                return 0.5 * (pivot + Problem2.getMedianHelper(greater, 0, False))
            else:
                return pivot
        elif even and n == lessLength - 1:
            return 0.5 * (pivot + Problem2.getMedianHelper(less, len(less) - 1, False))
        elif lessLength > n:
            return Problem2.getMedianHelper(less, n, even)
        elif lessLength < n:
            return Problem2.getMedianHelper(greater, n - lessLength - 1, even)

    @staticmethod
    def getMedian(arr):
        return Problem2.getMedianHelper(arr, len(arr) // 2, len(arr) % 2 == 0)

    @staticmethod
    def driverFunction():
        print("---===Problem 2===---")
        print()
        print("Enter number of elements:")
        n = int(input())

        array = list(np.random.permutation(n))

        print()
        print("The array whose median is going to be calculated:")
        print(array)
        print()
        print("Result:")
        print(Problem2.getMedian(array))
        print()


class CircularLinkedList:
    def __init__(self):
        self.values = []
        self.index = 0
        self.len = 0

    def length(self):
        return self.len

    def add(self, value):
        self.len += 1
        self.values.append(value)

    def current(self):
        self.index = self.index % self.len
        return self.values[self.index]

    def next(self):
        self.index += 1
        return self.current()

    def pop(self):
        self.len -= 1
        self.values.pop(self.index)

    @staticmethod
    def fromArray(arr):
        result = CircularLinkedList()
        result.values = arr.copy()
        result.len = len(result.values)
        return result


class Problem3:
    @staticmethod
    def generateCircularLinkedList(n):
        return CircularLinkedList.fromArray(list(map(lambda i: f"P{i + 1}", range(n))))

    @staticmethod
    def findWinnderCircularLinkedList(circularLinkedList, printing=True):

        while circularLinkedList.length() > 1:
            if printing:
                print(f"{circularLinkedList.current()} eliminates ", end="")
            circularLinkedList.next()
            if printing:
                print(f"{circularLinkedList.current()}")
            circularLinkedList.pop()

        return circularLinkedList.current()

    @staticmethod
    def partA(n):
        print(
            f"{Problem3.findWinnderCircularLinkedList(Problem3.generateCircularLinkedList(n))} won."
        )

    @staticmethod
    def findWinnerLogn(n):
        if n == 1:
            return 0
        return 2 * (n % 2 + Problem3.findWinnerLogn(n // 2))

    @staticmethod
    def partB(n):
        print(f"P{1 + Problem3.findWinnerLogn(n)}")

    @staticmethod
    def driverFunction():
        print("---===Problem 3===---")
        print()

        print("Enter the number of players:")
        playerCount = int(input())
        print()

        print("Algorithm using circular linked list:")
        Problem3.partA(playerCount)
        print()

        print("The winner calculated in logn time complexity with no linkedlist:")
        Problem3.partB(playerCount)
        print()


def main():
    while True:
        Problem1.driverFunction()
        Problem2.driverFunction()
        Problem3.driverFunction()
        print("You may now close the program or press enter to start over.")
        input()
        print()

if __name__ == "__main__":
    main()
