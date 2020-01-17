class Solution:
    def invalidTransactions(self, transactions):
        result = []
        name_dict = {}
        for record in transactions:
            data = record.split(',')
            if data[0] not in name_dict:
                name_dict[data[0]] = []
            name_dict[data[0]].append(
                (int(data[1]), int(data[2]), data[3], record))  # data[1]:time  data[2]:amount  data[3]:city

        for customer in name_dict:
            name_dict[customer].sort(key=lambda x: x[0])  # sort by time
            print('name_dict = ', name_dict)
            for i in range(len(name_dict[customer]) - 1):
                if name_dict[customer][i][1] > 1000:
                    result.append(name_dict[customer][i][3])
                if abs(name_dict[customer][i][0] - name_dict[customer][i + 1][0]) < 60 and name_dict[customer][i][2] != \
                        name_dict[customer][i + 1][2]:
                    result.append(name_dict[customer][i][3])
                    result.append(name_dict[customer][i + 1][3])
        return list(set(result))


if __name__ == '__main__':
    solution = Solution()
    result = solution.invalidTransactions(
        ["bob,55,173,barcelona", "lee,113,952,zurich", "maybe,115,1973,madrid", "chalicefy,229,283,istanbul",
         "bob,24,874,shanghai", "alex,568,412,tokyo", "alex,242,1710,milan", "iris,722,879,shenzhen",
         "chalicefy,281,1586,warsaw", "maybe,246,778,bangkok", "xnova,605,166,newdelhi", "iris,631,991,hongkong",
         "chalicefy,500,620,tokyo", "chalicefy,380,428,istanbul", "iris,905,180,barcelona", "alex,810,732,shenzhen",
         "iris,689,389,paris", "xnova,475,298,singapore", "lee,58,709,amsterdam", "xnova,717,546,guangzhou"])
    print(result)
