import tkinter

# Screen
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=50)

FONT = ("Arial", 12)

# Entry
mile_entry = tkinter.Entry(width=10, font=FONT, justify="center")
mile_entry.grid(column=3, row=1, pady=10, padx=(0,5), sticky="E")
mile_entry.focus()

# Label - "Miles"
mile_label = tkinter.Label(text="Miles", font=FONT)
mile_label.grid(column=4, row=1, sticky="W", padx=(5,0))

# Label - "is equal to"
equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=1, row=2, sticky="E", padx=(0,5))

# Result Label (centered)
miles_calc = tkinter.Label(text="0", font=("Arial", 12, "bold"), justify="center")
miles_calc.grid(column=3, row=2, padx=(0,5), sticky="EW")

# Label - "Km"
km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=4, row=2, sticky="W", padx=(5,0))

# Function to calculate
def calc():
    try:
        mile = float(mile_entry.get())
        mile_to_km = mile * 1.60934
        miles_calc.config(text=f"{mile_to_km:.2f}")
    except ValueError:
        miles_calc.config(text="Invalid")

# Button
calculate_button = tkinter.Button(text="Calculate", font=FONT, command=calc, padx=5, pady=5)
calculate_button.grid(column=3, row=3, pady=10)

window.mainloop()
