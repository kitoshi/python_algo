

## Introduction

There are 6 problems involving recursion.

There is a separate test file for each problem.  If you find an error in the test file, please let me know.

You may run all test files with `python -m unittest` (or `python3`, depending on your seupt), or individual test files with lines such as `python -m unittest test_01_squashNested`.

Note that there will be additional tests for grading which I have not shared with you, although I have not deliberately left any tricks hidden.

## Grading

Each problem is worth 1 mark (that is, all 6 problems have equal weight).

Problems solved without recursion will be worth zero marks.

In general, expect for each problem to be graded either correct (1 mark) or incorrect (0 marks).  Expect exceptions only if I think the error is my fault.

## Solo work

Please remember that this assignment is solo work.  Do not share your work with others, nor use the work of other students, nor get help from others.

However, you may use what you can find on the internet, assuming that it was published before I handed out this assignment.  Remember that if you use more than a line or two from a source you found on the internet, too much citation (in comments or in a separate CREDITS.md file) is safer and better than too little.

## Submitting your work

I will release submission instructions soon, which will probably involve git.  I need to do some testing.  Stay tuned.  But I won't add problems or make the problems harder.


## Notes / Hints

### Problems 1 and 2

I don't know what to say to simplify these.  They are about recursively processing nested lists.

### Problem 3

Surprise, it's binary search.

You may slice, and personally I think this way is slightly easier.

Alternately, you can just use indices, which is overall probably harder, but it does avoid one tricky catch that happens with the slicing.

### Problem 4

This is a parsing problem.  In one way it's a bit harder than the one I did in class, and in another way it's a bit easier.

I supplied a bunch of the support code, to let you focus on the difficult part.

Note that, when you raise SyntaxErrors, my tests do not check what message you give, so I guess you could leave the message blank, but you might want to just write a half-decent message in there just for yourself.  If you haven't previously raised your own exceptions, there's an example in the provided stub code.

This is probably the problem with the longest code required.

### Problem 5

In this problem, you must find a combination of weights that adds up to a target.

One catch is that, in many cases, there might be more than one valid combination, but you must give a particular one of the combinations.  See the examples.

Here's a very straightforward hint: in my solution, there are two base cases (one success, one fail), and both are tested in the testing file.

Here is a more complicated hint, that I hope helps:  For each weight in the list of `weights`, there are two possible paths that could work out: either use the weight, or don't use it.  So that's two recursive calls!  (But there's no point in using a weight if it's too heavy to meet the target!)

Also, I think it's easier if you always let the better weights go first, so that as soon as you find a solution, it's automatically the correct one.  But you don't have to do it that way.

Fun fact, in terms of asymptotic complexit analysis, this problem has a very bad running time.  Don't let it bother you, we'll just run it for small inputs!

### Problem 6

This is a harder version of Problem 5.  What's harder is that the number of possible recursive calls is now variable.  You will not be able to hard-code the recursive calls, which is scary and weird.

Again, in terms of big-Oh running time, the solution to the problem is pretty bad.  Again, we'll just keep to running it for small inputs (say less than 10 weights).
