"""
Визуализация поиска самой длинной палиндромной подстроки.
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


def visualize(s):
    """Пошаговая визуализация разворота от центров."""
    
    n = len(s)
    start, max_len = 0, 1
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_palindrome(l, r, cur_len, is_new, mismatch=False):
        """Показать строку с подсвеченным палиндромом или несовпадением."""
        marker = f" {GREEN}← новый максимум!{RESET}" if is_new else ""
        color = RED if mismatch else YELLOW
        
        print(f"  ", end="")
        for j, ch in enumerate(s):
            if j == l and j == r:
                # Один символ — обе скобки вокруг него
                print(f"{color}[{ch}]{RESET}", end="")
            elif j == l:
                print(f"{color}[{ch}{RESET}", end="")
            elif j == r:
                print(f"{color}{ch}]{RESET}", end="")
            elif l < j < r:
                print(f"{color}{ch}{RESET}", end="")
            else:
                print(f"{ch}", end="")
        
        if mismatch:
            print(f"  {RED}✗ {s[l]} ≠ {s[r]}{RESET}")
        else:
            print(f"  длина={cur_len}{marker}")
    
    def expand(center_type, i):
        """Разворот от центра."""
        nonlocal start, max_len, step
        
        step += 1
        clear()
        
        if center_type == 'odd':
            label = f"нечётный центр [{i}]={s[i]!r}"
            l, r = i, i
        else:
            label = f"чётный центр [{i},{i+1}]={s[i]!r}{s[i+1]!r}"
            l, r = i, i + 1
        
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: {label}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"  Лучший пока: {GREEN}{s[start:start+max_len]!r}{RESET} (длина {max_len})")
        print()
        
        expanded = False
        
        while l >= 0 and r < n:
            if s[l] != s[r]:
                show_palindrome(l, r, 0, False, mismatch=True)
                print()
                break
            
            expanded = True
            cur_len = r - l + 1
            is_new = cur_len > max_len
            if is_new:
                max_len = cur_len
                start = l
            
            show_palindrome(l, r, cur_len, is_new)
            
            l -= 1
            r += 1
        
        if not expanded:
            print(f"  (центр пропущен)")
        
        print()
        wait()
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Палиндром: {s!r}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Лучший пока: {GREEN}{s[start:start+max_len]!r}{RESET} (длина {max_len})")
    print()
    wait()
    
    for i in range(n):
        expand('odd', i)
        if i + 1 < n:
            expand('even', i)
    
    # Финал
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    result = s[start:start + max_len]
    print(f"  {BOLD}Ответ:{RESET} {GREEN}{result!r}{RESET}")
    print(f"  {BOLD}Длина:{RESET} {GREEN}{max_len}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = ["babad", "cbbd", "racecar", "abba"]
    
    for s in examples:
        print(f"\n{CYAN}Строка: {s!r}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s)
        print()