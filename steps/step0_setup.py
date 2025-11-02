#!/usr/bin/env python3
"""
Step 0: Setup - Create input.json configuration
"""

import json
import sys

def test():
    """Test this step"""
    try:
        # Test JSON operations
        test_config = {"test": "value"}
        json.dumps(test_config)
        print("✅ Step 0 test passed")
        return True
    except Exception as e:
        print(f"❌ Step 0 test failed: {e}")
        return False

def main():
    """Create input.json with user inputs"""
    if not test():
        sys.exit(1)
        
    print("InterviewAI-Pro Setup")
    print("=" * 20)
    
    topic_name = input("Topic name: ")
    source_folder = input("Source folder path: ")
    num_questions = int(input("Number of questions (default 2): ") or "2")
    output_dir = input("Output directory (default 'questions'): ") or "questions"
    
    config = {
        "topic_name": topic_name,
        "source_folder": source_folder,
        "num_questions": num_questions,
        "output_dir": output_dir
    }
    
    with open('input.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Configuration saved to input.json")

if __name__ == "__main__":
    main()
