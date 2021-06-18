/*
* David Harmon
* 6-18-21
*
*this calculator is used for the purpose of allowing a user to enter in hardware
*calculations into this program for MPLAB and have the calculator calculate
*what registers should be used and the values to create the delay needed.
*
*
*/



public class MPLABInLineDelayCalculator {
/*
    public static void toTheNearest(double nearest, double input){
        int found = 0;
        for(int i = 0; i < input.length(); i++){
            if (input.charAt(i) == "."){
                found = -1;
            }
        }

        if (found == -1){
            System.out.println("The input is a decimal");
        }


    }
*/


     public static void main(String[] args){
         double test = 3.14159;
         String testString = Double.toString(test);
        //toTheNearest(4,9);

        System.out.println(testString.length());
        System.out.println(Double.toString(test).length());

        int i;
        for(i= 0; i < (Double.toString(test).length()); i++) {
            if(test.charAt(i) == "."){
                System.out.println("this number is not an integer ");
        } else {
            System.out.println("This number is an integer ");
        }
    }
}
}
