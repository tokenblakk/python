__author__ = 'Tramel Jones'
#Implement a Quad Tree that returns the amount of a given color of pixels
#Assume pixel values 1 or 0 (black or white)

class QTreeNode:
    black = 0
    col = 0
    def __init__(self, color):
        self.col = color
        if self.col == 1:
            self.black = 1
        self.children = []
        self.total = 1
    def AddChild(self, node, index):
        self.children[index] = node
        self.total += node.total
        self.black += node.black
    def GetNumberOfPixels(self, col):
        if col == 0:
            return self.total - self.black
        else: return self.black
def main():
    parent = QTreeNode(0)
    node1 = QTreeNode(1)
    node2 = QTreeNode(1)
    parent.AddChild(node1, 0)
    parent.AddChild(node2, 1)
    print "Tree has " + parent.GetNumberOfPixels(1) + " Black (ON) Pixels."
    print "Tree has " + parent.GetNumberOfPixels(0) + " White (OFF) Pixels."

if __name__ == "__main__":
    main()