
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import mysql.connector

def add_user_window():
    add_user_win = Toplevel()
    add_user_win.title("Add User")

    # Create labels, entry widgets, and buttons for adding a user
    Label(add_user_win, text="First Name:").pack()
    first_name_entry = Entry(add_user_win)
    first_name_entry.pack()

    Label(add_user_win, text="Last Name:").pack()
    last_name_entry = Entry(add_user_win)
    last_name_entry.pack()

    Label(add_user_win, text="Email:").pack()
    email_entry = Entry(add_user_win)
    email_entry.pack()

    # Connect to the database and insert the new user data
    def add_user():
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crudy")
            cursor = conn.cursor()

            #create table
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users"
                " (id int auto_increment primary key,firstName TEXT, lastName TEXT, email TEXT)")

            # Insert user data into the database
            insert_query = "INSERT INTO users (firstName, lastName, email) VALUES (%s, %s, %s)"
            user_data = (first_name_entry.get(), last_name_entry.get(), email_entry.get())
            cursor.execute(insert_query, user_data)
            conn.commit()

            messagebox.showinfo("Success", "User added successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add user: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Create a button to add the user
    add_button = Button(add_user_win, text="Add User", command=add_user)
    add_button.pack()

def update_user_window():
    update_user_win = Toplevel()
    update_user_win.title("Update User")

    # Create labels, entry widgets, and buttons for updating a user
    Label(update_user_win, text="User ID:").pack()
    user_id_entry = Entry(update_user_win)
    user_id_entry.pack()

    Label(update_user_win, text="First Name:").pack()
    first_name_entry = Entry(update_user_win)
    first_name_entry.pack()

    Label(update_user_win, text="Last Name:").pack()
    last_name_entry = Entry(update_user_win)
    last_name_entry.pack()

    Label(update_user_win, text="Email:").pack()
    email_entry = Entry(update_user_win)
    email_entry.pack()

    # Connect to the database and update the user data
    def update_user():
        try:
            # conn = sqlite3.connect('crud.db')
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crudy")
            cursor = conn.cursor()

            # Update user data in the database
            update_query = "UPDATE users SET firstName = %s, lastName = %s, email = %s WHERE id = %s"
            user_data = (first_name_entry.get(), last_name_entry.get(), email_entry.get(), user_id_entry.get())
            cursor.execute(update_query, user_data)
            conn.commit()

            messagebox.showinfo("Success", "User updated successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to update user: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Create a button to update the user
    update_button = Button(update_user_win, text="Update User", command=update_user)
    update_button.pack()

def delete_user_window():
    delete_user_win = Toplevel()
    delete_user_win.title("Delete User")

    # Create labels and entry widget for user ID
    Label(delete_user_win, text="User ID:").pack()
    user_id_entry = Entry(delete_user_win)
    user_id_entry.pack()

    # Connect to the database and delete the user
    def delete_user():
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crudy")
            cursor = conn.cursor()

            # Delete user from the database
            delete_query = "DELETE FROM users WHERE id = %s"
            user_id = (user_id_entry.get(),)
            cursor.execute(delete_query, user_id)
            conn.commit()

            messagebox.showinfo("Success", "User deleted successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to delete user: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Create a button to delete the user
    delete_button = Button(delete_user_win, text="Delete User", command=delete_user)
    delete_button.pack()

def display_users_window():
    display_users_win = Toplevel()
    display_users_win.title("Display Users")
    Label(display_users_win, text="User ID:").pack()
    user_id_entry = Entry(display_users_win)
    user_id_entry.pack()

    def view():
    # Connect to the database and fetch all users
        try:

            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crudy")
            cursor = conn.cursor()

            # Fetch all users from the database
            display = "SELECT * FROM users where id = %s"
            display_data = (user_id_entry.get(),)
            cursor.execute(display, display_data)
            users = cursor.fetchall()

        # Display users in a text widget

            users_text = Text(display_users_win)
            for user in users:
                # print(user)
                users_text.insert(END, f"ID: {user[0]},"
                                       f" First Name: {user[1]}, "
                                       f"Last Name: {user[2]}, Email: {user[3]}\n")
            users_text.pack()


        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to fetch users: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    btn = Button(display_users_win, text="Display", command=view)
    btn.pack()
def main():
    root = Tk()
    root.title("User Management App")
    root.geometry("400x400")
    root.resizable(False, False)

    # Load and display the background image
    background_image = Image.open("background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Create the rest of the UI on top of the background image
    btn_add_user = Button(root, text="Add User", width=10, command=add_user_window)
    btn_add_user.place(relx=0.1, rely=0.5)

    btn_update_user = Button(root, text="Update User", width=10, command=update_user_window)
    btn_update_user.place(relx=0.3, rely=0.5)

    btn_delete_user = Button(root, text="Delete User", width=10, command=delete_user_window)
    btn_delete_user.place(relx=0.5, rely=0.5)

    btn_display_users = Button(root, text="Display Users", width=10, command=display_users_window)
    btn_display_users.place(relx=0.7, rely=0.5)

    root.mainloop()

if __name__ == '__main__':
    main()