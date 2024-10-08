import pandas as pd
import random
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)

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
    file_path = r"\your\file\path  # Adjust to your path
    restaurants_df = load_restaurants(file_path)

    while True:
        # Present the unique styles of food
        styles = get_unique_styles(restaurants_df)
        print(Fore.CYAN + "\nAvailable food styles:")
        for i, style in enumerate(styles, start=1):
            print(f"{Fore.GREEN}{i}. {style}")
        
        # Get user's choice of style by number
        try:
            style_choice = int(input(Fore.YELLOW + "Please choose a style of food by number or type 'exit' to quit: ").strip())
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number or 'exit'.")
            continue

        if style_choice == 'exit':
            print(Fore.MAGENTA + "Exiting. Have a great day!")
            break

        if style_choice < 1 or style_choice > len(styles):
            print(Fore.RED + "Invalid choice. Please choose a valid number.")
            continue

        chosen_style = styles[style_choice - 1]

        # Get restaurants for the chosen style
        restaurants = get_restaurants_by_style(restaurants_df, chosen_style)

        while True:
            # Present the restaurants under the chosen style
            print(f"{Fore.CYAN}\nRestaurants for {chosen_style}:")
            for i, restaurant in enumerate(restaurants, start=1):
                print(f"{Fore.GREEN}{i}. {restaurant}")
            
            # Ask the user to choose or go for random, or go back to the previous step
            user_input = input(f"{Fore.YELLOW}Type the restaurant name, 'random' for a random choice, 'back' to choose a different style, or 'exit' to quit: ").strip().lower()

            if user_input == "random":
                chosen_restaurant = random.choice(restaurants)
                print(f"{Fore.MAGENTA}Randomly chosen restaurant: {chosen_restaurant}")
            elif user_input == "back":
                break  # Go back to style selection
            elif user_input == "exit":
                print(Fore.MAGENTA + "Exiting. Enjoy your meal!")
                return
            elif user_input.capitalize() in restaurants:
                print(f"{Fore.MAGENTA}You chose: {user_input.capitalize()}")
                return
            else:
                print(Fore.RED + "Invalid input. Please choose a valid restaurant name, type 'random', 'back', or 'exit'.")
            
# Run the script
choose_restaurant()
