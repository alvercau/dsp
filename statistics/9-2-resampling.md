[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>_In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
>An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.
>Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation. Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?_

```python
class DiffMeansResample(DiffMeansPermute):
    
    def Runmodel(self):
        resampled = thinkstats2.Resample(self.pool)
        data = resampled[:self.n], resampled[self.n:]
        return data

data = firsts.prglngth.values, others.prglngth.values
ht1 = DiffMeansPermute(data)
p1 = ht1.PValue(iters=10000)
print('\ndiff means permute preglength')
print('p-value =', p1)
print('actual =', ht1.actual)
print('ts max =', ht1.MaxTestStat())

ht2 = DiffMeansResample(data)
p2 = ht2.PValue(iters=10000)
print('\ndiff means resample preglength')
print('p-value =', p2)
print('actual =', ht2.actual)
print('ts max =', ht2.MaxTestStat())

data = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values
ht1 = DiffMeansPermute(data)
p1 = ht1.PValue(iters=10000)
print('\ndiff means permute birthweight')
print('p-value =', p1)
print('actual =', ht1.actual)
print('ts max =', ht1.MaxTestStat())

ht2 = DiffMeansResample(data)
p2 = ht2.PValue(iters=10000)
print('\ndiff means resample birthweight')
print('p-value =', p2)
print('actual =', ht2.actual)
print('ts max =', ht2.MaxTestStat())
```

>**The answer:** there is not much of a difference between the permutated model and the resampled model:
>diff means permute preglength
>p-value = 0.1658
>actual = 0.0780372667775
>ts max = 0.221853308036

>diff means resample preglength
>p-value = 0.1718
>actual = 0.0780372667775
>ts max = 0.226888063035

>diff means permute birthweight
>p-value = 0.0
>actual = 0.124761184535
>ts max = 0.115926801825

>diff means resample birthweight
>p-value = 0.0
>actual = 0.124761184535
>ts max = 0.121631763701


