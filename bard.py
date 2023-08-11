import tkinter as tk
import sqlite3
from tkinter import ttk

# Create the main application window
app = tk.Tk()
app.title("Relict Helper")
app.geometry("550x700")

# Create and configure frames
input_frame = tk.Frame(app, padx=10, pady=10)
input_frame.pack()

result_frame = tk.Frame(app, padx=10, pady=10)
result_frame.pack()

main_param = ["Flat HP",
              "Flat ATK",
              "HP%",
              "ATK%",
              "DEF%",
              "Crit Rate",
              "Crit DMG",
              "Outgoing Healing",
              "Effect Hit Rate",
              "Speed",
              "Break Effect",
              "Energy Regen Rate",

              "Fire DMG",
              "Ice DMG",
              "Lightning DMG",
              "Wind DMG",
              "Quantum DMG",
              "Imaginary DMG",
              "Physical DMG"
              ]

artifacts = ["Band of Sizzling Thunder",
             "Champion of Streetwise Boxing",
             "Eagle of Twilight Line",
             "Firesmith of Lava-Forging",
             "Genius of Brilliant Stars",
             "Guard of Wuthering Snow",
             "Hunter of Glacial Forest",
             "Knight of Purity Palace",
             "Longevous Disciple",
             "Messenger Traversing Hackerspace",
             "Musketeer of Wild Wheat",
             "Passerby of Wandering Cloud",
             "Thief of Shooting Meteor",
             "Wastelander of Banditry Desert",

             "Belobog of the Architects",
             "Broken Keel",
             "Celestial Differentiator",
             "Fleet of the Ageless",
             "Inert Salsotto",
             "Pan-Galactic Commercial Enterprise",
             "Rutilant Arena",
             "Space Sealing Station",
             "Sprightly Vonwacq",
             "Talia: Kingdom of Banditry", ]

relict_type = ["Head",
               "Gloves",
               "Body",
               "Feet",
               "Sphere",
               "Link"]

sub_stats = ["Flat_HP",
             "Flat_ATK",
             "Flat_DEF",
             "HP%",
             "ATK%",
             "DEF%",
             "Crit Rate",
             "Crit DMG",
             "Effect Hit Rate",
             "Effect RES",
             "Break Effect%",
             "Speed"]

artifact_label = tk.Label(input_frame, text="Relic name:")
artifact_label.grid(row=0, column=0, sticky='e')
artifact_dropdown = ttk.Combobox(input_frame, values=artifacts, state='readonly', width=30)
artifact_dropdown.grid(row=0, column=1, padx=5, pady=5)

type_label = tk.Label(input_frame, text="Relic type:")
type_label.grid(row=1, column=0, sticky='e')
type_dropdown = ttk.Combobox(input_frame, values=relict_type, state='readonly', width=30)
type_dropdown.grid(row=1, column=1, padx=5, pady=5)

main_param_label = tk.Label(input_frame, text="Main Stat:")
main_param_label.grid(row=2, column=0, sticky='e')
main_param_dropdown = ttk.Combobox(input_frame, values=main_param, state='readonly', width=30)
main_param_dropdown.grid(row=2, column=1, padx=5, pady=5)

# ---

sub_stat_one_label = tk.Label(input_frame, text="Sub-stats 1:")
sub_stat_one_label.grid(row=3, column=0, sticky="e")
sub_stat_one_dropdown = ttk.Combobox(input_frame, values=sub_stats, state='readonly', width=30)
sub_stat_one_dropdown.grid(row=3, column=1, padx=5, pady=5)

sub_stat_two_label = tk.Label(input_frame, text="Sub-stats 2:")
sub_stat_two_label.grid(row=4, column=0, sticky="e")
sub_stat_two_dropdown = ttk.Combobox(input_frame, values=sub_stats, state='readonly', width=30)
sub_stat_two_dropdown.grid(row=4, column=1, padx=5, pady=5)

sub_stat_three_label = tk.Label(input_frame, text="Sub-stats 3:")
sub_stat_three_label.grid(row=5, column=0, sticky="e")
sub_stat_three_dropdown = ttk.Combobox(input_frame, values=sub_stats, state='readonly', width=30)
sub_stat_three_dropdown.grid(row=5, column=1, padx=5, pady=5)

sub_stat_four_label = tk.Label(input_frame, text="Sub-stats 4:")
sub_stat_four_label.grid(row=6, column=0, sticky="e")
sub_stat_four_dropdown = ttk.Combobox(input_frame, values=sub_stats, state='readonly', width=30)
sub_stat_four_dropdown.grid(row=6, column=1, padx=5, pady=5)

# Create the result display
result_text = tk.Text(result_frame, width=80, height=40, wrap=tk.WORD)
result_text.pack()

# ---

# Create a reset button for the artifact name dropdown
artifact_name_reset_button = tk.Button(input_frame, text="Reset", command=lambda: artifact_dropdown.set(""))
artifact_name_reset_button.grid(row=0, column=2, padx=5, pady=5)

# Create a reset button for the relic type dropdown
relic_type_reset_button = tk.Button(input_frame, text="Reset", command=lambda: type_dropdown.set(""))
relic_type_reset_button.grid(row=1, column=2, padx=5, pady=5)

# Create a reset button for the main stat dropdown
main_stat_reset_button = tk.Button(input_frame, text="Reset", command=lambda: main_param_dropdown.set(""))
main_stat_reset_button.grid(row=2, column=2, padx=5, pady=5)

# Create a reset button for the sub-stats dropdowns
sub_stat_one_reset_button = tk.Button(input_frame, text="Reset", command=lambda: sub_stat_one_dropdown.set(""))
sub_stat_one_reset_button.grid(row=3, column=2, padx=5, pady=5)

sub_stat_two_reset_button = tk.Button(input_frame, text="Reset", command=lambda: sub_stat_two_dropdown.set(""))
sub_stat_two_reset_button.grid(row=4, column=2, padx=5, pady=5)

sub_stat_three_reset_button = tk.Button(input_frame, text="Reset", command=lambda: sub_stat_three_dropdown.set(""))
sub_stat_three_reset_button.grid(row=5, column=2, padx=5, pady=5)

sub_stat_four_reset_button = tk.Button(input_frame, text="Reset", command=lambda: sub_stat_four_dropdown.set(""))
sub_stat_four_reset_button.grid(row=6, column=2, padx=5, pady=5)

# Create a database connection
conn = sqlite3.connect("C:\\Users\\andre\\PycharmProjects\\HonkaiHelper\\old_files\\artifacts.db")

# Create a cursor object
cursor = conn.cursor()


# Create the search function
def search():
    # Get the relic name
    relic_name = artifact_dropdown.get()

    # Get the relic type
    relic_type = type_dropdown.get()

    # Get the main stat
    main_stat = main_param_dropdown.get()

    # Get the sub stats
    sub_stat_1 = sub_stat_one_dropdown.get()
    sub_stat_2 = sub_stat_two_dropdown.get()
    sub_stat_3 = sub_stat_three_dropdown.get()
    sub_stat_4 = sub_stat_four_dropdown.get()

    # Create the SQL query
    query = f"""
        SELECT DISTINCT Characters, Sub_Stats FROM artifacts
        WHERE (Relicts = '{relic_name}' OR Ormnaments = '{relic_name}')
        AND {relic_type} = "{main_stat}"
        AND (Sub_Stats LIKE "%{sub_stat_1}%"
        OR Sub_Stats LIKE "%{sub_stat_2}%"
        OR Sub_Stats LIKE "%{sub_stat_3}%"
        OR Sub_Stats LIKE "%{sub_stat_4}%")
    """

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Clear the result text area
    result_text.delete(1.0, tk.END)

    #  result_text.insert f"Результат поиска :{results}")

    # Check if the results are empty
    if results:
        for result in results:
            # Получить имя персонажа
            character_names = []
            character_names.append(result[0])
            if sub_stat_1 and sub_stat_4 and sub_stat_2 and sub_stat_3 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n"
                                               f"Sub_stat_4 = {sub_stat_4}")

            elif sub_stat_1 and sub_stat_2 and sub_stat_3 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_3 = {sub_stat_3}")

            elif sub_stat_1 and sub_stat_2 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_4 = {sub_stat_4}")

            elif sub_stat_1 and sub_stat_3 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n"
                                               f"Sub_stat_4 = {sub_stat_4}")

            elif sub_stat_2 and sub_stat_3 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n"
                                               f"Sub_stat_4 = {sub_stat_4}")

            elif sub_stat_1 and sub_stat_2 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"{result[1]}"
                                               f"{result[0]}")

            elif sub_stat_1 and sub_stat_3 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n")

            elif sub_stat_1 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n"
                                               f"Sub_stat_4 = {sub_stat_4}\n")

            elif sub_stat_2 and sub_stat_3 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n")

            elif sub_stat_2 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n"
                                               f"Sub_stat_4 = {sub_stat_4}\n")

            elif sub_stat_3 and sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n"
                                               f"Sub_stat_4 = {sub_stat_4}\n")

            elif sub_stat_1 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_1 = {sub_stat_1}\n")

            elif sub_stat_2 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_2 = {sub_stat_2}\n")

            elif sub_stat_3 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_3 = {sub_stat_3}\n")

            elif sub_stat_4 in result[1]:
                for character_name in character_names:
                    result_text.insert(tk.END, f"\n{character_name}\n"
                                               f"Sub_stat_4 = {sub_stat_4}\n")

            else:
                result_text.insert(tk.END, f"No results found")


# Create the search button
search_button = tk.Button(input_frame, text="Search")
search_button.grid(row=7, column=0, columnspan=2, pady=10)
search_button.config(state="disabled", command=search)


def are_all_dropdowns_selected():
    return (
            artifact_dropdown.get() and
            type_dropdown.get() and
            main_param_dropdown.get() and
            sub_stat_one_dropdown.get()
    )


def dropdowns_changed(event):
    search_button['state'] = 'normal' if are_all_dropdowns_selected() else 'disabled'


artifact_dropdown.bind("<<ComboboxSelected>>", dropdowns_changed)
type_dropdown.bind("<<ComboboxSelected>>", dropdowns_changed)
main_param_dropdown.bind("<<ComboboxSelected>>", dropdowns_changed)
sub_stat_one_dropdown.bind("<<ComboboxSelected>>", dropdowns_changed)

# Bind the search button to the search function
# search_button.bind("<Button-1>", lambda **kwargs: search())

# Run the mainloop
app.mainloop()
