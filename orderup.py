import pandas as pd
import random

# Load the CSV file
def load_restaurants(file_path):
    return pd.read_csv(file_path)

# Get unique food styles
def get_unique_styles(restaurants_df):
    return restaurants_df['Style'].unique()

# Get restaurants by style
def get_restaurants_by_style(restaurants_df, style):
    return restaurants_df[restaurants_df['Style'] == style]['RestuarantName'].tolist()

# Main script
def choose_restaurant():
    # Provide the path to your CSV file
    file_path = r"\your\file\path"  # Adjust to your path
    restaurants_df = load_restaurants(file_path)

    while True:
        # Present the unique styles of food
        styles = get_unique_styles(restaurants_df)
        print("\nAvailable food styles:")
        for i, style in enumerate(styles, start=1):
            print(f"{i}. {style}")
        
        # Get user's choice of style by number
        try:
            style_choice = int(input("Please choose a style of food by number or type 'exit' to quit: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")
            continue

        if style_choice == 'exit':
            print("Exiting. Have a great day!")
            break

        if style_choice < 1 or style_choice > len(styles):
            print("Invalid choice. Please choose a valid number.")
            continue

        chosen_style = styles[style_choice - 1]

        # Get restaurants for the chosen style
        restaurants = get_restaurants_by_style(restaurants_df, chosen_style)

        while True:
            # Present the restaurants under the chosen style
            print(f"\nRestaurants for {chosen_style}:")
            for i, restaurant in enumerate(restaurants, start=1):
                print(f"{i}. {restaurant}")
            
            # Ask the user to choose or go for random, or go back to the previous step
            user_input = input("Type the restaurant name, 'random' for a random choice, 'back' to choose a different style, or 'exit' to quit: ").strip().lower()

            if user_input == "random":
                chosen_restaurant = random.choice(restaurants)
                print(f"Randomly chosen restaurant: {chosen_restaurant}")
            elif user_input == "back":
                break  # Go back to style selection
            elif user_input == "exit":
                print("Exiting. Enjoy your meal!")
                return
            elif user_input.capitalize() in restaurants:
                print(f"You chose: {user_input.capitalize()}")
                return
            else:
                print("Invalid input. Please choose a valid restaurant name, type 'random', 'back', or 'exit'.")
            
# Run the script
choose_restaurant()
