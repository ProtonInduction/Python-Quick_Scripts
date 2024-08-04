import os

def create_python_app_with_modules(base_dir, module_names):
    # Create base directory
    os.makedirs(base_dir, exist_ok=True)
    print(f"Created directory: {base_dir}")
    
    # Create __init__.py file and write imports for modules
    init_file_path = os.path.join(base_dir, '__init__.py')
    with open(init_file_path, 'w') as init_file:
        for module in module_names:
            init_file.write(f"from .{module} import *\n")
        print(f"Created __init__.py with imports in {base_dir}")

    # Create blank modules
    for module in module_names:
        module_file_path = os.path.join(base_dir, f'{module}.py')
        with open(module_file_path, 'w') as module_file:
            # Optionally, write a comment in each module file
            module_file.write(f"# {module}.py - Blank module\n")
        print(f"Created blank module: {module_file_path}")

# Define the base directory for the app
base_directory = 'my_app/folder'

# Define the names of the modules
module_names = ['module1', 'module2', 'module3', 'module4']

# Create the Python app structure with modules
create_python_app_with_modules(base_directory, module_names)
