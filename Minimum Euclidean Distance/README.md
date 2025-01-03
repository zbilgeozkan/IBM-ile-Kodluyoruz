# Minimum Euclidean Distance Calculator

This project calculates the minimum Euclidean distance between points in a 2D space using Python. It demonstrates the use of functions and loops to solve the problem step by step.

## 📚 Description

Euclidean distance is the "ordinary" straight-line distance between two points in Euclidean space. The formula for two points ‘(x₁, y₁)’ and ‘(x₂, y₂)’ in a 2D plane is:

![Euclidean Distance Formula](https://upload.wikimedia.org/wikipedia/commons/5/55/Euclidean_distance_2d.svg)

### Formula:
```
d = √((x₂ - x₁)² + (y₂ - y₁)²)
```

This project includes the following tasks:

1. **Defining Points**:
   - Create a list called `points` to represent 2D points as tuples (x, y).

2. **Writing a Function for Euclidean Distance**:
   - Define a function called `euclideanDistance` that calculates the distance between two points.

3. **Calculating Distances**:
   - Use a loop to calculate the Euclidean distance for each pair of points in the list.

4. **Finding the Minimum Distance**:
   - Determine and print the minimum distance from the calculated distances.

---

## 🛠 Features

- Function to calculate Euclidean distance.
- Loop to iterate through point pairs.
- Stores distances in a list for further analysis.
- Identifies the minimum distance among all pairs.

---

## 🧑‍💻 How to Use

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd minimum-euclidean-distance
   ```

3. Run the Python script:
   ```bash
   python main.py
   ```

---

## 📋 Example Input
```python
points = [(0, 0), (1, 1), (2, 2), (3, 3)]
```

## 📋 Example Output
```
The minimum Euclidean distance is: 1.4142135623730951
```

---

## 🧰 Requirements
- Python 3.x

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

---

## 🙏 Acknowledgments
Inspired by the concept of Euclidean geometry and the foundation [Kodluyoruz](https://www.kodluyoruz.org).
