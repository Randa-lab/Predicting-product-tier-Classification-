import matplotlib.pyplot as plt
import seaborn as sns

numeric=['price', 'first_zip_digit', 'first_registration_year', 'age', 'search_views', 'detail_views', 'stock_days', 'ctr']

features = numeric

plt.figure(figsize=(18, 4))
for i in range(0, len(features)):
    plt.subplot(1, 8, i+1)
    sns.boxplot(y=df[features[i]], color='purple',orient='v')
    plt.tight_layout();
