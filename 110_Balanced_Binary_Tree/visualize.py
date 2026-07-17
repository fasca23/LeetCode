"""
Визуализация проверки сбалансированности дерева (post-order DFS).
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


def draw_tree(node, highlight=None, heights=None, prefix="", is_left=True):
    if node is None:
        return
    if node.right:
        draw_tree(node.right, highlight, heights, prefix + ("│   " if is_left else "    "), False)
    branch = "└── " if is_left else "┌── "
    h = f" (h={heights.get(node, '?')})" if heights and node in heights else ""
    if node == highlight:
        print(f"  {prefix}{branch}{YELLOW}{node.val}{h}{RESET}")
    else:
        print(f"  {prefix}{branch}{node.val}{h}")
    if node.left:
        draw_tree(node.left, highlight, heights, prefix + ("    " if is_left else "│   "), True)


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
    print(f"{BOLD}Balanced Binary Tree — post-order DFS{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Дерево: {values}")
    print()
    if root:
        draw_tree(root)
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  1. Обходим дерево снизу вверх (post-order)")
    print(f"  2. Каждый узел возвращает свою высоту")
    print(f"  3. Если |левая - правая| > 1 → дисбаланс")
    print(f"  4. Высота узла = 1 + max(левая, правая)")
    print()
    print(f"  {YELLOW}узел{RESET} — текущий, (h=X) — высота поддерева")
    print()
    wait()
    
    if not root:
        print(f"  {GREEN}Пустое дерево → True{RESET}\n")
        return
    
    stack = [(root, False)]
    heights = {None: 0}
    
    while stack:
        node, visited = stack.pop()
        
        if not visited:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
        else:
            step += 1
            left_h = heights[node.left]
            right_h = heights[node.right]
            diff = abs(left_h - right_h)
            is_ok = diff <= 1
            node_h = 1 + max(left_h, right_h)
            heights[node] = node_h
            
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: узел {node.val}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            
            draw_tree(root, node, heights)
            print()
            
            # Таблица — без правой рамки
            left_label = f"h({node.left.val})" if node.left else "h(None)"
            right_label = f"h({node.right.val})" if node.right else "h(None)"
            
            print(f"  node        = {YELLOW}{node.val}{RESET}")
            print(f"  left_h      = {left_h}   ← {left_label}")
            print(f"  right_h     = {right_h}   ← {right_label}")
            print(f"  |left−right|= {diff}")
            print(f"  высота      = 1 + max({left_h}, {right_h}) = {GREEN}{node_h}{RESET}")
            
            if is_ok:
                print(f"  баланс      = {GREEN}✓ ок (≤1){RESET}")
            else:
                print(f"  баланс      = {RED}✗ дисбаланс (>1) → False{RESET}")
                print()
                wait()
                return
            
            # Стек
            if stack:
                stack_vals = [f"({n.val},{'✓' if v else '…'})" for n, v in reversed(stack)]
                print(f"  стек        = {stack_vals}")
            else:
                print(f"  стек        = пуст")
            
            print()
            wait()
    
    # Финал
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Результат: дерево сбалансировано{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    draw_tree(root, heights=heights)
    print()
    print(f"  Все узлы: |h_left - h_right| ≤ 1")
    print(f"  Корень: h({root.val}) = {heights[root]}")
    print()


if __name__ == "__main__":
    examples = [
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 2, 3, 3, None, None, 4, 4],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    
    for values in examples:
        print(f"\n{CYAN}{values}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(values)
        print()
