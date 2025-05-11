Raw threading and manual management:

This code implements a custom threading framework that allows multiple functions to be executed in parallel, with a limited number of threads (controlled by max_threads). 
It defines a Base class that handles the creation and execution of threads, as well as a Function class to store the function and its arguments. 
The system attempts to execute the functions in parallel by creating and managing threads, polling them, and removing them once they are finished.

Base class handles the management of threads and function execution.

Function class wraps a function and its arguments.

The main logic (download_file) performs the file download via HTTP requests.


Raw thread management in Python (using the threading module directly) gives you the maximum control over the threads in your program. 
While higher-level libraries like ThreadPoolExecutor abstract much of this complexity away, there are still use cases where raw thread management is useful or even necessary.


P.S: Execute threading_test.py file
