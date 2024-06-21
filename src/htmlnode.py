

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag 
        self.value=value
        self.children=children
        self.props=props
    def to_html(self):
        raise NotImplementedError("")
    def props_to_html(self):
        result = ""
        if self.props is None:
            return result
        for k,v in self.props.items():
            result += f" {k}=\"{v}\""
        return result
    def __repr__(self):
        return f"tag={self.tag}\nvalue={self.value}\nchildren={self.children} \
                \nprops={self.props}"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag=tag,value=value,children=None,props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,children=children,value=None,props=props)
    def to_html(self):
        if not self.children:
            raise ValueError("Children required for parent node")
        if not self.tag:
            raise ValueError("Tag required")
        result = f"<{self.tag}>"
        for c in self.children:
            result+=c.to_html()
        result += f"</{self.tag}>"
        return result
