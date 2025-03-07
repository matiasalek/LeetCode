package Easy.Java;

public class PalindromeNumber9 {
    public boolean isPalindrome(int x) {
        String original = Integer.toString(x);
        String reverse = "";
        char c;

        for (int i=0; i<original.length(); i++){
            c = original.charAt(i);
            reverse = c + reverse;
        }
        return original.equals(reverse);
    }
}