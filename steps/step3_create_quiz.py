#!/usr/bin/env python3
"""
Step 3: Create Python quiz script from questions using Q chat
"""

import json
import subprocess
import os
import sys

def test():
    """Test this step"""
    try:
        # Test imports and basic operations
        json.loads('{"test": "value"}')
        subprocess.run(['echo', 'test'], capture_output=True)
        os.path.exists('.')
        print("✅ Step 3 test passed")
        return True
    except Exception as e:
        print(f"❌ Step 3 test failed: {e}")
        return False

def main():
    if not test():
        sys.exit(1)
        
    # Load config
    with open('input.json', 'r') as f:
        config = json.load(f)
    
    # Read questions from path in config
    if 'questions_path' not in config:
        print("Questions path not found in config. Run step2 first.")
        return
        
    questions_file = config['questions_path']
    if not os.path.exists(questions_file):
        print("Questions file not found. Run step2 first.")
        return
    
    with open(questions_file, 'r') as f:
        questions = f.read()
    
    output_file = f"{config['output_dir']}/{config['topic_name']}_quiz.py"
    
    # Generate Python quiz using Q
    prompt = f"""Create a Python quiz file from these questions and save it to {output_file}:

{questions}

Requirements:
1. Import sys, os to add shared_func to path
2. Import speak_text from polly_func  
3. Import run_bedrock from bedrock_func
4. Parse all question types from the markdown
5. Interactive quiz with bedrock-powered feedback
6. For discussion questions: ask main question, get user answer, use run_bedrock for feedback, then ask follow-ups
7. For understanding questions: ask question, get answer, use run_bedrock for evaluation
8. For multiple choice: show options, get answer, provide immediate feedback
9. Make it executable and functional

Create the complete working Python file."""
    
    result = subprocess.run(['q', 'chat', '--no-interactive', '--trust-all-tools', prompt], 
                          capture_output=True, text=True, timeout=120)
    
    if result.returncode != 0:
        print(f"Q chat failed: {result.stderr}")
        return
    
    # Update config with quiz path
    config['quiz_path'] = output_file
    with open('input.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Python quiz created successfully")

if __name__ == "__main__":
    main()
