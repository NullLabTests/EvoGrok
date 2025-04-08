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
            processed_items = ','.join(item.strip().lower() for item in sorted_items if item.strip())
            
            # Check if the processed items contain specific keywords
            if 'data' in processed_items and 'analysis' in processed_items:
                return f"{processed_items}, data analysis detected"
            elif 'math' in processed_items or 'mathematics' in processed_items:
                return f"{processed_items}, mathematics detected"
            elif 'text' in processed_items and 'processing' in processed_items:
                return f"{processed_items}, text processing detected"
            else:
                return processed_items
        else:
            # If it's not a string, return a lowercase string representation
            return str(input_data).lower()