"""
Визуализация поиска максимальной глубины дерева (DFS со стеком).
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


def visualize(values):
    root = build_tree(values)
    step = 0
    max_depth = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Maximum Depth — DFS со стеком{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Дерево: {values}")
    print()
    if root:
        draw_tree(root)
    print()
    print(f"  {BOLD}Алгоритм:{RESET} стек хранит (узел, глубина).")
    print(f"  pop → обновить max → push детей с глубиной +1.")
    print()
    wait()
    
    if not root:
        print(f"  {RED}Пустое дерево → глубина 0{RESET}\n")
        return
    
    stack = [(root, 1)]
    
    while stack:
        step += 1
        node, depth = stack.pop()
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: pop{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        draw_tree(root, node)
        print()
        
        print(f"  Узел: {YELLOW}{node.val}{RESET}  |  глубина: {depth}")
        print(f"  Максимум до: {max_depth}")
        
        if depth > max_depth:
            max_depth = depth
            print(f"  {GREEN}Новый максимум: {max_depth}{RESET}")
        print()
        
        # Дети
        children = []
        if node.left:
            children.append((node.left, "left"))
        if node.right:
            children.append((node.right, "right"))
        
        if children:
            print(f"  Дети:")
            for child, side in children:
                print(f"    push ({child.val}, {depth + 1})  ← {side}")
                stack.append((child, depth + 1))
        else:
            print(f"  {GREEN}Лист!{RESET} Детей нет, глубина = {depth}")
        
        # Стек
        if stack:
            print(f"\n  Стек ({len(stack)} шт.):")
            for n, d in reversed(stack):
                marker = " ← верх" if (n, d) == stack[-1] else ""
                print(f"    ({n.val}, {d}){marker}")
        else:
            print(f"\n  Стек: пуст")
        
        print()
        wait()
    
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Результат: глубина = {max_depth}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    draw_tree(root)
    print()


if __name__ == "__main__":
    examples = [
        [3, 9, 20, None, None, 15, 7],
        [1, None, 2],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    
    for values in examples:
        print(f"\n{CYAN}{values}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(values)
        print()
