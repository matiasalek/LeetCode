package Easy;

import java.lang.Math;

public class ScoreOfAString3110 {
    public int scoreOfString(String s) {
        int score = 0;
        int partial;
        for (int i = 0; i < s.length(); i++) {
            if (i+1 < s.length()) {
                partial = Math.abs(s.charAt(i) - s.charAt(i + 1));
                score = score + partial;
            }
        }
        return score;
    }
}
