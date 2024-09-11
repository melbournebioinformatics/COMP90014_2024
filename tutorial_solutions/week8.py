

##############
# Exercise 1 #
##############

### BEGIN SOLUTION
i = 0
max_components = len(pca.explained_variance_ratio_)

explained_variance = 0
while explained_variance < 0.9 and i < max_components:
    explained_variance += pca.explained_variance_ratio_[i]
    i += 1
    
print(f'{i} components explain {round(explained_variance * 100,2)}% of the variation in our data.')
### END SOLUTION


##############
# Exercise 2 #
##############

### BEGIN SOLUTION
reducer = MDS(n_components=2, normalized_stress='auto')
result = reducer.fit_transform(log_expression.values.T)
plot_two_dimensions(result, sample_categories)
### END SOLUTION


##############
# Exercise 3 #
##############

### BEGIN SOLUTION
reducer = TSNE(n_components=2, perplexity=7) # try with perplexity 20, 60
result = reducer.fit_transform(log_expression.values.T)
plot_two_dimensions(result, sample_categories)
### END SOLUTION


##############
# Exercise 4 #
##############

### BEGIN SOLUTION
reducer = umap.UMAP(n_components=2, n_neighbors=8)  # try with different n_neighbors eg 4, 10
result = reducer.fit_transform(log_expression.values.T)
plot_two_dimensions(result, sample_categories)
### END SOLUTION

