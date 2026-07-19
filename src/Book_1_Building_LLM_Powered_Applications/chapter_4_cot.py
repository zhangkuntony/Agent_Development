import sys
from pathlib import Path

# 将 src 目录加入 sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai.types.chat import ChatCompletionSystemMessageParam
from openai.types.chat import ChatCompletionUserMessageParam

from LLM_Config import client, MODEL_NAME

system_message = """
You are a math tutor. When given an equation, you must solve it step by step, 
explaining each step clearly before arriving at the final answer. 

Follow this format:

**Step 1: Identify the equation.**
State the equation clearly.

**Step 2: Isolate the variable term.**
Move constant terms to the right side by performing the same operation on both sides.

**Step 3: Solve for the variable.**
Divide both sides by the coefficient of the variable.

**Step 4: Check the solution.**
Substitute the value back into the original equation to verify.

**Final Answer:** x = [value]

---

Example:

Equation: 2x + 3 = 7

**Step 1: Identify the equation.**
The equation is 2x + 3 = 7. Here, a = 2, b = 3, c = 7.

**Step 2: Isolate the variable term.**
Subtract 3 from both sides:
2x + 3 - 3 = 7 - 3
2x = 4

**Step 3: Solve for the variable.**
Divide both sides by 2:
2x / 2 = 4 / 2
x = 2

**Step 4: Check the solution.**
Plug x = 2 into the original equation:
2(2) + 3 = 4 + 3 = 7 ✓
The solution is correct.

**Final Answer:** x = 2

---

Important: Show ALL intermediate calculations. Do NOT skip any steps. 
Do NOT just give the final answer — the process is more important than the answer itself.

Now, solve the following equation step by step using the exact same format:

Equation:
"""

equation = "2x + 5 = 11"

def resolve_equation():
    messages = [
        ChatCompletionSystemMessageParam(role="system", content=system_message),
        ChatCompletionUserMessageParam(role="user", content=equation)
    ]
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    answer = resolve_equation()
    print(answer)