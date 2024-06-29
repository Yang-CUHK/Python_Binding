from visitor import Visitor
class Python_C_API_Visitor(Visitor):
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
                    self.bindings2.append(child)

        self.bindings3 = []
        for tem in self.bindings2:
            for child in tem.children:
                if child.type == 'initializer_list' and '{NULL, NULL, 0, NULL}' not in str(child.text):
                    self.bindings3.append(child)

        self.python_c_binding = {}
        key, value = None, None
        for child in self.bindings3:
            key, value = self.getdict(child)
            if key is not None and value is not None:
                self.python_c_binding[key] = value
        print(self.python_c_binding)

        # self.binding = []
        # for tem in self.bindings3:
        #     for child in tem.children:
        #         self.binding.append(child)
        #         print(child.type,child.text)
        #
        # self.python_c_binding = {}
        # for tem in self.bindings3:
        #     is_value = 0
        #     if child.type == 'string_literal':
        #         keyname = str(child.text)
        #     if child.type == 'identifier' and is_value == 0:
        #         is_value = 1
            #     value = str(child.text)
            # for child in tem.children:
            #     if child.type == 'string_literal':
            #         keyname = str(child.text)
            #     if child.type == 'identifier' and is_value == 0:
            #         is_value = 1
            #         value = str(child.text)
            # self.python_c_binding[keyname] = value
    def getdict(self, initializer_list):
        iskey, isvalue = False, False
        key, value = None, None
        for child in initializer_list.children:
            #print(child.type,child.text)
            if child.type == 'string_literal' and iskey is False:
                iskey = True
                key = child.text
            if (child.type == 'identifier' or child.type == 'cast_expression') and isvalue is False:
                isvalue = True
                value = child.text
        return key, value
        # for child in initializer_list.children:
        #     print(child.type,child.text)





