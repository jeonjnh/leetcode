/*
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
*/

bool isSubsequence(char * s, char * t){
    int slen = strlen(s);
    int tlen = strlen(t);

    if(slen == 0) {return true;}

    int sidx=0,tidx=0;

    while((sidx < slen) && (tidx < tlen)){

        if(s[sidx] == t[tidx]) {
            if(sidx == slen -1) {return true;}
            sidx++;
            tidx++;
        }
        else {tidx++;}
    }

    return false; 

}
