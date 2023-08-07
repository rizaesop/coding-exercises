#include <iostream>
using namespace std ;

class Solution {
public:
    bool isPalindrome(int x) {
        string nums = to_string(x);
        int size = nums.size()-1;
        int j;
        for(int i = 0;i<size;i++){
            j = size - i;
            if(nums[i]!= nums[j])
                return false;
            }
        return true;
    }
};