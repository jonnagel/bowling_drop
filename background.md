# The following text is from [source](https://blogs.oregonstate.edu/rudb2/2022/02/22/two-bowling-balls/)

Two Bowling Balls
=================

Introduction
------------

	I started applying for internships in December of 2020. I submitted an
	application to one company before Christmas and planned on applying to more
	companies early in 2021. I was surprised with how quickly the first company got
	back to me and they wanted to set up an interview before Christmas. I was not
	expecting to hear back from them so quickly and was not fully prepared for
	technical interviews, but I thought it would be a good learning opportunity and
	the worst that could happen was I get a rejection and some experience
	interviewing.

	The first question I was asked was a fun problem. I wasn’t able to find the
	best solution during the interview, but found a good solution after the
	interview. In this blog post I’ll walk through the problem and my attempts at
	solving it.

The Problem
-----------

	You are given two identical bowling balls both with a hardness value. The
	hardness is an integer between 1 and 100. Your task is to find this hardness
	value by dropping the bowling balls from various levels of a 100 story
	building. If the hardness value is h and you drop the bowling ball from the hth
	floor (or higher) the bowling ball will break. For example, if the hardness
	value of the two bowling balls is 51 and you drop the bowling ball from the
	50th floor or below, the bowling balls will not break. If you drop the bowling
	balls from floors 51-100, they will break. Your task is to find the strategy
	that will yield the hardness value of the bowling balls in as few steps as
	possible.

My Initial Problem Solving Attempts
-----------------------------------

	I started off with a brute force approach. You could start at floor one and
	drop one of the bowling balls. If the bowling ball breaks, then you know the
	hardness value is one. If the bowling ball does not break, then go up one floor
	and drop one of the bowling balls. Continue this process until the bowling ball
	breaks. This is not a great solution, and in the worst case scenario (h = 100)
	it would take 100 drops to find the hardness of the bowling ball. This solution
	also does not leverage the fact that you have two bowling balls.

	Binary search reminded me of a better (but still not optimal) solution. If we
	dropped the bowling ball from the 50th floor, we could reduce the worst case
	scenario to 50 drops. If the first bowling ball breaks when dropped from the
	50th floor, we would need to test the second bowling ball by dropping the it
	from floors 1-49 (50 drops total including the drop from the 50th floor). If
	the first bowling ball did not break when dropped from the 50th floor we would
	need to test the second bowling ball by dropping it from floors 51-100 (50
	drops total including the drop from the 50th floor).

	This is as far as I got. I tried solving the problem more on my own after the
	fact but I didn’t get much further. I found
	a [blog](http://20bits.com/article/interview-questions-two-bowling-balls) with
	a good solution that I will walk through below.

A Better Solution
-----------------

	Let the number of floors in the building be N. We know that picking a floor
	from which to drop the first bowling ball (like the 50th floor for example)
	will reduce the number of drops needed. We can more arbitrarily define
	a strategy to test for the hardness of the bowling balls. First we define
	a step size, S, which is the number of floors from which to drop the first
	bowling ball. So initially, we drop the first bowling ball from the Sth floor.
	If it does not break, we go up another S floors until it breaks. Once the first
	bowling ball breaks, we drop the second bowling ball from floor from floor
	(k-1)S + 1 to floor kS – 1. Where k is the number of steps we have taken, so
	(k-1)S + 1 is the floor above the last step taken, and kS – 1 is the floor
	below the current step taken. In this strategy, the worst case scenario occurs
	when the hardness of the bowling balls is equal to N – 1. When this occurs, the
	number of drops as a function of the step size, S, can be defined as f(S) = N/S
	+ S – 1. We can find minimum value of this function by setting the first
	derivative equal to zero and solving for S. df(S)/dS = 1 – N/S^2 = 0

	Solving the above equation for S yields S = sqrt(N). So for a building with 100
	floors, the optimum step size using this strategy is 10 and the worst case
	scenario where the hardness is equal to 99 can be solved in 19 drops.

Lessons Learned
---------------

	This is not they type of interview question that I was expecting. It does not
	involve linked lists, or sorting, or finding O(n) runtimes. In fact, it does
	not rely on any of the math learned in the OSU post-bacc program. All you need
	to solve the problem is knowledge and ideas learned in calc 1 (easier said than
	done when you haven’t used calculus in almost 10 years). I did not do well on
	this interview question, but the interviewer helped step me through the
	problems when I got stuck and I gained valuable experience from the process.
