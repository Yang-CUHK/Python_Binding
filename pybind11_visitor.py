from visitor import Visitor
class Pybind11_Visitor(Visitor):
    def visit(self, node):
        self.target = []
        self.traverse(node)

    def traverse(self, node):
        if node.type == 'function_definition' and 'PYBIND11_MODULE' in str(node.text) and node not in self.target:
            self.target.append(node)
        for child in node.children:
            self.traverse(child)

    def bindinglist(self):
        self.pybind11_binding = {}
        self.bindings1 = []
        for tem in self.target:
            for child in tem.children:
                if str(child.type) == 'compound_statement':
                    self.bindings1.append(child)
        # print(child.type, child.text)
        # print(self.bindings1)

        self.bindings2 = []
        for tem in self.bindings1:
            # print(tem.type, tem.text)
            for child in tem.children:
                if child.type == 'expression_statement':
                    self.bindings2.append(child)

        self.bindings3 = []
        for tem in self.bindings2:
        # print(tem.type, tem.text)
            for child in tem.children:
                if str(child.type) == 'call_expression':
                    self.bindings3.append(child)

        self.bindings4 = []
        for tem in self.bindings3:
            for child in tem.children:
                if child.type == 'argument_list':
                    self.bindings4.append(child)

        for child in self.bindings4:
            key, value = self.getdict(child)
            if key is not None and value is not None:
                self.pybind11_binding[key] = value
        print(self.pybind11_binding)

    def getdict(self, initializer_list):
        #print(initializer_list.type, initializer_list.text)
        iskey, isvalue = None, None
        for child in initializer_list.children:
            #print(child.type,child.text)
            if child.type == 'string_literal' and iskey is None:
                iskey = True
                key = child.text
            if (child.type == 'pointer_expression' or child.type == 'identifier' or child.type == 'lambda_expression') and isvalue is None:
                isvalue = True
                value = child.text
        return key, value