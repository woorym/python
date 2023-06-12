import java.util.Stack;
import java.util.HashMap;
import java.util.Scanner;


class Main {

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        Stack<Character> st = new Stack<>();

        HashMap<Character, Integer> hm = new HashMap<>();

        hm.put('+', 1);
        hm.put('-', 1);
        hm.put('*', 2);
        hm.put('/', 2);
        hm.put('^', 3);
        hm.put('(', 0);
        // System.out.println(hm.get('*')instanceof Integer);
        String test = sc.nextLine();
        

        for (int i = 0; i < test.length(); i++) {
            
            char append = test.charAt(i);
            
            switch(test.charAt(i)) {

                case ')':
                    while (!st.empty() && !st.peek().equals('(')) {
                        sb.append(st.pop());
                    }
                    st.pop();
                    break;
                case '+':
                    while (!st.isEmpty() && hm.get(st.peek()) >= hm.get(append)) {
                        sb.append(st.pop());
                    }
                    st.push(append);
                    break;
                    // if (st.isEmpty()) {
                        // st.push(append);
                    // }
                    // else {
                        // int check = st.size();
                        // for (int k = 0; k < check; k++) {
                            // if (hm.get(test.charAt(i)) > hm.get(st.peek())) {
                                // System.out.println(3);
                                // st.push(append);
                                // break;
                            // } else {
                                // if (st.peek().equals('(')) {
                                    // st.push(append);
                                    // break;
                                // }
                                // sb.append(st.pop());
                                // 
                            // }
                        // } 
                        // st.push(append);
                    // }
                    // break;
                case '-':
                    while (!st.isEmpty() && hm.get(st.peek()) >= hm.get(append)) {
                        sb.append(st.pop());
                    }
                    st.push(append);
                    break;
                    // if (st.empty()) {
                        // st.push(append);
                    // }
                    // else {
                        // int check = st.size();
                        // for (int k = 0; k < check; k++) {
                            // if (hm.get(test.charAt(i)) > hm.get(st.peek())) {
                                // System.out.println(3);
                                // st.push(append);
                                // break;
                            // } else {
                                // if (st.peek().equals('(')) {
                                    // st.push(append);
                                    // break;
                                // }   
                                // sb.append(st.pop());
                                // 
                            // }
                        // } 
                        // st.push(append);
                    // }
                    // break;
                case '*':
                    while (!st.isEmpty() && hm.get(st.peek()) >= hm.get(append)) {
                        sb.append(st.pop());
                    }
                    st.push(append);
                    break;
                    // if (st.empty()) {
                        // st.push(append);
                    // }
                    // else {
                        // int check = st.size();
                        // for (int k = 0; k < check; k++) {
                            // if (hm.get(test.charAt(i)) > hm.get(st.peek())) {
                                // System.out.println(3);
                                // st.push(append);
                                // break;
                            // } else {
                                // if (st.peek().equals('(')) {
                                    // st.push(append);
                                    // break;
                                // } 
                                // sb.append(st.pop());
                                // 
                            // }
                        // } 
                        // st.push(append);
                    // }
                    // break;
                case '/':
                    while (!st.isEmpty() && hm.get(st.peek()) >= hm.get(append)) {
                        sb.append(st.pop());
                    }
                    st.push(append);
                    break;
                    // if (st.empty()) {
                        // st.push(append);
                    // }
                    // else {
                        // int check = st.size();
                        // for (int k = 0; k < check; k++) {
                            // if (hm.get(test.charAt(i)) > hm.get(st.peek())) {
                                // System.out.println(3);
                                // st.push(append);
                                // break;
                            // } else {
                                // if (st.peek().equals('(')) {
                                    // st.push(append);
                                    // break;
                                // }
                                // sb.append(st.pop());
                                // 
                            // }
                        // } 
                        // st.push(append);
                    // }
                    // break;
                case '(':
                        st.push(append);

                    break;
                
                default:

                    sb.append(append);
                    break;
                }
            }

        while (!st.empty()) {
            sb.append(st.pop());
        }

        System.out.println(sb);
    }
}

