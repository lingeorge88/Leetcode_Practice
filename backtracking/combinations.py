"""
Given 2 nums n & k, return all possible combinations of size = k,
choosing from values between 1 and n.
"""


def combinations(n, k):
    combinations = []

    helper(1, [], combinations, n, k)
    return combinations


def helper(i, currComb, combinations, n, k):
    if len(currComb) == k:
        combinations.append(currComb.copy())
        return

    if i > n:
        return

    currComb.append(i)  # include current number
    helper(i + 1, currComb, combinations, n, k)
    currComb.pop()  # backtrack remove last number

    helper(i + 1, currComb, combinations, n, k)  # does not include current number


def main():
    res = combinations(3, 2)
    print(res)


if __name__ == "__main__":
    main()
