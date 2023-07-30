import tkinter as tk
import sqlite3


def search_characters():
    relicts = entry_relicts.get()
    ornament = entry_ornament.get()

    conn = sqlite3.connect('artifacts.db')
    cursor = conn.cursor()

    # Build the SQL query dynamically based on the provided inputs
    if relicts and ornament:
        cursor.execute('''
                SELECT Characters
                FROM artifacts
                WHERE Relicts = ? AND Ormnaments = ?
            ''', (relicts, ornament))
    elif relicts:
        cursor.execute('''
                SELECT Characters
                FROM artifacts
                WHERE Relicts = ?
            ''', (relicts,))
    elif ornament:
        cursor.execute('''
                SELECT Characters
                FROM artifacts
                WHERE Ormnaments = ?
            ''', (ornament,))
    else:
        characters_text.delete(1.0, tk.END)
        characters_text.insert(tk.END, "Please enter at least one search criterion!")
        conn.close()
        return

    # Fetch the result
    results = cursor.fetchall()

    conn.close()

    if results:
        characters_text.delete(1.0, tk.END)
        characters_text.insert(tk.END, "Characters:\n")
        for result in results:
            characters_text.insert(tk.END, result[0] + "\n")
    else:
        characters_text.delete(1.0, tk.END)
        characters_text.insert(tk.END, "Characters not found!")


# Create the main Tkinter window
root = tk.Tk()
root.title("Artifacts Search")

# Input fields
label_relicts = tk.Label(root, text="Relicts:")
label_relicts.pack()
entry_relicts = tk.Entry(root)
entry_relicts.pack()

label_ornament = tk.Label(root, text="Ornament:")
label_ornament.pack()
entry_ornament = tk.Entry(root)
entry_ornament.pack()

# Button to search for characters
search_button = tk.Button(root, text="Search", command=search_characters)
search_button.pack()

# Label to display the result
characters_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
characters_text.pack()

root.mainloop()
