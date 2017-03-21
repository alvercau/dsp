[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>Using data from the NSFG, make a scatter plot of birth weight versus mother's age.  

```python
import first

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

weight=thinkstats2.Jitter(live.totalwgt_lb, 0.5)
thinkplot.Scatter(live.agepreg, weight, alpha=0.1, s=10)
thinkplot.Config(xlabel="mother's age", ylabel='birth weight', legend=False)
```
![scatter plot](https://github.com/alvercau/dsp/blob/master/statistics/scatterplot.pdf)

> Plot percentiles of birth weight versus mother's age.  

```python
#Plot percentiles of birth weight versus mother’s age
bins = np.arange(10, 48, 3)
indices = np.digitize(live.agepreg,bins)
groups = live.groupby(indices)

cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i,group in groups]
ages = [group.agepreg.mean() for i,group in groups]
for percent in [25, 50, 75]:
    weight_percentiles = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weight_percentiles, label=label)
thinkplot.Config(xlabel="mother's age", ylabel='birth weight (pounds)', legend=True)
```
![percentiles](https://github.com/alvercau/dsp/blob/master/statistics/percentiles.pdf)

> Compute Pearson's and Spearman's correlations. How would you characterize the relationship between these variables?  

```python
print("Pearson's corr", Corr(live.totalwgt_lb, live.agepreg))
print("Spearman's corr", SpearmanCorr(live.totalwgt_lb, live.agepreg))
```

> Pearson's corr 0.0688339703541  
> Spearman's corr 0.0946100410966  
> **Answer:** both correlation coefficients indicte that there is a small, but positive correlation. The difference between the two corrcoef indicate that there are some outliers and that the relation is not entirely linear.