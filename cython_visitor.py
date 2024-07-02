from visitor import Visitor
class Cython_Visitor(Visitor):
    def visit(self, node):
        self.target = []
        self.traverse(node)

    def traverse(self, node):
        if node.type == 'declaration':
            self.target.append(node)

        for child in node.children:
            self.traverse(child)

    def bindinglist(self):
        self.bindings = []
        for child in self.target:
            if 'static PyMethodDef' in str(child.text):
                self.bindings.append(child)


        self.bindings1 = []
        for tem in self.bindings:
            for child in tem.children:
                if child.type == 'init_declarator':
                    self.bindings1.append(child)

        self.bindings2 = []
        for tem in self.bindings1:
            for child in tem.children:
                if child.type == 'initializer_list':
                    #print(child.type, child.text)
                    self.bindings2.append(child)


        self.cython_binding = {}
        for tem in self.bindings2:
            is_string = False
            for child in tem.children:
                if child.type == 'string_literal' and is_string is False:
                    is_string = True
                    key = child.text
                if child.type == 'cast_expression' and is_string is True:
                    is_string = False
                    value = child.text
                    self.cython_binding[key] = value
                    key,value = None,None

        print(self.cython_binding)







