#--------------------------------------------------------------------orientation interne------------------------------------------------------------------------------
#-------------------------------------------------------------------transformation affine-----------------------------------------------------------------------------
#________________________________________________ariba sifelislam étudiants en école nationale supérieure des sciences géodésique et techniques spéciales____________________
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import numpy as np
import cv2
from matplotlib import pyplot as plt
root=Tk()

N=[]
X=[]
Y=[]
x=[]
y=[]
coef=[]
X_res=[]
Y_res=[]
def OpenFile():
   
     filepath=fd.askopenfilename(filetypes=(('gpx files','*.BMP'),('all files','*.*')))
     entry.insert(END,filepath)

buttonIns=ttk.Button(root,text='...',command=OpenFile)
buttonIns.grid(row=0,column=4,sticky='snew',columnspan=2)
L=ttk.Label(root,background='red',text='IMAGE')
L.grid(row=0,column=0,sticky='snew')
entry=ttk.Entry(root,width=40)
entry.grid(row=0,column=2,sticky='snew',columnspan=2)
LM=ttk.Label(root,background='red',text='entrez le nombre des marques repere')
LM.grid(row=1,column=0,sticky='snew')
entry_M=ttk.Entry(root)
entry_M.grid(row=1,column=1,sticky='snew')
LX1=ttk.Label(root,background='red',text='X PHOTO')
LX1.grid(row=2,column=0,sticky='snew')
entry_X1=ttk.Entry(root)
entry_X1.grid(row=2,column=1,sticky='snew')
LY1=ttk.Label(root,background='red',text='Y PHOTO')
LY1.grid(row=2,column=2,sticky='snew')
entry_Y1=ttk.Entry(root)
entry_Y1.grid(row=2,column=3,sticky='snew')
def append():
    X1=float(entry_X1.get())
    entry_X1.delete('0',END)
    X.append(X1)
    Y1=float(entry_Y1.get())
    entry_Y1.delete('0',END)
    Y.append(Y1)
button=ttk.Button(root,text='APPEND',command=append)
button.grid(row=2,column=4,sticky='snew')
def on_click(event):
     if event.dblclick:
         plt.plot(event.xdata,event.ydata, linestyle='dashed' ,linewidth=2,
                  marker='o', markersize=6, markerfacecolor='blue',
                  markeredgecolor='blue')
         x.append(event.xdata)
         y.append(event.ydata)
         print(event.xdata,event.ydata)
def ok():
     nbr_mrq=int(entry_M.get())
     entry_M.delete('0',END)
     N.append(nbr_mrq)
button3=ttk.Button(root,text='ok',command=ok)
button3.grid(row=1,column=2,sticky='snew')
#---------------------------------------------------------------------resodre le system matriciel(MOINDRE CARRE)-----------------------------------------------------
def rslt():
    nbr_mrq=N[0]
    a=[]
    k=[]
    if (nbr_mrq >=4 and (len(X)==nbr_mrq and len(X)==nbr_mrq)):
        for j in range (0,len(X)):
            aj=[x[j],y[j],0,0,1,0]
            a.append(aj)
        for c in range (0,len(Y)):
            bc=[0,0,x[c],y[c],0,1]
            a.append(bc)
        for v in range (0,len(x)):
            k.append(X[v])
        for g in range (0,len(y)):
            k.append(Y[g])
        A=np.array(a)
        B=np.array(k)
        At=A.T
        An=np.dot(At,A)
        Bn=np.dot(At,B)
        F=np.linalg.solve(An,Bn)
        print('a=',F[0],'b=',F[1],'c=',F[2],'d=',F[3],'Cx=',F[4],'Cy=',F[5])
        coef.append(F[0])
        coef.append(F[1])
        coef.append(F[2])
        coef.append(F[3])
        coef.append(F[4])
        coef.append(F[5])
        
    else:
        exit()
button1=ttk.Button(root,text='resultat',command=rslt)
button1.grid(row=3,column=1,sticky='snew')
#-----------------------------------------------------l'affichage de la photo-------------------------------------------------------------------------------------------
def affichage():
    path=entry.get()
    img = cv2.imread(path,0)
    plt.imshow(img , cmap ='gray',interpolation = 'bicubic')
    plt.connect('button_press_event', on_click)
    plt.show()
button2=ttk.Button(root,text='afficher',command=affichage)
button2.grid(row=3,column=2,sticky='snew')
def on_click1(event):
     if event.dblclick:
         plt.plot(event.xdata,event.ydata, linestyle='dashed' ,linewidth=2,
                  marker='o', markersize=6, markerfacecolor='blue',
                  markeredgecolor='blue')
         para_rot=[[coef[0],coef[1]],[coef[2],coef[3]]]
         xy=[event.xdata,event.ydata]
         para_trans=[coef[4],coef[5]]
         res=np.dot(para_rot,xy)
         Sss=res+para_trans
         print('X_res=',Sss[0])
         print('Y_res=',Sss[1])
def aff_IMG_RES():
    path=entry.get()
    entry.delete('0',END)
    img = cv2.imread(path,0)
    plt.imshow(img , cmap ='gray',interpolation = 'bicubic')
    plt.connect('button_press_event', on_click1)
    plt.show()
butt=ttk.Button(root,text='afficher_IMAGE_RESOLER',command=aff_IMG_RES)
butt.grid(row=3,column=3,sticky='snew')


root.mainloop()
