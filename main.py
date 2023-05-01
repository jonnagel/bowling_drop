""" More info in background.md 

                            BROKE   UNBROKEN
hardness >  dropped floor    F          T
hardness <= dropped floor    T          F
balls = 2
floors = 100
"""
import numpy as np
import seaborn as sns
from init import BinarySplit, Ball, binary_splitting, gradient_ascent
tests_per_type = 1_000
step_min = 4
step_max = 20 
# run many tests this will take a minute :) 
results = []
for x in range(tests_per_type):
    results.append(pd.DataFrame(binary_splitting()))
for x in range(tests_per_type):
    for n in range(step_min, step_max+1):
        results.append(pd.DataFrame(gradient_ascent(steps=n)))
results_df = pd.concat(results, ignore_index=True)
# What is the average number of floors tested per method? 
plot_df = results_df.groupby(['test_type','steps']).count_floors_checked.mean().reset_index()
plot_df = plot_df.assign(count_floors_checked_rank=plot_df.count_floors_checked.rank().astype(int))
# plot_df.query("count_floors_checked_rank <= 3")
#          test_type  steps  count_floors_checked  count_floors_checked_rank
# 7  gradient_ascent     10         12.3679791006                          1
# 8  gradient_ascent     11         12.6125350965                          2
# 9  gradient_ascent     12         12.6276162001                          3
# 
# stepping by 10 yields the minimum number of checks
#
for_plot = results_df[['test_type', 'count_floors_checked', 'steps']]
for_plot.columns = ['Test Type', 'Floors Checked', 'Steps']
p = sns.boxplot(data=for_plot.query('Steps > 0'), y='Floors Checked', x='Steps',
            notch=True, medianprops={'color': 'coral'}, showcaps=False,
            dodge=True, orient='v', width=0.40).set(title='plot_df')
fig = p[0].get_figure()
fig.savefig("plot.png")
