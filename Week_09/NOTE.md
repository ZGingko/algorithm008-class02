# 学习笔记
## 知识点总结
### 第19课-高级动态规划
1. 动态规划：递归、分治  
多种情况的动态规划的状态转移方程
进阶版动态规划  
递归、分治、回溯、动态规划  
递归 - 函数自己调用自己
    ```python
    def recur(int level, int param):
        // terminator
        if (level > MAX_LEVEL):
            // process result
            return;

        // process current logic
        process(level, param)

        // drill down
        recur(level: level + 1, newParam);

        // restore current status
    ```
2. 分而治之 Divide & Conquer
分治代码模板
    ```python
    def divide_conquer(problem, param1, param2, ...):
        # recursion terminator
        if problem is None:
            print_result
            return
        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)
        # conquer subproblems
        subresult1 = self.divide_conquer(subproblems[0], p1, ...)
        subresult2 = self.divide_conquer(subproblems[1], p1, ...)
        subresult3 = self.divide_conquer(subproblems[2], p1, ...)
        ...
        # process and generate the final result
        result = process_result(subresult1, subresult2, subresult3, ...)
        # revert the current level states
    ```
感触  
人肉递归低效、很累  
找到最近最简方法，将其拆解成可重复解决的问题  
数学归纳法思维  
本质:寻找重复性 —> 计算机指令集

3. 动态规划 Dynamic Programming
    1. “Simplifying a complicated problem by breaking it down into simpler sub-problems”(in a recursive manner)
    2. Divide & Conquer + Optimal substructure 分治 + 最优子结构  
顺推形式: 动态递推
DP 顺推模板
    ```python
    def DP():
        dp = [] # 二维情况
        for i in range(M):
            for j in range(N):
                dp[i][j] = _Function(dp[i’][j’]...)
        return dp[M][N];
    ```
关键点  
* 动态规划 和 递归或者分治 没有根本上的区别(关键看有无最优的子结构) 拥有共性:找到重复子问题
* 差异性:最优子结构、中途可以淘汰次优解

常见的 DP 题目和状态方程
爬楼梯
不同路径
打家劫舍
最小路径和
股票买卖  
* https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

* https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/

高阶的 DP 问题
复杂度来源
* 状态拥有更多维度(二维、三维、或者更多、甚至需要压缩)
* 状态方程更加复杂
* 本质:内功、逻辑思维、数学

爬楼梯问题改进  
* https://leetcode-cn.com/problems/min-cost-climbing-stairs/

1、2、3  
x1, x2, …, xm 步 前后不能走相同的步伐  

编辑距离  
* https://leetcode-cn.com/problems/edit-distance/

如果 word1[i] 与 word2[j] 相同，显然 dp=dp[i-1][j-1]  
如果 word1[i] 与 word2[j] 不同，那么 dp[i][j] 可以通过  
  1.  在 dp[i-1][j-1] 的基础上做 replace 操作达到目的
  2.  在 dp[i-1][j] 的基础上做 insert 操作达到目的
  3.  在 dp[i][j-1] 的基础上做 delete 操作达到目的  
取三者最小情况即可


### 第20课-字符串
字符串基础知识
字符串
Java
    ``` 
    String x = "abbc";
    string immutable:

* https://lemire.me/blog/2017/07/07/are-your-strings-immutable/

遍历字符串
```java
    String x = "abbc";
    for (int i = 0; i < x.size(); i++) {
        char ch = x.charAt(i); 
    }
    for ch in x.toCharArray() {
        System.out.println(ch); 
    }
```

字符串比较  
```java
    String x = "abb"; 
    String y = "abb";
    x == y --> false
    x.equals(y) --> true 
    x.equalsIgnoreCase(y) --> true
```
    
字符串相关算法  
基础问题  
* https://leetcode-cn.com/problems/to-lower-case/

* https://leetcode-cn.com/problems/length-of-last-word/

* https://leetcode-cn.com/problems/jewels-and-stones/

* https://leetcode-cn.com/problems/first-unique-character-in-a-string/

* https://leetcode-cn.com/problems/string-to-integer-atoi/

Atoi
```java
    public int myAtoi(String str) {
        int index = 0, sign = 1, total = 0; // 1. Empty string
        if (str.length() == 0)
            return 0;
        // 2. Remove Spaces
        while (str.charAt(index) == ' ' && index < str.length())
            index++;
        // 3. Handle signs
        if (str.charAt(index) == '+' || str.charAt(index) == '-') {
            sign = str.charAt(index) == '+' ? 1 : -1;
            index++;
        }
        // 4. Convert number and avoid overflow
        while (index < str.length()) {
            int digit = str.charAt(index) - '0';
            if (digit < 0 || digit > 9)
                break;
            // check if total will be overflow after 10 times and add digit
            if (Integer.MAX_VALUE / 10 < total || Integer.MAX_VALUE / 10 == total && Integer.MAX_VALUE % 10 < digit)
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            total = 10 * total + digit;
            index++;
        }
        return total * sign;
    }
```

字符串操作问题  
* https://leetcode-cn.com/problems/longest-common-prefix/description/
* https://leetcode-cn.com/problems/reverse-string https://leetcode-cn.com/problems/reverse-string-ii/
* https://leetcode-cn.com/problems/reverse-words-in-a-string/ https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
* https://leetcode-cn.com/problems/reverse-only-letters/  

Anagram异位词问题  
* https://leetcode-cn.com/problems/valid-anagram/
* https://leetcode-cn.com/problems/group-anagrams/
* https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/  
Palindrome 回文串问题  
* https://leetcode-cn.com/problems/valid-palindrome/
* https://leetcode-cn.com/problems/valid-palindrome-ii/
* https://leetcode-cn.com/problems/longest-palindromic-substring/  
  
高级字符串算法  
最长子序列、子串
Longest common sequence(最长公共子序列)  
* https://leetcode-cn.com/problems/longest-common-subsequence/

最长回文子串  
* https://leetcode-cn.com/problems/longest-palindromic-substring/

暴力 O(n^3)  
中间向两边扩张法 O(n^2)
动态规划 首先定义 P(i, j):  
P(i, j) = true s[i, j] 是回文串   
P(i, j) = false s[i, j] 不是a回文串  
接下来 P(i, j) = (P(i+1, j-1) && S[i] == S[j])  

字符串 + 递归 or DP  
* https://leetcode-cn.com/problems/regular-expression-matching/

重点:

* https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/

暴力递归
动态规划 dp 代表 T 前 i 字符串可以由 s 前 j 字符串组成最多个数。 所以动态方程:   
当 S[j] == T[i], dp[i][j] = dp[i-1][j-1] + dp[i][j-1]  
当 S[j] != T[i], dp[i][j] = dp[i][j-1]  

* https://leetcode-cn.com/problems/wildcard-matching/

* https://leetcode-cn.com/problems/distinct-subsequences/

字符串匹配算法  
暴力法(brute force) - O(mn)  
Rabin-Karp 算法  
KMP 算法  
课后了解: Boyer-Moore 算法:
* https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html  
 
Sunday 算法:
* https://blog.csdn.net/u012505432/article/details/52210975

暴力法
* https://shimo.im/docs/dQDxQW8yXPXxh3Hg/read

    ```java
    public int strStr(String txt, String pat) {
        int M = txt.length();
        int N = pat.length();

        for (int i = 0; i <= M - N; i++) {
            int j;
            for (j = 0; j < N; j++) {
                if (txt.charAt(i + j) != pat.charAt(j))
                    break;
            }
            if (j == N) {
                return i;
            }
            // 更加聪明？
            // 1. 预先判断 hash(txt.substring(i, M)) == hash(pat) - Rabin-Karp
            // 2. KMP
        }
        return -1;
    }
    ```
Rabin-Karp 算法  
在朴素算法中，我们需要挨个比较所有字符，才知道目标字符串中是否包含 子串。那么， 是否有别的方法可以用来判断目标字符串是否包含子串呢?

答案是肯定的，确实存在一种更快的方法。为了避免挨个字符对目标字符串 和子串进行比较， 我们可以尝试一次性判断两者是否相等。因此，我们需 要一个好的哈希函数(hash function)。 通过哈希函数，我们可以算出子 串的哈希值，然后将它和目标字符串中的子串的哈希值进行比较。 这个新 方法在速度上比暴力法有显著提升。 Rabin-Karp 算法的思想:

假设子串的长度为 M (pat)，目标字符串的长度为 N (txt)
计算子串的 hash 值 hash_pat
计算目标字符串txt中每个长度为 M 的子串的 hash 值(共需要计算 N-M+1 次)
比较 hash 值:如果 hash 值不同，字符串必然不匹配; 如果 hash 值相同， 还需要使用朴素算法再次判断
* https://shimo.im/docs/KXDdkT99TVtXvTXP/read  

    ```java
    public final static int D = 256;
    public final static int Q = 9997;
    static int RabinKarpSerach(String txt, String pat) {
        int M = pat.length();
        int N = txt.length();
        int i, j;
        int patHash = 0, txtHash = 0;

        for (i = 0; i < M; i++) {
            patHash = (D * patHash + pat.charAt(i)) % Q;
            txtHash = (D * txtHash + txt.charAt(i)) % Q;
        }

        int highestPow = 1;  // pow(256, M-1)
        for (i = 0; i < M - 1; i++) 
            highestPow = (highestPow * D) % Q;

        for (i = 0; i <= N - M; i++) { // 枚举起点
            if (patHash == txtHash) {
                for (j = 0; j < M; j++) {
                    if (txt.charAt(i + j) != pat.charAt(j))
                        break;
                }
                if (j == M)
                    return i;
            }
            if (i < N - M) {
                txtHash = (D * (txtHash - txt.charAt(i) * highestPow) + txt.charAt(i + M)) % Q;
                if (txtHash < 0)
                    txtHash += Q;
            }
        }
        return -1;
    }
    ```
KMP 算法  
KMP算法(Knuth-Morris-Pratt)的思想就是，当子串与目标字符串不匹配时， 其实你已经知道了前面已经匹配成功那 一部分的字符(包括子串与目标字符 串)。以阮一峰的文章为例，当空格与 D 不匹配时，你其实 知道前面六个字符是 “ABCDAB”。KMP 算法的想法是，设法利用这个已知信息，不要把“搜索位 置” 移回已经比较过的位置，继续把它向后移，这样就提高了效率。  
* https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171

* http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
