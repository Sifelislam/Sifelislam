#-----------------------------------------------------------------------transformation conform---------------------------------------------------------------
#--------------------------------------------ariba sifelislam étudiants en école nationale supérieure des sciences géodésique et techniques spéciales-algérie-----------
print('-----------------------------------------------------------------------transformation conform---------------------------------------------------------------')
X=[]
Y=[]
x=[]
y=[]
X_bar=[]
Y_bar=[]
x_bar=[]
y_bar=[]
x_car=[]
y_car=[]
xX=[]
yY=[]
xY=[]
yX=[]
n=int(input('n='))
for i in range(1,n+1):
    Xi=float(input('X='))
    X.append(Xi)
    Yi=float(input('Y='))
    Y.append(Yi)
    xi=float(input('x='))
    x.append(xi)
    yi=float(input('y='))
    y.append(yi)
print('X=',X,'Y=',Y,'x=',x,'y=',y)
SX=0
SY=0
sx=0
sy=0
for j in range(0,n):
    SX=SX+X[j]
    SY=SY+Y[j]
    sx=sx+x[j]
    sy=sy+y[j]
print('SX=',SX,'SY=',SY,'sx=',sx,'sy',sy)
for t in range(0,n):
    X_bart=X[t]-(SX/n)
    X_bar.append(X_bart)
    Y_bart=Y[t]-(SY/n)
    Y_bar.append(Y_bart)
    x_bart=x[t]-(sx/n)
    x_bar.append(x_bart)
    x_b_c=x_bart**2
    x_car.append(x_b_c)
    y_bart=y[t]-(sy/n)
    y_bar.append(y_bart)
    y_b_c=y_bart**2
    y_car.append(y_b_c)
    xXX=X_bart*x_bart
    xX.append(xXX)
    yYY=Y_bart*y_bart
    yY.append(yYY)
    xYY=x_bart*Y_bart
    xY.append(xYY)
    yXX=y_bart*X_bart
    yX.append(yXX)
print('X_bar=',X_bar,'Y_bar',Y_bar,'x_bar=',x_bar,'y_bar=',y_bar,'x_car=',x_car,'y_car',y_car,'xX=',xX,'yY=',yY,'xY=',xY,'yX=',yX)
sx_car=0
sy_car=0
SxX=0
SyY=0
SxY=0
SyX=0
for p in range (0,n):
    sx_car=sx_car+x_car[p]
    sy_car=sy_car+y_car[p]
    SxX=SxX+xX[p]
    SyY=SyY+yY[p]
    SxY=SxY+xY[p]
    SyX=SyX+yX[p]
print('sx_car=',sx_car,'sy_car=',sy_car,'SxX=',SxX,'SyY=',SyY,'SxY=',SxY,'SyX=',SyX)
N=sx_car+sy_car
a=(SxX+SyY)/N
b=(SxY-SyX)/N
print('a=',a)
print('b=',b)

