# Sorting-Visualizer-In-Python

## Description 🌟

Sorting-Visualizer-In-Python is an interactive tool that visualizes different sorting algorithms using the Pygame library. It provides a clear, graphical representation of how sorting algorithms work, making it easier to understand and learn about various sorting techniques.

## Features ✨

- **Real-time Visualization**: See sorting algorithms in action with real-time updates.
- **Multiple Sorting Algorithms**: Supports Bubble Sort, Selection Sort, and Insertion Sort.
- **Customizable Speed**: Adjust the speed of the sorting animation using a slider.
- **User-friendly Interface**: Intuitive buttons to select sorting algorithms.

## Installation 🛠️

To get started with Sorting-Visualizer-In-Python, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/Sorting-Visualizer-In-Python.git
   cd Sorting-Visualizer-In-Python
   ```

2. **Install Dependencies**:
   ```sh
   pip install pygame
   ```

## Usage 📦

Here's how you can use the program:

```python
# Import necessary modules
import pygame
from algo_test import bubble_sort, selection_sort, insertion_sort
from SortingVisualizer import SortingVisualizer

# Initialize Pygame
pygame.init()

# Create a sorting visualizer instance
visualizer = SortingVisualizer()

# Run the visualization
visualizer.run()
```

## Configuration 🔧

No additional configuration is required. The program handles all necessary settings internally.

## Tests 🧪

To run tests, ensure you have the required dependencies installed and execute:

```sh
pytest algo_test.py
```

## Project Structure 📁

The project structure is as follows:

```
Sorting-Visualizer-In-Python/
├── SortingAlgorithms.py
├── SortingVisualizer.py
├── main.py
└── README.md
```

## Contributing 🙌

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This README template is designed to be adaptable and informative. Feel free to modify it according to your specific needs and add any additional sections or information that may be relevant to your project.