"""
Визуализация сравнения двух деревьев (DFS со стеком).
Управление: Enter — шаг, q — выход.
"""

import os
import sys
from collections import deque

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def draw_tree(node, highlight=None, prefix="", is_left=True):
    if node is None:
        return
    if node.right:
        draw_tree(node.right, highlight, prefix + ("│   " if is_left else "    "), False)
    branch = "└── " if is_left else "┌── "
    if node == highlight:
        print(f"  {prefix}{branch}{YELLOW}{node.val}{RESET}")
    else:
        print(f"  {prefix}{branch}{node.val}")
    if node.left:
        draw_tree(node.left, highlight, prefix + ("    " if is_left else "│   "), True)


def visualize(p_vals, q_vals):
    p = build_tree(p_vals)
    q = build_tree(q_vals)
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_state(a, b, stack):
        print(f"  {BOLD}Дерево p:{RESET}")
        if p:
            draw_tree(p, a)
        else:
            print(f"  (пусто)")
        print()
        print(f"  {BOLD}Дерево q:{RESET}")
        if q:
            draw_tree(q, b)
        else:
            print(f"  (пусто)")
        print()
        
        # Текущая пара
        val_a = str(a.val) if a else "None"
        val_b = str(b.val) if b else "None"
        print(f"  {BOLD}Сравниваем:{RESET}  a = {YELLOW}{val_a}{RESET}  |  b = {YELLOW}{val_b}{RESET}")
        print()
        
        # Стек
        if stack:
            print(f"  {BOLD}Стек ({len(stack)} пар):{RESET}")
            for i, (x, y) in enumerate(reversed(stack)):
                vx = str(x.val) if x else "·"
                vy = str(y.val) if y else "·"
                marker = " ← верх" if i == 0 else ""
                print(f"    ({vx}, {vy}){marker}")
        else:
            print(f"  {BOLD}Стек:{RESET} пуст")
        print()
    
    clear()
    print(f"{CYAN}{'='*50}{RESET}")
    print(f"{BOLD}Same Tree — DFS со стеком{RESET}")
    print(f"{CYAN}{'='*50}{RESET}\n")
    print(f"  p = {p_vals}")
    print(f"  q = {q_vals}")
    print()
    print(f"  pop → сравнить → push left, push right")
    print()
    wait()
    
    stack = [(p, q)]
    
    while stack:
        step += 1
        a, b = stack.pop()
        
        clear()
        print(f"{CYAN}{'='*50}{RESET}")
        print(f"{BOLD}Шаг {step}: pop{RESET}")
        print(f"{CYAN}{'='*50}{RESET}\n")
        
        show_state(a, b, stack)
        
        if not a and not b:
            print(f"  {GREEN}оба None → ок, идём дальше{RESET}")
            print()
            wait()
            continue
        
        if not a or not b:
            reason = "a=None, b есть" if not a else "a есть, b=None"
            print(f"  {RED}{reason} → структура разная → False{RESET}")
            print()
            return
        
        if a.val != b.val:
            print(f"  {RED}{a.val} ≠ {b.val} → значения разные → False{RESET}")
            print()
            return
        
        left_a = str(a.left.val) if a.left else "·"
        left_b = str(b.left.val) if b.left else "·"
        right_a = str(a.right.val) if a.right else "·"
        right_b = str(b.right.val) if b.right else "·"
        
        print(f"  {GREEN}{a.val} == {b.val}{RESET}")
        print(f"  push left:  ({left_a}, {left_b})")
        print(f"  push right: ({right_a}, {right_b})")
        
        stack.append((a.left, b.left))
        stack.append((a.right, b.right))
        print()
        wait()
    
    clear()
    print(f"{GREEN}{'='*50}{RESET}")
    print(f"{BOLD}Результат: деревья одинаковы{RESET}")
    print(f"{GREEN}{'='*50}{RESET}\n")
    draw_tree(p)
    print(f"\n  p = q = {p_vals}")


if __name__ == "__main__":
    examples = [
        # Одинаковые, 3 уровня
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        # Разная структура
        ([1, 2, 3, 4], [1, 2, 3, None, None, None, 4]),
        # Разные значения
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 9]),
    ]
    
    for p_vals, q_vals in examples:
        print(f"\n{CYAN}p={p_vals}, q={q_vals}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(p_vals, q_vals)
        print()
