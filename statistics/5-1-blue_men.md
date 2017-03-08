[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>**The question:** In the BRFSS, the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women. In order to join Blue Man Group, you have to be male between 5’10” and 6’1”. What percentage of the U.S. male population is in this range?

```python
import scipy.stats
mu = 178
sigma = 7.7
# given mu and sigma (mean and std), give me a normal distribution dist
dist = scipy.stats.norm(loc=mu, scale=sigma)

def foot_to_cm(foot, inch):
    '''takes a measure in foot + inches and returns it in cm'''
    cm = foot*30.48
    cm += inch*2.54
    return cm

min_height = foot_to_cm(5,10)
max_height = foot_to_cm(6,1)

# norm.cdf gives you the percentage of vales smaller than the value specified in the argument

smaller_than_min = dist.cdf(min_height)
smaller_than_max = dist.cdf(max_height)
perc_right_height = smaller_than_max-smaller_than_min
print(perc_right_height)
```
>I have no clue why the effect size is mentioned in the "required exercises..."
