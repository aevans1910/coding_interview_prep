#Leetcode code

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another 
# expression.

# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would 
# always evaluate to a result and there won't be any divide by zero operation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #first need to loop through all the elements in linked list
        #if its a number, add it to the stack
        #if its an opperator, use it to do the opperation between the top
        # 2 numbers on the stack, and then add the result back to the stack
        #Once we have looped through all the elements, return the last 
        #element in the stack
        stack = []
        for token in tokens:
            if token in "+-*/":
                val_2 = stack.pop()
                val_1 = stack.pop()
                result = eval(val_1 + token + val_2)
                stack.append(str(int(result)))
            else:
                stack.append(token)
        return stack[0]

# ["4", "13", "5", "/", "+"]
# "4" -> stack=["4"]
# "13" -> stack=["4", "13"]
# "5" -> stack=["4", "13", "5"]
# "/" -> val_2="5" val_1="13" -> eval("13" + "/" + "5") -> 13/5=2.6 -> int(2.6)=2 -> stack=["4", "2"]
# "+" -> val_2="2" val_1="4" -> eval("2" + "+" + "4") -> 2+4=6 -> stack=["6"]
# return "6"