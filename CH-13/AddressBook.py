"""
rev: 1
class: CSC102
author: jonathan reiter
description: GUI version of a roladex
reference: 
reference: 

"""

import re
import pickle
import os.path
import tkinter as tkin
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox   


##############
##  COLORS  ##
##############
BLK = "\033[30m"      # black
RED = "\033[31m"      # red
GRN = "\033[32m"      # green
YLW = "\033[33m"      # yellow
BLU = "\033[34m"      # blue
MAG = "\033[35m"      # magenta
CYN = "\033[36m"      # cyan
WHT = "\033[37m"      # white
NC  = "\033[39m"      # reset




class Address:
    """This class creates the objects for saving a contact record into the DB"""
    def __init__(self, name, street, city, state, zip):
        """Initializer function""" 
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class AddressBook:
    """This class creates the GUI with all the required widgets and function calls"""
    def __init__(self):
        """Initializer function""" 
        window = tkin.Tk() # Create a window
        window.title("AddressBook") # Set title

        self.nameVar = tkin.StringVar()
        self.streetVar = tkin.StringVar()
        self.cityVar = tkin.StringVar()
        self.stateVar = tkin.StringVar()
        self.zipVar = tkin.StringVar()

        #############
        ## Frame 1 ##
        #############
        frame1 = tkin.Frame(window)
        frame1.pack()
        tkin.Label(frame1, text = "Name").grid(row = 1, 
                                               column = 1, 
                                               sticky = tkin.W)
        
        tkin.Entry(frame1, textvariable = self.nameVar, width = 40).grid(row = 1, column = 2)
        
        #############
        ## Frame 2 ##
        #############
        frame2 = tkin.Frame(window)
        frame2.pack()
        
        tkin.Label(frame2, text = "Street").grid(row = 1, 
                                                 column = 1, 
                                                 sticky = tkin.W)
        
        tkin.Entry(frame2, textvariable = self.streetVar, width = 40).grid(row = 1, column = 2)
            
        
        #############
        ## Frame 2 ##
        #############
        frame3 = tkin.Frame(window)
        frame3.pack()
        tkin.Label(frame3, text = "City", width = 5).grid(row = 1, 
                                                          column = 1, 
                                                          sticky = tkin.W)
        
        tkin.Entry(frame3, textvariable = self.cityVar).grid(row = 1, column = 2)
        tkin.Label(frame3, text = "State").grid(row = 1, 
                                                column = 3, sticky = tkin.W)
        
        tkin.Entry(frame3, textvariable = self.stateVar, width = 5).grid(row = 1, column = 4)
        tkin.Label(frame3, text = "ZIP").grid(row = 1, 
                                              column = 5, 
                                              sticky = tkin.W)
                                              
        tkin.Entry(frame3, textvariable = self.zipVar, width = 5).grid(row = 1, column = 6)
        

        #############
        ## Frame 4 ##
        #############
        frame4 = tkin.Frame(window)
        frame4.pack()
        btnAdd = tkin.Button( frame4, 
                              text="Add",
                              fg="blue",
                              command=self.processAdd).grid(row = 1, column = 1)

        btnFrst = tkin.Button(frame4, 
                              text="First",
                              fg="red",
                              command=self.processFirst).grid(row = 1, column = 2)

        btnNext = tkin.Button(frame4, 
                              text="Next",
                              fg="dark grey", 
                              command=self.processNext).grid(row = 1, column = 3)

        btnPrev = tkin.Button(frame4, 
                              text="Previous",
                              fg="dark blue", 
                              command=self.processPrevious).grid(row = 1, column = 4)

        btnLast = tkin.Button(frame4, 
                              text="Last",
                              fg="purple",
                              command=self.processLast).grid(row = 1, column = 5)
        
        btnImport = tkin.Button(frame4,
                                text="Import",
                                fg="dark blue",
                                command=self.importFile).grid(row=1, column=6)
        
        btnExport = tkin.Button(frame4,
                                text="Export",
                                fg="red",
                                command=self.exportFile).grid(row=1, column=7)

        self.addressList = self.loadAddress()
        self.current = 0
      
        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop() # Create an event loop



    def exportFile(self):
        """Exports the current DB and allows the user to choose where to save the file"""


        file_name = asksaveasfilename(defaultextension=".html",
                                      filetypes=(("HTML files",".html"),("All files","*.*"))
                                     )

        html = """
<html>
  <head>
    <title>Address Book</title>
  </head>
  <body>
    <style> table, th, td { border: 1px solid black; } </style>
  <table border="2" cellspacing="2" cellpadding="2" >
    <tr>
      <th>Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Zip</th>
    </tr>"""

        more = """
<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</td>"""

        closing_tags = """
  </table>
  </body>
</html>"""


        with open(file_name, "w") as wf:
            wf.seek(0)
            wf.write(html)
            for record in self.addressList:
                wf.write(more.format(record.name, 
                                     record.street, 
                                     record.city, 
                                     record.state, 
                                     record.zip))
            wf.write(closing_tags)
            
        wf.close()



    def importFile(self):
        """Function for importing a file of records"""

        file_name = askopenfilename(filetypes=(("Text files","*.txt"),("All files","*.*")),
                                   title="Choose a file"
                                   )

        print("Opening file {} as read only...".format(file_name))
        
        contacts = []

        with open(file_name, 'r') as infile:
            stuff = infile.readlines()
            #print("{}printing the contents of the file{}".format(YLW, NC))
            #print("{}{}{}".format(MAG, stuff, NC))
            #print(len(stuff), NC)
            #print(type(stuff))

            for thing in stuff:
                if thing.strip() != '':
                    #print(YLW, thing.strip(), NC)
                    contacts.append(thing.strip())
                else:
                    print("{}[+]{} Successfully loaded record: {}".format(GRN, WHT, NC))
                    print("{}   {}{}".format(GRN, contacts, NC))
                    print("\n{}[!] PROCESSING NEXT RECORD{}\n".format(RED, NC))

                    addy = Address(contacts[0], contacts[1], contacts[2], contacts[3], contacts[4])
                    self.addressList.append(addy)
                    self.saveAddress()
                    contacts.clear()

                    
            

        infile.close()


    def saveAddress(self):
        """Function that saves addresses"""
        outfile = open("address.dat", "wb")
        pickle.dump(self.addressList, outfile)
        tkinter.messagebox.showinfo("Address saved", "A new address is saved")
        outfile.close()


    def loadAddress(self):
        """Function that loads addresses from a file"""
        if not os.path.isfile("address.dat"):
            return [] # Return an empty list

        try:
            infile = open("address.dat", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []
            
        infile.close()
        return addressList


    def processAdd(self):
        """Adds the current information in the text boxes into the DB"""
        address = Address(self.nameVar.get(), 
            self.streetVar.get(), self.cityVar.get(), 
            self.stateVar.get(), self.zipVar.get())
        self.addressList.append(address)
        self.saveAddress()


    def processFirst(self):
        """Jumps to the first record found in the DB"""
        self.current = 0
        self.setAddress()
    

    def processNext(self):
        """Jumps to the next record found in the DB"""
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()
    

    def processPrevious(self):
        """Jumps to the previous record found in the DB"""
        if self.current > 0 :
            self.current -= 1
            self.setAddress()


    def processLast(self):
        """Jumps to the last record found in the DB"""
        if len(self.addressList) == 0:
            pass
        else:
            self.current = len(self.addressList) - 1
            self.setAddress()


    def setAddress(self):
        """Sets the current address"""
        self.nameVar.set(self.addressList[self.current].name)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)

AddressBook() # Create GUI
