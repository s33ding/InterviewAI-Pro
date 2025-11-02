#!/usr/bin/env python3
"""
Main runner that tests each step before execution
"""

import subprocess
import sys
import os

def test_step(step_file):
    """Test a step file for syntax errors"""
    try:
        result = subprocess.run([sys.executable, '-m', 'py_compile', step_file], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ {step_file} has syntax errors:")
            print(result.stderr)
            return False
        print(f"✅ {step_file} passed syntax check")
        return True
    except Exception as e:
        print(f"❌ Error testing {step_file}: {e}")
        return False

def run_step(step_file):
    """Run a step file"""
    try:
        result = subprocess.run([sys.executable, step_file], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ {step_file} execution failed:")
            print(result.stderr)
            return False
        print(f"✅ {step_file} executed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except Exception as e:
        print(f"❌ Error running {step_file}: {e}")
        return False

def main():
    steps = [
        'step0_setup.py',
        'step1_extract.py', 
        'step2_generate_questions.py',
        'step3_create_quiz.py'
    ]
    
    print("Testing all steps before execution...")
    
    # Test all steps first
    all_tests_passed = True
    for step in steps:
        if not test_step(step):
            all_tests_passed = False
    
    if not all_tests_passed:
        print("\n❌ Some steps failed testing. Fix errors before running.")
        return
    
    print("\n✅ All steps passed testing. Running pipeline...")
    
    # Run steps sequentially
    for step in steps:
        print(f"\n--- Running {step} ---")
        if not run_step(step):
            print(f"Pipeline stopped at {step}")
            return
    
    print("\n🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()
