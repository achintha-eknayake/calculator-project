# Calculator Application

A modern calculator application built with Python and Tkinter, featuring a personalized welcome screen and customizable color themes.

## Features

- User-friendly graphical interface
- Personalized welcome screen
- Customizable calculator background color
- Basic arithmetic operations (+, -, *, /)
- Chaining calculations
- Error handling for incorrect calculations
- Centered windows for better user experience

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)

## Project Structure

```
calculator/
│
├── calculator.py       # Main calculator implementation
├── main.py            # Entry point of the application
├── icon.ico           # Application icon
└── README.md          # Documentation
```

## Installation

1. Clone the repository or download the source code
2. Ensure Python 3.x is installed on your system
3. Place an icon file named `icon.ico` in the project directory
4. Run the application using `main.py`

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. On the welcome screen:
   - Enter your name
   - Choose a custom background color (optional)
   - Click "Login" to access the calculator
   - Or click "Quit" to exit

3. Using the calculator:
   - Click number buttons (0-9) to input values
   - Use operation buttons (+, -, *, /, %) for calculations
   - Press "=" to see the result
   - Press "C" to clear the display
   - Results can be used in subsequent calculations

## Features Details

### Welcome Screen
- Personalized greeting with user's name
- Color picker for calculator customization
- Input validation for smooth user experience

### Calculator
- Large, clear display for calculations
- Intuitive button layout
- Error handling for invalid operations
- Continuous calculation support
- Responsive design
- Custom background color based on user selection

## Technical Implementation

The project consists of two main classes:

### WelcomeMessage Class
- Handles initial user interaction
- Manages name input and color selection
- Provides smooth transition to calculator

### Calculator Class
- Implements core calculator functionality
- Manages calculation display and updates
- Handles user input and mathematical operations
- Provides error handling and input validation

## Error Handling

The calculator includes robust error handling for:
- Division by zero
- Invalid mathematical expressions
- Syntax errors
- Empty calculations

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open-source and available for personal and educational use.
