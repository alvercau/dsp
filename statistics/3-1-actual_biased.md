[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>**The question:** Plot the actual and biased distributions of the number of children in a household.

>**Code:**
```python
resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp['numkdhh'], label='Actual number of children in household')
biased = pmf.Copy(label='Observed number of kids')
for n, p in pmf.Items():
    biased.Mult(n, n)
biased.Normalize()
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel='number of kids', ylabel = 'PMF')
print (pmf.Mean())
print (biased.Mean())
```
> The plot of the distributions:
![distribution children in household](https://github.com/alvercau/dsp/blob/master/statistics/Chap3ex1.pdf)

>The actual mean is 1, while the biased mean is 2.4. The means differ considerably. 
