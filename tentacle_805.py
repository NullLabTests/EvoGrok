def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and content
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Check for specific class attributes in the HTML tag
            if 'class="' in lowercase_input:
                classes = lowercase_input.split('class="')[1].split('"')[0].split()
                return f"generic html document with classes: {', '.join(classes)}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, (str, list, tuple)):
            # Convert input to a list of strings
            if isinstance(input_data, (list, tuple)):
                items = [str(item) for item in input_data]
            else:
                items = input_data.split(',')
            
            # Process and sort the items
            processed_items = sorted([item.strip().lower() for item in items if item.strip()])
            
            # Try to evaluate as a mathematical expression
            try:
                result = eval(','.join(processed_items))
                return str(result).lower()
            except:
                # If evaluation fails, try to join items with different separators
                for separator in [' ', ',', '+', '-']:
                    try:
                        result = eval(separator.join(processed_items))
                        return str(result).lower()
                    except:
                        pass
                
                # If all evaluations fail, try to process as a string
                joined_items = ','.join(processed_items)
                try:
                    result = eval(joined_items)
                    return str(result).lower()
                except:
                    # If all else fails, return the sorted and joined items
                    return joined_items
        else:
            # If it's not a string, list, or tuple, return a lowercase string representation
            return str(input_data).lower()