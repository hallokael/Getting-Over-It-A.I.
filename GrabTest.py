from Common import *
MoveWindow2zeroName('Getting Over It')
sleep(5)
im=[]
for i in range(100):
    im.append(ImageGrab.grab())
for i in range(100):
    im[i].save('hh'+str(i)+'.png')
