# 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # 更加简单，节省计算
        i,ans = 0, 0 # i 代表最大字串的起始位置 ans 代表最终长度
        hash_dict = {} # 键 str中出现的字符 值 这个键最后出现的位置加1
        for j in range(len(s)):
            # print(j,'j value') # j 从0开始
            if hash_dict.get(s[j]) is not None and hash_dict.get(s[j]) > i: # 如果字典中已经有了j位置的字符 且 长度大于 i
                i = hash_dict.get(s[j])
            ans = max(ans, j - i + 1)
            hash_dict[s[j]] = j + 1
        return ans

    def lengthOfLongestSubstringbili(self, s: str)-> int: # 易于理解
        left = right = length = maxlength = 0
        hash_dict = set()
        while(right < len(s)):
            if(s[right] not in hash_dict):
                hash_dict.add(s[right])
                length+=1
                if(length > maxlength):
                    maxlength = length
                right +=1
            else:
                while(s[right]  in hash_dict):
                    hash_dict.remove(s[left])
                    left += 1
                    length -= 1

                hash_dict.add(s[right])
                length += 1
                right += 1
        return maxlength


if __name__ == '__main__':
    my_solution = Solution()
    print(my_solution.lengthOfLongestSubstring('pwwkew'))
    print(my_solution.lengthOfLongestSubstringbili('pwwkew'))
    # dic1 = {'Author': 'Python当打之年', 'age': 99, 'sex': '男'}
    # print(dic1.get('Author1'))
