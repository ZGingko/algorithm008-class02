from typing import List

class Solution:
    letter_dict = dict()
    def __init__(self):
        Solution.letter_dict["2"] = "abc"
        Solution.letter_dict["3"] = "def"
        Solution.letter_dict["4"] = "ghi"
        Solution.letter_dict["5"] = "jkl"
        Solution.letter_dict["6"] = "mno"
        Solution.letter_dict["7"] = "pqrs"
        Solution.letter_dict["8"] = "tuv"
        Solution.letter_dict["9"] = "wxyz"

    def letterCombinations(self, digits: str) -> List[str]:
        """
        17. 电话号码的字母组合
            给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
            给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
                tmpDict["2"] = "abc"
                tmpDict["3"] = "def"
                tmpDict["4"] = "ghi"
                tmpDict["5"] = "jkl"
                tmpDict["6"] = "mno"
                tmpDict["7"] = "pqrs"
                tmpDict["8"] = "tuv"
                tmpDict["9"] = "wxyz"

            示例:
                输入："23"
                输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
        """
        if not digits:
            return []
        def process(s, digits, i,result):
            if i == len(digits):
                result.append(s)
                return
            tmpStr = Solution.letter_dict[digits[i]]
            for ch in tmpStr:
                process(s+ch,digits,i+1,result)

        result = []
        process("", digits, 0, result)
        return result
        

    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        def process(s, digits, i, result, tmpDict):
            if i == len(digits):
                result.append(s)
                return
            tmpStr = tmpDict[digits[i]]
            for item in tmpStr:
                process(s+item, digits, i+1, result, tmpDict)

        tmpDict = dict()
        tmpDict["2"] = "abc"
        tmpDict["3"] = "def"
        tmpDict["4"] = "ghi"
        tmpDict["5"] = "jkl"
        tmpDict["6"] = "mno"
        tmpDict["7"] = "pqrs"
        tmpDict["8"] = "tuv"
        tmpDict["9"] = "wxyz"
        result = []
        process("", digits, 0, result, tmpDict)
        return result


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
