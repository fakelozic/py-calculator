def get_number(prompt: str):
    """Asks the user for a number until they provide a valid one."""
    while True:
        raw_input = input(prompt)
        try:
            return float(raw_input)
        except ValueError:
            print(f'Error: Expected a number but got "{raw_input}". Try again.\n')


def div_from_input() -> float | None:
    first_num = get_number("First number: ")
    second_num = get_number("Second number: ")

    try:
        result = first_num / second_num
        return result
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
        return None
    except Exception as e:
        print(f"Error: Unknown - {e}")
        return None
    finally:
        print("Done")


# this is standard way to start a python script
if __name__ == "__main__":
    div_from_input()
