CURRENT_YEAR = 2025
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = CURRENT_YEAR - birth_year

hobbies = []
hobby = ''
counter = 0
while hobby != 'stop':
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby != 'stop':
        hobbies.append(hobby)
        counter += 1

def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

life_stage = generate_profile(current_age)

user_profile = {
    "name" : user_name,
    "age" : current_age,
    "stage" : life_stage,
    "hobbies" : hobbies
}

print(f"---\nProfile Summary:\nName: {user_profile.get("name")}\nAge: {user_profile.get("age")}\nLife Stage: {life_stage}")
if not hobby:
    print("You didn't mention any hobbies.")
else:
    print(f"Favourite hobbies ({counter}): ")
    for i in range(counter):
        print(f" - {hobbies[i]}")
print("---")
