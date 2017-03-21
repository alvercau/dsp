[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>_Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval._ 
```python
def Estimate6(iters, n):
    lam=2
    means = []
    for _ in range(iters):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)
    return means

Ls = Estimate6(1000, 10)
cdf = thinkstats2.Cdf(Ls)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='estimate L',
                 ylabel='CDF')
print('Standard error', RMSE(Ls, 2))
print('Confidence interval', cdf.Percentile(5), cdf.Percentile(95))
```
> Standard error 0.837322141141  
> Confidence interval 1.26939447748 3.71806893081  
![sampling distribution of estimate L](https://github.com/alvercau/dsp/blob/master/statistics/sampling_distr.pdf)

>_Repeat the experiment with a few different values of n and make a plot of standard error versus n._  

```python
STEs=[]
ns=[]
for n in range(10,30):
    estimates = Estimate6(1000, n)
    STE= RMSE(estimates, 2)
    ns.append(n)
    STEs.append(STE)
thinkplot.Plot(ns, STEs)
thinkplot.Config(xlabel='number of values', ylabel='Standard errors')
``` 
![standard error versus n](https://github.com/alvercau/dsp/blob/master/statistics/standard_errors.pdf)
