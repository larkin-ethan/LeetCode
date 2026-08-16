class Solution {
public:
    bool isPalindrome(int x) {
        std::string intToString = std::to_string(x);
        std::string reversedString = intToString;
        std::reverse(reversedString.begin(), reversedString.end());
        if (intToString == reversedString){
            return true;
        } else {
            return false;
        }
    }
};