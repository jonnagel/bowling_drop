# Introduction
Recently during an interview I was asked how I would approach a problem. At face value the question could be seen as a binary search optimization problem but the intent was to determine how I would interact with questioner.

The question as phrased: "Given 2 bowling balls that need drop hardness testing, efficiently determine their breaking floor"
* When a ball is dropped at or above breaking floor it will break.
* There are only 2 balls.
* Minimise test drops.

The answer to the basic question of how to check with the fewest steps and limited to 2 balls is 10.

TL;DR Check every 10 floors until a break

In English - Start at the tenth floor going up by 10 floors for each unbroken ball, leaving one ball in reserve yields an average of 12.36 checks.

![](plot.png?raw=True)

## The background can be found in [here](background.md)

Note: The problem I was given is slightly different than the one described in background.md
