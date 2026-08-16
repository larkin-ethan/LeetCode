class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i <= nums.size()-2; i++) {
            for(int j = 1; j <= nums.size()-1; j++){
                if(nums.size() == 2){
                    return{i,j};
                }else{
                    if (i != j) {
                        if (nums[i] + nums[j] == target){
                            return {i,j};
                        }
                    }
                }
            }
        }
        return {0};
    }
};