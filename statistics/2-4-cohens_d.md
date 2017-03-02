[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>**The Question:** Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference inpregnancy length?
>
>**How I solved this question:** I calculated Cohen's d for both the total wieght and the pregnancy lengths using the following code:

```python
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
print CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print CohenEffectSize(firsts.prglngth, others.prglngth)
```
>First, I selected only the live born babies from the data (outcome 1). then, I subdivided the live born babies into first childs (birthord 1) and other children (birthord not 1). Then I calculated the necessary Cohen's ds with the function CohenEffectSize that was defined in the notebook:

```python
def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d
```

>**The answer:** Cohen's d for the total weight (in pounds) of first vs. other babies is *-0.09*. This means that other babies are slightly heavier than first babies, but the effect size is small, and can thus be ignored. Cohen's d for the length of the pregnancy for first vs. other babies is *0.03*. The length of the pregnancy for first babies is thus sligtly longer than for other babies, but the effect size is very small, and can thus be ignored. In conclusion, there is no significant difference between first borns and other children when it comes to pregnancy length or weight.
