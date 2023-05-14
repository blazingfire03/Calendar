from tkinter import *
import calendar
#function to display calendar
def DisplayCalendar():
  newRoot=Tk()
  newRoot.title('CalendarScreen')
  newRoot.config(bg='light blue')
  newRoot.geometry('700x700')
  actualyear=int(yearEntry.get())
  calendarContent= calendar.calendar(actualyear)
  lblNew=Label(newRoot, text=calendarContent,font='Consolas 10 bold')
  lblNew.grid(row=0,column=0,padx=30,pady=30)
  newRoot.mainloop()
  

#design first window
root=Tk()
root.title('Calendar App')
root.geometry("400x400")

header = Label(root, text= 'CALENDAR', bg='light pink', fg='brown', font=('times',32,'bold'))
header.grid(row=0, column=0, padx=25, pady=25)

lbl = Label(root, text='Enter the year: ')
lbl.grid(row=1, column=0, padx=25)

yearEntry = Entry(root, width=5)
yearEntry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = Button(root, text='Show Calendar', fg= 'dark green', command=DisplayCalendar)
showcalendar.grid(row=3, column=0, padx=25)
showcalendar=Button(root,text='Show Calendar', fg='black')
command=DisplayCalendar()
showcalendar.grid(row=3,column=0,padx=25)
exitButton=Button(root,text='Exit',fg='purple',command=root.destroy)
exitButton.grid(row=4,column=0,padx=25)
root.mainloop()

