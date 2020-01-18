class Game:
    player = True
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.board=[]
        self.moveCount=0
        for i in range(h):
            temp = []
            for j in range(w):
                temp.append(0)
            self.board.append(temp)

    def __str__(self):
        print(' \t',end=" ",flush=True)
        for i in range(self.width):
            print(i+1,end=" ",flush=True)
        print()

        for a in range(self.height):
            print(a+1,'\t',end=" ",flush=True)
            for b in range(self.width):
                print(self.board[a][b],end=" ",flush=True)
            print()
        return " "

    def move(self,x,y,bool):
        if bool:                            # ADD NODE VALUE
            if(self.board[x][y]<0):
                self.board[x][y] *=-1
                self.board[x][y] += 1
            else:
                self.board[x][y] += 1

        else:
            if(self.board[x][y]>0):
                self.board[x][y] *= -1
                self.board[x][y] += -1
            else:
                self.board[x][y] += -1

        while( int(self.board[x][y]/4) !=0):                               # IF THE NODE HAS TO EXPLODE TAKE FLOOR TO CHECK
            if bool:
                self.board[x][y] +=-4
            else:
                self.board[x][y] += 4

            if x+1 == self.height:          #BELOW NODE THRU EDGE
                self.move(0,y,bool)
            else:                           #NORMAL NODE BELOW
                self.move(x+1,y,bool)

            if y+1 == self.width:           #NODE RIGHT THRU EDGE
                self.move(x,0,bool)
            else:                           #NODE RIGHT NORMAL
                self.move(x,y+1,bool)

            self.move(x-1,y,bool)      #ABOVE NODE
            self.move(x,y-1,bool)      #NODE LEFT

    def isValid(self,x,y):
        if x<0 or x>self.height-1:          # IN PROPER RANGE OF BOARD
            return False
        if y<0 or y>self.width-1:
            return False

        if self.player and self.board[x][y]<0:  # NOT PROPER POSITION FOR 1ST MOVE
            return False
        if not self.player and self.board[x][y]>0:
            return False
        return True

    def isOver(self):
        count =[0,0]

        for i in range(self.height):            # CHECK FOR PLAYER 1
            if count[0] >0:
                break
            for j in range(self.width):
                if self.board[i][j]>0:
                    count[0]+=1
                    break

        for i in range(self.height):            # CHECK FOR PLAYER 2
            if count[1] >0:
                break
            for j in range(self.width):
                if self.board[i][j]<0:
                    count[1]+=1
                    break

        if count[0] ==0:
            return -1
        if count[1] ==0:
            return  1
        return 0

    def Play(self):
        while(True):
            if self.moveCount >2:
                isOver = self.isOver()
                if isOver!=0:
                    return isOver
            print(self)
            try:
                inp = input("Select Position to add Node at")
                x = int(inp[0])-1
                y = int(inp[2])-1

                if self.isValid(x,y):
                    self.move(x,y,self.player)
                    self.player = not self.player
                    self.moveCount +=1

                else:
                    print("INVALID MOVE CHOICE")
            except:
                print("ERROR")



a = Game(7,7)
result = a.Play()
print(a)
if result>0:
    print("PLAYER 1 IS THE WINNER")
else:
    print("PLAYER 2 IS THE WINNER")