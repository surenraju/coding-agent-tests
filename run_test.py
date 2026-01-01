#!/usr/bin/env python3

import sys
import os

# Add the current directory to Python path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Import and run the test
    import test_library
    
    print("Running library management system test...")
    print("=" * 50)
    
    # Execute the main function from the test file
    import test_library
    
    # Capture output by redirecting stdout
    import io
    from contextlib import redirect_stdout
    
    f = io.StringIO()
    with redirect_stdout(f):
        test_library.main()
    
    output = f.getvalue()
    print(output)
    
    print("=" * 50)
    print("Test completed successfully!")
    
except Exception as e:
    print(f"Error running test: {e}")
    import traceback
    traceback.print_exc()