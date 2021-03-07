import pyshorteners
from tkinter import *
import clipboard

root = Tk()
root.title("Url Shortner")
root.geometry("450x200")

#creating a function for shorting url
def url_shortner():
    try:
        short = pyshorteners.Shortener()
        main_url = unshorted_url.get()
        shorted_url = short.tinyurl.short(main_url)
        short_url.set(shorted_url)
        display_url = Label(root, text=shorted_url,background="lightgreen",font=16)
        display_url.grid(row=2,column=0, pady=5)
        unshorted_url.delete(0,END)

    except:
        unshorted_url.set("Enter url!!")


# function for copy url
def copy_url():
    try:
        clipboard.copy(short_url.get())
        copied = Label(root,text="Url Copy Successfully", background="yellow")
        copied.grid(row=3,column=1,pady=5)
    except:
        copied_failed = Label(root, text="Something went wrong try again !",background="red")
        copied_failed.grid(row=3,column=1)



# main brand name
company = Label(root, text="Url Shortner By Geeky Asif",font=50)
company.grid(row=0,column=0, padx=20,pady=10)

# creating input for url
unshorted_url = StringVar()
unshorted_url.set("Enter Url ")
unshorted_url_entry = Entry(root, textvariable=unshorted_url, font=16)
unshorted_url_entry.grid(row=1,column=0, pady=5)


# creating button to create url
shorting_url_btn = Button(text="Short Url", command=url_shortner,padx=20,pady=5, background="red")
shorting_url_btn.grid(row=1,column=1, pady=5)

# creating a variable for displaying the shorted url
short_url = StringVar()
short_url_label = Label(root,text="No url Found !", background="lightgreen",font=16)
short_url_label.grid(row=2,column=0, pady=5)

# url copy btn
url_copy_btn = Button(root, text="Copy Url" ,command=copy_url, background="lightblue")
url_copy_btn.grid(row=2, column=1, pady=5)


root.mainloop()


