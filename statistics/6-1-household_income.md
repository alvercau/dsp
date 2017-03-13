[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>**Question:** Compute the median, mean, skewness and Pearson's skewness of the sample created by ```InterpolateSample```. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?
```InterpolateSample``` _generates a pseudo-sample; that is, a sample of house hold incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale._

>**The first sample:** it is assumed that the upper bound of income is one million dollars. The highest category of income thus ranges from 250.000 to 1.000.000 dollars.

```python
import hinc
income_df = hinc.ReadData()
log_sample = InterpolateSample(income_df, log_upper=6.0)
sample = np.power(10, log_sample)
```
> Compute median, mean, skewness and Pearson's skewness of the sample:

```python
mean = Mean(sample)
median = Median(sample)
skewness = Skewness(sample)
ps = PearsonMedianSkewness(sample)
print(mean, median, skewness, ps)
```
> The mean (74278.7075312) is bigger than the median (51226.4544789), which indicates long right tail. Both skewness (4.94992024443) and ps (0.736125801914) are positive, which confirms positive skew. 

> In order to determine which percentage of the population earns less than the mean, we need to find the CDF of the mean:

```python
print(cdf.Prob(mean))
```
> 66% of the population has an income below the mean.


**The second sample:** let's assume that the upper bound is ten million dollars:

```python
log_sample = InterpolateSample(income_df, log_upper=7.0)
sample = np.power(10, log_sample)
mean = Mean(sample)
median = Median(sample)
skewness = Skewness(sample)
ps = PearsonMedianSkewness(sample)
print(mean, median, skewness, ps)
print(cdf.Prob(mean))
```

> Mean: 65308.9999054 
> Median: 51226.4544789 
> Skewness: 1.17955077982 
> Pearson's skewness: 0.810102449294
> percentage: 60.3%


**The third sample:** the upper bound is 100.000 dollars.

```python
log_sample = InterpolateSample(income_df, log_upper=5.0)
sample = np.power(10, log_sample)
mean = Mean(sample)
median = Median(sample)
skewness = Skewness(sample)
ps = PearsonMedianSkewness(sample)
print(mean, median, skewness, ps)
print(cdf.Prob(mean))
```

> Mean: 124267.397222 
> Median: 51226.4544789 
> Skewness: 11.6036902675 
> Pearson's skewness: 0.391564509277
> Percentage: 85.7%

> If the upper limit is lowered, the mean is lower, the median remains the same, the skewness is smaller and pearson's skewness is bigger. Percentage of people earning less than mean is smaller.
> If the upper limit is higher, the mean is higher, the median remains the same, the skewness is a lot bigger and pearson's skewness is smaller.  Percentage earning less than mean is bigger.
> This shows that mean is influenced by outliers, while median is robust. The fact that the sample skewness increased a lot when the upper limit was set to a higher number, indicates that it is sensitive to outliers. Pearson's skewness also varies, but less dramatically.
