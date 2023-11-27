import ast
import re

class URLPatternChecker:
    name = "flake8_backend_url"
    version = "0.1.0"
    pattern = re.compile(r"/.*\/$")

    def __init__(self, tree, filename="(none)", file_tokens=None):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if self.pattern.search(node.value):
                    yield (
                        node.lineno,
                        node.col_offset,
                        "URLP001 URL slash found",
                        type(self)
                    )



# import ast
# import re
#
#
# class URLPatternChecker:
#     name = "flake8_backend_url"
#     version = "0.1.0"
#     pattern = re.compile(r"^\/.*\/$")
#
#     def __init__(self, tree, filename="(none)", file_tokens=None):
#         self.tree = tree
#
#     def run(self):
#         for node in ast.walk(self.tree):
#             if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
#                 if isinstance(node.right, ast.BinOp):
#                     continue
#
#
#                 # 左側が 'settings.BACKEND_BASE_URL'
#                 left_matches = (isinstance(node.left, ast.Attribute) and node.left.attr == "BACKEND_BASE_URL")
#                 # 右側が特定のパターンにマッチする文字列リテラル
#                 right_matches = (isinstance(node.right, ast.Constant) and isinstance(node.right.value,
#                                                                                      str) and self.pattern.search(
#                     node.right.value))
#
#                 if left_matches and right_matches:
#                     # 条件に一致した場合の処理
#                     yield (
#                     node.lineno, node.col_offset, "F001 Found pattern with settings.BACKEND_BASE_URL", type(self))
