class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Разная длина — невозможно
        if len(s) != len(goal):
            return False
        
        # goal должен быть подстрокой s + s
        return goal in (s + s)
