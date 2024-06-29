from tree_sitter import Language, Parser
import warnings

warnings.filterwarnings('ignore', category=Warning)

# 注意C++对应cpp，C#对应c_sharp（！这里短横线变成了下划线）
# 看仓库名称
C_LANGUAGE = Language('build/my-languages.so', 'c')

# 举一个CPP例子
c_parser = Parser()
c_parser.set_language(C_LANGUAGE)

# 这是b站网友写的代码，解析看看
with open("mypow.c", "r") as file:
    cpp_code_snippet = file.read()


# 没报错就是成功
tree = cpp_parser.parse(bytes(cpp_code_snippet, "utf8"))

# 注意，root_node 才是可遍历的树节点
root_node = tree.root_node





def traverse_tree(node):
    # 访问当前节点
    process_node(node)

    # 遍历当前节点的子节点
    for child in node.children:
        traverse_tree(child)


def process_node(node):
    # 在这里执行你想要的操作，比如打印节点类型或者执行其他操作
    print("Node Type:", node.type)
    print("Node Text:", node.text)
    # 你也可以根据节点的类型执行不同的操作
    if node.type == "function_declaration":
        process_function_declaration(node)


# 示例：处理函数声明节点
def process_function_declaration(node):
    # 提取函数名称
    function_name = node.child_by_field_name("name").text
    print("Function Declaration:", function_name)


# 开始遍历语法树
traverse_tree(tree.root_node)

