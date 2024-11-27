Finds a path (i.e. a sequence of connecting flights) between 2 cities A and B such that
  1. The first flight departs from A at a time >= `t1`
  2. The last flight arrives at B at a time <= `t2`
  3. If flight `g` is taken after flight `f`, then `g` must depart at a time >= `f.arrival_time + 20`
  4. The path is optimal with respect to one of the following optimizations:
     1. it is the cheapest path satisfying 1, 2 and 3
     2. it uses the fewest number of flights among all paths satisfying 1, 2 and 3, and among all fewest flight paths it either
        1. arrives the earliest, or
        2. is the cheapest
Refer [problem statement](https://github.com/ayaandroid/COL106-assignments/blob/main/A5/COL106_A5.pdf) for more details.
