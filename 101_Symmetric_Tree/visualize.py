"""
Визуализация проверки дерева на симметричность (DFS со стеком).
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


def draw_tree(node, highlight_left=None, highlight_right=None, prefix="", is_left=True):
    """Рисует дерево. Подсвечивает два узла одновременно."""
    if node is None:
        return
    if node.right:
        draw_tree(node.right, highlight_left, highlight_right,
                  prefix + ("│   " if is_left else "    "), False)
    branch = "└── " if is_left else "┌── "
    if node == highlight_left:
        print(f"  {prefix}{branch}{YELLOW}L:{node.val}{RESET}")
    elif node == highlight_right:
        print(f"  {prefix}{branch}{CYAN}R:{node.val}{RESET}")
    else:
        print(f"  {prefix}{branch}{node.val}")
    if node.left:
        draw_tree(node.left, highlight_left, highlight_right,
                  prefix + ("    " if is_left else "│   "), True)


def visualize(values):
    root = build_tree(values)
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Symmetric Tree — DFS со стеком{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Дерево: {values}")
    print()
    if root:
        draw_tree(root)
    print()
    print(f"  {BOLD}Идея:{RESET} сравниваем узлы перекрёстно:")
    print(f"  (левый-левый ↔ правый-правый) + (левый-правый ↔ правый-левый)")
    print(f"  {YELLOW}L{RESET} — левая сторона, {CYAN}R{RESET} — правая сторона")
    print()
    wait()
    
    if not root:
        print(f"  {GREEN}Пустое дерево → True{RESET}\n")
        return
    
    stack = [(root.left, root.right)]
    
    while stack:
        step += 1
        a, b = stack.pop()
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: pop{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        draw_tree(root, a, b)
        print()
        
        # Сравниваемая пара
        val_a = str(a.val) if a else "·"
        val_b = str(b.val) if b else "·"
        print(f"  Сравниваем:  {YELLOW}L={val_a}{RESET}  ↔  {CYAN}R={val_b}{RESET}")
        print()
        
        # Стек
        if stack:
            print(f"  Стек ({len(stack)} пар):")
            for i, (x, y) in enumerate(reversed(stack)):
                vx = str(x.val) if x else "·"
                vy = str(y.val) if y else "·"
                marker = " ← верх" if i == 0 else ""
                print(f"    L:{vx} ↔ R:{vy}{marker}")
        else:
            print(f"  Стек: пуст")
        print()
        
        if not a and not b:
            print(f"  {GREEN}Оба · → симметрично, идём дальше{RESET}")
            print()
            wait()
            continue
        
        if not a or not b:
            reason = "L=·, R есть" if not a else "L есть, R=·"
            print(f"  {RED}{reason} → структура разная → False{RESET}")
            print()
            return
        
        if a.val != b.val:
            print(f"  {RED}{a.val} ≠ {b.val} → значения разные → False{RESET}")
            print()
            return
        
        left_a = str(a.left.val) if a.left else "·"
        right_b = str(b.right.val) if b.right else "·"
        right_a = str(a.right.val) if a.right else "·"
        left_b = str(b.left.val) if b.left else "·"
        
        print(f"  {GREEN}{a.val} == {b.val}{RESET}")
        print(f"  push:  L.left={left_a} ↔ R.right={right_b}")
        print(f"  push:  L.right={right_a} ↔ R.left={left_b}")
        
        stack.append((a.left, b.right))   # перекрёстно
        stack.append((a.right, b.left))   # перекрёстно
        print()
        wait()
    
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Результат: дерево симметрично{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    draw_tree(root)
    print()


if __name__ == "__main__":
    examples = [
        # Симметричное, 3 уровня
        [1, 2, 2, 3, 4, 4, 3],
        # Несимметричное (разные значения)
        [1, 2, 2, None, 3, None, 3],
        # Симметричное, но с пропусками
        [1, 2, 2, None, 3, 3],
    ]
    
    for values in examples:
        print(f"\n{CYAN}{values}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(values)
        print()
