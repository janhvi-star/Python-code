def convert_base(number: str, from_base: int, to_base: int) -> str:
    """
    Converts a number from one base to another.

    :param number: The number as a string.
    :param from_base: The base of the input number (2-36).
    :param to_base: The base to convert the number to (2-36).
    :return: The converted number as a string.
    """
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        raise ValueError("Bases must be between 2 and 36 inclusive.")

    # Convert the input number to decimal (base 10)
    decimal_number = int(number, from_base)

    # Convert the decimal number to the target base
    def to_target_base(num: int, base: int) -> str:
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while num > 0:
            result.append(chars[num % base])
            num //= base
        return ''.join(reversed(result)) or '0'

    return to_target_base(decimal_number, to_base)

# Example usage:
if __name__ == "__main__":
    try:
        number = input("Enter the number: ").strip()
        from_base = int(input("Enter the base of the given number: ").strip())
        to_base = int(input("Enter the target base: ").strip())

        result = convert_base(number, from_base, to_base)
        print(f"The number {number} in base {from_base} is {result} in base {to_base}.")
    except ValueError as e:
        print(f"Error: {e}")
