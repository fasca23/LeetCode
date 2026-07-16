"""Тесты для Convert Sorted Array to BST."""
import unittest
from solution import Solution, tree_to_list, TreeNode


def get_height(root):
    """Высота дерева."""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def is_balanced(root):
    """Проверяет что дерево сбалансировано."""
    if not root:
        return True
    left_h = get_height(root.left)
    right_h = get_height(root.right)
    if abs(left_h - right_h) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)

def collect_values(root):
    """Собирает все значения из дерева."""
    if not root:
        return []
    return collect_values(root.left) + [root.val] + collect_values(root.right)


class TestSortedArrayToBST(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, nums):
        root = self.sol.sortedArrayToBST(nums)
        if not nums:
            self.assertIsNone(root)
            return
        
        # Дерево содержит все элементы
        values = collect_values(root)
        self.assertEqual(values, sorted(nums),
                         f"Дерево должно содержать все элементы {nums}")
        
        # Дерево сбалансировано
        self.assertTrue(is_balanced(root),
                        f"Дерево должно быть сбалансированным")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([-10, -3, 0, 5, 9])
    
    def test_example_2(self):
        self.check([1, 3])
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check([])
    
    def test_single(self):
        self.check([0])
    
    def test_two_elements(self):
        self.check([1, 2])
    
    # ---------- Больше ----------
    def test_odd_length(self):
        self.check([1, 2, 3, 4, 5, 6, 7])
    
    def test_even_length(self):
        self.check([1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
