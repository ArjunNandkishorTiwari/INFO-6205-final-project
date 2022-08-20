from tkinter import *
import time

class Graph:
    def __init__(self, root)-> None:
        self.display = root
        self.canvas_Creation = Canvas(self.display,
                                      bg="turquoise",
                                      relief=RAISED,
                                      bd=8,
                                      width=700,
                                      height=700
                                      )
        self.canvas_Creation.pack()

      
        self.state = None

        self.arrayVertex = []
        self.arrayCircle = []
        self.array = []

        self.initialSetUp()
        self.createVertices()

    def initialSetUp(self)-> None:
        title = Label(self.canvas_Creation,
                      text="Graph Traversing Visualization",
                      bg="brown",
                      fg="yellow",
                      font=("Times",19,"bold"))
        title.place(x=50,y=10)

     

        buttonDFSAction = Button(self.display, 
                                 text="DFS", 
                                 font=("Times", 15), 
                                 bg="black", 
                                 fg="green", 
                                 relief=RAISED, 
                                 bd=8, 
                                 command=self.graphTraversal)
        buttonDFSAction.place(x=650, y=750)

        self.state = Label(self.canvas_Creation,
                            text="Not Visited",
                            bg="black",fg="brown",
                            font=("Times",20,"bold","italic")
                            )
        self.state.place(x=45,y=395)
        
    
    def connectUpward(self,i,j)-> None:
        c1 = self.canvas_Creation.coords(self.arrayCircle[i])
        c2 = self.canvas_Creation.coords(self.arrayCircle[j])
        xStart = (c1[0]+c1[2]) / 2
        xEnd = (c2[0]+c2[2]) / 2
        yStart = (c1[1]+c1[3]) / 2
        yEnd = (c2[1]+c2[3]) / 2
        self.canvas_Creation.create_line(xStart+10,yStart-10,xEnd-10,yEnd+10,width=3)
        
    
    def connectDownward(self,i,j)-> None:
        c1 = self.canvas_Creation.coords(self.arrayCircle[i])
        c2 = self.canvas_Creation.coords(self.arrayCircle[j])
        xStart = (c1[0] + c1[2]) / 2
        xEnd = (c2[0] + c2[2]) / 2
        yStart = (c1[1] + c1[3]) / 2
        yEnd = (c2[1] + c2[3]) / 2
        self.canvas_Creation.create_line(xStart+12 , yStart +5, xEnd - 12, yEnd -5, width=3)


    def connectParentNode(self,origin,con1,con2)-> None:
        dummy = []
        dummy.append(self.arrayCircle[origin])

        if con1:
            dummy.append(self.arrayCircle[con1])
        else:
            dummy.append(None)

        if con2:
            dummy.append(self.arrayCircle[con2])
        else:
            dummy.append(None)

        self.arrayVertex.append(dummy)


    def createVertices(self)->None:
        i = 0
        while i<= 16:
            self.arrayCircle.append(i)
            i = i + 1
            
        
            

        self.arrayCircle[0] = self.canvas_Creation.create_oval(90, 260, 120, 290, width = 2)

        self.arrayCircle[1] = self.canvas_Creation.create_oval(170, 190, 200, 220, width = 2)

        self.arrayCircle[2] = self.canvas_Creation.create_oval(170, 330, 200, 360, width = 2)

        self.arrayCircle[3] = self.canvas_Creation.create_oval(240, 140, 270, 170, width = 2)

        self.arrayCircle[4] = self.canvas_Creation.create_oval(240, 230, 270, 260, width = 2)

        self.arrayCircle[5] = self.canvas_Creation.create_oval(240, 270, 270, 300, width = 2)

        self.arrayCircle[6] = self.canvas_Creation.create_oval(240, 380, 270, 410, width = 2)

        self.arrayCircle[7] = self.canvas_Creation.create_oval(290, 90, 320, 120, width = 2)

        self.arrayCircle[8] = self.canvas_Creation.create_oval(290, 190, 320, 220, width = 2)

        self.arrayCircle[9] = self.canvas_Creation.create_oval(290, 260, 320, 290, width = 2)

        self.arrayCircle[10] = self.canvas_Creation.create_oval(290, 330, 320, 360, width = 2)

        self.arrayCircle[11] = self.canvas_Creation.create_oval(290, 430, 320, 460, width = 2)

        self.arrayCircle[12] = self.canvas_Creation.create_oval(360, 140, 390, 170, width = 2)

        self.arrayCircle[13] = self.canvas_Creation.create_oval(360, 230, 390, 260, width =2)

        self.arrayCircle[15] = self.canvas_Creation.create_oval(360, 370, 390, 400, width = 2)
        
        self.arrayCircle[14] = self.canvas_Creation.create_oval(360, 300, 390, 330, width = 2)
        
        self.arrayCircle[16] = self.canvas_Creation.create_oval(360, 420, 390, 450, width = 2)
        
       



        self.connectUpward(0, 1)
        self.connectUpward(1, 3)
        self.connectUpward(2, 5)
        self.connectUpward(3, 7)
        
        self.connectUpward(8, 12)
        self.connectUpward(9, 13)
        self.connectUpward(10, 14)
        
        
        
        self.connectDownward(0, 2)
        self.connectDownward(1,4)
        self.connectDownward(2, 6)
        self.connectDownward(3, 8)
        self.connectDownward(4, 9)
        self.connectDownward(5, 10)
        self.connectDownward(6, 11)
        self.connectDownward(10, 15)
        self.connectDownward(11,16)

       
        
        
        
        
        self.connectParentNode(0,1,2) # Parent, top, down
        self.connectParentNode(1, 3, 4)
        self.connectParentNode(2, 5, 6)
        self.connectParentNode(3, 7, 8)
        self.connectParentNode(4, None, 9)
        self.connectParentNode(5, None, 10)
        self.connectParentNode(6, None, 11)
        self.connectParentNode(8, 12, None)
        self.connectParentNode(9, 13, None)
        self.connectParentNode(10, 14, 15)
        self.connectParentNode(11,None,16)
        



    def binarySearch(self,low,high,parent)-> None:
        while low<=high:
            mid = int((low+high)/2)
            if self.arrayVertex[mid][0] == parent:
                return self.arrayVertex[mid]
            elif self.arrayVertex[mid][0] < parent:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    

    def graphTraversal(self)-> None:
        try:
            self.state['text'] = "Traversed : Red"
            self.array.append(self.arrayVertex[0][0])
            while self.array:
                rootVertex = self.array.pop()
                print(rootVertex)
                self.canvas_Creation.itemconfig(rootVertex, fill="red")
                self.display.update()
                time.sleep(8/10)
                dummy = self.binarySearch(0, 10, rootVertex)
                if dummy != -1:
                   if dummy[1]:
                      self.array.append(dummy[1])
                   if dummy[2]:
                      self.array.append(dummy[2])
            self.state['text'] = "Traversal Complete"
        except:
            print("stop: some error occured")

if __name__ == '__main__':
    display = Tk()
    display.title("DFS Graph Traversal Visualizer")
    display.geometry("800x800")
    display.maxsize(800,800)
   
    display.config(bg="green")
    
    Graph(display)
    
    display.mainloop()
