#!/usr/bin/env python3
"""
InterviewAI-Pro - Modular pipeline for question generation
"""

import subprocess
import sys
import json
import argparse

def run_step(step_num):
    """Run a specific step"""
    steps = {
        0: ("steps/step0_setup.py", "Setting up configuration..."),
        1: ("steps/step1_extract.py", "Extracting content from files..."),
        2: ("steps/step2_generate_questions.py", "Generating questions..."),
        3: ("steps/step3_create_quiz.py", "Creating Python quiz...")
    }
    
    if step_num not in steps:
        print(f"Invalid step: {step_num}")
        return False
    
    script, message = steps[step_num]
    print(f"{message}")
    
    # Step 0 needs interactive input, others can capture output
    if step_num == 0:
        result = subprocess.run([sys.executable, script])
    else:
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Failed: {script}")
        if hasattr(result, 'stderr') and result.stderr:
            print(f"Error: {result.stderr}")
        return False
    
    print(f"✅ Completed: {script}")
    return True

def main():
    """Main pipeline orchestrator"""
    parser = argparse.ArgumentParser(description='InterviewAI-Pro Pipeline')
    parser.add_argument('steps', nargs='*', type=int, help='Steps to run (0-3). If none specified, runs all steps.')
    args = parser.parse_args()
    
    print("InterviewAI-Pro Pipeline")
    print("=" * 25)
    
    # If no steps specified, run all steps
    if not args.steps:
        steps_to_run = [0, 1, 2, 3]
    else:
        steps_to_run = args.steps
    
    # Load config if it exists (for display purposes)
    try:
        with open('input.json', 'r') as f:
            config = json.load(f)
        print(f"Topic: {config['topic_name']}")
        print(f"Questions: {config['num_questions']}")
    except FileNotFoundError:
        if 0 not in steps_to_run:
            print("No input.json found. Run step 0 first.")
            return
    
    for step in steps_to_run:
        print(f"\nRunning Step {step}:")
        if not run_step(step):
            return
    
    print(f"\n🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()
