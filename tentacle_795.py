def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lower_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and content
        if 'data analysis' in lower_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lower_input:
            return "wikipedia text processing html document detected"
        else:
            # Check for specific classes or attributes
            if 'class="mw-page-title-main"' in lower_input:
                return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, lowercase it, and sort its characters
        sorted_result = ''.join(sorted(str(result).lower()))
        
        # Count the number of unique characters
        unique_chars = len(set(sorted_result))
        
        # Calculate the sum of digits if any are present
        digit_sum = sum(int(char) for char in sorted_result if char.isdigit())
        
        return f"{sorted_result} (unique characters: {unique_chars}, digit sum: {digit_sum})"
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, remove duplicates, and join it back together
            sorted_items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            result = ','.join(sorted_items)
            
            # Count the number of items
            item_count = len(sorted_items)
            
            # Calculate the average length of items
            avg_length = sum(len(item) for item in sorted_items) / item_count if item_count > 0 else 0
            
            return f"{result} (item count: {item_count}, average length: {avg_length:.2f})"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements and join them
            sorted_items = sorted(str(item).lower() for item in input_data)
            result = ','.join(sorted_items)
            
            # Count the number of items
            item_count = len(sorted_items)
            
            # Calculate the average length of items
            avg_length = sum(len(str(item)) for item in input_data) / item_count if item_count > 0 else 0
            
            return f"{result} (item count: {item_count}, average length: {avg_length:.2f})"
        else:
            # For other types, return a lowercase string representation
            # and include the type of the input and its length
            str_repr = str(input_data).lower()
            return f"{str_repr} (type: {type(input_data).__name__}, length: {len(str_repr)})"