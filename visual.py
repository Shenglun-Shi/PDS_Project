import pylab as p
fig = p.figure()

ax = fig.add_subplot(1,1,1)
y = [314, 323, 332]
N = len(y)
ind = range(N)

ax.bar(ind, y, facecolor='#0000FF',
       align='center', ecolor='black')
ax.set_ylabel('Electoral Votes')
ax.set_title('Obama Results Across Models')
ax.set_xticks(ind)

group_labels = ['7 Factor', '5 Factor',
                'Actual']

ax.set_xticklabels(group_labels)

fig.autofmt_xdate()

p.show()
