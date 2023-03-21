# Predicting-product-tier-Classification-
This example demonstrates the prediction of the product tier of cars sold on a website from the information contained in the columns of the data 'Items_Cars_Data.csv'.  The file 'Data_description.csv' describes the columns.
The entire chain of model development: data loading, derivation of new features, exploratory data analysis, preparation of data for training, model building, cross-validation, hyperparameter tuning, learning curve analysis, evaluation on the hold-out set (test data set), and feature importance analysis was covered. 
The algorithms include Logistic regression and Random forest. 
The prediction is a case of imbalanced classes. The imbalance was addressed by balancing the classes. This resulted in a significant improvement in learning and generalization, leading to more balanced accuracy and a higher F1 macro score, as well as a higher number of true positives for minority classes, as shown by the confusion matrix.
