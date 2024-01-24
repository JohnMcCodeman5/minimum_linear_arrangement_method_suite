import pandas as pd
from matplotlib import pyplot as plt

dfb = pd.read_csv('comparison_tables/bests.csv')
columns1 = ['Dim','brute_force','brute_force_time','greedy','greedy_time','local_search','local_search_time']
columns2 = ['Dim','local_search_perm','local_search_perm_time','sim_annealing','sim_annealing_time','vns','vns_time']
columns3 = ['Dim','genetic_alg','genetic_alg_time','tabu','tabu_time','taloc_combo','taloc_combo_time']
dfb1 = dfb[columns1]
dfb2 = dfb[columns2]
dfb3 = dfb[columns3]


#adjust the figure size based on the number of columns
fig, ax = plt.subplots(figsize=(10, 4)) 
#hide axes, no need for them here
ax.axis('off')
#use pandas plotting.table for better control
table = pd.plotting.table(ax, dfb1, loc='center', colWidths=[0.2]*len(dfb1.columns), cellLoc='center')
#adjust font size
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
start_index = 11
for i in range(start_index, len(dfb1) + 1):
    for j in range(len(dfb1.columns)):
        table[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/best_table1.png', bbox_inches='tight', pad_inches=0.1)


table = pd.plotting.table(ax, dfb2, loc='center', colWidths=[0.2]*len(dfb2.columns), cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
for i in range(start_index, len(dfb2) + 1):
    for j in range(len(dfb2.columns)):
        table[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/best_table2.png', bbox_inches='tight', pad_inches=0.1)

table = pd.plotting.table(ax, dfb3, loc='center', colWidths=[0.2]*len(dfb3.columns), cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
for i in range(start_index, len(dfb3) + 1):
    for j in range(len(dfb3.columns)):
        table[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/best_table3.png', bbox_inches='tight', pad_inches=0.1)

#-------------------------------------------------averages-------------------------------------------------------#
dfa = pd.read_csv('comparison_tables/averages.csv')
dfa1 = dfa[columns1]
dfa2 = dfa[columns2]
dfa3 = dfa[columns3]

fig1, ax1 = plt.subplots(figsize=(10, 4)) 
ax1.axis('off')

table1 = pd.plotting.table(ax1, dfa1, loc='center', colWidths=[0.2]*len(dfa1.columns), cellLoc='center')
table1.auto_set_font_size(False)
table1.set_fontsize(10)
table1.scale(1, 1.5)
for i in range(start_index, len(dfa1) + 1):
    for j in range(len(dfa1.columns)):
        table1[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/avg_table1.png', bbox_inches='tight', pad_inches=0.1)

table1 = pd.plotting.table(ax1, dfa2, loc='center', colWidths=[0.2]*len(dfa2.columns), cellLoc='center')
table1.auto_set_font_size(False)
table1.set_fontsize(10)
table1.scale(1, 1.5)
for i in range(start_index, len(dfa2) + 1):
    for j in range(len(dfa2.columns)):
        table1[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/avg_table2.png', bbox_inches='tight', pad_inches=0.1)

table1 = pd.plotting.table(ax1, dfa3, loc='center', colWidths=[0.2]*len(dfa3.columns), cellLoc='center')
table1.auto_set_font_size(False)
table1.set_fontsize(10)
table1.scale(1, 1.5)
for i in range(start_index, len(dfa3) + 1):
    for j in range(len(dfa3.columns)):
        table1[(i, j)].set_facecolor('yellow')
plt.savefig('table_images/avg_table3.png', bbox_inches='tight', pad_inches=0.1)