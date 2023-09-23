def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def explain_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Healthy weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def suggest_diet_and_exercise(bmi):
    if bmi < 18.5:
        print("You should eat more calorie-dense foods and increase your daily physical activity.")
    elif bmi >= 18.5 and bmi < 25:
        print("You have a healthy weight. Keep up the good work!")
    elif bmi >= 25 and bmi < 30:
        print("You should eat a balanced diet and increase your physical activity to lose weight.")
    else:
        print("You should eat a healthy diet and engage in daily physical activity to lose weight.")

def calculate_ideal_weight(height, bmi):
    ideal_bmi1 = 18.5
    ideal_bmi2 = 25
    ideal_weight1 = ideal_bmi1 * (height ** 2)
    ideal_weight2 = ideal_bmi2 * (height ** 2)
    current_weight = bmi * (height ** 2)
    if current_weight-ideal_weight1 < ideal_weight2-current_weight :
        ideal_weight=ideal_weight1
    else:
        ideal_weight=ideal_weight2

    weight_to_lose_or_gain = ideal_weight - current_weight
    return weight_to_lose_or_gain

def main():
    name = input("Enter your full name: ")
    height = float(input("Enter your height in meters: "))
    if height > 6:
        height = height / 100
    weight = float(input("Enter your weight in kilograms: "))
    bmi = calculate_bmi(weight, height)
    bmi_category = explain_bmi(bmi)
    print("{}, your BMI is {:.2f} and you are classified as {}.".format(name, bmi, bmi_category))
    suggest_diet_and_exercise(bmi)
    if bmi_category != "Healthy weight":
        weight_to_lose_or_gain = calculate_ideal_weight(height, bmi)
        if weight_to_lose_or_gain > 0:
            print("To be a healthy weight, you need to gain {:.2f} kilograms.".format(weight_to_lose_or_gain))
        else:
            print("To be a healthy weight, you need to lose {:.2f} kilograms.".format(-weight_to_lose_or_gain))

if __name__ == "__main__":
    main()
