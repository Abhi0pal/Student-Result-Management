def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id.get() == "":
                messagebox.showerror("Error", "Search Student result first", parent=self.root)
                return
            cur.execute("SELECT * FROM result WHERE rid=?", (self.var_id,))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                return  # Exit the function if the course does not exist
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)  # Use askyesno
                if op:  # op will be True if the user clicks 'Yes'
                    cur.execute("DELETE FROM result WHERE rid=?", (self.var_id,))
                    con.commit()
                    messagebox.showinfo("Delete", "result Deleted Successfully", parent=self.root)
                    self.clear()
                    self.show()  # Optionally refresh the table to reflect the deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()