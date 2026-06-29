"""
Визуализация поиска медианы двух отсортированных массивов.
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


def visualize(nums1, nums2):
    """Пошаговая визуализация бинарного поиска."""
    
    original = (nums1[:], nums2[:])
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        swapped = True
    else:
        swapped = False
    
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2
    left, right = 0, m
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_arrays(mid1, mid2):
        """Показать оба массива с разделением."""
        # nums1
        print(f"  nums1 {nums1}")
        print(f"        ", end="")
        for i in range(len(nums1) + 1):
            if i == mid1:
                print(f"{YELLOW}│{RESET}", end=" ")
            elif i < len(nums1):
                print(f"  ", end="")
        print()
        if mid1 > 0:
            print(f"        L1 = {GREEN}{nums1[mid1 - 1]}{RESET}", end="")
        else:
            print(f"        L1 = {GREEN}-∞{RESET}", end="")
        if mid1 < m:
            print(f"    R1 = {GREEN}{nums1[mid1]}{RESET}")
        else:
            print(f"    R1 = {GREEN}+∞{RESET}")
        print()
        
        # nums2
        print(f"  nums2 {nums2}")
        print(f"        ", end="")
        for i in range(len(nums2) + 1):
            if i == mid2:
                print(f"{YELLOW}│{RESET}", end=" ")
            elif i < len(nums2):
                print(f"  ", end="")
        print()
        if mid2 > 0:
            print(f"        L2 = {GREEN}{nums2[mid2 - 1]}{RESET}", end="")
        else:
            print(f"        L2 = {GREEN}-∞{RESET}", end="")
        if mid2 < n:
            print(f"    R2 = {GREEN}{nums2[mid2]}{RESET}")
        else:
            print(f"    R2 = {GREEN}+∞{RESET}")
        print()
    
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Медиана двух отсортированных массивов{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    
    if swapped:
        print(f"  Поменяли местами для скорости:")
    print(f"  nums1 = {nums1}  (len={m})")
    print(f"  nums2 = {nums2}  (len={n})")
    print(f"  total = {total},  half = {half}")
    print(f"  Бинарный поиск по nums1: [{left}, {right}]")
    print()
    wait()
    
    while True:
        step += 1
        mid1 = (left + right) // 2
        mid2 = half - mid1
        
        l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = nums1[mid1] if mid1 < m else float('inf')
        l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = nums2[mid2] if mid2 < n else float('inf')
        
        clear()
        print(f"{CYAN}{'='*60}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*60}{RESET}\n")
        
        print(f"  Границы поиска: left={left}, right={right}")
        print(f"  mid1 = ({left}+{right})//2 = {mid1}")
        print(f"  mid2 = half - mid1 = {half} - {mid1} = {mid2}")
        print()
        
        show_arrays(mid1, mid2)
        print()
        
        print(f"  {BOLD}Проверка:{RESET}")
        print(f"    l1({l1}) ≤ r2({r2}) ?  {GREEN if l1 <= r2 else RED}{l1 <= r2}{RESET}")
        print(f"    l2({l2}) ≤ r1({r1}) ?  {GREEN if l2 <= r1 else RED}{l2 <= r1}{RESET}")
        print()
        
        if l1 <= r2 and l2 <= r1:
            print(f"  {GREEN}Разбиение верное!{RESET}")
            if total % 2 == 1:
                result = float(min(r1, r2))
                print(f"  Нечётное ({total}) → медиана = min(r1,r2) = min({r1},{r2}) = {GREEN}{result}{RESET}")
            else:
                left_max = max(l1, l2)
                right_min = min(r1, r2)
                result = (left_max + right_min) / 2
                print(f"  Чётное ({total}) → медиана = (max(L)+min(R))/2")
                print(f"    max({l1},{l2}) = {left_max}")
                print(f"    min({r1},{r2}) = {right_min}")
                print(f"    ({left_max} + {right_min}) / 2 = {GREEN}{result}{RESET}")
            
            print()
            print(f"  {BOLD}Исходные:{RESET} {original[0]}, {original[1]}")
            print(f"  {BOLD}Медиана:{RESET} {GREEN}{result}{RESET}")
            print(f"{GREEN}{'='*60}{RESET}\n")
            return
        
        if l1 > r2:
            print(f"  {RED}l1 > r2 → nums1 даёт слишком много{RESET}")
            print(f"  right = mid1 - 1 = {mid1} - 1 = {mid1 - 1}")
            right = mid1 - 1
        else:
            print(f"  {RED}l2 > r1 → nums1 даёт слишком мало{RESET}")
            print(f"  left = mid1 + 1 = {mid1} + 1 = {mid1 + 1}")
            left = mid1 + 1
        
        print()
        wait()


if __name__ == "__main__":
    examples = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([1, 3, 8], [7, 9, 10, 11]),
    ]
    
    for nums1, nums2 in examples:
        print(f"\n{CYAN}{nums1} + {nums2}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums1, nums2)
        print()
