'''
Created on 2009-09-08

@author: beaudoin

Contains a abstract syntactic tree visitor for printing
nested function calls in a nice way. Used for cleaning-up 
output of the serialize method.

See the python standard ast module for details.
'''

import ast

class Fancify( ast.NodeVisitor ):
    
    def __init__(self):
        super( Fancify, self ).__init__()        
        self._tabLevel = 0
        self._spacesPerTab = 4

    def visitListElements(self, elements):
        """Inserts commas between elements and will go multi-line if needed."""
        # Try single line
        content = ", ".join( elements ) + " "
        nbCR = content.count('\n')
        isLong = len(content) > 100  or  nbCR > 0
        veryLong = isLong and nbCR > 40
        if isLong:
            # Too long, go multi-line
            spacer = "\n" + " " * (self._tabLevel * self._spacesPerTab)
            if veryLong : spacer = "\n" + spacer
            content = spacer
            spacer = "," + spacer
            content += spacer.join( elements )
            if veryLong :
                content += "\n" + " " * ((self._tabLevel-1) * self._spacesPerTab)
            else :
                content += " "
        return content

    def visitListType(self, list):
        """Visits anything that looks like a list of AST nodes.""" 
        self._tabLevel += 1
        # NOTE: Python 3 returns map(func, list) as iterable object
        elements_map = map( self.visit, list )
        elements = [e for e in elements_map]
        result = self.visitListElements( elements )
        self._tabLevel -= 1
        return result
    
    def visit_Call(self, node):
        """Fancify a function a call or an object creation."""
        # Python 3.5+ no longer provides node.starargs, and node.kwargs are in node.keywords
        # Ref: https://greentreesnakes.readthedocs.io/en/latest/nodes.html#Call
        #assert (node.starargs is None and node.kwargs is None), "Star arguments not supported by fancify"
        return self.visit(node.func) + "( " + self.visitListType( node.args + node.keywords ) + ")"
        
    def visit_List(self, node):
        """Fancify a list."""
        return "[ " + self.visitListType( node.elts ) + "]"
        
    def visit_Dict(self, node):
        """Fancify a dictionary."""
        self._tabLevel += 1
        # NOTE: Python 3 returns map(func, list) as iterable object
        keys_map = map( self.visit, node.keys )
        keys = [k for k in vkeys_map]
        values_map = map( self.visit, node.values )
        values =[v for v in values_map]
        elements = []
        for key, value in zip(keys,values):
            elements.append( key + ' : ' + value )        
        result = "{ " + self.visitListElements( elements ) + "}"
        self._tabLevel -= 1
        return result
        
    def visit_Tuple(self, node):
        """Fancify a tuple."""
        return "( " + self.visitListType( node.elts ) + ")"
        
    def visit_Name(self, node):
        """Visits a simple identifier"""
        return node.id
    
    def visit_Attribute(self, node):
        """Visits an 'object.attribute' node"""
        return self.visit(node.value) + '.' + node.attr
        
    def visit_keyword(self, node):
        """Fancify a keyword within a function a call or an object creation."""
        return str(node.arg) + " = " + self.visit( node.value )
    
    def visit_Str(self, node):
        """Fancify a simple string"""
        return repr(node.s)

    def visit_UnaryOp(self, node):
        """Fancify a signed value or expression"""
        return self.visit( node.op ) + self.visit( node.operand )

    def visit_UAdd(self, node):
        """Plus sign for fancified signed value or expression"""
        return str("+")

    def visit_USub(self, node):
        """Minus sign for fancified signed value or expression"""
        return str("-")

    def visit_Num(self, node):
        """Fancify a number"""
        return str(node.n)
    
    def generic_visit(self, node):
        return "\n".join( map( self.visit, ast.iter_child_nodes(node) ) )

        
    
