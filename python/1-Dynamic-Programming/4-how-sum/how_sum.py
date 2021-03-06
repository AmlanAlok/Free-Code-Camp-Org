import unittest

'''
TC = O(n^m * m)
SC = O(2m) = O(m)
'''


def how_sum(target_sum, numbers):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for n in numbers:
        remainder = target_sum - n
        # ans.append(n)

        ans = how_sum(remainder, numbers)
        if ans is not None:
            # in the worst case this operation will take m steps
            return ans + [n]                # ans.append(n) returns None

    return ans


'''
TC = O(n * m * m)
SC = O(m^2)
'''


def how_sum_memo(target_sum, numbers, memo={}):

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for n in numbers:
        remainder = target_sum - n

        ans = how_sum_memo(remainder, numbers, memo)
        memo[remainder] = ans

        if ans is not None:
            # memo[remainder] = ans + [n]
            return memo[remainder] + [n]             # ans.append(n) returns None

    return None


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))
        self.assertEqual([3, 2], how_sum(5, [2, 3]))
        self.assertEqual(None, how_sum(7, [2, 4]))
        # print(how_sum(5, [2, 3]))

    def test_02(self):
        self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        # self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))
        # self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual(None, how_sum_memo(7, [2, 4]))
        self.assertEqual([3, 2], how_sum_memo(5, [2, 3]))

        # print(how_sum_memo(7, [2, 4]))

    def test_03(self):
        self.assertEqual(None, how_sum_memo(300, [7, 14]))
        self.assertEqual([100, 100, 100], how_sum_memo(300, [100, 7, 14]))

    def test_04(self):
        self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))


if __name__ == '__main__':
    unittest.main()
