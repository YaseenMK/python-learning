def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)
    
    # TODOo 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        # Add try-except block here
        try:
            return a / b
            
        except ZeroDivisionError:# Replace with your code
            return None
                
                
        # Test your function
        
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    
    # TODOo 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        # Add appropriate exception handling
         # Replace with your code
        try:
             return lst[index]
         
        except IndexError:
             return "Not Found"
    
    
    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")
    
    # TODOo 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        # Try int first, then float, handle ValueError
        try:
            return int(value)
        
        except (ValueError, TypeError):
            try:
                return float(value)
        
            except (ValueError, TypeError):
                return None # Replace with your code
            # Test conversions
        
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")

# Run the practice
practice_1_basic_exceptions()






def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
print("\n" + "="*50)
print("EXERCISE 2: Exception Hierarchy")
print("="*50)
# TODOo 1: Catch multiple related exceptions efficiently

def access_data(data_structure, key):
    """
    Access data[key] whether data is list or dict.
    Return None if key doesn't exist.
    """
    try:
        return data_structure[key]

    except LookupError: # TODOo: Replace with appropriate parent exception
        print("Lookup failed")
        return None
    
# Test with different data structures
test_list = [10, 20, 30]
test_dict = {"a": 1, "b": 2}
    
print(f"List[1]: {access_data(test_list, 1)}")
print(f"List[10]: {access_data(test_list, 10)}")
print(f"Dict['a']: {access_data(test_dict, 'a')}")
print(f"Dict['z']: {access_data(test_dict, 'z')}")
    
# TODOo 2: Order exception handlers correctly
def parse_value(value):
    """
    Try to parse value as int, then float, then return as string.
    """
# TODO: Fix the order of exception handlers
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)
            # Add specific exceptions in correct order
            print("Value Failed")
            return str(value)
# Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")
# Run the practice
practice_2_exception_hierarchy()

print("\n")
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)
    
    # TODOo 1: File processor with complete error handling

def process_file(filename):
    """
    Read file, process content, ensure file is closed.
    Return processed content or None.
    """
    file = None
    try:
        # TODOO: Open file
        file = open(filename)
        return file.read()
    except FileNotFoundError:
        # TODO: Handle missing file
        print(f"File not found --> {filename}")
        return None
    except PermissionError:
        # TODO: Handle permission issues
        print(f"Permission not allowed --> {filename}")
        return None
    else:
        # TODO: Process file content (only if opened successfully)
        print(f"File: {filename}")
    finally:
        # TODO: Ensure file is closed
        if file:
            print("Closing file")
            file.close()
    
    # Test with different scenarios
test_files = ["exists.txt", "missing.txt", "/root/file"]
for filename in test_files:
    result = process_file(filename)
    print(f"Processing '{filename}': {result}")
    
    # TODOo 2: Resource manager
class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None
        
    def acquire(self):
        """Acquire resource - might fail."""
        # TODOo: Implement with possible RuntimeError
        if not self.name:
            raise RuntimeError("Invalid name")
       
        
        self.resource = f"{self.name}_connection" 
        print(f" Acquired -- {self.resource}")
        
    
    def release(self):
        """Release resource - must always happen."""
        # TODOo: Implement cleanup
        if self.resource:
            print(f"releasing {self.resource}.")
            self.resource = None
           
    
    def use(self):
        """Use resource - only if acquired."""
        # TODOo: Implement usage
        if not self.resource:
           raise RuntimeError("Resource is not acquired")
        print(f"Using {self.resource}")
           
    
    # Test resource management
rm = ResourceManager("Database")
# TODOO: Use try-except-else-finally to manage resource
try:
        rm.acquire()
except RuntimeError as e:
        print(e)
else:
        rm.use()
    
finally:
        rm.release()
        

practice_3_complete_pattern()

