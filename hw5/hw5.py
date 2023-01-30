import numpy as np


class Problem1:
    @staticmethod
    def getCommongSubstring(text1, text2, noneAccepted=True):
        if noneAccepted:
            if text1 == None:
                return text2
            if text2 == None:
                return text1

        def tempGenerator():
            for char1, char2 in zip(text1, text2):
                if char1 != char2:
                    break
                yield char1

        return "".join(tempGenerator())

    @staticmethod
    def getLongestCommonSubstring(array):
        match array:
            case [x]:
                return x
            case []:
                return None
        halfLength = len(array) // 2
        return Problem1.getCommongSubstring(
            Problem1.getLongestCommonSubstring(array[:halfLength]),
            Problem1.getLongestCommonSubstring(array[halfLength:]),
        )

    @staticmethod
    def test(words, answer):
        result = Problem1.getLongestCommonSubstring(words)
        print(f"{words=}\n{result=}")
        print("Correct." if result == answer else "False.")
        print()

    @staticmethod
    def driver():
        print("---=== Problem 1 ===---")
        Problem1.test(
            [
                "programmable",
                "programming",
                "programmer",
                "programmatic",
                "programmability",
            ],
            "programm",
        )
        Problem1.test(
            ["compute", "compatible", "computer", "compare", "compactness"], "comp"
        )

        print(
            "You can also enter test words, or just press enter to continue to next problem."
        )
        while userInput := input():
            words = [
                userInput
                + "".join(
                    map(chr, 97 + np.random.randint(0, 26, (np.random.randint(5),)))
                )
                for i in range(np.random.randint(2, 5))
            ]
            Problem1.test(words, userInput)
        print()


class Problem2:
    # Couldn't figure out.
    
    # @staticmethod
    # def getMostProfitableDaysDAC(priceList, side=None):

    # match priceList:
    #     case [x]:
    #         return (0, 0, 0)

    # length = len(priceList)
    # halfLength = length // 2

    # leftBuyDay, leftSellDay, cheapestDay = Problem2.getMostProfitableDaysDAC(
    #     priceList[:halfLength], 0
    # )
    # rightBuyDay, rightSellDay, expensivestDay = Problem2.getMostProfitableDaysDAC(
    #     priceList[halfLength:], 1
    # )

    # leftBuyPrice = priceList[leftBuyDay]
    # leftSellPrice = priceList[leftSellDay]
    # leftProfit = leftSellPrice - leftBuyPrice

    # rightBuyDay += halfLength
    # rightSellDay += halfLength
    # expensivestDay += halfLength
    # rightBuyPrice = priceList[rightBuyDay]
    # rightSellPrice = priceList[rightSellDay]
    # rightProfit = rightSellPrice - rightBuyPrice

    # expensivestPrice = priceList[expensivestDay]
    # cheapestPrice = priceList[cheapestDay]
    # mixedProfit = expensivestPrice - cheapestPrice

    # extremeDay = None

    # if side == 0:
    #     if cheapestPrice < expensivestPrice:
    #         extremeDay = cheapestDay
    #     else:
    #         extremeDay = expensivestDay
    # elif side == 1:
    #     if cheapestPrice < expensivestPrice:
    #         extremeDay = expensivestDay
    #     else:
    #         extremeDay = cheapestDay

    # if mixedProfit > leftProfit and mixedProfit > rightProfit:
    #     return (cheapestDay, expensivestDay, extremeDay)
    # elif leftProfit > rightProfit:
    #     return (leftBuyDay, leftSellDay, extremeDay)
    # else:
    #     return (rightBuyDay, rightSellDay, extremeDay)

    @staticmethod
    def getMostProfitableDays(priceList):
        buyDay = 0
        sellDay = 0
        cheapestDay = 0

        for day, price in enumerate(priceList):
            if priceList[cheapestDay] > price:
                cheapestDay = day
            elif (
                price - priceList[cheapestDay] >= priceList[sellDay] - priceList[buyDay]
            ):
                sellDay = day
                buyDay = cheapestDay

        return (buyDay, sellDay)

    @staticmethod
    def driver():
        print("---=== Problem 2 ===---")

        center = np.random.randint(10, 200) / 10
        low, high = int(7 * center), int(13 * center)
        priceList = np.random.randint(low, high, np.random.randint(5, 11))
        answer = Problem2.getMostProfitableDays(priceList)
        print(f"{priceList=}\n{answer=}")
        print()

        print(
            "Press enter to see more examples, or type anything then press enter to continue to next problem."
        )
        while not input():
            center = np.random.randint(10, 200) / 10
            low, high = int(7 * center), int(13 * center)
            priceList = np.random.randint(low, high, np.random.randint(5, 11))
            answer = Problem2.getMostProfitableDays(priceList)
            print(f"{priceList=}\n{answer=}")

        print()


class Problem3:
    @staticmethod
    def getMaxConsecutiveIncreasingLength(array):
        arrayLength = len(array)

        if arrayLength == 0:
            return 0

        lengths = [1] * arrayLength

        for i in range(1, arrayLength):
            if array[i] > array[i - 1]:
                lengths[i] = lengths[i - 1] + 1

        return max(lengths)

    @staticmethod
    def driver():
        print("---=== Problem 3 ===---")
        length = np.random.randint(5, 15)
        integers = np.random.randint(1, 11, (length,))
        result = Problem3.getMaxConsecutiveIncreasingLength(integers)
        print(f"{integers=}\n{result=}")
        print()

        print(
            "Press enter to see more examples, or type anything then press enter to continue to next problem."
        )
        while not input():
            length = np.random.randint(5, 15)
            integers = np.random.randint(1, 11, (length,))
            result = Problem3.getMaxConsecutiveIncreasingLength(integers)
            print(f"{integers=}\n{result=}")

        print()


class Problem4:
    @staticmethod
    def generateGameMap(n, m, minPoint=0, maxPoint=100):
        return np.random.randint(minPoint, maxPoint, size=(n, m))

    @staticmethod
    def findBestRouteDynamic(gameMap):
        height, width = np.array(gameMap).shape

        maxPointMap = np.zeros((height, width), dtype=int)
        maxPointMap[-1, -1] = gameMap[-1][-1]

        for i in range(1, min(height, width) + 1):
            for j in range(2, width + 1):
                maxPointMap[-i, -j] = max(
                    gameMap[-i][-j] + maxPointMap[1 - i, -j],
                    gameMap[-i][-j] + maxPointMap[-i, 1 - j],
                )
            for j in range(2, height + 1):
                maxPointMap[-j, -i] = max(
                    gameMap[-j][-i] + maxPointMap[-j, 1 - i],
                    gameMap[-j][-i] + maxPointMap[1 - j, -i],
                )

        return maxPointMap[0, 0]

    @staticmethod
    def findBestRouteGreedy(gameMap):
        height, width = np.array(gameMap).shape

        result = gameMap[0][0]

        i = 0
        j = 0
        while i < height - 1 and j < width - 1:
            if gameMap[i + 1][j] > gameMap[i][j + 1]:
                result += gameMap[i + 1][j]
                i += 1
            else:
                result += gameMap[i][j + 1]
                j += 1

        while i == height - 1 and j < width - 1:
            j += 1
            result += gameMap[i][j]

        while j == width - 1 and i < height - 1:
            i += 1
            result += gameMap[i][j]

        return result

    @staticmethod
    def driver():
        print("---===Problem 1===---")
        print()
        while True:
            print("Enter n:")
            n = int(input())
            print()
            print("Enter m:")
            m = int(input())

            gameMap = Problem4.generateGameMap(n, m)

            print()
            print(f"{n=}, {m=}")
            print("Game map:")
            print(gameMap)
            print()

            print(f"Greedy algorithm result: {Problem4.findBestRouteGreedy(gameMap)}")
            print(f"Dynamic algorithm result: {Problem4.findBestRouteDynamic(gameMap)}")
            print()

            print(
                "You can press enter to see more examples, or type anything then press enter to continue."
            )

            if input():
                break
        print()


def main():
    while True:
        Problem1.driver()
        Problem2.driver()
        Problem3.driver()
        Problem4.driver()
        print()
        print(
            "You can now press enter to get back to first problem and test out all of them again, or type anything then press enter to quit."
        )
        if input():
            break


if __name__ == "__main__":
    main()
