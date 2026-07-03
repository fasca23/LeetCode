"""
Визуализация 4Sum — сортировка + два указателя.
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
    """Пошаговая визуализация поиска четвёрок."""
    
    n = len(nums)
    nums = sorted(nums)
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_array(i=None, j=None, left=None, right=None):
        """Показать массив с подсветкой индексов."""
        print(f"  ", end="")
        for k, num in enumerate(nums):
            if k == i:
                print(f"{YELLOW}[{num}]{RESET}", end="")
            elif k == j:
                print(f"{YELLOW}[{num}]{RESET}", end="")
            elif k == left:
                print(f"{GREEN}{num}{RESET}", end="")
            elif k == right:
                print(f"{GREEN}{num}{RESET}", end="")
            else:
                print(f"{num}", end="")
            if k < n - 1:
                print(", ", end="")
        print()
    
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}4Sum: target = {target}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    print(f"  Отсортированный массив: {nums}")
    print(f"  Длина: {n}")
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  1. Фиксируем i (первое число)")
    print(f"  2. Фиксируем j (второе число)")
    print(f"  3. left/right ищут оставшиеся два")
    print()
    wait()
    
    for i in range(n - 3):
        # Пропуск дубликатов
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Ранний выход
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                continue
            
            left, right = j + 1, n - 1
            need = target - nums[i] - nums[j]
            
            step += 1
            clear()
            print(f"{CYAN}{'='*60}{RESET}")
            print(f"{BOLD}Шаг {step}{RESET}")
            print(f"{CYAN}{'='*60}{RESET}\n")
            
            print(f"  Зафиксировали:")
            print(f"    i={i}: {YELLOW}{nums[i]}{RESET}")
            print(f"    j={j}: {YELLOW}{nums[j]}{RESET}")
            print(f"  Ищем пару с суммой = target - {nums[i]} - {nums[j]} = {CYAN}{need}{RESET}")
            print()
            show_array(i, j, left, right)
            print()
            print(f"  left={left} ({nums[left]}), right={right} ({nums[right]})")
            print()
            wait()
            
            found_in_step = []
            
            while left < right:
                cur_sum = nums[left] + nums[right]
                
                clear()
                print(f"{CYAN}{'='*60}{RESET}")
                print(f"{BOLD}Шаг {step} — поиск пары{RESET}")
                print(f"{CYAN}{'='*60}{RESET}\n")
                
                print(f"  i={i} ({nums[i]}), j={j} ({nums[j]})")
                print(f"  need = {need}")
                print()
                show_array(i, j, left, right)
                print()
                
                print(f"  nums[{left}] + nums[{right}] = {nums[left]} + {nums[right]} = {cur_sum}")
                print(f"  {cur_sum} vs {need}: ", end="")
                
                if cur_sum == need:
                    print(f"{GREEN}нашли!{RESET}")
                    found = [nums[i], nums[j], nums[left], nums[right]]
                    found_in_step.append(found)
                    print(f"  {GREEN}Добавляем: {found}{RESET}")
                    
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                    if left < right:
                        print(f"  Новый left={left} ({nums[left]}), right={right} ({nums[right]})")
                
                elif cur_sum < need:
                    print(f"{YELLOW}мало → left++{RESET}")
                    left += 1
                else:
                    print(f"{YELLOW}много → right--{RESET}")
                    right -= 1
                
                print()
                wait()
            
            if found_in_step:
                print(f"  {GREEN}Найдено на этом шаге: {found_in_step}{RESET}")
                print()
                wait()
    
    # Финал — собираем все четвёрки
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")
    print(f"  target = {target}, массив = {nums}")
    print()
    
    # Запускаем алгоритм для сбора результата
    from solution import Solution
    result = Solution().fourSum(nums, target)
    
    print(f"  {BOLD}Все четвёрки:{RESET} ({len(result)} шт.)")
    for q in result:
        print(f"    {GREEN}{q}{RESET}  →  sum = {sum(q)}")
    print(f"{GREEN}{'='*60}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ([1, 0, -1, 0, -2, 2], 0),
        ([2, 2, 2, 2, 2], 8),
        ([-1, 0, 1, 2, -1, -4], -1),
    ]
    
    for nums, target in examples:
        print(f"\n{CYAN}nums={nums}, target={target}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums, target)
        print()
