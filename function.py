class Function:
    #wrapper class around the function and its arguments
    def __init__(self, func, args, priority):
        self.func=func
        self.args=args
        self.priority = priority

    def __lt__(self, other):
        """Compare two function objects based on priority and return bool value"""
        return self.priority < other.priority
