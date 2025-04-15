# bc Command Cheatsheet

This cheatsheet provides a reference for functions and constants available in the `bc` command on Linux. The `bc` command is an arbitrary-precision calculator language. Some functions are built-in, while others require the math library (loaded with `bc -l`).

## Built-in Functions

These functions are available in `bc` without requiring the math library.

| Function | Description |
|----------|-------------|
| `length(expression)` | Returns the number of significant decimal digits in the expression. |
| `read()` | Reads a number from standard input, using the current `ibase` for conversion. Note: Use cautiously to avoid mixing data and program input. |
| `scale(expression)` | Returns the number of digits after the decimal point in the expression. |
| `sqrt(expression)` | Returns the square root of the expression. If the expression is negative, a runtime error occurs. |

## Math Library Functions

These functions are available when `bc` is run with the `-l` option (`bc -l`), which loads the standard math library and sets the default `scale` to 20.

| Function | Description |
|----------|-------------|
| `s(x)` | Returns the sine of `x`, where `x` is in radians. |
| `c(x)` | Returns the cosine of `x`, where `x` is in radians. |
| `a(x)` | Returns the arctangent of `x`, returning the result in radians. |
| `l(x)` | Returns the natural logarithm of `x`. |
| `e(x)` | Returns the exponential function, \( e^x \). |
| `j(n, x)` | Returns the Bessel function of integer order `n` of `x`. |

## Constants

The `bc` math library does not define many built-in constants, but you can compute common ones using the math library functions. Below are commonly derived constants in `bc`.

| Constant | Description | How to Compute |
|----------|-------------|----------------|
| `pi` | The mathematical constant π (~3.14159). | `scale=20; 4*a(1)` (uses arctangent: \( 4 \times \arctan(1) = \pi \)). |
| `e` | The base of the natural logarithm (~2.71828). | `scale=20; e(1)` (computes \( e^1 \)). |

## Notes

- **Scale**: The `scale` variable controls the number of decimal places for calculations. Default is 0 (integer mode) unless `-l` is used, which sets it to 20. Set it manually with `scale=n`.
- **Math Library**: Use `bc -l` to access trigonometric, logarithmic, exponential, and Bessel functions.
- **Custom Functions**: You can define your own functions in `bc` using the `define` keyword, e.g., `define f(x) { return x*x; }` for squaring a number.
- **Input/Output Base**: Use `ibase` and `obase` to set input and output number bases (default is 10). For example, `obase=16` outputs in hexadecimal.

## Example Usage

```bash
# Start bc with math library
bc -l

# Compute pi
scale=10; 4*a(1)
# Output: 3.1415926532

# Compute sine of 1 radian
s(1)
# Output: .84147098480789650665

# Define a custom function
define square(x) { return x*x; }
square(5)
# Output: 25


# bc Command Cheatsheet

This cheatsheet provides a reference for functions and constants available in the `bc` command on Linux. The `bc` command is an arbitrary-precision calculator language. Some functions are built-in, while others require the math library (loaded with `bc -l`).

## Built-in Functions

These functions are available in `bc` without requiring the math library.

| Function | Description |
|----------|-------------|
| `length(expression)` | Returns the number of significant decimal digits in the expression. |
| `read()` | Reads a number from standard input, using the current `ibase` for conversion. Note: Use cautiously to avoid mixing data and program input. |
| `scale(expression)` | Returns the number of digits after the decimal point in the expression. |
| `sqrt(expression)` | Returns the square root of the expression. If the expression is negative, a runtime error occurs. |

## Math Library Functions

These functions are available when `bc` is run with the `-l` option (`bc -l`), which loads the standard math library and sets the default `scale` to 20.

| Function | Description |
|----------|-------------|
| `s(x)` | Returns the sine of `x`, where `x` is in radians. |
| `c(x)` | Returns the cosine of `x`, where `x` is in radians. |
| `a(x)` | Returns the arctangent of `x`, returning the result in radians. |
| `l(x)` | Returns the natural logarithm of `x`. |
| `e(x)` | Returns the exponential function, \( e^x \). |
| `j(n, x)` | Returns the Bessel function of integer order `n` of `x`. |

## Constants

The `bc` math library does not define many built-in constants, but you can compute common ones using the math library functions. Below are commonly derived constants in `bc`.

| Constant | Description | How to Compute |
|----------|-------------|----------------|
| `pi` | The mathematical constant π (~3.14159). | `scale=20; 4*a(1)` (uses arctangent: \( 4 \times \arctan(1) = \pi \)). |
| `e` | The base of the natural logarithm (~2.71828). | `scale=20; e(1)` (computes \( e^1 \)). |

## Notes

- **Scale**: The `scale` variable controls the number of decimal places for calculations. Default is 0 (integer mode) unless `-l` is used, which sets it to 20. Set it manually with `scale=n`.
- **Math Library**: Use `bc -l` to access trigonometric, logarithmic, exponential, and Bessel functions.
- **Custom Functions**: You can define your own functions in `bc` using the `define` keyword, e.g., `define f(x) { return x*x; }` for squaring a number.
- **Input/Output Base**: Use `ibase` and `obase` to set input and output number bases (default is 10). For example, `obase=16` outputs in hexadecimal.

## Example Usage

```bash
# Start bc with math library
bc -l

# Compute pi
scale=10; 4*a(1)
# Output: 3.1415926532

# Compute sine of 1 radian
s(1)
# Output: .84147098480789650665

# Define a custom function
define square(x) { return x*x; }
square(5)
# Output: 25
