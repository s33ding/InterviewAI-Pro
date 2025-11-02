#!/usr/bin/env python3
"""
Step 2: Generate questions from extracted content using Q chat
"""

import json
import subprocess
import os
import re
import sys

def test():
    """Test this step"""
    try:
        # Test imports and basic operations
        json.loads('{"test": "value"}')
        subprocess.run(['echo', 'test'], capture_output=True)
        os.path.exists('.')
        re.compile(r'test')
        print("✅ Step 2 test passed")
        return True
    except Exception as e:
        print(f"❌ Step 2 test failed: {e}")
        return False

def clean_ansi_codes(text):
    """Remove ANSI escape codes from text"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def clean_output(text):
    """Clean unwanted output from Q chat response"""
    # Remove ANSI codes
    text = clean_ansi_codes(text)
    
    # Find "Completed in" line and remove everything up to it
    lines = text.split('\n')
    start_index = 0
    
    for i, line in enumerate(lines):
        if 'Completed in' in line:
            start_index = i + 1
            break
    
    # Take only lines after "Completed in" and filter out lines with >
    filtered_lines = []
    for line in lines[start_index:]:
        if '>' not in line:
            filtered_lines.append(line)
    
    result = '\n'.join(filtered_lines)
    return result.strip()

def main():
    if not test():
        sys.exit(1)
        
    # Load config
    with open('input.json', 'r') as f:
        config = json.load(f)
    
    # Read extracted content with topic-linked filename
    content_file = f"{config['output_dir']}/{config['topic_name']}_extracted_content.txt"
    if not os.path.exists(content_file):
        print("Extracted content not found. Run step1 first.")
        return
    
    with open(content_file, 'r') as f:
        content = f.read()
    
    # Generate questions using Q
    prompt = f"""Based on this content about {config['topic_name']}, create exactly {config['num_questions']} discussion questions. EACH discussion question must be immediately followed by exactly ONE related multiple choice question.

CONTENT:
{content}

STRICT FORMAT - Generate exactly {config['num_questions']} of this pattern:

## Discussion Questions

Q1: [Discussion Question 1]
A: [Sample Answer 1]
Follow-up Questions:
- [Follow-up 1]
- [Follow-up 2]
- [Follow-up 3]

Multiple Choice for Discussion Question 1:
Q: [Related multiple choice question]
Options:
1. [Option A]
2. [Option B]
3. [Option C]
4. [Option D]
A: [Correct number with explanation]

Q2: [Discussion Question 2]
A: [Sample Answer 2]
Follow-up Questions:
- [Follow-up 1]
- [Follow-up 2]
- [Follow-up 3]

Multiple Choice for Discussion Question 2:
Q: [Related multiple choice question]
Options:
1. [Option A]
2. [Option B]
3. [Option C]
4. [Option D]
A: [Correct number with explanation]

## Understanding Questions
Q: [Question 1]
A: [Answer 1]

## Multiple Choice Questions
Q: [Question 1]
Options:
1. [Option A]
2. [Option B]
3. [Option C]
4. [Option D]
A: [Correct number with explanation]

IMPORTANT: Each discussion question MUST have exactly one multiple choice question paired with it."""
    
    result = subprocess.run(['q', 'chat', '--no-interactive', '--trust-all-tools', prompt], 
                          capture_output=True, text=True, timeout=120)
    
    if result.returncode != 0:
        print(f"Q chat failed: {result.stderr}")
        return
    
    # Clean output and save questions
    questions_file = f"{config['output_dir']}/{config['topic_name']}_questions.md"
    clean_content = clean_output(result.stdout)
    
    with open(questions_file, 'w') as f:
        f.write(clean_content)
    
    # Update config with questions path
    config['questions_path'] = questions_file
    with open('input.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Questions generated successfully")

if __name__ == "__main__":
    main()
