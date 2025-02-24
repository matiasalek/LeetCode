package Easy;

import java.util.HashMap;

public class RomanToInteger13 {
    public int romanToInt(String s) {
        int result = 0;
        HashMap<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            int currentValue = romanMap.get(c);

            if (i+1 < s.length() && currentValue < romanMap.get(s.charAt(i + 1))) {
                result += romanMap.get(s.charAt(i + 1)) - romanMap.get(c);
                i++;
            } else {
                result += currentValue;
            }
        }
        return result;
    }
}