from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result: List[bool] = []
    highestCandies = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= highestCandies:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == "__main__":
    print(kidsWithCandies([2,3,5,1,3], 3))
    print(kidsWithCandies([4,2,1,1,2], 1))
    print(kidsWithCandies([12,1,12], 10))