/*
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

*/

void reverseString(char* s, int start, int end){

    char temp;

    while(start < end) {
        temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;

    }

}

char * reverseWords(char * s){

    int start = 0;
    int end = strlen(s) - 1;
    int i = 0;

    while(s[i] != 0){

        if(s[i] == ' '){
            reverseString(s,start,i-1);
            start = i+1;
        }

        i++;
    }

    reverseString(s,start,end);

    return s;

}
