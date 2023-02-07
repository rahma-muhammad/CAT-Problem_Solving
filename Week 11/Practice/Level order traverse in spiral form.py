#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    h = height(root)
    ltr = False
    res = []
    
    for i in range(1, h + 1):
        printLevel(root, i, ltr, res)
        ltr = not ltr
    
    return res
    
#Function to print each level 
def printLevel(root, level, ltr, res):
    if root == None :
        return
    if level == 1:
        res.append(root.data)
        
    elif level > 1:
        if ltr:
            printLevel(root.left, level - 1, ltr, res)
            printLevel(root.right, level - 1, ltr, res)
        else:
            printLevel(root.right, level - 1, ltr, res)
            printLevel(root.left, level - 1, ltr , res)
        

#Function to get the height of the node
def height(node):
 
    if (node == None):
        return 0
    else:
 
        """ compute the height of each subtree """
        lheight = height(node.left)
        rheight = height(node.right)
 
        """ use the larger one """
        if (lheight > rheight):
            return(lheight + 1)
        else:
            return(rheight + 1)
        
