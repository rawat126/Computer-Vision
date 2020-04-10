import cv2
import os
import img2pdf
from tkinter import *
from tkinter import messagebox as msg
from tkinter.ttk import Progressbar
import time

os.chdir('E:\\alphabets\\')

A = cv2.resize(cv2.imread('A.png'),(27,27))
B = cv2.resize(cv2.imread('B.png'),(27,27))
C = cv2.resize(cv2.imread('C.png'),(27,27))
D = cv2.resize(cv2.imread('D.png'),(27,27))
E = cv2.resize(cv2.imread('E.png'),(27,27))
F = cv2.resize(cv2.imread('F.png'),(27,27))
G = cv2.resize(cv2.imread('G.png'),(27,27))
H = cv2.resize(cv2.imread('H.png'),(27,27))
I = cv2.resize(cv2.imread('I.png'),(27,27))
J = cv2.resize(cv2.imread('J.png'),(27,27))
K = cv2.resize(cv2.imread('K.png'),(27,27))
L = cv2.resize(cv2.imread('L.png'),(27,27))
M = cv2.resize(cv2.imread('M.png'),(27,27))
N = cv2.resize(cv2.imread('N.png'),(27,27))
O = cv2.resize(cv2.imread('O.png'),(27,27))
P = cv2.resize(cv2.imread('P.png'),(27,27))
Q = cv2.resize(cv2.imread('Q.png'),(27,27))
R = cv2.resize(cv2.imread('R.png'),(27,27))
S = cv2.resize(cv2.imread('S.png'),(27,27))
T = cv2.resize(cv2.imread('T.png'),(27,27))
U = cv2.resize(cv2.imread('U.png'),(27,27))
V = cv2.resize(cv2.imread('V.png'),(27,27))
W = cv2.resize(cv2.imread('W.png'),(27,27))
X = cv2.resize(cv2.imread('X.png'),(27,27))
Y = cv2.resize(cv2.imread('Y.png'),(27,27))
Z = cv2.resize(cv2.imread('Z.png'),(27,27))

a = cv2.resize(cv2.imread('small_a.png'),(27,27))
b = cv2.resize(cv2.imread('small_b.png'),(27,27))
c = cv2.resize(cv2.imread('small_c.png'),(27,27))
d = cv2.resize(cv2.imread('small_d.png'),(27,27))
e = cv2.resize(cv2.imread('small_e.png'),(27,27))
f = cv2.resize(cv2.imread('small_f.png'),(27,27))
g = cv2.resize(cv2.imread('small_g.png'),(27,27))
h = cv2.resize(cv2.imread('small_h.png'),(27,27))
i = cv2.resize(cv2.imread('small_i.png'),(27,27))
j = cv2.resize(cv2.imread('small_j.png'),(27,27))
k = cv2.resize(cv2.imread('small_k.png'),(27,27))
l = cv2.resize(cv2.imread('small_l.png'),(27,27))
m = cv2.resize(cv2.imread('small_m.png'),(27,27))
n = cv2.resize(cv2.imread('small_n.png'),(27,27))
o = cv2.resize(cv2.imread('small_o.png'),(27,27))
p = cv2.resize(cv2.imread('small_p.png'),(27,27))
q = cv2.resize(cv2.imread('small_q.png'),(27,27))
r = cv2.resize(cv2.imread('small_r.png'),(27,27))
s = cv2.resize(cv2.imread('small_s.png'),(27,27))
t = cv2.resize(cv2.imread('small_t.png'),(27,27))
u = cv2.resize(cv2.imread('small_u.png'),(27,27))
v = cv2.resize(cv2.imread('small_v.png'),(27,27))
w = cv2.resize(cv2.imread('small_w.png'),(27,27))
x = cv2.resize(cv2.imread('small_x.png'),(27,27))
y = cv2.resize(cv2.imread('small_y.png'),(27,27))
z = cv2.resize(cv2.imread('small_z.png'),(27,27))

#print(w.shape,e.shape,a.shape,l.shape,)
comma = cv2.resize(cv2.imread('comma.png'),(27,27))
end_bracket = cv2.resize(cv2.imread('end_bracket.png'),(27,27))
start_bracket = cv2.resize(cv2.imread('start_bracket.png'),(27,27))
question_mark = cv2.resize(cv2.imread('question_mark.png'),(27,27))
space = cv2.resize(cv2.imread('space.png'),(27,27))
start_quote = cv2.resize(cv2.imread('start_quote.png'),(27,27))
end_quote = cv2.resize(cv2.imread('end_quote.png'),(27,27))
colon = cv2.resize(cv2.imread('colon.png'),(27,27))
fullstop = cv2.resize(cv2.imread('fullstop.png'),(27,27))
slash = cv2.resize(cv2.imread('slash.png'),(27,27))
hestric = cv2.resize(cv2.imread('hestric.png'),(27,27))
hashtag = cv2.resize(cv2.imread('hash.png'),(27,27))
hypen = cv2.resize(cv2.imread('hypen.png'),(27,27))
and1 =  cv2.resize(cv2.imread('and1.png'),(27,27))

one = cv2.resize(cv2.imread('one.png'),(27,27))
two = cv2.resize(cv2.imread('two.png'),(27,27))
three = cv2.resize(cv2.imread('three.png'),(27,27))
four = cv2.resize(cv2.imread('four.png'),(27,27))
five = cv2.resize(cv2.imread('five.png'),(27,27))
six = cv2.resize(cv2.imread('six.png'),(27,27))
seven = cv2.resize(cv2.imread('seven.png'),(27,27))
eight = cv2.resize(cv2.imread('eight.png'),(27,27))
nine = cv2.resize(cv2.imread('nine.png'),(27,27))
zero = cv2.resize(cv2.imread('zero.png'),(27,27))


dd = []

#print(xd[0],(xd[1]),(xd[2]),(xd[3]),(xd[4]),(xd[5]))


def fun(xd):      
    l2=[]

    for i1 in xd:
        l1=[]
        for j1 in i1:
            #print(j1)
            if(ord(j1)==65):
                l1.append(A)
            elif(ord(j1)==66):
                l1.append(B)
            elif(ord(j1)==67):
                l1.append(C)
            elif(ord(j1)==68):
                l1.append(D)
            elif(ord(j1)==69):
                l1.append(E)
            elif(ord(j1)==70):
                l1.append(F)
            elif(ord(j1)==71):
                l1.append(G)
            elif(ord(j1)==72):
                l1.append(H)
            elif(ord(j1)==73):
                l1.append(I)
            elif(ord(j1)==74):
                l1.append(J)
            elif(ord(j1)==75):
                l1.append(K)
            elif(ord(j1)==76):
                l1.append(L)
            elif(ord(j1)==77):
                l1.append(M)
            elif(ord(j1)==78):
                l1.append(N)
            elif(ord(j1)==79):
                l1.append(O)
            elif(ord(j1)==80):
                l1.append(P)
            elif(ord(j1)==81):
                l1.append(Q)
            elif(ord(j1)==82):
                l1.append(R)
            elif(ord(j1)==83):
                l1.append(S)
            elif(ord(j1)==84):
                l1.append(T)
            elif(ord(j1)==85):
                l1.append(U)
            elif(ord(j1)==86):
                l1.append(V)
            elif(ord(j1)==87):
                l1.append(W)
            elif(ord(j1)==88):
                l1.append(X)
            elif(ord(j1)==89):
                l1.append(Y)
            elif(ord(j1)==90):
                l1.append(Z)

            elif(ord(j1)==32):
                l1.append(space)
            elif(ord(j1)==44):
                l1.append(comma)
            elif(ord(j1)==40):
                l1.append(start_bracket)
            elif(ord(j1)==41):
                l1.append(end_bracket)
            elif(ord(j1)==63):
                l1.append(question_mark)
            elif(ord(j1)==39):
                l1.append(start_quote)
            elif(ord(j1)==58):
                l1.append(colon)
            elif(ord(j1)==46):
                l1.append(fullstop)
            elif(ord(j1)==42):
                l1.append(hestric)
            elif(ord(j1)==35):
                l1.append(hashtag)
            elif(ord(j1)==47):
                l1.append(slash)
            elif(ord(j1)==45):
                l1.append(hypen)
            elif(ord(j1) ==38):
                l1.append(and1)

            elif(ord(j1)==97):
                l1.append(a)
            elif(ord(j1)==98):
                l1.append(b)
            elif(ord(j1)==99):
                l1.append(c)
            elif(ord(j1)==100):
                l1.append(d)
            elif(ord(j1)==101):
                l1.append(e)
            elif(ord(j1)==102):
                l1.append(f)
            elif(ord(j1)==103):
                l1.append(g)
            elif(ord(j1)==104):
                l1.append(h)
            elif(ord(j1)==105):
                l1.append(i)
            elif(ord(j1)==106):
                l1.append(j)
            elif(ord(j1)==107):
                l1.append(k)
            elif(ord(j1)==108):
                l1.append(l)
            elif(ord(j1)==109):
                l1.append(m)
            elif(ord(j1)==110):
                l1.append(n)
            elif(ord(j1)==111):
                l1.append(o)
            elif(ord(j1)==112):
                l1.append(p)
            elif(ord(j1)==113):
                l1.append(q)
            elif(ord(j1)==114):
                l1.append(r)
            elif(ord(j1)==115):
                l1.append(s)
            elif(ord(j1)==116):
                l1.append(t)
            elif(ord(j1)==117):
                l1.append(u)
            elif(ord(j1)==118):
                l1.append(v)
            elif(ord(j1)==119):
                l1.append(w)
            elif(ord(j1)==120):
                l1.append(x)
            elif(ord(j1)==121):
                l1.append(y)
            elif(ord(j1)==122):
                l1.append(z)

            elif(ord(j1)==48):
                l1.append(zero)
            elif(ord(j1)==49):
                l1.append(one)
            elif(ord(j1)==50):
                l1.append(two)
            elif(ord(j1)==51):
                l1.append(three)
            elif(ord(j1)==52):
                l1.append(four)
            elif(ord(j1)==53):
                l1.append(five)
            elif(ord(j1)==54):
                l1.append(six)
            elif(ord(j1)==55):
                l1.append(seven)
            elif(ord(j1)==56):
                l1.append(eight)
            elif(ord(j1)==57):
                l1.append(nine)
            
            else:
                l1.append(space)

        #cv2.imshow('frame',cv2.hconcat(l1))
        #print(s1.shape)
        l2.append(cv2.hconcat(l1))
    return(cv2.blur(cv2.resize(cv2.vconcat(l2),(1320,1550)),(2,2)))

global names
names =[]


def img_to_pdf(root):
    with open('E:\\Assignment.pdf','wb') as ff:
        ff.write(img2pdf.convert(names))
        msg.showinfo('Done...','PDF Saved Sucessfully....')

def image(s1,e11):
        print(s1.shape)
        cv2.imwrite(e11,s1)
        names.append(e11)
        #msg.showinfo('Done...','Image Saved Sucessfully....')

def clear(foot,root,tb):
    tb.delete(1.0,END)

def exit1(foot,root):
    foot.destroy()
    root.destroy()

def excess(root):
    foot = Frame(root,height=1000,width=970)
    foot.pack(expand=True)
    tb = Text(foot,height=25,font=(10),width=48,bd=12)
    tb.place(x=180,y=135)
    
    b = Button(foot,text = 'Save as image',width=17,font=('Times',18,'underline'),bd=7,fg='black',command=lambda:pr(root,e1,foot,tb.get("1.0",END)),bg='light blue')
    #b.bind('<Button-1>',bar)
    b.place(x=700,y=647)

    b2 = Button(foot,text = 'Exit',width=10,font=('Times',17,'underline'),command=lambda:exit1(foot,root),bd=7,fg='black',bg='light blue')
    b2.place(x=743,y=135)

    b1 = Button(foot,text = 'Clear',width=10,font=('Times',17,'underline'),command=lambda:clear(foot,root,tb),bd=7,fg='black',bg='light blue')
    b1.place(x=743,y=217)

    b1 = Button(foot,text = 'PDF',width=10,font=('Times',17,'underline'),command=lambda:img_to_pdf(root),bd=7,fg='black',bg='light blue')
    b1.place(x=743,y=303)

    e1 = Entry(foot,width=23,font=('times',17),bd=5)
    e1.place(x=689,y=577)
    
    lb1 = Label(foot,text='Enter Path for Image :',font=('times',14,'underline'),fg='black')
    lb1.place(x=689,y=540)
    
    lb = Label(foot,text='Digital to Hand Written Convertor',font=('times',43,'underline'),fg='blue')
    lb.place(x=112,y=7)

def bar(pro,foot1):
        pro['value']=20
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=40
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=50
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=60
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=80
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=90
        foot1.update_idletasks()
        time.sleep(0.05)

        pro['value']=100
        time.sleep(0.01)

def destroy(foot3):
    foot3.destroy()
    
def pr(root,e11,foot,e1):
    #foot.destroy()
    foot1 = Frame(root,height=0,width=0)
    foot1.place(x=250,y=270)
    pro = Progressbar(foot1,orient='horizontal',length=290,mode='determinate')
    bar(pro,foot1)
    l1 = Label(foot1,text='            Processing.......           ',font=('arial',17,'underline'))
    l1.pack()
    pro.pack(padx=15,pady=35)
    b1 = Button(foot1,text='   ok    ',bd=3,command=lambda :destroy(foot1),font=('arial',10,'underline'))
    b1.place(x=129,y=92)
    
    xd = e1.split('''
''')
    for i1 in xd:
        dd.append(len(i1))
    m1 = max(dd)
    for k1,i1 in enumerate(xd):
        val = m1-len(i1)
        for j1 in range(val):
            xd[k1]=xd[k1]+' '
    
    s1 = fun(xd)
    
    print(e11.get())
    image(s1,e11.get())
    
root = Tk()
#root.geometry('100x87')
#root.title('Digital To HandWritten Convertor')
excess(root)

print(names)

