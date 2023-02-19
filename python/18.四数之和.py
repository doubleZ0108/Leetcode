#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# 解法1(超时)：直接四重循环+如果已经比target大就提前终止还是会超时
#     需要注意的是因为我们是从小到大排序，因此只有当当前数本身为正且target也为正时，才能根据当前已经超过target来提前结束；反过来负数是不可以的，因为我们是从小到大排序的
#
# 解法2(T5% S78%)：跟三数之和做法类似，只不过改成两重外层暴力循环，内层两层通过双指针来控制移动，重复结果通过将结果拼接为字符串并用集合维护
#     数字拼接成字符串通过集合维护不是很优美，但暂时没想到更简单易做的去重方法

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        visited = set()

        for i in range(0, n-3):
            if nums[i]>0 and nums[i]>target: break
            for j in range(i+1, n-2):
                if nums[i]+nums[j]>0 and nums[i]+nums[j]>target: break
                
                p, q = j+1, n-1
                while p < q:
                    tmp = [nums[i], nums[j], nums[p], nums[q]]
                    tmpsum = sum(tmp)
                    if tmpsum == target:
                        tmps = ",".join(map(lambda x: str(x), tmp))
                        if tmps not in visited:
                            res.append(tmp)
                            visited.add(tmps)
                        p += 1
                        q -= 1
                    elif tmpsum < target:
                        p += 1
                    else:
                        q -= 1
        return list(res)
# @lc code=end

