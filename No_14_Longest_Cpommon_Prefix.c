/*
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/

char * longestCommonPrefix(char ** strs, int strsSize){
    if(strsSize == 0) return "";

    int min_length = INT_MAX;
    for(int i=0;i<strsSize;i++){
        if(strlen(strs[i])<min_length){
            min_length = strlen(strs[i]);
        }
    }

    char *prefix = (char *)malloc(sizeof(char)*(min_length+1));

    for(int i=0;i<min_length;i++){
        char c = strs[0][i];
        for(int j=1;j<strsSize;j++){
            if(strs[j][i] != c){
                prefix[i] = '\0';
                return (prefix);
            }
        }
        prefix[i] = c;
    }
    prefix[min_length] = '\0';
    return (prefix);    
}
