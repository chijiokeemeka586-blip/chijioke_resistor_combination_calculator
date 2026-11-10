# Resistor Combination Calculator
# Calculates total resistance in series and in parallel.
# My own twist: it also takes a supply voltage and works out the
# current and power for each circuit, and shows resistances in ohms or kilo-ohms.


def get_number(prompt, whole_number=False):
    """Keep asking until the user types a valid number greater than zero.
    Returns an int if whole_number is True, otherwise a float."""
    while True:
        text = input(prompt)
        try:
            # Convert the typed text into a number
            if whole_number:
                value = int(text)
            else:
                value = float(text)
        except ValueError:
            # This runs when the user types letters or symbols
            print("  That is not a valid number. Please try again.")
            continue

        if value <= 0:
            print("  The number must be greater than zero. Please try again.")
        else:
            return value


def series_resistance(resistors):
    """Series: just add all the resistor values together."""
    total = 0
    for r in resistors:
        total = total + r
    return total


def parallel_resistance(resistors):
    """Parallel: 1/Rt = 1/R1 + 1/R2 + ... so add the inverses, then flip."""
    inverse_sum = 0
    for r in resistors:
        inverse_sum = inverse_sum + 1 / r
    return 1 / inverse_sum


def format_ohms(value):
    """Show the value in ohms or kilo-ohms so it is easy to read."""
    if value >= 1000:
        return f"{value / 1000:.2f} kOhm"
    else:
        return f"{value:.2f} Ohm"


def show_circuit(name, resistance, voltage):
    """Print resistance, current (I = V/R) and power (P = V*I) for a circuit."""
    current = voltage / resistance
    power = voltage * current
    print(f"\n{name} circuit")
    print(f"  Total resistance : {format_ohms(resistance)}")
    print(f"  Current drawn    : {current * 1000:.2f} mA")
    print(f"  Power used       : {power * 1000:.2f} mW")
    return power


def main():
    print("=== Resistor Combination Calculator ===")

    again = "y"
    while again == "y":
        # How many resistors, and their values (stored in a list)
        count = get_number("\nHow many resistors do you have? ", whole_number=True)
        resistors = []
        for i in range(1, count + 1):
            value = get_number(f"Enter value of resistor {i} in ohms: ")
            resistors.append(value)

        # Twist: ask for the supply voltage
        voltage = get_number("Enter the supply voltage in volts: ")

        # Do the calculations
        r_series = series_resistance(resistors)
        r_parallel = parallel_resistance(resistors)

        print("\n--- Results ---")
        p_series = show_circuit("Series", r_series, voltage)
        p_parallel = show_circuit("Parallel", r_parallel, voltage)

        # Compare which one uses more power
        if p_series > p_parallel:
            print("\nThe series circuit uses more power.")
        elif p_parallel > p_series:
            print("\nThe parallel circuit uses more power.")
        else:
            print("\nBoth circuits use the same power (only one resistor).")

        # Let the user run it again
        again = input("\nCalculate again? (y/n): ").strip().lower()

    print("Thank you for using the calculator. Goodbye!")


main()
