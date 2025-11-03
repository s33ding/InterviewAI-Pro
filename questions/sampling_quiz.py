#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared_func'))

from polly_func import speak_text
from bedrock_func import run_bedrock

def run_quiz():
    print("=== Sampling Methods Quiz ===\n")
    
    # Discussion Questions
    discussion_questions = [
        {
            "q": "How would you determine the appropriate sampling interval for systematic sampling when studying customer satisfaction across different time periods of the day?",
            "a": "Calculate the sampling interval by dividing the population size by desired sample size (k = N/n). Consider temporal patterns - if customers arrive in waves (lunch rush, evening peak), the interval might coincide with these patterns, introducing bias. Randomize starting point and consider stratifying by time periods instead.",
            "followups": [
                "What happens if your sampling interval coincides with a natural pattern in your population?",
                "How would you modify systematic sampling for a 24-hour business cycle?",
                "When might systematic sampling be preferred over simple random sampling despite potential bias?"
            ]
        },
        {
            "q": "In what scenarios would cluster sampling be more practical than simple random sampling, and what trade-offs should researchers consider?",
            "a": "Cluster sampling is ideal when populations are geographically dispersed, individual listings are unavailable, or travel costs are high. Trade-offs include potential increased sampling error if clusters are heterogeneous, but significant cost savings and logistical advantages. Best when clusters are internally diverse but similar to each other.",
            "followups": [
                "How do you ensure clusters are representative of the overall population?",
                "What's the impact of cluster homogeneity on sampling error?",
                "How would you decide between single-stage and multi-stage cluster sampling?"
            ]
        },
        {
            "q": "How do you balance the trade-off between sample size and acceptable margin of error when budget constraints limit your research?",
            "a": "Use the sample size formula to calculate required n for different error levels. Evaluate cost per additional respondent versus value of increased precision. Consider stratified sampling to maintain precision with smaller samples, or accept larger margins of error for preliminary studies that inform larger investigations.",
            "followups": [
                "How does population variance affect your sample size requirements?",
                "What role does confidence level play in budget planning?",
                "When might a pilot study help optimize your sampling strategy?"
            ]
        }
    ]
    
    # Understanding Questions
    understanding_questions = [
        {
            "q": "What is the key difference between systematic sampling and simple random sampling in terms of selection process?",
            "a": "Systematic sampling selects every nth element after a random starting point, while simple random sampling gives every element an equal and independent chance of selection throughout the process."
        }
    ]
    
    # Multiple Choice Questions
    mc_questions = [
        {
            "q": "A researcher wants to sample 50 customers from a population of 1000. What should be the sampling interval for systematic sampling?",
            "options": ["10", "20", "25", "50"],
            "correct": 1,
            "explanation": "The sampling interval k = N/n = 1000/50 = 20, meaning every 20th customer should be selected after a random starting point."
        },
        {
            "q": "Which sampling method would be most appropriate for studying voting patterns across different neighborhoods in a large city?",
            "options": ["Simple random sampling", "Systematic sampling", "Cluster sampling", "Convenience sampling"],
            "correct": 2,
            "explanation": "Cluster sampling is most appropriate because neighborhoods serve as natural clusters, making it cost-effective to survey all residents within selected neighborhoods rather than traveling across the entire city for individual random selections."
        },
        {
            "q": "For proportion estimation, when is the required sample size largest?",
            "options": ["When p = 0.1", "When p = 0.3", "When p = 0.5", "When p = 0.9"],
            "correct": 2,
            "explanation": "When p = 0.5, the product p×q is maximized (0.5×0.5 = 0.25), requiring the largest sample size for a given margin of error."
        }
    ]
    
    score = 0
    total = len(discussion_questions) + len(understanding_questions) + len(mc_questions)
    
    # Discussion Questions
    print("=== DISCUSSION QUESTIONS ===\n")
    for i, dq in enumerate(discussion_questions, 1):
        print(f"Discussion Question {i}:")
        print(f"{dq['q']}\n")
        
        user_answer = input("Your answer: ")
        
        feedback_prompt = f"Question: {dq['q']}\nUser Answer: {user_answer}\nExpected Answer: {dq['a']}\n\nProvide constructive feedback on the user's answer, highlighting strengths and areas for improvement."
        
        feedback = run_bedrock(feedback_prompt)
        print(f"\nAI Feedback: {feedback}\n")
        
        for j, followup in enumerate(dq['followups'], 1):
            print(f"Follow-up {j}: {followup}")
            followup_answer = input("Your answer: ")
            print()
        
        score += 1
        print("-" * 50 + "\n")
    
    # Understanding Questions
    print("=== UNDERSTANDING QUESTIONS ===\n")
    for i, uq in enumerate(understanding_questions, 1):
        print(f"Understanding Question {i}:")
        print(f"{uq['q']}\n")
        
        user_answer = input("Your answer: ")
        
        eval_prompt = f"Question: {uq['q']}\nUser Answer: {user_answer}\nCorrect Answer: {uq['a']}\n\nEvaluate if the user's answer demonstrates understanding. Provide feedback."
        
        evaluation = run_bedrock(eval_prompt)
        print(f"\nAI Evaluation: {evaluation}\n")
        print(f"Expected Answer: {uq['a']}\n")
        
        score += 1
        print("-" * 50 + "\n")
    
    # Multiple Choice Questions
    print("=== MULTIPLE CHOICE QUESTIONS ===\n")
    for i, mcq in enumerate(mc_questions, 1):
        print(f"Multiple Choice Question {i}:")
        print(f"{mcq['q']}\n")
        
        for j, option in enumerate(mcq['options']):
            print(f"{j+1}. {option}")
        
        try:
            user_choice = int(input("\nYour choice (1-4): ")) - 1
            if user_choice == mcq['correct']:
                print("✓ Correct!")
                score += 1
            else:
                print(f"✗ Incorrect. The correct answer is {mcq['correct']+1}.")
            
            print(f"Explanation: {mcq['explanation']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.\n")
        
        print("-" * 50 + "\n")
    
    print(f"Quiz Complete! Final Score: {score}/{total}")
    speak_text(f"Quiz completed. You scored {score} out of {total}.")

if __name__ == "__main__":
    run_quiz()
