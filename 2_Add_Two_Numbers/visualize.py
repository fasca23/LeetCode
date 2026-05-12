"""
Визуализация сложения двух чисел.
Использует Solution из solution.py, не меняя его.
Управление: Enter — следующий шаг, q — выход.
"""

import os
import sys
from solution import Solution, ListNode, to_list, to_linked

# Цвета (работает без colorama)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


def visualize(nums1, nums2):
    """Пошаговая визуализация сложения двух чисел."""
    
    l1 = to_linked(nums1)
    l2 = to_linked(nums2)
    
    # Копируем узлы для обхода
    p1, p2 = l1, l2
    carry = 0
    dummy = ListNode(0)
    current = dummy
    result = []
    step = 0
    
    # Названия разрядов
    places = ["единицы", "десятки", "сотни", "тысячи"]
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    
    # Заголовок
    print(f"{CYAN}{'='*50}{RESET}")
    print(f"{BOLD}Сложение: {nums1} + {nums2}{RESET}")
    print(f"{CYAN}{'='*50}{RESET}\n")
    
    # Главный цикл
    while p1 or p2 or carry:
        step += 1
        
        v1 = p1.val if p1 else 0
        v2 = p2.val if p2 else 0
        
        # Исходные списки с указателями
        print(f"  {BOLD}L1:{RESET}", end=" ")
        tmp = l1
        i = 0
        while tmp:
            marker = f"{GREEN}▼{RESET}" if tmp == p1 else " "
            print(f"{marker}[{tmp.val}]", end=" → " if tmp.next else "\n")
            tmp = tmp.next
            i += 1
        if not p1:
            print(f"     {RED}▼ [NULL]{RESET}")
        
        print(f"  {BOLD}L2:{RESET}", end=" ")
        tmp = l2
        while tmp:
            marker = f"{GREEN}▼{RESET}" if tmp == p2 else " "
            print(f"{marker}[{tmp.val}]", end=" → " if tmp.next else "\n")
            tmp = tmp.next
        if not p2:
            print(f"     {RED}▼ [NULL]{RESET}")
        
        # Результат
        print(f"  {BOLD}R:{RESET}  ", end="")
        if result:
            print(" → ".join([f"[{v}]" for v in result[:-1]]), end="")
            if len(result) > 1:
                print(" → ", end="")
        print(f"{CYAN}[{result[-1] if result else '?'}]{RESET}" if step > 1 or result else "[ ]")
        
        print()
        print(f"  {BOLD}Шаг {step}{RESET} ({places[step-1] if step-1 < len(places) else f'10^{step-1}'})")
        print(f"  {YELLOW}l1.val={v1}  l2.val={v2}  carry_in={carry}{RESET}")
        
        total = v1 + v2 + carry
        carry_out = total // 10
        digit = total % 10
        
        print(f"  {v1} + {v2} + {carry} = {total}  →  ", end="")
        print(f"пишем {GREEN}{digit}{RESET}", end="")
        if carry_out:
            print(f",  перенос {RED}{carry_out}{RESET}")
        else:
            print(f",  перенос 0")
        
        # Создаём узел
        current.next = ListNode(digit)
        current = current.next
        result.append(digit)
        carry = carry_out
        
        # Шагаем
        if p1: p1 = p1.next
        if p2: p2 = p2.next
        
        print()
        wait()
        clear()
        print(f"{CYAN}{'='*50}{RESET}")
        print(f"{BOLD}Сложение: {nums1} + {nums2}{RESET}")
        print(f"{CYAN}{'='*50}{RESET}\n")
    
    # Финал
    print(f"  {BOLD}Результат:{RESET} {GREEN}{' → '.join([f'[{v}]' for v in result])}{RESET}")
    print(f"  {BOLD}Число:{RESET}     {GREEN}{int(''.join(map(str, reversed(result))))}{RESET}")
    print(f"\n{CYAN}{'='*50}{RESET}")
    print(f"{GREEN}Готово!{RESET}\n")


if __name__ == "__main__":
    # Примеры
    examples = [
        ([2, 4, 3], [5, 6, 4], "342 + 465 = 807"),
        ([9, 9, 9], [1], "999 + 1 = 1000"),
        ([9, 9, 9, 9], [9, 9, 9, 9], "9999 + 9999 = 19998"),
    ]
    
    for nums1, nums2, desc in examples:
        print(f"\n{CYAN}{desc}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums1, nums2)
        print()
