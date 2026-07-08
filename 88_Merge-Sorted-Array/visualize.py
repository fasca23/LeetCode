"""
Визуализация слияния массивов — две вертикальные полоски.
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


def visualize(nums1_orig, m, nums2_orig, n):
    """Визуализация слияния — элементы падают в результат."""
    
    arr = nums1_orig[:]
    nums2 = nums2_orig[:]
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1
    step = 0
    done = False
    
    total = m + n
    height = max(m, n, total)
    nums1_valid = nums1_orig[:m]
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def draw():
        """Нарисовать три колонки."""
        print(f"  {BOLD}nums1          nums2          Результат (всего {total}){RESET}")
        print(f"  ─────          ─────          ─────────────────")
        print()
        
        for row in range(height - 1, -1, -1):
            # nums1
            if row < m:
                val = arr[row]
                if row == p1 and not done:
                    col1 = f"{YELLOW}[{val}]{RESET}"
                else:
                    col1 = f" {val} "
            else:
                col1 = "   "
            
            # nums2
            if row < n:
                val = nums2[row]
                if row == p2 and not done:
                    col2 = f"{YELLOW}[{val}]{RESET}"
                else:
                    col2 = f" {val} "
            else:
                col2 = "   "
            
            # Результат
            if row < total:
                if row > p or done:
                    # Уже заполненные (или всё готово)
                    val = arr[row]
                    if not done and step > 0 and row == p + 1:
                        col3 = f"{GREEN}[{val}]{RESET}"
                    else:
                        col3 = f" {GREEN}{val}{RESET} "
                elif row == p and p2 >= 0:
                    col3 = f" {CYAN}_{RESET} "
                else:
                    col3 = " · "
            else:
                col3 = "   "
            
            print(f"    {col1}            {col2}            {col3}")
        
        print()
        if done:
            print(f"  p1=∅            p2=∅            p=∅")
        else:
            print(f"  p1={p1 if p1 >=0 else '∅'}            p2={p2 if p2 >=0 else '∅'}            p={p}")
        print()
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Merge Sorted Array{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  {YELLOW}Жёлтый{RESET} — сравниваем, {GREEN}зелёный{RESET} — только что упал")
    print(f"  Сравниваем верхние элементы. Больший падает в результат.")
    print()
    draw()
    print()
    wait()
    
    while p2 >= 0:
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        if p1 >= 0 and arr[p1] > nums2[p2]:
            chosen = arr[p1]
            print(f"  {YELLOW}{arr[p1]}{RESET} > {nums2[p2]}  →  {GREEN}{chosen}{RESET} падает из nums1")
            arr[p] = arr[p1]
            p1 -= 1
        else:
            chosen = nums2[p2]
            if p1 < 0:
                print(f"  nums1 кончился  →  {GREEN}{chosen}{RESET} падает из nums2")
            else:
                print(f"  {arr[p1]} ≤ {YELLOW}{nums2[p2]}{RESET}  →  {GREEN}{chosen}{RESET} падает из nums2")
            arr[p] = nums2[p2]
            p2 -= 1
        
        p -= 1
        print()
        draw()
        print()
        wait()
    
    # Финал
    done = True
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  {BOLD}Готово!{RESET}")
    print()
    draw()
    
    expected = sorted(nums1_valid + nums2_orig)
    ok = arr == expected
    print(f"  Результат: {GREEN}{arr}{RESET}")
    print(f"  Ожидалось: {expected}")
    print(f"  Статус: {GREEN}✓ Верно{RESET}" if ok else f"  Статус: {RED}✗ Ошибка{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),
        ([0], 0, [1], 1),
        ([2, 4, 6, 0, 0, 0], 3, [1, 3, 5], 3),
        ([1, 2, 2, 0, 0], 3, [1, 2], 2),
        ([1, 5, 9, 0, 0, 0, 0], 3, [2, 3, 6, 7], 4),
    ]
    
    for nums1, m, nums2, n in examples:
        print(f"\n{CYAN}nums1={nums1[:m]}, nums2={nums2}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums1, m, nums2, n)
        print()
