/*
 * @lc app=leetcode.cn id=28 lang=c
 *
 * [28] 实现 strStr()
 */

// @lc code=start


int strStr(char * haystack, char * needle){
    int i = 0;
    while(haystack[i] != '\0'){
        int j = 0;
        while(needle[j] != '\0'){
            if(haystack[i] != needle[j]){
                i++;
                break;
            }   
            j++;
        }
        return i - j + 1;
    }
    return -1;
}


// @lc code=end

