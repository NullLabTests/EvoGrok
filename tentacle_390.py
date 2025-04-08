def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            # If no specific type is detected, return a generic message
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort its characters
        return ''.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, and join it back together
            sorted_items = sorted(input_data.split(','))
            processed_items = [item.strip().lower() for item in sorted_items if item.strip()]
            
            # If the result is not empty, return it
            if processed_items:
                return ','.join(processed_items)
            else:
                # If the result is empty, return a message indicating an empty string
                return "empty string processed"
        elif isinstance(input_data, (list, tuple, set)):
            # If input is a collection, sort its items and join them
            sorted_items = sorted(str(item).lower() for item in input_data)
            return ','.join(sorted_items)
        else:
            # For other types, return a lowercase string representation
            return str(input_data).lower()