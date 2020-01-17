class Solution:
    def reverseWords(self, s: str):
        while s != s.replace('  ', ' '):
            s = s.replace('  ', ' ')
        s = s.split()
        result = ""
        for w in s[::-1]:
            result += (w+" ")
        return result.strip()


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("  hello world!  "))
    assert solution.reverseWords("  hello world!  ") == "world! hello"
    assert solution.reverseWords("a good   example") == "example good a"
