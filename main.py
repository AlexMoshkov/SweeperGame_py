__version__ = '0.0.1'

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint


class Container(BoxLayout):

    def getZero(self, x, y):

        q = [[x,y]]
        d = []
        while len(q) != 0:


            tmp = q.pop()
            i = tmp[0]
            j = tmp[1]
            if ( [i, j] not in d):
                d.append( [i, j] )

                for child in self.gl.children:
                    if child.id == str(i) + " " + str(j):
                        child.text = '0'
                        child.background_color = (0, 0, 0, 1)
                        break

                if (i + 1 != 6) and (self.arr[i + 1][j] == 0):
                    q.append( [i + 1, j] )
                elif (self.arr[i + 1][j] != 0):
                    for child in self.gl.children:
                        if child.id == str(i + 1) + " " + str(j):
                            child.text = str( self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] )
                            child.background_color = (0, 0, 0, 1)
                            break
                if (i - 1 != -1) and (self.arr[i - 1][j] == 0):
                    q.append([i - 1, j])
                elif (self.arr[i + 1][j] != 0):
                    for child in self.gl.children:
                        if child.id == str(i - 1) + " " + str(j):
                            child.text = str( self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] )
                            child.background_color = (0, 0, 0, 1)
                            break
                if (j + 1 != 5) and (self.arr[i][j + 1] == 0):
                    q.append([i , j + 1])
                elif (self.arr[i + 1][j] != 0):
                    for child in self.gl.children:
                        if child.id == str(i) + " " + str(j+1):
                            child.text = str( self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] )
                            child.background_color = (0, 0, 0, 1)
                            break
                if (j - 1 != -1) and (self.arr[i][j - 1] == 0):
                    q.append([i, j - 1])
                elif (self.arr[i + 1][j] != 0):
                    for child in self.gl.children:
                        if child.id == str(i) + " " + str(j - 1):
                            child.text = str( self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] )
                            child.background_color = (0, 0, 0, 1)
                            break



    def getFlag(self):
        if self.flag.text == 'Flag: OFF':
            self.flag.text = 'Flag: ON'
        else:
            self.flag.text = 'Flag: OFF'



    def Show(self, instance):
        x = int(instance.id.split(' ')[0])
        y = int(instance.id.split(' ')[1])
        if (self.button_play.text != "Again ?"):

            if self.flag.text == "Flag: ON":
                if instance.text == "" and self.k_mine > 0:
                    instance.text = "F"
                    self.k_mine -= 1
                    self.mines.text = "Mines: " + str(self.k_mine)
                elif instance.text == 'F':
                    instance.text = ""
                    self.k_mine += 1
                    self.mines.text = "Mines: " + str(self.k_mine)

            elif self.arr[x][y] == -1 and self.flag.text == "Flag: OFF" and instance.text != 'F':
                instance.background_color = (0, 0, 0, 1)
                self.button_play.text = "Again ?"
                self.open = False
                instance.text = str(self.arr[x][y])
            elif instance.text != 'F':

                if (self.arr[x][y] == 0):
                    self.getZero(x, y)
                instance.background_color = (0, 0, 0, 1)
                instance.text = str( self.arr[x][y] )

        #Проверка на победу!
        if self.k_mine == 0:
            k = 0
            for child in self.gl.children:
                if child.text == "F" and self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] == -1:
                    k += 1
            if k == len(self.arr_mine):
                self.button_play.text = "You Win!"
                self.open = False
                for child in self.gl.children:
                    if child.text == "F":
                        continue
                    child.text = str( self.arr[int( child.id.split(' ')[0] )][int( child.id.split(' ')[1] )] )
                    child.background_color = (0, 0, 0, 1)









    def GetNum(self):
        for i in range(6):
            for j in range(5):

                if self.arr[i][j] == -1:
                    continue

                tmp = 0

                if (i + 1 != 6):
                    tmp += self.arr[i+1][j] == -1
                if (i - 1 != -1):
                    tmp += self.arr[i-1][j] == -1

                if (j + 1 != 5):
                    tmp += self.arr[i][j+1] == -1
                if (j - 1 != -1):
                    tmp += self.arr[i][j-1] == -1

                if (i + 1 != 6) and (j + 1 != 5):
                    tmp += self.arr[i + 1][j + 1] == -1

                if (i + 1 != 6) and (j - 1 != -1):
                    tmp += self.arr[i + 1][j - 1] == -1

                if (i - 1 != -1) and (j + 1 != 5):
                    tmp += self.arr[i - 1][j + 1] == -1

                if (i - 1 != -1) and (j - 1 != -1):
                    tmp += self.arr[i - 1][j - 1] == -1


                self.arr[i][j] = tmp



    def GetMine(self):
        for i in range(6):
            y = True
            while y:
                f = False
                a = randint(0, 5)
                b = randint(0, 4)
                for x in self.arr_mine:
                    if [a, b] == x:
                        f = True
                if (f):
                    continue
                else:
                    y = False
            self.k_mine += 1
            self.arr[a][b] = -1 # это мина !
            self.arr_mine.append( [a, b] )

        self.mines.text = "Mines:" + str( self.k_mine )



    def play(self):
        if (self.button_play.text == "Again ?" or self.button_play.text == "You Win!"):
            self.button_play.text = "Play"
            self.arr = []
            self.k_mine = 0
            self.arr_mine = []
            for child in self.gl.children[:30]:
                print(child)
                self.gl.remove_widget(child)

        if (not self.open):
            self.open = not self.open

            for i in range(6):
                self.arr.append( [0]*5 )
                for j in range(5):
                    B = Button(id=str(i) + " " +str(j),
                           text = "",
                           on_release=self.Show)

                    self.gl.add_widget( B )

            self.GetMine()
            self.GetNum()
            print(self.arr)


class SweeperApp(App):
    def build(self):
        global Cont
        Cont = Container()
        return Cont


if __name__ == "__main__":
    SweeperApp().run()