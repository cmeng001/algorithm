# 节点对象
class Node:
    def __init__(self,data,nextNode):
        self.data = data
        self.next = nextNode

# 连表对象
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def add(self,element):
        node = Node(element,None)
        tem = self.last
        if(tem==None):            
            self.first = node
        else:
            tem.next = node
        self.last = node
        self.size = self.size+1

    
    def addFirst(self,element):
        newFirst = Node(element,None);
        newFirst.next = self.first;
        self.first = newFirst;
        self.size = self.size+1
    
    def delete(self,element):
        if(self.first.data==element):
            self.first = self.first.next
            self.size = self.size-1
            return
        i=self.first
        while(i!=None and i.next!=None):
            if(i.next.data==element):
                i.next = i.next.next 
                if(i.next==None):
                    self.last = i
            i = i.next                       
        self.size = self.size-1

    def printLink(self):        
        index = 0
        i=self.first
        while(i!=None):            
            index = index+1
            dataStr = str("index："+str(index)+";内容："+str(i.data))
            i = i.next
            print(dataStr)

    def getValue(self,element):
        i=self.first
        while(i!=None):            
            if(element==i.data):                
                return i.data
            i = i.next

# LUR缓存（最近最少使用策略）
def lur(link,element):
    value = link.getValue(element)
    if(value==None):
        if(link.size>4):
            link.delete(link.last.data)
            link.addFirst(element)
        else:
            link.addFirst(element)    
    else:
        link.delete(element)
        link.addFirst(element)

# 回文字符串
def palindromic(link):
    one = link.first
    two = link.first
    reverse = None
    while(two!=None and two.next!=None):
        two = two.next.next
        oneNext = one.next
        # 前半段反序        
        one.next = reverse
        reverse = one
        one = oneNext
    
    if(two!=None):
        one = one.next
    while(one!=None and reverse!=None):
        if(one.data!=reverse.data):
            print('flase')
        one = one.next
        reverse = reverse.next
    
        
    




if __name__ == '__main__':
    link = LinkedList();
    link.add(1);
    link.add(2);
    link.add(3);
    link.add(2);
    link.add(1);
    palindromic(link)
    
    link1 = LinkedList();
    link1.add(4);
    link1.add(5);
    link1.add(6);
    link1.add(6);
    link1.add(5);
    link1.add(4);
    palindromic(link1)




        
















