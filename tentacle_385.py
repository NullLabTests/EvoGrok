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
            # If it's not a recognized type, process as a generic HTML document
            # Extract and sort unique words from the document
            words = sorted(set(word.strip() for word in lowercase_input.split() if word.strip()))
            return f"generic html document detected with keywords: {', '.join(words[:5])}"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if it's a comma-separated list
            if ',' in input_data:
                # Split the input, sort it, and join it back together
                sorted_items = sorted(input_data.split(','))
                return ','.join(item.strip().lower() for item in sorted_items if item.strip())
            else:
                # If it's not a list, return the input as a lowercase string
                return input_data.strip().lower()
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort and join its elements
            sorted_items = sorted(str(item).strip().lower() for item in input_data if str(item).strip())
            return ','.join(sorted_items)
        else:
            # For other types, return a lowercase string representation
            return str(input_data).lower()