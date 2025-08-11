import tkinter as tk
import random

def generate_random_number():
    """Generates and displays a random number based on the user's input."""
    try:
        start_val = int(start_entry.get())
        end_val = int(end_entry.get())

        if start_val > end_val:
            result_label.config(text="Start value must be less than or equal to End value.", fg="red")
        else:
            random_num = random.randint(start_val, end_val)
            result_label.config(text=f"Random number: {random_num}", fg="yellow")
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="teal")

# Create the main application window
app = tk.Tk()
app.title("Random Number Generator")
app.geometry("300x200") # Set window size

# Create and place widgets
title_label = tk.Label(app, text="Random Number Generator", font=("Arial", 14))
title_label.pack(pady=10)

range_frame = tk.Frame(app)
range_frame.pack()

start_label = tk.Label(range_frame, text="From:")
start_label.pack(side=tk.LEFT)
start_entry = tk.Entry(range_frame, width=5)
start_entry.insert(0, "1")
start_entry.pack(side=tk.LEFT)

end_label = tk.Label(range_frame, text="To:")
end_label.pack(side=tk.LEFT, padx=(10, 0))
end_entry = tk.Entry(range_frame, width=5)
end_entry.insert(0, "100")
end_entry.pack(side=tk.LEFT)

generate_button = tk.Button(app, text="Generate", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack()

# Start the application's event loop
app.mainloop()
