### Permutation feature importance overcomes the limitations of impurity-based feature importance: 
### it has no bias towards high-cardinality features and can be computed on a hold-out test set.

from sklearn.inspection import permutation_importance
import pandas as pd
import matplotlib.pyplot as plt

# Balanced Random forest tuned model
# Permutation feature importance on train dataset

features=['price', 'first_zip_digit', 'first_registration_year', 'age', 'search_views', 'detail_views', 'stock_days', 'ctr']

result = permutation_importance(model_rfb_clf, X_train, y_train, n_repeats=5, random_state=42, n_jobs=2)
forest_importances = pd.Series(result.importances_mean, index=features)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Permutation feature importance (train data)")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.rcParams.update({'font.size': 14})
plt.show()



# Permutation feature importance on test dataset
result = permutation_importance(model_rfb_clf, X_test, y_test, n_repeats=5, random_state=42, n_jobs=2)
forest_importances = pd.Series(result.importances_mean, index=features)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Permutation feature importance (test data)")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.rcParams.update({'font.size': 14})
plt.show()
