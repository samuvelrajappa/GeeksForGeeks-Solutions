<h2><a href="https://www.geeksforgeeks.org/problems/geek-and-his-binary-strings1951/1">Count Prefix-Balanced Binary Strings</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an integer <strong>n</strong>, count the number of binary strings of length <strong>2 × n</strong> that contain exactly <strong>n</strong> ones and<strong> n </strong>zeros, such that in every prefix of the string, the number of ones is greater than or equal to the number of zeros.</span></p>
<p><span style="font-size: 18px;">A prefix is any substring that starts from the first character of the string and ends at any position. </span><span style="font-size: 18px;">Return the count modulo 10^9 + 7.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: n = 2
<strong>Output:</strong> 2</span>
<span style="font-size: 18px;"><strong>Explanation</strong>: The two valid strings are "1100" and "1010".
For "1100", every prefix has at least as many ones as zeros:
"1" -&gt; 1 one, 0 zeros
"11" -&gt; 2 ones, 0 zeros
"110" -&gt; 2 ones, 1 zero
"1100" -&gt; 2 ones, 2 zeros
Similarly, "1010" also satisfies the condition for every prefix. Therefore, the answer is 2.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: n = 3
<strong>Output:</strong> 5</span>
<span style="font-size: 18px;"><strong>Explanation</strong>: The five valid strings are "111000", "110100", "110010", "101100", and "101010".
For example, consider "110100":
"1" -&gt; 1 one, 0 zeros
"11" -&gt; 2 ones, 0 zeros
"110" -&gt; 2 ones, 1 zero
"1101" -&gt; 3 ones, 1 zero
"11010" -&gt; 3 ones, 2 zeros
"110100" -&gt; 3 ones, 3 zeros
The condition is satisfied for every prefix. All five listed strings satisfy the same condition, so the answer is 5.</span></pre></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;