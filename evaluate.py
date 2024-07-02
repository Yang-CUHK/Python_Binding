import argparse
import os
import cython
from tree_sitter import Language, Parser
from python_c_visitor import Python_C_API_Visitor
from pybind11_visitor import Pybind11_Visitor
from cython_visitor import Cython_Visitor
import warnings

# the language
warnings.filterwarnings('ignore', category=Warning)


# argument
ap = argparse.ArgumentParser()
ap.add_argument('project', help='project to be analyzed')
ap.add_argument('-c', '--config',
    help='compilation options for specific project')
# ap.add_argument('-s', '--sources',
#     help='source paths already given in a file')
args = ap.parse_args()

if args.config == 'pybind11':
    CPP_LANGUAGE = Language('build/my-languages.so', 'cpp')
    cpp_parser = Parser()
    cpp_parser.set_language(CPP_LANGUAGE)
elif args.config == 'cython':
    C_LANGUAGE = Language('build/my-languages.so', 'c')
    c_parser = Parser()
    c_parser.set_language(C_LANGUAGE)
else:
    C_LANGUAGE = Language('build/my-languages.so', 'c')
    c_parser = Parser()
    c_parser.set_language(C_LANGUAGE)


# project -> C/C++ source
sources = []
if os.path.isfile(args.project):
    sources.append(args.project)
else:
    for dir, subdirs, files in os.walk(args.project):
        for f in files:
            if args.config == 'pybind11':
                if f.endswith('.cpp'):
                    sources.append(os.path.join(dir, f))
            elif args.config == 'cython':
                if f.endswith('.pyx'):
                    os.system(f"cython {os.path.join(dir, f)}")
                    filename = f.replace('.pyx', '.c')
                    sources.append(os.path.join(dir, filename))

            else:
                if f.endswith('.c'):
                    sources.append(os.path.join(dir, f))


for s in sources:
    if args.config == 'cython':
        print(s.replace('.c', '.pyx'))
    else:
        print(s)

    # C/Cpp source -> ast
    # preprocess, parse
    ast = None
    try:
        if args.config == 'pybind11':
            with open(s, "r") as file:
                cpp_code_snippet = file.read()
            tree = cpp_parser.parse(bytes(cpp_code_snippet, "utf-8"))
        elif args.config == 'cython':
            with open(s, "r") as file:
                c_code_snippet = file.read()
            tree = c_parser.parse(bytes(c_code_snippet, "utf8"))
        else:
            with open(s, "r") as file:
                c_code_snippet = file.read()
            tree = c_parser.parse(bytes(c_code_snippet, "utf8"))
    except Warning as w:
        print(w)
    except Exception as e:
        print(e)
        print("[ERROR] Preprocess failed, fix compilation options.")

    root_node = tree.root_node

    if args.config == 'pybind11':
        visitor = Pybind11_Visitor()
    elif args.config == 'cython':
        visitor = Cython_Visitor()
    else:
        visitor = Python_C_API_Visitor()
    visitor.visit(root_node)


    visitor.bindinglist()


if args.config == 'cython':
    for s in sources:
        os.remove(s)

    #print(visitor.python_c_binding)

    # for child in visitor.bindings3:
    #     print(child.type, child.text)
    #     visitor.getdict(child)
        # print(visitor.getdict(child))

    #print(visitor.python_c_binding.items())

