class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    '''
    滑动窗口，使用首尾两个下标索引，使用map类型维护尾部索引已遍历的所有字符最后出现时的下标
    '''
        maxlen = 0
        currentlen = 0
        indHash = {}
        leftside = -1
        ls = len(s)
        for ind, ch in enumerate(s):
            # 如果当前字符之前已出现过，且出现的下标比当前窗口的左下标大，则更新窗口的左下标
            if (ch in indHash) and (leftside < indHash[ch]):
                leftside = indHash[ch];
            # 计算当前的长度
            currentlen = ind - leftside;
            # 更新长度的最大值
            if currentlen > maxlen:
                maxlen = currentlen
            # 将当前字符的下标写入map中
            indHash[ch] = ind
        # 计算最后的一次的长度
        currentlen = ls - leftside - 1
        if currentlen > maxlen:
            maxlen = currentlen
        return maxlen