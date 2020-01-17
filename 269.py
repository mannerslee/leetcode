class Solution:
    def list2str(self, s):
        result = ''
        for w in s:
            result += w
        return result

    def compareWord(self, s1, s2):
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s1[i], s2[i]
        return None

    def getLetterList(self, words):
        letter_set = set()
        for word in words:
            for letter in word:
                letter_set.add(letter)
        return list(letter_set)

    def initLetterOrderList(self, letter_set):
        in_map = {}
        out_map = {}
        for letter in letter_set:
            in_map[letter] = ""
            out_map[letter] = ""
        return in_map, out_map

    def alien_order(self, words):
        letter_list = self.getLetterList(words)
        in_map, out_map = self.initLetterOrderList(letter_list)

        for i in range(len(words) - 1):
            compare = self.compareWord(words[i], words[i + 1])
            if compare is not None:
                in_map[compare[1]] = compare[0]
                out_map[compare[0]] = compare[1]

        print('letter_list = ', letter_list)
        print("in_map: ", in_map)
        print("=======================================")
        print("out_map: ", out_map)
        # ---------------------Topological sort----------------------------------
        result = []
        flag = True
        while flag:
            print('                 **letter_list', letter_list)
            for i in letter_list:
                if in_map[i] == "":
                    print('                         @i  = ', i)
                    del in_map[i]
                    result.append(i)
                    if out_map[i] == "":
                        return self.list2str(result)
                    else:
                        print('                         @ set out_map[', i, ']  = "" ')
                        in_map[out_map[i]] = ""
                        letter_list.remove(i)
                        break
                else:
                    print('---->>>>>')
                    flag = False
            print('remove :', i)

        return []


if __name__ == '__main__':
    ls = ["wrt", "wrf", "er", "ett", "rftt"]
solution = Solution()

result = solution.alien_order(ls)
print("result = ", result)
