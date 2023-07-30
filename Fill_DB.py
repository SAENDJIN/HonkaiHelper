import sqlite3
import tkinter as tk
from tkinter import messagebox


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS artifacts (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Characters TEXT NOT NULL,
                    Element TEXT NOT NULL,
                    Rare TEXT NOT NULL,
                    Relicts TEXT NOT NULL,
                    Ormnaments TEXT NOT NULL,
                    Head TEXT NOT NULL,
                    Gloves TEXT NOT NULL,
                    Body TEXT NOT NULL,
                    Feet TEXT NOT NULL,
                    Sphere TEXT NOT NULL,
                    Link TEXT NOT NULL,
                    Sub_Stat_1 TEXT NOT NULL,
                    Sub_Stat_2 TEXT NOT NULL,
                    Sub_Stat_3 TEXT NOT NULL,
                    Sub_Stat_4 TEXT NOT NULL
                )''')
    conn.commit()


def insert_data(conn, characters, element, rare, relicts, ormnaments, head, gloves, body, feet, sphere, link,
                sub_stat_1, sub_stat_2, sub_stat_3, sub_stat_4):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO artifacts (Characters, Element, Rare, Relicts, Ormnaments, Head, Gloves, Body, Feet,
                      Sphere, Link, Sub_Stat_1, Sub_Stat_2, Sub_Stat_3, Sub_Stat_4)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (characters, element, rare, relicts, ormnaments, head, gloves, body, feet, sphere, link,
                    sub_stat_1, sub_stat_2, sub_stat_3, sub_stat_4))
    conn.commit()


def on_confirm_button_click():
    characters = characters_entry.get()
    element = element_entry.get()
    rare = rare_entry.get()
    relicts = relicts_entry.get()
    ormnaments = ormnaments_entry.get()
    head = head_entry.get()
    gloves = gloves_entry.get()
    body = body_entry.get()
    feet = feet_entry.get()
    sphere = sphere_entry.get()
    link = link_entry.get()
    sub_stat_1 = sub_stat_1_entry.get()
    sub_stat_2 = sub_stat_2_entry.get()
    sub_stat_3 = sub_stat_3_entry.get()
    sub_stat_4 = sub_stat_4_entry.get()

    if characters and relicts and ormnaments and element and rare and head and gloves and body \
            and feet and sphere and link and sub_stat_1 and sub_stat_2 and sub_stat_3 and sub_stat_4:
        # Create a connection to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('artifacts.db')

        # Create the table if it doesn't exist
        create_table(conn)

        # Insert data into the table
        insert_data(conn, characters, element, rare, relicts, ormnaments, head, gloves, body, feet, sphere, link,
                    sub_stat_1, sub_stat_2, sub_stat_3, sub_stat_4)

        # Close the connection
        conn.close()

        # Clear the input fields
        characters_entry.delete(0, tk.END)
        element_entry.delete(0, tk.END)
        rare_entry.delete(0, tk.END)
        relicts_entry.delete(0, tk.END)
        ormnaments_entry.delete(0, tk.END)
        head_entry.delete(0, tk.END)
        gloves_entry.delete(0, tk.END)
        body_entry.delete(0, tk.END)
        feet_entry.delete(0, tk.END)
        sphere_entry.delete(0, tk.END)
        link_entry.delete(0, tk.END)
        sub_stat_1_entry.delete(0, tk.END)
        sub_stat_2_entry.delete(0, tk.END)
        sub_stat_3_entry.delete(0, tk.END)
        sub_stat_4_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Data inserted into the 'artifacts.db' database successfully.")
    else:
        messagebox.showerror("Error", "Please enter data in all fields.")


# Create the main application window
root = tk.Tk()
root.title("Artifact Fill Database")

window_width = 480
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create input fields for the data
characters_label = tk.Label(root, text="Characters:")
characters_label.pack()
characters_entry = tk.Entry(root, width=30)
characters_entry.pack()

element_label = tk.Label(root, text="Element:")
element_label.pack()
element_entry = tk.Entry(root, width=30)
element_entry.pack()

rare_label = tk.Label(root, text="Rare:")
rare_label.pack()
rare_entry = tk.Entry(root, width=30)
rare_entry.pack()

relicts_label = tk.Label(root, text="Relicts:")
relicts_label.pack()
relicts_entry = tk.Entry(root, width=30)
relicts_entry.pack()

ormnaments_label = tk.Label(root, text="Ormnaments:")
ormnaments_label.pack()
ormnaments_entry = tk.Entry(root, width=30)
ormnaments_entry.pack()

head_label = tk.Label(root, text="Head:")
head_label.pack()
head_entry = tk.Entry(root, width=30)
head_entry.pack()

gloves_label = tk.Label(root, text="Gloves:")
gloves_label.pack()
gloves_entry = tk.Entry(root, width=30)
gloves_entry.pack()

body_label = tk.Label(root, text="Body:")
body_label.pack()
body_entry = tk.Entry(root, width=30)
body_entry.pack()

feet_label = tk.Label(root, text="Feet:")
feet_label.pack()
feet_entry = tk.Entry(root, width=30)
feet_entry.pack()

sphere_label = tk.Label(root, text="Sphere:")
sphere_label.pack()
sphere_entry = tk.Entry(root, width=30)
sphere_entry.pack()

link_label = tk.Label(root, text="Link:")
link_label.pack()
link_entry = tk.Entry(root, width=30)
link_entry.pack()

sub_stat_1_label = tk.Label(root, text="Sub_Stat_1:")
sub_stat_1_label.pack()
sub_stat_1_entry = tk.Entry(root, width=30)
sub_stat_1_entry.pack()

sub_stat_2_label = tk.Label(root, text="Sub_Stat_2:")
sub_stat_2_label.pack()
sub_stat_2_entry = tk.Entry(root, width=30)
sub_stat_2_entry.pack()

sub_stat_3_label = tk.Label(root, text="Sub_Stat_3:")
sub_stat_3_label.pack()
sub_stat_3_entry = tk.Entry(root, width=30)
sub_stat_3_entry.pack()

sub_stat_4_label = tk.Label(root, text="Sub_Stat_4:")
sub_stat_4_label.pack()
sub_stat_4_entry = tk.Entry(root, width=30)
sub_stat_4_entry.pack()

# Create the "Confirm" button
confirm_button = tk.Button(root, text="Confirm", command=on_confirm_button_click)
confirm_button.pack()

# def fetch_data(conn, characters):
#     cursor = conn.cursor()
#     cursor.execute('''SELECT * FROM artifacts WHERE Characters = ?''', (characters,))
#     row = cursor.fetchone()
#     return row
#
# def on_fetch_button_click():
#     characters = characters_entry.get()
#     if characters:
#         conn = sqlite3.connect('artifacts.db')
#         row = fetch_data(conn, characters)
#         conn.close()
#
#         if row:
#             # Populate input fields with data from the database
#             element_entry.delete(0, tk.END)
#             element_entry.insert(0, row[2])
#
#             rare_entry.delete(0, tk.END)
#             rare_entry.insert(0, row[3])
#
#             relicts_entry.delete(0, tk.END)
#             relicts_entry.insert(0, row[4])
#
#             ormnaments_entry.delete(0, tk.END)
#             ormnaments_entry.insert(0, row[5])
#
#             head_entry.delete(0, tk.END)
#             head_entry.insert(0, row[6])
#
#             gloves_entry.delete(0, tk.END)
#             gloves_entry.insert(0, row[7])
#
#             body_entry.delete(0, tk.END)
#             body_entry.insert(0, row[8])
#
#             feet_entry.delete(0, tk.END)
#             feet_entry.insert(0, row[9])
#
#             sphere_entry.delete(0, tk.END)
#             sphere_entry.insert(0, row[10])
#
#             link_entry.delete(0, tk.END)
#             link_entry.insert(0, row[11])
#
#             sub_stat_1_entry.delete(0, tk.END)
#             sub_stat_1_entry.insert(0, row[12])
#
#             sub_stat_2_entry.delete(0, tk.END)
#             sub_stat_2_entry.insert(0, row[13])
#
#             sub_stat_3_entry.delete(0, tk.END)
#             sub_stat_3_entry.insert(0, row[14])
#
#             sub_stat_4_entry.delete(0, tk.END)
#             sub_stat_4_entry.insert(0, row[15])
#
#         else:
#             messagebox.showerror("Error", "No matching record found.")
#     else:
#         messagebox.showerror("Error", "Please enter a value in the 'Characters' field.")

# ... (your existing code for the main application window)

# # Create the "Fetch" button
# fetch_button = tk.Button(root, text="Fetch Data", command=on_fetch_button_click)
# fetch_button.pack()

# Start the Tkinter event loop
root.mainloop()
