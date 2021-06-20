import tkinter as tk

def submit():
    plyr1 = player1_var.get()
    plyr2 = player2_var.get()

    print("Player1 : " + plyr1)
    print("Player2 : " + plyr2)
    root.quit()
    player1_var.set("")
    player2_var.set("")


root = tk.Tk()

# setting the windows size
root.geometry("300x100")

# declaring string variable
player1_var = tk.StringVar()
player2_var = tk.StringVar()

player1_label = tk.Label(root, text='Player1', font=('calibre', 10, 'bold'))

player1_entry = tk.Entry(root, textvariable=player1_var, font=('calibre', 10, 'normal'))

player2_label = tk.Label(root, text='Player2', font=('calibre', 10, 'bold'))

player2_entry = tk.Entry(root, textvariable=player2_var, font=('calibre', 10, 'normal'))


sub_btn = tk.Button(root, text='Start Game', command=submit)

player1_label.grid(row=0, column=0)
player1_entry.grid(row=0, column=1)
player2_label.grid(row=1, column=0)
player2_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)




# performing an infinite loop
# for the window to display
root.mainloop()
