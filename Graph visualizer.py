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
def bipartite_graph():
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
def star_graph():
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
def complete_graph():
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
def cycle_graph():
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
def path_graph():
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
def normal_graph():
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
        normal_graph()
    if clicked.get()=="Path graph":
        path_graph()
    if clicked.get()=="Cycle graph":
        cycle_graph()
    if clicked.get()=="Star graph":
        star_graph()
    if clicked.get()=="Complete graph":
        complete_graph()
    if clicked.get()=="Bipartite graph":
        bipartite_graph()


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

