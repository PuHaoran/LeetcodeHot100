"""
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
"""
""" 题解
法一：小顶堆。先将词频保存到字典中，然后将词频转化为数组；
先构建一个大小为K的小顶堆，若当前元素大于堆顶元素，则替换堆顶元素。
不断弹出m-k个最小值，堆中剩下的就是前topK元素。
法二：快排。先将词频保存到字典中，然后将词频转化为数组；最后使用快排求topK的元素。
"""


class Solution:
    def topKFrequent(self, nums, k):
        import heapq
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
        arr = list(d.items())
        heap = []
        for (key, value) in arr:
            if len(heap) >= k:
                if value > heap[0][0]:
                    heapq.heapreplace(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        return [i[1] for i in heap]
        # 法二
        # def quick_sort(arr, l, r, k):
        #     if l >= r:
        #         return
        #     i, j = l-1, r+1
        #     x = arr[l][1]
        #     while i < j:
        #         while 1:
        #             i += 1
        #             if arr[i][1] <= x:
        #                 break
        #         while 1:
        #             j -= 1
        #             if arr[j][1] >= x:
        #                 break
        #         if i < j:
        #             arr[i], arr[j] = arr[j], arr[i]
        #     if j-l+1 >= k:
        #         quick_sort(arr, l, j, k)
        #     else:
        #         quick_sort(arr, j+1, r, k-(j-l+1))
        # quick_sort(arr, 0, len(arr)-1, k)
        # return [i[0] for i in arr][:k]


nums = [4,1,-1,2,-1,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))


