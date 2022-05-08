#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#
# 解法1(T70% S86%): 没什么值得说的，饱和式限制条件就好，这种题一般都是找到False的条件提交返回，检查到最后都没错就返回True。这里我是保存了上一位的状态和首字母的状态进行判断，提前终止的条件包括：如果首字母是小写但我是大写；非第二字符时上一个字符是大写但我是小写；如果我是大写但前一位是小写

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1: return True

        first_is_lower = word[0].islower()
        last_is_lower = first_is_lower
        for i in range(1, len(word)):
            this_is_lower = word[i].islower()
            if first_is_lower and not this_is_lower: return False
            if i!=1 and not last_is_lower and this_is_lower: return False
            if not this_is_lower and last_is_lower: return False
            last_is_lower = this_is_lower
        return True
# @lc code=end

