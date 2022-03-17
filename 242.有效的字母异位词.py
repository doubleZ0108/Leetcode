#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#
# 解法1: 双重for循环判断，要加标志位防止重复字符
# 解法2(T22% S5%): 字符串排序之后比较
#   字符串要转列表才能排序，这里可能比较耗资源，但转为列表之后不用再转回字符串，可以直接开始比较
# 解法3: 构建字典，字符作为key，有某个字符就++，最后一次循环来判断
#   改进(T90% S100%)：只用一个字典，看第一个字符串时+，看第二个字符串时-，最后看字典里是不是全零

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        D = {}
        for l in s:
            if l in D:
                D[l] += 1
            else:
                D[l] = 1
        for l in t:
            if l in D:
                D[l] -= 1
            else:
                return False
        for k, v in D.items():
            if v > 0:
                return False
        return True


    def otherSolution(self, s, t):
        # 解法2
        if len(s) != len(t):
            return False

        # s = ''.join(sorted(list(s)))
        for l_s, l_t in zip(sorted(list(s)), sorted(list(t))):
            if l_s != l_t:
                return False

        return True
# @lc code=end

