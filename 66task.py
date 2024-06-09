class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_leftmost_leaf(root):
    """
    Находит значение самого левого листа в дереве.

    :param root: корень дерева
    :return: значение самого левого листа
    """
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.value
    if root.left:
        return find_leftmost_leaf(root.left)
    return find_leftmost_leaf(root.right)

def count_occurrences(root, value):
    """
    Подсчитывает число вхождений значения в дереве.

    :param root: корень дерева
    :param value: значение для подсчета
    :return: число вхождений значения в дереве
    """
    if root is None:
        return 0
    count = 1 if root.value == value else 0
    count += count_occurrences(root.left, value)
    count += count_occurrences(root.right, value)
    return count

def assign_leftmost_and_count(tree):
    """
    Присваивает параметру E значение самого левого листа и
    определяет число вхождений записи E в дереве T.

    :param tree: корень дерева
    :return: значение самого левого листа и число его вхождений
    """
    E = find_leftmost_leaf(tree)
    if E is not None:
        count = count_occurrences(tree, E)
        return E, count
    return None, 0

# Пример использования
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)
                        ),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7)
                        )
               )

E, count = assign_leftmost_and_count(root)
print(f"Значение самого левого листа: {E}")
print(f"Число вхождений значения {E} в дереве: {count}")
