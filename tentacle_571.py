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
            # If it's an HTML document but doesn't match specific types, process it further
            title_start = lowercase_input.find('<title>')
            title_end = lowercase_input.find('</title>')
            if title_start != -1 and title_end != -1:
                title = lowercase_input[title_start+7:title_end].strip()
                return f"html document detected: {title}"
            
            # Check for specific class attributes
            if 'class="data-analysis"' in lowercase_input:
                return "data analysis html document detected (class attribute)"
            elif 'class="mathematics"' in lowercase_input:
                return "mathematics html document detected (class attribute)"
            elif 'class="text-processing"' in lowercase_input:
                return "text processing html document detected (class attribute)"
            
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a comma-separated list or a single item
        if isinstance(input_data, str):
            # Split the input, sort it, and join it back together
            items = input_data.split(',')
            if len(items) > 1:
                sorted_items = sorted(item.strip() for item in items if item.strip())
                return ','.join(sorted_items).lower()
            else:
                # If it's a single item, return it as a lowercase string
                return input_data.strip().lower()
        else:
            # If it's not a string, return a lowercase string representation
            return str(input_data).lower()