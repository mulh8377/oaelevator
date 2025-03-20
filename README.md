# oaelevator
1-d traversal for an elevator implemented in python

# Installation.

You can clone this repository and use pip to build. If you are using uv, a simple
`uv install` should also work!

# Follow-on Steps.

1. Setup the CI/CD environment. Use Jenkins, Gitlab, etc. Many of the steps you need to make the pipeline handle formatting, static code analysis, and linting are listed as dependencies for oaelevator. I would also recommend setting up tox to have testing for various python versions.
2. Test Coverage & generating developer documentation would be nice, but may be overkill for a library this small.
3. Publish this to a public or private pypi for easy integration into other projects.

# Some Assumptions I Made & Some Improvements.
The callable doesn't check for variance of type in v_floors; it assumes a vector of ints. I handled the case for duplicate floors being
present in the dataset, since a customer spamming a floor seems probable. There is an optimization I can make when calculating the total distance, but for readability and the likelihood that N is pretty small, I went with the more readable option.

## Follow-up on the above point.
I went ahead and did the optimization & pushed up a PR. Here are the results from my benchmarks:

```
optimization, large_n, small_n
None,               0.00019413088916000562, 4.949173039931338e-06
Reduced Iterations, 5.467006386999856e-05, 2.0684644000721166e-06
```

I assumed the run-time cost would be dominated by timsort -- but pointless iterations will incur a significant impact on performance.