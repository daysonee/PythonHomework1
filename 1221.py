class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        pointer = 0
        countL = 0
        countR = 0
        while(pointer < len(s)):
            if(s[pointer] == "L"): countL+=1
            if(s[pointer] == "R"): countR+=1
            if(countL == countR): 
                count+=1
                countL = countR = 0
            pointer+=1
        return count