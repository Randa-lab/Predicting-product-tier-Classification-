import matplotlib.pyplot as plt

numeric=['price', 'first_zip_digit', 'first_registration_year', 'age', 'search_views', 'detail_views', 'stock_days', 'ctr']

data_num = df[numeric]

k = len(data_num.columns)
n = 3
m = (k - 1) // n + 1

fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))

for i, (name, col) in enumerate(data_num.iteritems()):
    r, c = i // n, i % n
    ax = axes[r, c]
    col.hist(ax=ax, color='red')
    ax2 = col.plot.kde(ax=ax, secondary_y=True, title=name, color='black')
    ax2.set_ylim(0)
fig.tight_layout();
