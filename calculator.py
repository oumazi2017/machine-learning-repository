#!/usr/bin/env python3
"""
Simple GUI Calculator Application
Built with Python and tkinter
"""

import tkinter as tk
from tkinter import font


class Calculator:
    """A simple GUI calculator application"""
    
    def __init__(self, root):
        """Initialize the calculator"""
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Configure colors
        self.bg_color = "#1e1e1e"
        self.display_bg = "#2d2d2d"
        self.button_bg = "#3d3d3d"
        self.button_fg = "#ffffff"
        self.operator_bg = "#ff9500"
        self.equals_bg = "#ff9500"
        
        # Set background color
        self.root.configure(bg=self.bg_color)
        
        # Current expression
        self.current_expression = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")
        
        # Create UI elements
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=20)
        
        # Display
        display = tk.Label(
            display_frame,
            textvariable=self.display_text,
            font=('Arial', 40, 'bold'),
            bg=self.display_bg,
            fg=self.button_fg,
            anchor=tk.E,
            padx=20,
            pady=20
        )
        display.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        button_font = ('Arial', 18, 'bold')
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                # Determine button properties
                if button_text == '=':
                    bg = self.equals_bg
                    colspan = 2
                elif button_text in ['/', '*', '-', '+']:
                    bg = self.operator_bg
                    colspan = 1
                elif button_text in ['C', '⌫', '%']:
                    bg = "#505050"
                    colspan = 1
                else:
                    bg = self.button_bg
                    colspan = 1
                
                # Special handling for '0' button (wider)
                if button_text == '0':
                    colspan = 1
                
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    font=button_font,
                    bg=bg,
                    fg=self.button_fg,
                    borderwidth=0,
                    command=lambda x=button_text: self.on_button_click(x),
                    activebackground=bg,
                    activeforeground=self.button_fg
                )
                
                button.grid(
                    row=i,
                    column=j,
                    columnspan=colspan,
                    sticky='nsew',
                    padx=2,
                    pady=2
                )
        
        # Configure grid weights for responsive layout
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        """Handle button click events"""
        if char == 'C':
            # Clear all
            self.current_expression = ""
            self.display_text.set("0")
        elif char == '⌫':
            # Backspace
            self.current_expression = self.current_expression[:-1]
            if not self.current_expression:
                self.display_text.set("0")
            else:
                self.display_text.set(self.current_expression)
        elif char == '=':
            # Evaluate expression
            try:
                result = eval(self.current_expression)
                # Format result
                if isinstance(result, float):
                    # Remove trailing zeros
                    result = float(result)
                    if result.is_integer():
                        result = int(result)
                self.display_text.set(str(result))
                self.current_expression = str(result)
            except:
                self.display_text.set("Error")
                self.current_expression = ""
        else:
            # Append character to expression
            if self.current_expression == "0" or self.display_text.get() == "Error":
                self.current_expression = char
            else:
                self.current_expression += char
            self.display_text.set(self.current_expression)
    
    def run(self):
        """Run the calculator application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    root = tk.Tk()
    calculator = Calculator(root)
    calculator.run()


if __name__ == "__main__":
    main()
