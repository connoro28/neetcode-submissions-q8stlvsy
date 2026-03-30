class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1;
            else:
                my_dict[i] = 1;
            if (my_dict[i] == 2):
                return True;
        return False;
        