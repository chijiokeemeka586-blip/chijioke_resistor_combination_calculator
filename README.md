# Resistor Combination Calculator

## What it does
This Python program asks how many resistors you have and the value of each one. It then calculates the total resistance when they are connected in series and in parallel. It also checks for wrong input, like letters or negative numbers, and asks again.

## How to run it
Install Python 3, then run: python resistor_calculator.py

## Sample output
```
How many resistors do you have? 3
Enter value of resistor 1 in ohms: 100
Enter value of resistor 2 in ohms: 200
Enter value of resistor 3 in ohms: 300
Enter the supply voltage in volts: 12

--- Results ---

Series circuit
  Total resistance : 600.00 Ohm
  Current drawn    : 20.00 mA
  Power used       : 240.00 mW

Parallel circuit
  Total resistance : 54.55 Ohm
  Current drawn    : 220.00 mA
  Power used       : 2640.00 mW

The parallel circuit uses more power.
```

## My own twist
After the resistances, the program asks for a supply voltage and calculates the current (I = V/R) and power (P = V x I) for both the series and parallel circuits. It then tells you which circuit uses more power. It also shows large values in kOhm and lets you calculate again without restarting.

## What I learned
I learned how to use a while loop with try/except to stop the program from crashing when someone types a letter instead of a number. I also learned how to split a program into small functions.

## Author
Chijioke Emeka, ND2 Mechatronics Engineering, YabaTech.
