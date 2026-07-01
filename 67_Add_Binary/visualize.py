"""
Визуализация сложения бинарных строк.
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


def visualize(a, b):
    """Пошаговая визуализация бинарного сложения."""
    
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_numbers(pos_a, pos_b):
        """Показать оба числа с указателями."""
        # Выравниваем по правому краю
        max_len = max(len(a), len(b))
        
        # a
        print(f"     ", end="")
        for k in range(max_len - len(a)):
            print(" ", end="")
        for k, ch in enumerate(a):
            idx_in_a = k
            if idx_in_a == pos_a:
                print(f"{YELLOW}{ch}{RESET}", end="")
            elif idx_in_a > pos_a:
                print(f"{GREEN}{ch}{RESET}", end="")
            else:
                print(f"{ch}", end="")
        print()
        
        # b
        print(f"   + ", end="")
        for k in range(max_len - len(b)):
            print(" ", end="")
        for k, ch in enumerate(b):
            idx_in_b = k
            if idx_in_b == pos_b:
                print(f"{YELLOW}{ch}{RESET}", end="")
            elif idx_in_b > pos_b:
                print(f"{GREEN}{ch}{RESET}", end="")
            else:
                print(f"{ch}", end="")
        print()
        print(f"   " + "-" * (max_len + 2))
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Add Binary{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Складываем:")
    print(f"    a = {a!r}")
    print(f"    b = {b!r}")
    print()
    print(f"  Идём справа налево.")
    print(f"  total = bit_a + bit_b + carry")
    print(f"  бит результата = total % 2")
    print(f"  перенос = total // 2")
    print()
    wait()
    
    while i >= 0 or j >= 0 or carry:
        step += 1
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        total = bit_a + bit_b + carry
        digit = total % 2
        old_carry = carry
        carry = total // 2
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        show_numbers(i, j)
        print()
        
        # Текущий разряд
        if i >= 0:
            print(f"  bit_a = a[{i}] = {YELLOW}{bit_a}{RESET}", end="")
        else:
            print(f"  bit_a = {RED}0 (a кончилась){RESET}", end="")
        
        if j >= 0:
            print(f"    bit_b = b[{j}] = {YELLOW}{bit_b}{RESET}")
        else:
            print(f"    bit_b = {RED}0 (b кончилась){RESET}")
        
        print(f"  carry = {old_carry}")
        print(f"  ─────────────────")
        print(f"  total = {bit_a} + {bit_b} + {old_carry} = {YELLOW}{total}{RESET}")
        print(f"  бит = total % 2 = {total} % 2 = {GREEN}{digit}{RESET}")
        print(f"  carry = total // 2 = {total} // 2 = {RED if carry else GREEN}{carry}{RESET}")
        print()
        
        result.append(str(digit))
        print(f"  Результат пока: {GREEN}{''.join(reversed(result))!r}{RESET}")
        print()
        
        i -= 1
        j -= 1
        wait()
    
    # Финал
    final = ''.join(reversed(result))
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  {a!r} + {b!r} = {GREEN}{final!r}{RESET}")
    print(f"  Проверка: {int(a,2)} + {int(b,2)} = {int(final,2)}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ("11", "1"),
        ("1010", "1011"),
        ("111", "111"),
        ("101", "10"),
    ]
    
    for a, b in examples:
        print(f"\n{CYAN}{a!r} + {b!r}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(a, b)
        print()
