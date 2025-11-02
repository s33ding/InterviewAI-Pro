# Linear Algebra and Statistics Interview Questions

## Discussion Questions

Q: Explain the relationship between matrix determinants and invertibility. How would you use this concept in a machine learning context?
A: A matrix is invertible if and only if its determinant is non-zero. In ML, this is crucial for solving normal equations in linear regression (X^T X must be invertible), ensuring unique solutions exist. Zero determinant indicates linear dependence in features, leading to multicollinearity issues.
Follow-up Questions:
- How would you handle a near-zero determinant in practice?
- What are the computational implications of checking determinant vs other invertibility tests?
- How does this relate to regularization techniques like Ridge regression?

Q: Compare and contrast Pearson and Spearman correlation. When would you choose one over the other in data analysis?
A: Pearson measures linear relationships and assumes normal distribution, while Spearman measures monotonic relationships using ranks and is non-parametric. Use Pearson for linear relationships with continuous data; use Spearman for ordinal data or non-linear but consistent trends.
Follow-up Questions:
- How do outliers affect each correlation measure differently?
- Can you give an example where Spearman correlation is high but Pearson is low?
- How would you test the statistical significance of these correlations?

Q: Describe the mathematical foundation of PCA and explain why covariance matrices are central to the algorithm.
A: PCA finds principal components by computing eigenvectors of the covariance matrix. The covariance matrix captures how variables vary together, and its eigenvectors represent directions of maximum variance. Eigenvalues indicate the amount of variance explained by each component.
Follow-up Questions:
- Why do we typically standardize data before applying PCA?
- How do you determine the optimal number of components to retain?
- What are the limitations of PCA for non-linear data?

Q: Explain how R² relates to the concepts of explained and unexplained variance in regression models.
A: R² represents the proportion of variance in the dependent variable explained by the model. It's calculated as 1 - (SSE/SST), where SSE is sum of squared errors and SST is total sum of squares. Higher R² indicates better model fit, but doesn't guarantee causation or model validity.
Follow-up Questions:
- Why can R² be misleading in multiple regression with many features?
- How does adjusted R² address some limitations of regular R²?
- What are alternative metrics for evaluating regression performance?

Q: Discuss the geometric interpretation of matrix determinants and how this relates to linear transformations.
A: The determinant represents the scaling factor of area (2D) or volume (3D) under linear transformation. A determinant of 2 means areas are doubled; negative determinant indicates orientation reversal. Zero determinant means the transformation "flattens" space to lower dimensions.
Follow-up Questions:
- How does this geometric interpretation help understand singular matrices?
- What happens to determinants under matrix multiplication?
- How does this concept apply to change of variables in integration?

## Understanding Questions

Q: What is the identity matrix and why is it considered the "neutral element" for matrix multiplication?
A: The identity matrix is a square matrix with 1s on the main diagonal and 0s elsewhere. It's neutral because multiplying any matrix A by the identity matrix I yields A (A × I = I × A = A), similar to how multiplying by 1 in scalar arithmetic leaves the number unchanged.

Q: Define covariance and explain what positive and negative covariance values indicate about variable relationships.
A: Covariance measures how two variables change together. Positive covariance means variables tend to increase or decrease together; negative covariance means when one increases, the other tends to decrease. Zero covariance suggests no linear relationship.

Q: What makes PCA an "unsupervised" learning technique and how does this affect its applications?
A: PCA is unsupervised because it doesn't use target labels - it only analyzes the structure of input features to find directions of maximum variance. This makes it useful for exploratory data analysis, dimensionality reduction, and data compression without requiring labeled training data.

Q: Explain why Pearson correlation is "standardized" compared to covariance.
A: Pearson correlation standardizes covariance by dividing by the product of standard deviations, making it unitless and bounded between -1 and 1. This allows comparison of relationships between different variable pairs regardless of their scales or units.

Q: What does it mean for a matrix to be "non-degenerate" in terms of its determinant?
A: A non-degenerate matrix has a non-zero determinant, meaning it doesn't "flatten" or collapse the space it transforms. This ensures the matrix is invertible and represents a transformation that preserves the dimensionality of the space.

## Multiple Choice Questions

Q: Which condition must be satisfied for a matrix to have an inverse?
Options:
1. The matrix must be symmetric
2. The matrix must be square with non-zero determinant
3. All elements must be positive
4. The matrix must be diagonal
A: 2. A matrix is invertible if and only if it's square and has a non-zero determinant. Symmetry, positive elements, or diagonal structure are not required for invertibility.

Q: What is the range of possible values for Pearson correlation coefficient?
Options:
1. 0 to 1
2. -∞ to +∞
3. -1 to 1
4. 0 to 100
A: 3. Pearson correlation is bounded between -1 (perfect negative linear relationship) and 1 (perfect positive linear relationship), with 0 indicating no linear relationship.

Q: In PCA, what do the eigenvalues of the covariance matrix represent?
Options:
1. The correlation between original variables
2. The amount of variance explained by each principal component
3. The number of dimensions in the original data
4. The mean values of the transformed data
A: 2. Eigenvalues represent the amount of variance explained by each corresponding principal component (eigenvector). Larger eigenvalues indicate components that capture more variance in the data.

Q: What does a covariance value of zero between two variables indicate?
Options:
1. The variables are perfectly correlated
2. The variables have no relationship whatsoever
3. The variables have no linear relationship
4. One variable is constant
A: 3. Zero covariance indicates no linear relationship between variables, but non-linear relationships may still exist. It doesn't mean the variables are completely unrelated.

Q: Which statement about the identity matrix is correct?
Options:
1. It has the same value in all positions
2. It has 1s on the main diagonal and 0s elsewhere
3. It must be a 3×3 matrix
4. Its determinant is always zero
A: 2. The identity matrix has 1s on the main diagonal and 0s in all other positions. It can be any size (n×n), and its determinant is always 1, not zero.
