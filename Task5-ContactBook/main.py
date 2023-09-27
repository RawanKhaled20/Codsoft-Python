import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import re

# List to store contacts
contacts = []


# Function to display contacts in the listbox
def display_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")


# Function to handle the Add Contact button click
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Regular expression pattern to match a valid Gmail address
    gmail_pattern = r'[a-zA-Z0-9._%+-]+@gmail\.com$'

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required fields.")
    elif not re.match(r'^[a-zA-Z\s]*$', name):
        messagebox.showerror("Error", "Name should only contain letters and spaces.")
    elif not re.match(r'^[0-9]*$', phone):
        messagebox.showerror("Error", "Phone should only contain digits.")
    elif email and not re.match(gmail_pattern, email):
        messagebox.showerror("Error", "Invalid Gmail address.")
    else:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        display_contacts()
        clear_entries()


# Function to handle the Search button click
def search_contact():
    query = search_entry.get().lower()
    search_results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    display_search_results(search_results)


# Function to display search results in the listbox
def display_search_results(results):
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    search_entry.delete(0, tk.END)


# Function to handle the Delete button click
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name, phone = selected_contact.split(" - ")
        for contact in contacts:
            if contact['name'] == name and contact['phone'] == phone:
                contacts.remove(contact)
                break
        display_contacts()


# Function to handle the Update button click
def update_contact():
    # Regular expression pattern to match a valid Gmail address
    gmail_pattern = r'[a-zA-Z0-9._%+-]+@gmail\.com$'
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name, phone = selected_contact.split(" - ")
        for contact in contacts:
            if contact['name'] == name and contact['phone'] == phone:
                updated_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
                updated_phone = simpledialog.askstring("Update Contact", "Enter new phone number:",
                                                       initialvalue=contact['phone'])
                updated_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
                updated_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])
                if updated_name and updated_phone:
                     if not re.match(r'^[a-zA-Z\s]*$', updated_name):
                           messagebox.showerror("Error", "Name should only contain letters and spaces.")
                     elif not re.match(r'^[0-9]*$', updated_phone):
                            messagebox.showerror("Error", "Phone should only contain digits.")
                     elif updated_email and not re.match(gmail_pattern, updated_email):
                            messagebox.showerror("Error", "Invalid Gmail address.")
                     else:
                         contact['name'] = updated_name
                         contact['phone'] = updated_phone
                         contact['email'] = updated_email
                         contact['address'] = updated_address
                display_contacts()
                break


# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x700")
root.resizable(False, False)
root.config(bg="blue")

custom_font = ("Times New Roman", 14, "bold")
custom_font2 = ("Times New Roman", 10, "bold")

# Create input fields and labels
name_label = tk.Label(root, text="Name:", bg="blue", font=custom_font)
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

phone_label = tk.Label(root, text="Phone:", bg="blue", font=custom_font)
phone_label.pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

email_label = tk.Label(root, text="Email:", bg="blue", font=custom_font)
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

address_label = tk.Label(root, text="Address:", bg="blue", font=custom_font)
address_label.pack(pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.pack(pady=5)

width=12
height=3

# Create Add Contact button
add_button = tk.Button(root, text="Add Contact", command=add_contact, fg="white", bg="black", font=custom_font2, width=width, height=2)
add_button.pack(pady=5)

# Create a listbox to display contacts
contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=5)

# Create a search bar and Search button
search_label = tk.Label(root, text="Search:", bg="blue", font=custom_font)
search_label.pack(pady=5)
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)
search_button = tk.Button(root, text="Search", command=search_contact, fg="white", bg="black", font=custom_font2, width=width, height=height)
search_button.pack( side=tk.LEFT,padx=20)

# Create a Delete button
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, fg="white", bg="black", font=custom_font2, width=width, height=height)
delete_button.pack( side=tk.LEFT, padx=20)

# Create an Update button
update_button = tk.Button(root, text="Update Contact", command=update_contact, fg="white", bg="black", font=custom_font2, width=width, height=height)
update_button.pack( side=tk.LEFT, padx=20)

# Display initial contacts
display_contacts()

# Run the GUI application
root.mainloop()
