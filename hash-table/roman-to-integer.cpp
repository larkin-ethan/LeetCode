class Solution {
public:
    int romanToInt(string s) {
        std::map<char, int> romanValues = {{'I', 1},{'V', 5},{'X', 10},{'L', 50},{'C', 100},{'D', 500},{'M', 1000}};

        int totalValue = 0;
        for(int i = 0; i < s.size(); i++){
            int ithValue = romanValues[s[i]];
            int i1Value = romanValues[s[i+1]];
            if(ithValue < i1Value){
                totalValue -= ithValue;
            }else{
                totalValue += ithValue;
            }
        }
        return totalValue;
    }
};