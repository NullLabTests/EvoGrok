def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title and content
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return "data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "mathematics html document detected"
        elif 'text processing' in lower_input:
            return "text processing html document detected"
        else:
            # Check for specific classes or attributes
            if 'class="wikitable"' in lower_input:
                return "wikipedia table html document detected"
            elif 'id="toc"' in lower_input:
                return "wikipedia article with table of contents detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a comma-separated list or a single item
        if ',' in input_data:
            # Sort and join the items
            sorted_items = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each item
            cleaned_items = [item.strip() for item in sorted_items]
            return ','.join(cleaned_items)
        else:
            # If no commas, check if it's a number and return it as a float if possible
            try:
                return str(float(input_data)).lower()
            except ValueError:
                # If it's not a number, return the input as a lowercase string
                return str(input_data).lower()