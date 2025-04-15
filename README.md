# Run Streamlit BC Calculator

### Install Requirements
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

### Run Streamlit BC Calculator
  streamlit run streamlit_bc.py

# BC Calculator Reference
  
## Basic Arithmetic Operators

| Operator | Description      | Example     | Result |
|----------|------------------|-------------|--------|
| `+`      | Addition         | `5 + 3`     | 8      |
| `-`      | Subtraction      | `10 - 4`    | 6      |
| `*`      | Multiplication   | `3 * 4`     | 12     |
| `/`      | Division         | `10 / 3`    | 3      |
| `%`      | Modulus          | `10 % 3`    | 1      |
| `^`      | Exponentiation   | `2 ^ 3`     | 8      |

## Number Base Conversion

| Variable | Description               | Valid Range | Example               | Result |
|----------|---------------------------|-------------|-----------------------|--------|
| `ibase`  | Input base (source)       | 2-16        | `ibase=2; 1101`       | 13     |
| `obase`  | Output base (destination) | 2-16        | `obase=16; 255`       | FF     |

**Important Notes:**
- Always set `ibase` before `obase` to avoid confusion
- Bases work only with integer values
- Letters A-F are used for bases >10 (case insensitive)


## Comparison Operators

| Operator | Description       | Example     | Result |
|----------|------------------|-------------|--------|
| `==`     | Equal            | `5 == 5`    | 1      |
| `!=`     | Not Equal        | `5 != 3`    | 1      |
| `<`      | Less Than        | `3 < 5`     | 1      |
| `<=`     | Less or Equal    | `5 <= 5`    | 1      |
| `>`      | Greater Than     | `5 > 3`     | 1      |
| `>=`     | Greater or Equal | `5 >= 5`    | 1      |

## Logical Operators

| Operator | Description | Example      | Result |
|----------|-------------|--------------|--------|
| `&&`     | AND         | `1 && 0`     | 0      |
| `\|\|`   | OR          | `1 \|\| 0`   | 1      |
| `!`      | NOT         | `!0`         | 1      |

## Bitwise Operators

| Operator | Description | Example   | Result |
|----------|-------------|-----------|--------|
| `&`      | AND         | `6 & 2`   | 2      |
| `\|`     | OR          | `6 \| 2`  | 6      |
| `^`      | XOR         | `6 ^ 2`   | 4      |
| `~`      | NOT         | `~0`      | -1     |
| `<<`     | Left Shift  | `4 << 1`  | 8      |
| `>>`     | Right Shift | `4 >> 1`  | 2      |

## Math Functions (require `-l` flag)

| Function | Description      | Example       | Result      |
|----------|------------------|---------------|-------------|
| `s(x)`   | Sine             | `s(1.57)`     | ~1.0        |
| `c(x)`   | Cosine           | `c(0)`        | 1.0         |
| `a(x)`   | Arctangent       | `a(1)`        | .7854       |
| `l(x)`   | Natural Log      | `l(2)`        | .6931       |
| `e(x)`   | Exponential      | `e(1)`        | 2.7183      |
| `sqrt(x)`| Square Root      | `sqrt(9)`     | 3           |


## Constants

The `bc` math library does not define many built-in constants, but you can compute common ones using the math library functions. Below are commonly derived constants in `bc`.

| Constant | Description | How to Compute                                         |
|----------|-------------|--------------------------------------------------------|
| `pi` | The mathematical constant π (~3.14159). | `scale=20; 4*a(1)`             |
| `e` | The base of the natural logarithm (~2.71828). | `scale=20; e(1)`          |
| `phi` | Golden Ratio (φ, phi) (~1.6180339887). | `scale=10; (1 + sqrt(5)) / 2`  |


## Examples

```bc
# Integer division
scale = 0
17 / 3  # Returns 5

# Floating-point division
scale = 2
17 / 3  # Returns 5.66

# Using math library
scale = 4
s(3.14/2)  # Returns ~1.0
