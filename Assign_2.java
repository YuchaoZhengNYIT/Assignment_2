// Run a class file in java 
  
// import java.io.*; 
  
class Assign_2 { 
    public static void main(String[] args) 
    { 
    	String message = args[0];
    	String input_2 = args[1];
    	String[] input_2s = input_2.split(",",2);
        String depth = input_2s[0].substring(1,input_2s[0].length());
        String rtimes = input_2s[1].substring(0,input_2s[0].length()-1);

        Integer depth_i = Integer.parseInt(depth);
        Integer rtimes_i = Integer.parseInt(rtimes);

        System.out.println("message is "+message); 
        System.out.println("depth is "+depth_i);
        System.out.println("rtimes is "+rtimes_i);

    } 
}