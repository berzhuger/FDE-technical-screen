Here is a `README.md` file for your project:

```markdown
# Box Sorter

This project provides a Python function, `sort`, that categorizes boxes based on their dimensions and mass. The function determines whether a box is `STANDARD`, `SPECIAL`, or should be `REJECT`ed based on specific criteria.

## Features

- Categorizes boxes as:
  - `STANDARD`: Not bulky or heavy.
  - `SPECIAL`: Bulky or heavy.
  - `REJECT`: Both bulky and heavy.
- Validates input to ensure all dimensions and mass are positive numbers.
- Includes comprehensive unit tests for various scenarios.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:berzhuger/FDE-technical-screen.git
   ```

2. Ensure you have Python 3.7+ installed.

## Usage

The `sort` function is defined in `main.py`. You can use it as follows:

```python
from main import sort

result = sort(width=10, height=10, lenght=10, mass=5)
print(result)  # Output: STANDARD
```

### Parameters

- `width` (float or int): Width of the box in cm.
- `height` (float or int): Height of the box in cm.
- `lenght` (float or int): Length of the box in cm.
- `mass` (float or int): Mass of the box in kg.

### Return Values

- `STANDARD`: Box is neither bulky nor heavy.
- `SPECIAL`: Box is bulky or heavy.
- `REJECT`: Box is both bulky and heavy.

## Testing

Unit tests are provided in `test_sort.py`. To run the tests:

```bash
python -m unittest test_sort.py
```

## Project Structure

```
.
├── main.py          # Contains the `sort` function
├── test_sort.py     # Unit tests for the `sort` function
└── README.md        # Project documentation
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
