#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared_func'))

from polly_func import speak_text
from bedrock_func import run_bedrock

def main():
    print("=== Linear Models Quiz ===\n")
    
    # Discussion Questions
    discussion_questions = [
        {
            "question": "Explain the relationship between matrix determinants and invertibility. How would you use this concept in practice when working with linear transformations?",
            "followups": [
                "What happens geometrically when a 2x2 matrix has a determinant of 0?",
                "How does the magnitude of the determinant relate to the scaling factor of the transformation?",
                "In what machine learning scenarios would you need to check matrix invertibility?"
            ]
        },
        {
            "question": "Compare and contrast Pearson and Spearman correlation coefficients. When would you choose one over the other in data analysis?",
            "followups": [
                "How do outliers differently affect Pearson vs Spearman correlations?",
                "What assumptions does Pearson correlation make about the data distribution?",
                "Can you have a high Spearman correlation but low Pearson correlation?"
            ]
        },
        {
            "question": "Describe the role of covariance in Principal Component Analysis (PCA). How does understanding covariance help in dimensionality reduction?",
            "followups": [
                "Why do we use eigenvectors of the covariance matrix rather than the original variables?",
                "How does centering the data affect the covariance matrix in PCA?",
                "What happens to PCA results when variables have very different scales?"
            ]
        },
        {
            "question": "Explain how the identity matrix functions as the \"neutral element\" in matrix multiplication. Why is this property crucial for understanding matrix operations?",
            "followups": [
                "How does the identity matrix relate to the concept of matrix inverses?",
                "What role does the identity matrix play in solving systems of linear equations?",
                "Why must the identity matrix always be square?"
            ]
        },
        {
            "question": "Discuss the significance of R² (coefficient of determination) in model evaluation. How does it relate to the concepts of variance and correlation?",
            "followups": [
                "What are the limitations of using R² as the sole model evaluation metric?",
                "How does R² behave when you add more features to a linear regression model?",
                "What's the difference between R² and adjusted R²?"
            ]
        }
    ]
    
    # Multiple Choice Questions
    mc_questions = [
        {
            "question": "What does a determinant value of 0 indicate about a matrix?",
            "options": [
                "The matrix is the identity matrix",
                "The matrix cannot be inverted and flattens space",
                "The matrix only contains positive values",
                "The matrix is symmetric"
            ],
            "correct": 2,
            "explanation": "The matrix cannot be inverted and flattens space - A zero determinant means the matrix is singular (non-invertible) and the transformation collapses the space into a lower dimension."
        },
        {
            "question": "Which correlation coefficient would be most appropriate for analyzing the relationship between customer satisfaction ratings (1-5 scale) and purchase frequency?",
            "options": [
                "Pearson correlation only",
                "Spearman correlation only",
                "Both would be equally appropriate",
                "Neither correlation method applies"
            ],
            "correct": 2,
            "explanation": "Spearman correlation only - Since satisfaction ratings are ordinal data (ranked categories), Spearman correlation is more appropriate as it works with ranked values rather than assuming continuous linear relationships."
        },
        {
            "question": "In PCA, what do the eigenvalues of the covariance matrix represent?",
            "options": [
                "The correlation between original variables",
                "The amount of variance explained by each principal component",
                "The number of dimensions in the original dataset",
                "The mean values of the transformed data"
            ],
            "correct": 2,
            "explanation": "The amount of variance explained by each principal component - Eigenvalues indicate how much variance each principal component captures, helping determine which components are most important for dimensionality reduction."
        },
        {
            "question": "What is the result of multiplying any 3×3 matrix A by the 3×3 identity matrix?",
            "options": [
                "A matrix of all zeros",
                "A matrix of all ones",
                "The original matrix A",
                "The transpose of matrix A"
            ],
            "correct": 3,
            "explanation": "The original matrix A - The identity matrix is the neutral element for matrix multiplication, so A × I = I × A = A for any compatible matrix A."
        },
        {
            "question": "An R² value of 0.85 in a regression model indicates that:",
            "options": [
                "85% of predictions are correct",
                "85% of the variance in the target variable is explained by the model",
                "The model has 85% accuracy",
                "There's an 85% correlation between all variables"
            ],
            "correct": 2,
            "explanation": "85% of the variance in the target variable is explained by the model - R² specifically measures the proportion of variance explained, not accuracy or correctness of individual predictions."
        },
        {
            "question": "Which statement best describes the difference between covariance and correlation?",
            "options": [
                "Covariance is always between -1 and 1, correlation is not",
                "Correlation is standardized and unitless, covariance depends on variable units",
                "Covariance measures linear relationships, correlation measures any relationship",
                "They are identical measures with different names"
            ],
            "correct": 2,
            "explanation": "Correlation is standardized and unitless, covariance depends on variable units - Correlation standardizes covariance by dividing by the product of standard deviations, making it scale-independent and bounded between -1 and 1."
        }
    ]
    
    # Understanding Questions
    understanding_questions = [
        {
            "question": "What mathematical condition must be satisfied for a matrix to have an inverse?",
            "answer": "The matrix must be square and have a non-zero determinant (det(A) ≠ 0)."
        }
    ]
    
    # Run Discussion Questions
    print("PART 1: DISCUSSION QUESTIONS\n")
    for i, q in enumerate(discussion_questions, 1):
        print(f"Discussion Question {i}:")
        print(f"{q['question']}\n")
        
        user_answer = input("Your answer: ")
        
        prompt = f"Evaluate this answer to the question '{q['question']}': {user_answer}. Provide constructive feedback."
        feedback = run_bedrock(prompt)
        print(f"\nAI Feedback: {feedback}\n")
        
        for j, followup in enumerate(q['followups'], 1):
            print(f"Follow-up {j}: {followup}")
            followup_answer = input("Your answer: ")
            
            followup_prompt = f"Evaluate this answer to '{followup}': {followup_answer}. Provide brief feedback."
            followup_feedback = run_bedrock(followup_prompt)
            print(f"Feedback: {followup_feedback}\n")
        
        print("-" * 50)
    
    # Run Understanding Questions
    print("\nPART 2: UNDERSTANDING QUESTIONS\n")
    for i, q in enumerate(understanding_questions, 1):
        print(f"Understanding Question {i}:")
        print(f"{q['question']}\n")
        
        user_answer = input("Your answer: ")
        
        prompt = f"Compare this answer: '{user_answer}' with the expected answer: '{q['answer']}'. Evaluate accuracy and completeness."
        feedback = run_bedrock(prompt)
        print(f"\nAI Evaluation: {feedback}")
        print(f"Expected Answer: {q['answer']}\n")
        print("-" * 50)
    
    # Run Multiple Choice Questions
    print("\nPART 3: MULTIPLE CHOICE QUESTIONS\n")
    score = 0
    for i, q in enumerate(mc_questions, 1):
        print(f"Multiple Choice Question {i}:")
        print(f"{q['question']}\n")
        
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                answer = int(input("\nYour choice (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if answer == q['correct']:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect.")
        
        print(f"Explanation: {q['explanation']}\n")
        print("-" * 50)
    
    print(f"\nFinal Score: {score}/{len(mc_questions)} ({score/len(mc_questions)*100:.1f}%)")
    print("Quiz completed!")

if __name__ == "__main__":
    main()
