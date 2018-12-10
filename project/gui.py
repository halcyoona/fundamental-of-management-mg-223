import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from file import *

# import tkMessageBox
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
direcor = []
manager = []
op = []
staff =[]
reg = []
prod = []
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.Fobj = functionalStructure()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, width=500, height=500, bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, FunctionalStructure, FunctionalStructure1, FunctionalStructure2, FunctionalStructure3, GeographicalStructure, GeographicalStructure1, GeographicalStructure2, GeographicalStructure3, GeographicalStructure4, MarketBaseStructure, ProductStructure, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()





class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Function Structure", width = 20,
                            command=lambda: controller.show_frame("FunctionalStructure"))
        button2 = tk.Button(self, text="Geographical Structure", width = 20,
                            command=lambda: controller.show_frame("GeographicalStructure"))
        button3 = tk.Button(self, text="MarketBase Structure", width = 20,
                            command=lambda: controller.show_frame("MarketBaseStructure"))
        button4 = tk.Button(self, text="Product Structure",width = 20,
                            command=lambda: controller.show_frame("ProductStructure"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()





class FunctionalStructure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.obj1 = functionalStructure()
        label = tk.Label(self, text="Add Director")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("FunctionalStructure1"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def on_button(self):
        v = self.e1.get()
        v = "Director : "+v
        direcor.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)


class FunctionalStructure1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.obj1 = functionalStructure()
        label = tk.Label(self, text="Add Manager")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("FunctionalStructure2"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def on_button(self):
        v = self.e1.get()
        v = "Manager : "+v
        manager.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)



class FunctionalStructure2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.obj1 = functionalStructure()
        label = tk.Label(self, text="Add Operational Manager")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("FunctionalStructure3"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def on_button(self):
        v = self.e1.get()
        v = "OP : "+v
        op.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)

class FunctionalStructure3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.obj1 = functionalStructure()
        label = tk.Label(self, text="Add Staff")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Draw graph", width=15, command=self.draw_graph)
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def on_button(self):
        v = self.e1.get()
        v = "staff : "+v
        staff.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)

    def draw_graph(self):
    	obj = functionalStructure()
    	obj.addDirector(direcor)
    	obj.addManager(manager)
    	obj.addOperationalManager(op)
    	obj.addStaff(staff)
    	obj.drawGraph()



class GeographicalStructure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Region")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("GeographicalStructure1"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()

    def on_button(self):
        v = self.e1.get()
        v = "Region : "+v
        reg.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)


class GeographicalStructure1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Product")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("GeographicalStructure2"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()

    def on_button(self):
        v = self.e1.get()
        v = "prod : "+v
        prod.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)


class GeographicalStructure2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Manager")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("GeographicalStructure3"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()

    def on_button(self):
        v = self.e1.get()
        v = "Manager : "+v
        manager.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)


class GeographicalStructure3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Operational Manager")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Go to the next page", width=15, command=lambda: controller.show_frame("GeographicalStructure4"))
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()

    def on_button(self):
        v = self.e1.get()
        v = "op : "+v
        op.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)


class GeographicalStructure4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.obj1 = functionalStructure()
        label = tk.Label(self, text="Add Staff")
        label.pack( fill="x", pady=10)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        button1 = tk.Button(self, text='Show', command=self.on_button, width=15)
        button2 = tk.Button(self, text="Draw graph", width=15, command=self.draw_graph)
        button3 = tk.Button(self, text="Go to the start page", width=15, command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def on_button(self):
        v = self.e1.get()
        v = "staff : "+v
        staff.append(v)
        label = tk.Label(self, text=v)
        label.pack( fill="x", pady=10)

    def draw_graph(self):
    	obj = GeographicStructure()
    	obj.addRegion(reg)
    	obj.addProduct(prod)
    	obj.addManager(manager)
    	obj.addOperationalManager(op)
    	obj.addStaff(staff)
    	obj.drawGraph()



class MarketBaseStructure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class ProductStructure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()





class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()






if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()