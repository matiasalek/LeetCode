package Easy;

import java.lang.Math;

public class ScoreOfAString3110 {
    public int scoreOfString(String s) {
        char c;
        int result = 0;
        int result2;
        for (int i = 0; i < s.length(); i++) {
            if (i+1 < s.length()) {
                c = s.charAt(i);
                result2 = Math.abs(c - s.charAt(i + 1));
                result = result + result2;
            }
        }
        return result;
    }
}
