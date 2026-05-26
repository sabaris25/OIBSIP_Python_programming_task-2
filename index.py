

from __future__ import annotations


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Normal weight"
    if bmi < 30.0:
        return "Overweight"
    return "Obesity"


def _prompt_float(prompt: str, *, min_value: float, max_value: float | None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 70 or 1.75).")
            continue

        if value <= 0:
            print("Value must be greater than 0.")
            continue

        if value < min_value:
            print(f"Value is too small. Minimum allowed is {min_value:g}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value is too large. Maximum allowed is {max_value:g}.")
            continue

        return value


def main() -> None:
    print("=== BMI Calculator ===")

    while True:
        weight_kg = _prompt_float(
            "Enter your weight in kilograms (kg): ",
            min_value=1.0,
            max_value=500.0,
        )
        height_m = _prompt_float(
            "Enter your height in meters (m): ",
            min_value=0.5,
            max_value=2.5,
        )

        bmi = calculate_bmi(weight_kg, height_m)
        category = classify_bmi(bmi)

        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Category: {category}\n")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()

