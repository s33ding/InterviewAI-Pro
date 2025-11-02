#!/usr/bin/env python3
"""Test step 3 - Create quiz"""

import os
import shutil

def main():
    print("Testing Step 3 - Create quiz")
    os.chdir('..')
    shutil.copy('test/test_input.json', 'input.json')
    os.system('python main.py 1 2 3')
    print("✅ Step 3 test completed")

if __name__ == "__main__":
    main()
