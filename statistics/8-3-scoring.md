[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

>In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.
Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.  

> Given code:  
```python
def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.

    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1

    # estimated goal-scoring rate is the actual number of goals scored
    L = goals
    return L
```
>Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE. Is this way of making an estimate biased?
> My code:  

```python
def Manygames(n, lam):
    'n is the number of games, lam is the rate of goals per game'
    Ls=[]
    for _ in range(n):
        L = SimulateGame(lam)
        Ls.append(L)
    print('Mean error', MeanError(Ls, lam))
    print('RMSE', RMSE(Ls, lam))
    
Manygames(1000000, 2)
```
> Mean error -0.001905  
> RMSE 1.41211083134  
> **Answer:** It's not biased: the higher the number of games, the closer ME gets to zero.







---