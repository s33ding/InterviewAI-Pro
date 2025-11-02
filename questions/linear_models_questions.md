Q1: Explain the relationship between matrix determinants and invertibility. How would you use this concept in practice when working with linear 
transformations?
A: A matrix is invertible if and only if its determinant is non-zero. The determinant acts as a test for invertibility because it measures whether the 
matrix transformation preserves dimensionality. When det(A) = 0, the matrix "flattens" space, making it impossible to reverse the transformation. In 
practice, I'd calculate the determinant before attempting matrix inversion to avoid computational errors and understand the geometric properties of the 
transformation.
Follow-up Questions:
• What happens geometrically when a 2x2 matrix has a determinant of 0?
• How does the magnitude of the determinant relate to the scaling factor of the transformation?
• In what machine learning scenarios would you need to check matrix invertibility?

Multiple Choice for Discussion Question 1:
Q: What does a determinant value of 0 indicate about a matrix?
Options:
1. The matrix is the identity matrix
2. The matrix cannot be inverted and flattens space
3. The matrix only contains positive values
4. The matrix is symmetric
A: 2. The matrix cannot be inverted and flattens space - A zero determinant means the matrix is singular (non-invertible) and the transformation collapses 
the space into a lower dimension.

Q2: Compare and contrast Pearson and Spearman correlation coefficients. When would you choose one over the other in data analysis?
A: Pearson correlation measures linear relationships between continuous variables and ranges from -1 to 1. Spearman correlation measures monotonic 
relationships using ranked values, making it non-parametric. I'd use Pearson for linear relationships with normally distributed data, and Spearman for 
ordinal data or when the relationship is monotonic but not necessarily linear. Spearman is more robust to outliers since it uses ranks rather than raw 
values.
Follow-up Questions:
• How do outliers differently affect Pearson vs Spearman correlations?
• What assumptions does Pearson correlation make about the data distribution?
• Can you have a high Spearman correlation but low Pearson correlation?

Multiple Choice for Discussion Question 2:
Q: Which correlation coefficient would be most appropriate for analyzing the relationship between customer satisfaction ratings (1-5 scale) and purchase 
frequency?
Options:
1. Pearson correlation only
2. Spearman correlation only
3. Both would be equally appropriate
4. Neither correlation method applies
A: 2. Spearman correlation only - Since satisfaction ratings are ordinal data (ranked categories), Spearman correlation is more appropriate as it works with
ranked values rather than assuming continuous linear relationships.

Q3: Describe the role of covariance in Principal Component Analysis (PCA). How does understanding covariance help in dimensionality reduction?
A: In PCA, we compute the covariance matrix of the dataset to understand how variables change together. The eigenvectors of this covariance matrix become 
the principal components, representing directions of maximum variance. Covariance helps identify which variables are correlated and how they contribute to 
the overall data structure. By finding directions where data varies most (high covariance), PCA can reduce dimensions while preserving the most important 
information.
Follow-up Questions:
• Why do we use eigenvectors of the covariance matrix rather than the original variables?
• How does centering the data affect the covariance matrix in PCA?
• What happens to PCA results when variables have very different scales?

Multiple Choice for Discussion Question 3:
Q: In PCA, what do the eigenvalues of the covariance matrix represent?
Options:
1. The correlation between original variables
2. The amount of variance explained by each principal component
3. The number of dimensions in the original dataset
4. The mean values of the transformed data
A: 2. The amount of variance explained by each principal component - Eigenvalues indicate how much variance each principal component captures, helping 
determine which components are most important for dimensionality reduction.

Q4: Explain how the identity matrix functions as the "neutral element" in matrix multiplication. Why is this property crucial for understanding matrix 
operations?
A: The identity matrix acts like the number 1 in regular multiplication - any matrix multiplied by the identity matrix equals itself (A × I = A). This 
property is crucial because it establishes a reference point for matrix operations and is fundamental to matrix inversion (A × A⁻¹ = I). Understanding this 
helps grasp concepts like matrix inverses, eigenvalue problems, and linear transformations where the identity represents "no change."
Follow-up Questions:
• How does the identity matrix relate to the concept of matrix inverses?
• What role does the identity matrix play in solving systems of linear equations?
• Why must the identity matrix always be square?

Multiple Choice for Discussion Question 4:
Q: What is the result of multiplying any 3×3 matrix A by the 3×3 identity matrix?
Options:
1. A matrix of all zeros
2. A matrix of all ones
3. The original matrix A
4. The transpose of matrix A
A: 3. The original matrix A - The identity matrix is the neutral element for matrix multiplication, so A × I = I × A = A for any compatible matrix A.

Q5: Discuss the significance of R² (coefficient of determination) in model evaluation. How does it relate to the concepts of variance and correlation?
A: R² measures the proportion of variance in the dependent variable explained by the model, ranging from 0 to 1. It's calculated as the square of the 
correlation coefficient between predicted and actual values. R² helps evaluate model performance by showing how much of the data's variability the model 
captures. A higher R² indicates better fit, but it must be interpreted carefully as it can be artificially inflated by adding more variables or may not 
detect overfitting.
Follow-up Questions:
• What are the limitations of using R² as the sole model evaluation metric?
• How does R² behave when you add more features to a linear regression model?
• What's the difference between R² and adjusted R²?

Multiple Choice for Discussion Question 5:
Q: An R² value of 0.85 in a regression model indicates that:
Options:
1. 85% of predictions are correct
2. 85% of the variance in the target variable is explained by the model
3. The model has 85% accuracy
4. There's an 85% correlation between all variables
A: 2. 85% of the variance in the target variable is explained by the model - R² specifically measures the proportion of variance explained, not accuracy or 
correctness of individual predictions.

## Understanding Questions
Q: What mathematical condition must be satisfied for a matrix to have an inverse?
A: The matrix must be square and have a non-zero determinant (det(A) ≠ 0).

## Multiple Choice Questions
Q: Which statement best describes the difference between covariance and correlation?
Options:
1. Covariance is always between -1 and 1, correlation is not
2. Correlation is standardized and unitless, covariance depends on variable units
3. Covariance measures linear relationships, correlation measures any relationship
4. They are identical measures with different names
A: 2. Correlation is standardized and unitless, covariance depends on variable units - Correlation standardizes covariance by dividing by the product of 
standard deviations, making it scale-independent and bounded between -1 and 1.