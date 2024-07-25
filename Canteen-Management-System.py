import streamlit as st

class Snack:
    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Available: {self.available}"


class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, id, name, price, available):
        snack = Snack(id, name, price, available)
        self.inventory.append(snack)
        return f"Snack added: {snack}"

    def remove_snack(self, id):
        snack = next((s for s in self.inventory if s.id == id), None)
        if snack:
            self.inventory.remove(snack)
            return f"Snack removed: {snack}"
        else:
            return f"Snack with ID {id} not found."

    def update_availability(self, id, available):
        snack = next((s for s in self.inventory if s.id == id), None)
        if snack:
            snack.available = available
            return f"Availability updated: {snack}"
        else:
            return f"Snack with ID {id} not found."

    def record_sale(self, id):
        snack = next((s for s in self.inventory if s.id == id), None)
        if snack:
            if snack.available == "Yes":
                self.sales_records.append(snack)
                snack.available = "No"
                return f"Sale recorded: {snack}"
            else:
                return f"Snack with ID {id} is not available."
        else:
            return f"Snack with ID {id} not found."

    def display_inventory(self):
        return [{"ID": snack.id, "Name": snack.name, "Price": snack.price, "Available": snack.available} for snack in self.inventory]

    def display_sales_records(self):
        return [{"ID": snack.id, "Name": snack.name, "Price": snack.price, "Available": snack.available} for snack in self.sales_records]


# Initialize session state if not already done
if 'canteen' not in st.session_state:
    st.session_state.canteen = Canteen()

canteen = st.session_state.canteen

# Streamlit UI
st.title("Canteen Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an option", [
    "Add Snack", "Remove Snack", "Update Availability", "Record Sale", "Display Inventory", "Display Sales Records"])

if option == "Add Snack":
    st.subheader("Add a Snack")
    id = st.text_input("Enter Snack ID")
    name = st.text_input("Enter Snack Name")
    price = st.number_input("Enter Snack Price", min_value=0.0, format="%.2f")
    available = st.selectbox("Is it available?", ["Yes", "No"])
    if st.button("Add Snack"):
        result = canteen.add_snack(id, name, price, available)
        st.write(result)

elif option == "Remove Snack":
    st.subheader("Remove a Snack")
    id = st.text_input("Enter Snack ID to remove")
    if st.button("Remove Snack"):
        result = canteen.remove_snack(id)
        st.write(result)

elif option == "Update Availability":
    st.subheader("Update Availability")
    id = st.text_input("Enter Snack ID to update availability")
    available = st.selectbox("Is it available?", ["Yes", "No"])
    if st.button("Update Availability"):
        result = canteen.update_availability(id, available)
        st.write(result)

elif option == "Record Sale":
    st.subheader("Record a Sale")
    id = st.text_input("Enter Snack ID to record sale")
    if st.button("Record Sale"):
        result = canteen.record_sale(id)
        st.write(result)

elif option == "Display Inventory":
    st.subheader("Inventory")
    inventory = canteen.display_inventory()
    st.table(inventory)

elif option == "Display Sales Records":
    st.subheader("Sales Records")
    sales_records = canteen.display_sales_records()
    st.table(sales_records)
