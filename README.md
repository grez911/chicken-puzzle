# chicken-puzzle

> In a barn, 100 chicks sit peacefully in a circle. Suddenly, each chick randomly pecks the chick immediately to its left or right. What is the expected number of unpecked chicks?

When I first heard this problem I thought this way: "The maximum number of pecked chickens is 100 (in case each chicken pecks his left neighbour) and the minimum is 50 (if they pecks each other in pairs). So the average number of pecked chickens is in the middle -- 75, and 25 unpecked chikens is expected".

But let's prove it. How? By running 100000 rounds of simulation, of course!

```
you@localhost:/tmp$ git clone https://github.com/grez911/chicken-puzzle.git
you@localhost:/tmp$ cd chicken-puzzle/   
you@localhost:/tmp/chicken-puzzle$ python3 main.py 
Number of rounds: 100000
Average of unpecked: 25.00436
```

So results are really expected.
