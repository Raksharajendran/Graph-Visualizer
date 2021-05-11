from pyvis.network import Network
from tkinter import *
from itertools import combinations
from collections import namedtuple
from functools import partial
import numpy as np
from tkinter import messagebox as m_box


                             #show functionality
def show3(graph, output_filename):
    g = Network(directed=False)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)

def show(graph, output_filename):
    g = Network(directed=True)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)
    return g

def show_adj(graph):
    adj1=adjacency_dict(graph)
    adj2=adjacency_matrix(graph)
    window = Tk()
    label_w1 = Label(window, text="The dict representation is:", bg="black", fg="salmon",font=("Comic Sans MS", 15, "bold")).pack()
    label_w = Label(window, text=adj1, fg="black", bg="white", font=("Comic Sans MS", 15, "bold"))
    label_w.pack()
    label_w2 = Label(window, text="The matrix representation is:", bg="black", fg="salmon",font=("Comic Sans MS", 15, "bold")).pack()
    label_w1 = Label(window, text=adj2, fg="black", bg="white", font=("Comic Sans MS", 15, "bold"))
    label_w1.pack()

            #Functoins defined for specific graphs

def adjacency_matrix(graph):
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] = 1
    return adj

def adjacency_dict(graph):
    adj= { node:[] for node in graph.nodes}
    for edge in graph.edges:
        node1,node2= edge[0],edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj

#Bipartite Graph
def do_this6():
    text6 = entry.get()
    edges = []
    if text6 == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res = eval(text6)
            net = Network()
            Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
            n=res//2
            for i in range(n):
                for j in range(n,n+n):
                    edges.append((i,j))
            nodes = range(res)
            G = Graph(nodes, edges,is_directed=True)
            show3(G, "bipartite.html")
            show_adj(G)
        except:
            m_box.showwarning('WARNING', 'Please enter proper nodes')


#Star Graph
def do_this5():
    text4 = entry.get()
    if text4 == '':
        m_box.showerror('ERROR', 'Please fill in !')
    else:
        try:
            res4 = eval(text4)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res4 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
                nodes = range(res4)
                edges = [(0, i) for i in range(1, res4)]
                G = Graph(nodes, edges,is_directed=True)
                show_adj(G)
                show(G, "star path.html")

#Complete graph
def do_this4():
    text3 = entry.get()
    if text3=='':
        m_box.showerror('ERROR','Please fill in !')
    else:
        try:
            res3 = eval(text3)
        except:
            m_box.showerror('ERROR','Enter only POSITIVE DIGITS !')
        else:
            if res3 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
                nodes = range(res3)
                edges = list(combinations(nodes, 2))
                G = Graph(nodes, edges,is_directed=True)
                show(G, "complete path.html")
                show_adj(G)


#cycle function
def do_this3():
    text2 = entry.get()
    if text2 == '':
        m_box.showerror('ERROR', 'Please fill in !')
    else:
        try:
            res2 = eval(text2)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res2 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
                nodes = range(res2)
                edges = [(i, i + 1) for i in range(res2 - 1)]
                G = Graph(nodes, edges,is_directed=True)
                G.edges.append((res2 - 1, 0))
                show(G, "cycle path.html")
                show_adj(G)



#path function
def do_this2():
    text1 = entry.get()
    if text1 == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res1 = eval(text1)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res1 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
                nodes = range(res1)
                edges = [(i, i + 1) for i in range(res1 - 1)]
                G = Graph(nodes, edges,is_directed=True)
                show(G, "path.html")
                show_adj(G)


#Normal graph
def doo_this():
    text= entry.get()
    edges = []
    count = 0
    if text == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res = eval(text)
            for i in res:
                edges.append(i)
                count += 1
            net = Network()
            Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
            nodes = range(count - 1)
            G = Graph(nodes, edges,is_directed=True)
            show(G, "basic.html")
            show_adj(G)
        except:
            m_box.showwarning('WARNING', 'Please enter proper nodes')


                 #Designing of buttons

                 #Setting up Tkinter module

root = Tk()
root.title("Graph theory")
root.config(bg="light coral")
label_tit = Label(root,text="Graph Visualizer",bg="peach puff",fg="black",font=("Calibri",35,"bold","italic"))
label_tit.grid(row=0,column=8,pady=15)

# Adjust size
root.geometry("400x900")
c=Canvas(root,height=250,width=250)
c.grid(row=20,column=8,pady=15)
filename = PhotoImage(file="C:\\Users\\Dell\\Downloads\\graph1.png")
c.create_image(10,10,anchor=NW,image=filename)

# Change the label text
def show1():
    if clicked.get()=="Normal graph":
        doo_this()
    if clicked.get()=="Path graph":
        do_this2()
    if clicked.get()=="Cycle graph":
        do_this3()
    if clicked.get()=="Star graph":
        do_this5()
    if clicked.get()=="Complete graph":
        do_this4()
    if clicked.get()=="Bipartite graph":
        do_this6()


options = [
    "Normal graph",
    "Cycle graph",
    "Path graph",
    "Star graph",
    "Complete graph",
    "Bipartite graph"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Normal graph")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.config(width=15,bg="orange",fg="black",font=("Comic Sans MS",20,"bold"))
drop.grid(row=2,column=8,pady=15)

label1=Label(root,text="Enter the number of nodes:",fg="black",bg="pale turquoise",font=("Comic Sans MS",20,"bold"))
label1.grid(row=3,column=8,pady=15)
entry = Entry(root,width=36)
entry.grid(row=4,column=8,ipady=3)


# Create button, it will change label text
button_drop = Button(root, text="Submit",fg="salmon",bg="black", command=show1,font=("Comic Sans MS",15,"bold"))
button_drop.grid(row=5,column=8,pady=15)

# Creating the Label
label_drop = Label(root, text=" ")
label_drop.grid(row=9,column=8,pady=15)

root.mainloop()




'''from pyvis.network import Network
from tkinter import *
from itertools import combinations
from collections import namedtuple
from tkinter import messagebox as m_box


window = Tk()
window.geometry("800x700")

               #Inserting the image in tkinter
c=Canvas(window,bg="gray16",height=200,width=200)
filename=PhotoImage(file="C:\\Users\\Dell\\OneDrive\\Pictures\\graphtheory.png")
background_label=Label(window,image=filename)
background_label.place(x=0,y=0 ,relwidth=1,relheight=1)
c.grid(row=0,column=0)

             #Label for the window
window.title("Graph theory")
label = Label(window,text="Graph Visualizer",bg="yellow",fg="purple",font=("Calibri",35,"bold","italic"))
label.grid(row=0,column=2,sticky='n')

lbl = Label(window, text="Enter the number of nodes",bg="black",fg="white",font=("Comic Sans MS",20,"bold","italic"))
lbl.grid(row=1,column=2)

#show functionality
def show(graph, output_filename):
    g = Network(directed=True)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)
def show3(graph, output_filename):
    g = Network(directed=False)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)


#entry
label_nor=Label(window,text="NORMAL GRAPH",bg="salmon",fg="black",font=("Courier",20,"bold"))
label_nor.grid(row=2,column=1,pady=15)
entry2 = Entry(window,width=36)
entry2.grid(row=2,column=2,ipady=3)

#entry
label_path=Label(window,text="PATH GRAPH",bg="salmon",fg="black",font=("Courier",20,"bold"))
label_path.grid(row=3,column=1,pady=15)
entry3=Entry(window,width=36)
entry3.grid(row=3,column=2,ipady=3)

#entry
label_cycle=Label(window,text="CYCLE GRAPH",bg="salmon",fg="black",font=("Courier",20,"bold"))
label_cycle.grid(row=4,column=1,pady=15)
entry4=Entry(window,width=36)
entry4.grid(row=4,column=2,ipady=3)

#entry
label_comp=Label(window,text="COMPLETE GRAPH",bg="salmon",fg="black",font=("Courier",20,"bold"))
label_comp.grid(row=5,column=1,pady=15)
entry5=Entry(window,width=36)
entry5.grid(row=5,column=2,ipady=3)


#entry
label_star=Label(window,text="STAR GRAPH",bg="salmon",fg="black",font=("Courier",20,"bold"))
label_star.grid(row=6,column=1,pady=15)
entry6=Entry(window,width=36)
entry6.grid(row=6,column=2,ipady=3)

label_us= Label(window,text="By,Raksha and Niranjani....!",fg="saddle brown",bg="lavender",font=("Comic Sans MS",20,"bold","italic"))
label_us.grid(row=10,column=2)
            #Functoins defined for specific buttons
def adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph.
    Assumes that graph.nodes is equivalent to range(len(graph.nodes)).
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    print(adj)
#star graph
def do_this5():
    text4 = entry6.get()
    if text4 == '':
        m_box.showerror('ERROR', 'Please fill in !')
    else:
        try:
            res4 = eval(text4)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res4 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])
                nodes = range(res4)
                edges = [(0, i) for i in range(1, res4)]
                G = Graph(nodes, edges,is_directed=True)
                show(G, "star path.html")
                adjacency_matrix(G)

#complete graph
def do_this4():
    text3 = entry5.get()
    if text3=='':
        m_box.showerror('ERROR','Please fill in !')
    else:
        try:
            res3 = eval(text3)
        except:
            m_box.showerror('ERROR','Enter only POSITIVE DIGITS !')
        else:
            if res3 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges"])
                nodes = range(res3)
                edges = list(combinations(nodes, 2))
                G = Graph(nodes, edges)
                show(G, "complete path.html")


#cycle function
def do_this3():
    text2 = entry4.get()
    if text2 == '':
        m_box.showerror('ERROR', 'Please fill in !')
    else:
        try:
            res2 = eval(text2)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res2 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges"])
                nodes = range(res2)
                edges = [(i, i + 1) for i in range(res2 - 1)]
                G = Graph(nodes, edges)
                G.edges.append((res2 - 1, 0))
                show(G, "cycle path.html")



#path function
def do_this2():
    text1 = entry3.get()
    if text1 == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res1 = eval(text1)
        except:
            m_box.showerror('ERROR', 'Enter only POSITIVE DIGITS !')
        else:
            if res1 < 0:
                m_box.showwarning('WARNING', 'Enter POSITIVE DIGITS !')
            else:
                net = Network()
                Graph = namedtuple("Graph", ["nodes", "edges"])
                nodes = range(res1)
                edges = [(i, i + 1) for i in range(res1 - 1)]
                G = Graph(nodes, edges)
                show(G, "path.html")

def do_this():
    text = entry2.get()
    if text == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res = eval(text)
            net = Network()
            Graph1 = namedtuple("Graph",["nodes"])
            nodes = range(res)
            G1=Graph1(nodes)
            show3(G1,"bipartite")
        except:
            m_box.showwarning('WARNING', 'Please enter proper nodes')

#normal graph
def do_this():
    text = entry2.get()
    edges = []
    count = 0
    if text == '':
        m_box.showerror('Error', 'Please fill in !')
    else:
        try:
            res = eval(text)
            net = Network()
            Graph = namedtuple("Graph", ["nodes", "edges"])
            n=res//2
            for i in range(n):
                for j in range(n,n+n):
                    edges.append((i,j))
            print(edges)
            nodes = range(res)
            G = Graph(nodes, edges)
            show3(G, "basic.html")
        except:
            m_box.showwarning('WARNING', 'Please enter proper nodes')


                 #Designing of buttons

#button 1
my_btn = Button(window, text="Submit", command=do_this,bg="powder blue",fg="black",font=("Comic Sans MS",15,"bold","italic"))
my_btn.grid(row=2,column=5)
#button 2
my_btn2= Button(window,text="Submit",command=do_this2,bg="powder blue",fg="black",font=("Comic Sans MS",15,"bold","italic"))
my_btn2.grid(row=3,column=5)

#button 3
my_btn3= Button(window,text="Submit",command=do_this3,bg="powder blue",fg="black",font=("Comic Sans MS",15,"bold","italic"))
my_btn3.grid(row=4,column=5)

#button 4
my_btn4=Button(window,text="Submit",command=do_this4,bg="powder blue",fg="black",font=("Comic Sans MS",15,"bold","italic"))
my_btn4.grid(row=5,column=5)

#button 5
my_btn5=Button(window,text="Submit",command=do_this5,bg="powder blue",fg="black",font=("Comic Sans MS",15,"bold","italic"))
my_btn5.grid(row=6,column=5)

window.mainloop()'''