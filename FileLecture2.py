def practice_3_beginner():
    """
    Beginner: Basic pickle operations and directory creation
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("=" * 50)
    
    import pickle
    import os
# --- Part A: Pickle ---
# TODOo 1: Create a list to pickle
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]
    
# TODOo 2: Save with pickle
    with open("shopping.pkl", "wb") as f:
        pickle.dump(shopping_list,f)
    print("Shopping saved with pickle")
        # TODOo: Use pickle.dump
        
    
    print("Shopping list pickled!")
# TODOo 3: Load with pickle
    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f) # Replace with pickle.load(f)
    print(f"Loaded list: {loaded_list}")
    

    
    
# TODOo 4: Add items and re-save

        
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")
    

        
    with open("shopping.pkl", "wb") as f:
        pickle.dump(loaded_list, f)
        
    print(f"Updated List: {loaded_list}")
# TODOo: Save updated list

# --- Part B: Directory Structure ---
# TODOo 5: Create project directory
    project_name = "my_project"
    
    
    if not os.path.exists(project_name):
# TODOo: Create the directory
        os.mkdir(project_name)
        print(f"Created {project_name}/")
        
    
# TODOo 6: Create subdirectories
    subdirs = ["src", "docs", "tests", "data"]
    
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
# TODOo: Create each subdirectory
        if not os.path.exists(path):
            os.mkdir(path)
        
# TODOo 7: Create initial files (README.md, main.py in src)
    thereadme = os.path.join(project_name, "README.md")
    with open(thereadme, "w") as f:
        f.write("The Project")
        
    main = os.path.join(project_name, "main.py")
    with open(main, "w") as f:
        f.write("Main Project")
# TODOo 8: List project structure
    print("\nProject structure:")
    
    for root, dirs, files in os.walk(project_name):
        print(root)
        for d in dirs:
            print(" ", d)
        for file in files:
            print(" ", file)
    
    
# Run the exercise
practice_3_beginner()


print("\n" "Exercise 2")
def practice_2_intermediate():
    """

    Intermediate: Application settings in JSON
    """
    print("\n" + "=" * 50)
    print("EXERCISE 2.2: Settings Manager")
    print("=" * 50)
    
    import json
    
# Default settings
    default_settings = {
        "app_name": "My App",
        "version": "1.0.0",
        "user_preferences": {
            "theme": "dark",
            "font_size": 12,
            "auto_save": True
        },
        "recent_files": [],
        "window_size": [800, 600]
    }

    # TODOo 1: Save default settings with nice formatting   
    with open("settings.json", "w") as settings_json:
        
        json.dump(default_settings,settings_json, indent=4)

    print("Default settings created")
# TODOo 2: Load and modify settings
# Change theme to "light", add a file to recent_files, etc
    with open("settings.json", "r") as settings_json:
        loaded_data = json.load(settings_json)
        
    loaded_data["user_preferences"]["theme"] = "light"
    loaded_data["recent_files"].append("document.txt")
# TODOo 3: Save updated settings
    with open("settings.json", "w") as settings_json:
        json.dump(loaded_data, settings_json, indent=4)
          

# TODOo 4: Create backup
    with open("settings.json", "r") as settings_json:
        json_load = json.load(settings_json)

    with open("settings_backup.json", "w") as settings_backup:
        json.dump(json_load, settings_backup, indent=4)

    print("Settings backed up")
# Run the exercise
practice_2_intermediate()


print("\nExercise 1")

def practice_1_beginner():
    """
    Beginner: Convert text to CSV
    """
    print("\n" + "=" * 50)
    print("EXERCISE 1.1: Text to CSV Converter")
    print("=" * 50)
    
# Create a text file with data
    with open("employees.txt", "w") as employees:
        employees.write("John Smith 35 Engineer\n")
        employees.write("Jane Doe 28 Designer\n")
        employees.write("Bob Johnson 42 Manager\n")
        
# TODOo 1: Read text file and convert to CSV
    with open("employees.txt", "r") as employees:
        with open("employees.csv", "w") as employees_csv:
            # Write CSV header
            employees_csv.write("First,Last,Age,Job\n")
# TODOo: Read each line and convert
            for line in employees:
                parts = line.strip().split()
# parts[0] = first name, parts[1] = last name, etc.
# TODoO: Write as CSV line
# Format: John,Smith,35,Engineer
                csv_line = ",".join(parts) # Replace with comma-separated values
# employees_csv.write(csv_line + "\n")
                employees_csv.write(csv_line + "\n")
# TODoO 2: Read and verify CSV
        print("\nCSV Contents:")
        with open("employees.csv", "r") as employees_csv:
# TODoO: Read and display
            for line in employees_csv:
                  print(line.strip())

# Run the exercise
practice_1_beginner()