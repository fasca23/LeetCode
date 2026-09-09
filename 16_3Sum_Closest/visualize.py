"""
Визуализация 3Sum Closest — сортировка + два указателя.
Управление: Enter — шаг, q — выход.
"""

import os
import sys

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


def visualize(nums, target):
    """Пошаговая визуализация поиска ближайшей суммы."""
    
    nums = sorted(nums)
    n = len(nums)
    closest = float('inf')
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_array(i, left, right):
        """Показать массив с выделением."""
        print(f"  [", end="")
        for k, val in enumerate(nums):
            if k > 0:
                print(", ", end="")
            if k == i:
                print(f"{YELLOW}{val}{RESET}", end="")
            elif k == left:
                print(f"{CYAN}{val}{RESET}", end="")
            elif k == right:
                print(f"{CYAN}{val}{RESET}", end="")
            else:
                print(f"{val}", end="")
        print(f"]")
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}3Sum Closest: target = {target}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Отсортированный массив: {nums}")
    print(f"  {YELLOW}i{RESET} — первое число, {CYAN}left/right{RESET} — пара")
    print()
    wait()
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            step += 1
            cur_sum = nums[i] + nums[left] + nums[right]
            diff = abs(cur_sum - target)
            best_diff = abs(closest - target)
            
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            
            show_array(i, left, right)
            print()
            print(f"  i = {i} ({nums[i]}), left = {left} ({nums[left]}), right = {right} ({nums[right]})")
            print(f"  Сумма = {nums[i]} + {nums[left]} + {nums[right]} = {YELLOW}{cur_sum}{RESET}")
            print(f"  |{cur_sum} - {target}| = {diff}")
            print()
            
            if cur_sum == target:
                print(f"  {GREEN}Точно target! Ответ: {target}{RESET}")
                return
            
            if diff < best_diff:
                closest = cur_sum
                print(f"  {GREEN}Новая ближайшая сумма: {closest}{RESET}")
            else:
                print(f"  Ближайшая пока: {closest}")
            
            if cur_sum < target:
                print(f"  {cur_sum} < {target} → left++")
                left += 1
            else:
                print(f"  {cur_sum} > {target} → right--")
                right -= 1
            
            print()
            wait()
    
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Готово! Ближайшая сумма: {closest}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([4, 0, 5, -5, 3, 3], -1),
    ]
    
    for nums, target in examples:
        print(f"\n{CYAN}nums={nums}, target={target}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums, target)
        print()
