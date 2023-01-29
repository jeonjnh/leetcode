/*
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
*/

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

int maxArea(int* height, int heightSize){

    int start = 0;
    int end = heightSize - 1;
    int step = heightSize - 1;
    int max_area = 0;
    int curr_area;

    while(start < end) {
        curr_area = (MIN(height[end],height[start])) * step;
        if(max_area < curr_area) {
            max_area = curr_area;
        }

        if(height[start] < height[end]) {
            start++;
        }
        else {
            end--;
        }
        step--;
    }

    return max_area;

}
