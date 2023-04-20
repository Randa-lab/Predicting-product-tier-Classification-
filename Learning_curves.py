from sklearn.model_selection import learning_curve
from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt

# define scoring
scoring = ['accuracy', 'balanced_accuracy', 'f1_micro', 'f1_macro']

def learning_curves(estimator, features, target, train_sizes, cv, scoring): 
  train_sizes, train_scores, validation_scores = learning_curve(estimator, features, target, train_sizes = train_sizes, cv = cv, scoring = scoring)
  train_scores_mean = train_scores.mean(axis = 1)
  validation_scores_mean = validation_scores.mean(axis = 1)
  
  plt.plot(train_sizes, train_scores_mean, label = 'Training accuracy')
  plt.plot(train_sizes, validation_scores_mean, label = 'Validation accuracy')
  plt.ylabel('Accuracy', fontsize = 16)
  plt.xlabel('Training set size', fontsize = 16)
  title = 'Learning curves for a ' + str(estimator).split('(')[0] + ' model'
  plt.title(title, fontsize = 18, y = 1.03)
  plt.legend() 
  plt.rcParams.update({'font.size': 16})
  plt.ylim(0.4, 1)
  
# plt.figure(figsize = (16,5))
# train_sizes = [1, 100, 500, 2000, 5000, 10000, 20000, 30000, 40000]
# learning_curves(model_rfb_clf, X_train, y_train, train_sizes, 5, 'accuracy')
