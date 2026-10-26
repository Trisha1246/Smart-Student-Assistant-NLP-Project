from pathlib import Path
import re


PROJECT_DIR = Path(__file__).resolve().parent

CHATBOT_FILE = (
    PROJECT_DIR
    / "app"
    / "chatbot.py"
)

BACKUP_FILE = (
    PROJECT_DIR
    / "app"
    / "chatbot.py.backup"
)


NEW_IS_CALCULATION_FUNCTION = '''
def is_calculation_question(q):

    q = str(q).lower().strip()

    # Remove common question words
    for prefix in [
        "what is ",
        "what's ",
        "calculate ",
        "find ",
        "solve ",
        "evaluate ",
        "compute "
    ]:

        if q.startswith(prefix):

            q = q[len(prefix):]

            break

    # Remove final punctuation
    q = q.rstrip(" ?.!,")

    # Percentage using %
    if "%" in q:

        parts = q.split("%", 1)

        if len(parts) == 2:

            left = parts[0].strip()

            right = parts[1].strip()

            if right.startswith("of "):

                right = right[3:].strip()

            try:

                float(left)
                float(right)

                return True

            except ValueError:

                pass

    # Percentage using "percent of"
    if "percent of" in q:

        parts = q.split(
            "percent of",
            1
        )

        if len(parts) == 2:

            left = parts[0].strip()

            right = parts[1].strip()

            try:

                float(left)
                float(right)

                return True

            except ValueError:

                pass

    # Basic arithmetic
    for operator in [
        "+",
        "-",
        "*",
        "/"
    ]:

        if operator in q:

            parts = q.split(
                operator
            )

            if len(parts) == 2:

                left = parts[0].strip()

                right = parts[1].strip()

                try:

                    float(left)
                    float(right)

                    return True

                except ValueError:

                    pass

    return False
'''


NEW_CALCULATION_FUNCTION = '''
def get_calculation_answer(q):

    q = str(q).lower().strip()

    # Remove common question words
    for prefix in [
        "what is ",
        "what's ",
        "calculate ",
        "find ",
        "solve ",
        "evaluate ",
        "compute "
    ]:

        if q.startswith(prefix):

            q = q[len(prefix):]

            break

    # Remove final punctuation
    q = q.rstrip(" ?.!,")

    # ========================================================
    # PERCENTAGE USING %
    # ========================================================

    if "%" in q:

        parts = q.split(
            "%",
            1
        )

        if len(parts) == 2:

            left = parts[0].strip()

            right = parts[1].strip()

            if right.startswith("of "):

                right = right[3:].strip()

            try:

                a = float(left)

                b = float(right)

                result = (
                    a * b / 100
                )

                return (
                    f"{a:g}% of {b:g} = "
                    f"{a:g} × {b:g} ÷ 100 = "
                    f"{result:g}"
                )

            except ValueError:

                pass

    # ========================================================
    # PERCENTAGE USING "PERCENT OF"
    # ========================================================

    if "percent of" in q:

        parts = q.split(
            "percent of",
            1
        )

        if len(parts) == 2:

            left = parts[0].strip()

            right = parts[1].strip()

            try:

                a = float(left)

                b = float(right)

                result = (
                    a * b / 100
                )

                return (
                    f"{a:g}% of {b:g} = "
                    f"{a:g} × {b:g} ÷ 100 = "
                    f"{result:g}"
                )

            except ValueError:

                pass

    # ========================================================
    # BASIC ARITHMETIC
    # ========================================================

    for operator in [
        "+",
        "-",
        "*",
        "/"
    ]:

        if operator not in q:

            continue

        parts = q.split(
            operator
        )

        if len(parts) != 2:

            continue

        left = parts[0].strip()

        right = parts[1].strip()

        try:

            a = float(left)

            b = float(right)

        except ValueError:

            continue

        if operator == "+":

            result = a + b

        elif operator == "-":

            result = a - b

        elif operator == "*":

            result = a * b

        else:

            if b == 0:

                return (
                    "Division by zero is undefined."
                )

            result = a / b

        return (
            f"{a:g} {operator} {b:g} = "
            f"{result:g}"
        )

    return None
'''


def replace_function(
    text,
    function_name,
    new_function
):

    pattern = (
        rf"def {re.escape(function_name)}\s*\("
        rf".*?"
        rf"(?=\n(?:async\s+)?def\s+|\Z)"
    )

    updated_text, count = re.subn(
        pattern,
        new_function.strip() + "\n\n",
        text,
        count=1,
        flags=re.DOTALL
    )

    if count != 1:

        raise RuntimeError(
            f"Could not find function: "
            f"{function_name}"
        )

    return updated_text


def main():

    print(
        "Opening original chatbot backup..."
    )

    if not BACKUP_FILE.exists():

        print(
            "ERROR: chatbot.py.backup was not found."
        )

        print(
            "The script will not modify chatbot.py."
        )

        return

    original_text = (
        BACKUP_FILE.read_text(
            encoding="utf-8"
        )
    )

    print(
        "Original backup loaded."
    )

    # Replace calculation-question detection
    updated_text = replace_function(
        original_text,
        "is_calculation_question",
        NEW_IS_CALCULATION_FUNCTION
    )

    print(
        "is_calculation_question() updated."
    )

    # Replace calculation-answer function
    updated_text = replace_function(
        updated_text,
        "get_calculation_answer",
        NEW_CALCULATION_FUNCTION
    )

    print(
        "get_calculation_answer() updated."
    )

    # Write the modified chatbot
    CHATBOT_FILE.write_text(
        updated_text,
        encoding="utf-8"
    )

    print()
    print(
        "Calculation fix completed successfully."
    )

    print()
    print(
        "Original backup remains here:"
    )

    print(
        BACKUP_FILE
    )

    print()
    print(
        "Test examples:"
    )

    print(
        "What is 25% of 240?"
    )

    print(
        "25% of 240"
    )

    print(
        "Calculate 25% of 240"
    )

    print(
        "What is 20 + 15?"
    )

    print(
        "Calculate 50 / 5"
    )


if __name__ == "__main__":

    main()