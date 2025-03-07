package Easy.Java;

public class LengthOfLastWord58 {
    public int lengthOfLastWord(String s) {
        String[] splitted = s.split(" ");
        return splitted[splitted.length-1].length();
    }
}
