


###################
### CLASSIFIERS ###
###################

# Naive Bayes
clf.fit(data_train, label_train)
pred_NB = clf.predict(data_test)

# K-Nearest Neighbors 
clf.fit(data_train, label_train)
pred_KNN = clf.predict(data_test)

# Support Vector Machine
clf.fit(data_train, label_train)
pred_SVM = clf.predict(data_test)

# Decision Tree
clf.fit(data_train, label_train)
pred_DT = clf.predict(data_test)


#####################
### MODEL METRICS ###
#####################

# Accuracy
acc = (tp + tn) / (tp + tn + fp + fn)

# Precision
precision = tp / (tp+fp)

# Recall
recall = tp / (tp + fn)

# False-positive rate
fpr = fp / (fp + tn)

# F1 measure 
f1 = 2 * tp / (2 * tp + fp + fn)
