def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, and join it back together
            sorted_items = sorted(input_data.split(','))
            processed_items = [item.strip().lower() for item in sorted_items if item.strip()]
            
            # If the processed items form a valid mathematical expression, evaluate it
            try:
                result = eval(','.join(processed_items))
                return str(result).lower()
            except:
                # If evaluation fails, check if it's a list-like structure
                if all(item.isdigit() or (item.startswith('[') and item.endswith(']')) for item in processed_items):
                    # If it looks like a list of numbers, perform a simple analysis
                    numbers = [int(item) for item in processed_items if item.isdigit()]
                    if numbers:
                        return f"list analysis: min={min(numbers)}, max={max(numbers)}, sum={sum(numbers)}"
                # If not a list-like structure, return the sorted and joined items
                return ','.join(processed_items)
        elif isinstance(input_data, list):
            # Handle list inputs (inspired by data analysis knowledge)
            numbers = [item for item in input_data if isinstance(item, (int, float))]
            if numbers:
                return f"list analysis: min={min(numbers)}, max={max(numbers)}, sum={sum(numbers)}"
            else:
                return ','.join(str(item).lower() for item in sorted(input_data))
        else:
            # If it's not a string or list, return a lowercase string representation
            return str(input_data).lower()