class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to keep track of numbers
        # when an operator comes up
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                second = stack.pop()
                stack.append(stack.pop() - second)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            # Make sure division truncates toward zero
            elif t == "/":
                second = stack.pop()
                stack.append(int(float(stack.pop()) / second))
            else:
                stack.append(int(t))
        
        return stack[-1]