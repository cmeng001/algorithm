class Node:
    def __init__(self,data,nextNode):
        self.data = data
        self.next = nextNode

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
        value = None;
        i=self.first
        while(i!=None):            
            if(element==i.data):                
                value = i.data
                return i.data
            i = i.next

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


def palindromic(link):
    one = link.first
    two = link.first
    firstHalf = ''
    while(two!=None and two.next!=None):
        firstHalf = firstHalf + str(one.data)
        one = one.next
        two = two.next.next
    secondHalf = ''
    if(link.size%2!=0):
        firstHalf = firstHalf+str(one.data)
    while(one!=None):
        secondHalf = str(one.data) + secondHalf 
        one = one.next
    print('前半段：'+firstHalf)
    print('后半段：'+secondHalf)





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




        
















