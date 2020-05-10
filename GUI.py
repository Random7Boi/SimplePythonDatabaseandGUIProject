from tkinter import *
from PIL import ImageTk,Image
from main import *
import os

os.system('cls') # clears the terminal from code, use 'clear' on linux/Mac

root = Tk()
root.title('Python SQLite3 Ktinker Project!')
root.iconbitmap('Images/queue-24px.ico')
root.geometry("400x600")

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
email = Entry(root, width=30)
email.grid(row=2, column=1)
address = Entry(root, width=30)
address.grid(row=3, column=1)
city = Entry(root, width=30)
city.grid(row=4, column=1)
state = Entry(root, width=30)
state.grid(row=5, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
city_label = Label(root, text="City")
city_label.grid(row=4, column=0)
state_label = Label(root, text="State")
state_label.grid(row=5, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=6, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=10, column=0, pady=5)

# add items to record from GUI
def addToRecord():

    # call insert function from database script
    firstName = f_name.get()
    lastName = l_name.get()
    emailAddress = email.get()
    _address = address.get()
    _city = city.get()
    _state = state.get()
    _zipcode = zipcode.get()
    insert(firstName, lastName, emailAddress, _address, _city, _state, _zipcode)

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    email.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# query the items for display to GUI
def Query():

    output = show_query()
    query_label = Label(root, text=output)
    query_label.grid(row=13, column=0, columnspan=2)

# insert the delete record ID from GUI to delete function
def Remove():

    removalNumber = delete_box.get()
    delete(removalNumber)
    delete_box.delete(0, END)

# function to create a second GUI to use the update function with
def Modify():

    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.iconbitmap('Images/queue-24px.ico')
    editor.geometry("400x300")

    #Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global email_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global editor_delete_box

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    email_editor = Entry(editor, width=30)
    email_editor.grid(row=2, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=4, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=5, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=6, column=1)

    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    email_label = Label(editor, text="Email")
    email_label.grid(row=2, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=3, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=4, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=5, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=6, column=0)

    # create an order ID entry and label
    editor_delete_box = Entry(editor, width=30)
    editor_delete_box.grid(row=8, column=1, pady=5)
    editor_delete_box_label = Label(editor, text="Select ID")
    editor_delete_box_label.grid(row=8, column=0, pady=5)

    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Save Record", command=Modifier)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# function to call the update function and close the second window
def Modifier():

    update(editor_delete_box.get(), f_name_editor.get(), l_name_editor.get(), email_editor.get(), address_editor.get(), city_editor.get(), state_editor.get(), zipcode_editor.get())
    editor.destroy()
    root.deiconify()

# Create Submit Button 
submit_btn = Button(root, text="Add Record To Database", command = addToRecord)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query 
query_btn = Button(root, text="Show Records", command = Query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command = Remove)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command = Modify)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

createDatabase()

root.mainloop()