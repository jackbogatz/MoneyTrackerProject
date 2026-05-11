import csv
from tkinter import *
from tkinter import messagebox

# Keeps track of a money_tracker object
class money_tracker:

    # Creates a money_tracker object with a instance variable, self.total_money, as a dictionary with entry, amount as the key value pairs
    def __init__(self, starting_amount):
        self.total_money = {}
        self.total_money[1] = starting_amount

    # Adds an entry to total_money
    def add_entry(self, week, amount):
        # Adds the entry to self.total_money and creates a new dictionary where it will contain the sorted version of self.total_money
        self.total_money[week] = amount
        sorted_total_money = {}

        # Sorts the entries and then adds each entry to sorted_total_mony 
        sorted_keys = sorted(list(self.total_money.keys()))
        for w in sorted_keys:
            sorted_total_money[w] = self.total_money[w]    
        
        # Reassigns self.total_money with the sorted version 
        self.total_money = sorted_total_money

    # Deltes an entry from self.total_money
    def delete_entry(self, week):
        self.total_money.pop(week)
    
    # Returns the total amount of money stored in a money_tracker object
    def see_total(self):
        total = 0
        for money in self.total_money.values():
            total += money

        return total
    
    def __repr__(self):
        return f'{self.total_money}'

# Creates a Tkinker instance, a menu instance, and a variable to keep track of the money_tracker objects
main = Tk()
menu1 = Menu(main)
ultimate_money_tracker = {}
main.geometry("1100x345")
main.title("Money Holder")
main.config(bg = "white")
main.config(menu = menu1)

# When called upon, it saves the money_tracker objects to a csv file named saved_data.csv
def save_data():
    #  Writes to saved_data.csv 
    with open("saved_data.csv", 'w') as csv_writer:
        writer = csv.writer(csv_writer)
        writer.writerow("Job, Entry, Money".split(','))

        # Writes each mone_tracker object variable to saved_data.csv by writing the job, entry, and money
        for job in ultimate_money_tracker.keys():
            for entry, money in ultimate_money_tracker[job].total_money.items():
                writer.writerow((job, entry, money))

# When called upon, it reads from saved_data.csv and recreates each money_tracker object so the user can pick up where they left off
def load_data():
    try:
        # Opens saved_data.csv and reads each header which contains information about a money_tracker object
        with open("saved_data.csv", 'r') as csv_reader:
            reader = csv.reader(csv_reader)

            # Traverses through each column
            for row in reader:
                # Skips the first row as it is the headers
                if reader.line_num == 1:
                    continue
               # Looks for when entry is 1, as that is when it knows to create a new money_tracker object
                elif row[1] == '1':
                    ultimate_money_tracker[row[0]] = money_tracker(float(row[2]))
                # Adds an entry to the right money_tracker object
                else:
                    ultimate_money_tracker[row[0]].add_entry(int(row[1]), float(row[2]))
   # If the file does not exist, show an error message
    except IOError:
        messagebox.showerror("Error", "You do not have any data to load!")

# Creates the save function 
save = Menu(menu1, tearoff = 0)
save.add_command(label = 'Save', command = save_data)
menu1.add_cascade(label = 'Save here', menu = save)

# Creates the load function
load = Menu(menu1, tearoff = 0)
load.add_command(label = 'Load', command = load_data)
menu1.add_cascade(label = 'Load data', menu = load)

# For Button1
job1 = StringVar()
money1 = StringVar()

# For Button2
job2 = StringVar()
money2 = StringVar()
week2 = StringVar()

# For Button3
job3 = StringVar()
week3 = StringVar()

# For Button4
job4 = StringVar()

# For Button5
job5 = StringVar()

# For Button6
job6 = StringVar()


# Adds an entry to the specified job
def add_to_money_tracker(job, week, amount):
    ultimate_money_tracker[job].add_entry(week, amount)

# Deletes a job from ultimate_money_tracker
def delete_from_ultimate_money_tracker(job):
    ultimate_money_tracker.pop(job)

# Deletes the specified entry 
def delete_entry_from_money_tracker(job, week):
    ultimate_money_tracker[job].delete_entry(week)


# Checks to make sure no one enters the same job in ultimate_money_tracker
def button1check_for_job_registration(job):    
        if len(ultimate_money_tracker) == 0:
            ultimate_money_tracker[job] = money_tracker(float(money1.get()))
            messagebox.showinfo("Message", "You have sucessfully registered this job into our money tracker system!")
        else:
            if job in ultimate_money_tracker:
                    messagebox.showerror("Error", "You already have this job registered!")
            else:
                ultimate_money_tracker[job] = money_tracker(float(money1.get()))
                messagebox.showinfo("Message", "You have sucessfully registered this job into our money tracker system!")

# Checks to make sure the user enters a numeric value
def button1check_for_numeric_input(money):
    try:
        if money == '':
            return True
        float(money)
        return True
    except ValueError:
        messagebox.showerror("Error", "Enter a numeric number!")
        return False

# Checks to make sure the inpu the user enters can be converted to a numeric value
def check_for_numeric_input_for_week(week):
    if week == '':
        return True
    elif not week.isdigit():
        messagebox.showwarning("Warning", "Enter a number!")
        return False
    else:
        return True

# Creates a money_tracker object when clicked
def button1():
    # Creates a window when button1 is clicked and a varaible where it can validate to make the user is typing the appropriate thing to type
    button1_window = Toplevel()
    button1_window.geometry("800x150")
    button1_window.title("Start tracking your money")
    button1_window.config(bg = "White")
    validation = button1_window.register(button1check_for_numeric_input)

    # Creates a Label and tracks what the user says for what job they are registering and creates an Entry that keeps track of 
    # user's input
    Label(button1_window, text = "What job are you tracking this for?", bg = 'White', fg = 'Black', font = ("Times New Roman", 20, "bold")).pack(anchor= 'nw')
    job_ = Entry(button1_window, textvariable = job1, bg = 'white', fg = 'black', relief = SOLID)
    job_.pack(fill=BOTH)
    
    # Creates a Label and tracks what the user says for how much money they are inputing and creates an Entry that keeps track of
    # the users's input
    Label(button1_window, text = "How much money are you inputing? Enter your answer in ###.## format",bg = 'White', fg = 'Black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'w')
    money_ = Entry(button1_window, textvariable = money1, validate = 'key', validatecommand = (validation, "%P"), bg = 'white', fg = 'black', relief = SOLID)
    money_.pack(fill =BOTH)

    # Creates a button that when clicked will check to make sure the user typed in what was expected, and if that is true, then it successfully adds the job as a money_tracker object as a key in ultimate_money_tracker
    # in button1check_forjob_registration, and closes the window
    Button(button1_window, text="Click here if you are all set", bg = 'white', fg = 'black', command = lambda: [button1check_for_job_registration(job1.get()), button1check_for_numeric_input(money1.get()), button1_window.destroy()], relief = SOLID).pack(anchor = 'w')

# Add an entry when clicked
def button2():

    # Adds the entries to the listbox by traversing through ultimate_money_tracker which then unlocks
    # self.total_money because ultimate_money_tracker's key is the job, and its value is the money_tracker object that is associated
    # with that job
    def entry_list(*args):
        listbox2.configure(state = NORMAL)
        listbox2.delete(0, 'end')
        i = 1
        if job2.get() != "Select job":
            for entry in ultimate_money_tracker[job2.get()].total_money.keys():
                listbox2.insert(i, entry)
                i += 1
            listbox2.pack(fill = BOTH)
            listbox2.configure(state = DISABLED)

    # Checks to see if there are no money_tracker objects and shows a messagebox if there are not
    if len([job for job in ultimate_money_tracker]) == 0:
        messagebox.showerror("Error", "You do not have any jobs to add an entry too!")
    else:
        # Creates a window when button2 is clicked and a variable where it can validate to make sure the user is typing the apropriate thing to type
        button2_window = Toplevel()
        button2_window.geometry("1200x500")
        button2_window.title("Create entry")
        button2_window.config(bg = 'White')
        validation = button2_window.register(check_for_numeric_input_for_week)

        # Creates a Label that asks what job the user wants to add an entry to
        Label(button2_window, text = "What job do you want to add an entry to?", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'nw')
        
        # Creates an Option menu that lists what jobs thte user has registered, so they can pick one
        job2.set("Select Job")
        job2.trace_add("write", entry_list)
        droplist2 = OptionMenu(button2_window, job2, *[job for job in ultimate_money_tracker])
        droplist2.pack(fill = BOTH)
       
        # Creates a Label that aks how much money the user is inputting and creates an Entry object that keeps track of what
        # the user enters
        Label(button2_window, text = "How much money are you inputing? Enter your answer in ###.## format", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'w')
        money_ = Entry(button2_window, textvariable = money2, bg = 'white', fg = 'black', relief = SOLID)
        money_.pack(fill = BOTH)
        
        # Creates a Label that asks what number entry this is and then creates another label that will show the user's previous entries
        Label(button2_window, text = "What number entry is this? Enter your answer using these numbers: 2,3,4,5,6,7,8,9 Your first entry is autimatically 1!",bg = 'White', fg = 'Black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'w')
        Label(button2_window, text = "Your previous entries", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(fill = BOTH)
        
        # Creates a Frame for the listbox to appear which will display the user's previous entries
        frame2 = Frame(button2_window, bg = 'black')
        frame2.pack()
        listbox2 = Listbox(frame2, bg = 'white', fg = 'black', font = ("Times New Roman", 15, "bold"))
        
        # Creates an Entry that will keep track of what the user inputs and verify that it is appripriate
        week_ = Entry(button2_window, textvariable = week2, validate = "key", validatecommand = (validation, "%P"), bg = 'white', fg = 'black', relief = SOLID)
        week_.pack(fill = BOTH)

        # Creates a Button that when clicked will add to the money_tracker object
        Button(button2_window, text = "Click here if you are all set", bg = 'white', fg = 'black', command = lambda: [add_to_money_tracker(job2.get(), int(week2.get()), float(money2.get())), messagebox.showinfo("Message", "You have successfully added an entry to your money tracker!"), button2_window.destroy()], relief = SOLID).pack(anchor = 'w')

# Deletes an entry when clicked
def button3():

    # Shows what entry the user wants to delete
    def show_submenu(*args):

         # Creates an OptionmMenu which will display what entry the user wants to delete
        week3.set("Select entry")
        droplist3_2 = OptionMenu(button3_window, week3, [])

        # Creates a Label that displays what entry the user wants to delete from
        Label(button3_window, text = "What entry do you want to delete?", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'w')
        
        # When the user selects a job, the new droplist deletes what was previously there, and adds the new options to it
        if job3.get() != 'Select job':
            droplist3_2['menu'].delete(0, 'end')
            
            entries = [week for week in ultimate_money_tracker[job3.get()].total_money.keys()]
            for week in entries:
                droplist3_2['menu'].add_command(label = week, command = lambda o = week: week3.set(o))

            droplist3_2.pack(fill = BOTH)   

            # Creates a Button that when clicked will successfully the delete the entry  
            Button(button3_window, text = "Click here if you are all set", bg = 'white', fg = 'black', command = lambda: [delete_entry_from_money_tracker(job3.get(), int(week3.get())), messagebox.showinfo("Message", "You have successsfully deleted an entry from your money tracker"), button3_window.destroy()], relief = SOLID).pack(anchor = 'w')


    # If there are not jobs registerred, display a messagebox
    if len([job for job in ultimate_money_tracker]) == 0:
        messagebox.showerror("Error", "You do not have a job to delete an entry for!")
    # If a job does not have any entries meaning a user deleted all of them, display this message ()
    elif any(ultimate_money_tracker[job].total_money == {} for job in ultimate_money_tracker):
        messagebox.showerror("Error", "You do not have any entries to delete.")
    else:
        # Creates a window that will be viewed
        button3_window = Toplevel()
        button3_window.geometry("800x140")
        button3_window.title('Delete entry')
        button3_window.config(bg = 'white')

        # Creates a Label that will display what job the user wants to delete an entry from
        Label(button3_window, text = "What job do you want to delete an entry from?", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'nw')
        
        # Creates an OptionMeny where the user can click on whaat job they want to delete an entry from 
        job3.set("Select job")
        # Constanstly opens show_submenu and enacts whats in there if the condtions are met
        job3.trace_add('write', show_submenu)
        droplist3 = OptionMenu(button3_window, job3, *[job for job in ultimate_money_tracker])
        droplist3.pack(fill = BOTH)
       
# Deletes a job when clicked
def button4():
    # If there are no jobs registered, display this messagebox
    if len([job for job in ultimate_money_tracker]) == 0:
         messagebox.showerror("Error", "You do not have any job registered!")
    else:
        # Creates a window when button4 is clicked
        button4_window = Toplevel()
        button4_window.geometry("1000x80")
        button4_window.title('Delete job')
        button4_window.config(bg = 'white')

        # Creates a Label that displays what job the user wants to delete
        Label(button4_window, text = "What job do you want to delete?", bg = 'white', fg = 'black', font = ("Times New Roman", 20, "bold")).pack(anchor = 'nw')
        
        # Creates an OptionMenu that displays all of the user's jobs
        job4.set("Select job")
        droplist4 = OptionMenu(button4_window, job4, *[job for job in ultimate_money_tracker])
        droplist4.pack(fill = BOTH)
        Button(button4_window, text = "Click here if you are all set", bg = 'white', fg = 'black', command = lambda: [delete_from_ultimate_money_tracker(job4.get()), messagebox.showinfo("Message", "You have successsfully deleted an entry from your money tracker"), button4_window.destroy()], relief = SOLID).pack(anchor = 'w')

# Allows a user to view their earnings when clicked
def button5():

    # If there are no jobs registered, a messagebox is dipsplayed
    if len([job for job in ultimate_money_tracker]) == 0:
        messagebox.showerror("Error", "You do not have any jobs registered!")
    else:
        # Create a window for button5
        button5_window = Toplevel()
        button5_window.geometry("1200x500")
        button5_window.title('Total amount')
        button5_window.config(bg = 'white')

        # Create a Label that displays what jobs the user wants to see
        Label(button5_window, text = "Select the jobs that you want to see how much you have earned:", bg = 'white', fg = 'black', font = ('Times New Roman', 20, 'bold')).pack(fill = BOTH)
       
        # Creates a Frame that the Listbox will surround and the Listbox will list all of the user's job's and their entries
        # meaning their week and the amount they paid that week
        frame5 = Frame(button5_window, bg = 'black')
        frame5.pack(side = TOP)
        listbox5 = Listbox(frame5, bg = 'white', fg = 'black', selectmode = MULTIPLE)
        i = 1
        for job in ultimate_money_tracker:
            listbox5.insert(i, job)
            i += 1
        listbox5.pack(fill = BOTH)

        # Displays a Label that displays how much the user has earned
        def show_me_the_money():
            total = 0
            for i in listbox5.curselection():
                if ultimate_money_tracker[listbox5.get(i)].total_money == {}:
                     messagebox.showerror("Error", "You do not have any entries, and therefore no money from this job!")
                else:
                    total += ultimate_money_tracker[listbox5.get(i)].see_total()

            Label(button5_window, text = f'You have earned ${total}', bg = 'white', fg = 'black', font = ("Times New Roman", 25, 'bold')).pack()
        
        # Creates a Button that when clicked will show the user how much they have made
        Button(button5_window, text = "Finished?", bg = 'white', fg = 'black', command = show_me_the_money).pack(fill = BOTH)

# Lists the user's entries when clicked
def button6():
    # If there are no jobs registered, display this messagebox
    if len([job for job in ultimate_money_tracker]) == 0:
        messagebox.showerror("Error", "You do not have any jobs registered!")
    else:
        # Create a window for button6
        button6_window = Toplevel()
        button6_window.geometry("1000x500")
        button6_window.title('View your entries')
        button6_window.config(bg = 'white')

        # Create a Label for the entries
        Label(button6_window, text = "Select your jobs to see all of your entries:", bg = 'white', fg = 'black', font = ("Times New Roman", 20, 'bold')).pack(fill = BOTH)  
        
        # Create a Frame for the Listbox which will display all of the user's jobs
        frame6 = Frame(button6_window, bg = 'black')
        frame6.pack()
        listbox6 = Listbox(frame6, bg = 'white', fg = 'black', selectmode = MULTIPLE)
        i = 1
        for job in ultimate_money_tracker:
            listbox6.insert(i, job)
            i += 1
        listbox6.pack(fill = BOTH)
    
        # Creates a Label that contains all of the user's entries meaning their job and their week and their amount
        def view_entries():
            entries = ''
            for job in listbox6.curselection():
                entry = ultimate_money_tracker[listbox6.get(job)].total_money
                if entry == {}:
                    messagebox.showerror("Error", "You do not have any entries for this job!")
                else:
                    for entry, amount in entry.items():
                        entries += f'Job: {listbox6.get(job)}, Entry: {entry}, Amount: ${amount}\n'
        
                    Label(button6_window, text = entries, bg = 'white', fg = 'black', font = ("Times New Roman", 20, 'bold')).pack()
    
        # When clicked, it displays the user's entries
        Button(button6_window, text = "Finished?", command = view_entries, bg ='white', fg = 'black').pack(fill = BOTH)
    

# Creates a Welcome Label
label1 = Label(main, text = "Welcome! Please Load in your data if you have used this tracker system before!", bg = 'white', fg = 'blue', font = ("Times New Roman", 30, 'italic'), relief = SOLID).pack()

# Creates a Button that will start registering 
Button1 = Button(main, text = "Click here to start tracking your money", command = button1, relief = SOLID, font = ("Times New Roman", 16, "bold")).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)

# Creates a Button that will add an entry to a registered job
Button2 = Button(main, text = 'Click here to add an entry to your money tracker ', command = button2, relief = SOLID, font = ("Times New Roman", 16, "bold")).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)

# Creates a Button that will delete an entry from a registered job
Button3 = Button(main, text = "Click here to delete an entry", command = button3, relief = SOLID, font = ("Times New Roman", 16, "bold", )).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)

# Creates a Button that will delete a registered job
Button4 = Button(main, text = "Click here to delete a job", command = button4, relief = SOLID, font = ("Times New Roman", 16, "bold")).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)

# Creates a Button that will allow the user to see their total amount that they have earned
Button5 = Button(main, text = 'Click here to see the total amount you have stored ', command = button5, relief = SOLID, font = ("Times New Roman", 16, "bold")).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)

# Creates a Button that will allow a user to view all of their entries
Button6 = Button(main, text = 'Click here to view all entries', command = button6, relief = SOLID, font = ("Times New Roman", 16, 'bold')).pack(fill = BOTH)

# Creates a blank Label to create space
Label(main, bg = 'white').pack(fill= BOTH)


# Allows the tkinker instance to run
main.mainloop()