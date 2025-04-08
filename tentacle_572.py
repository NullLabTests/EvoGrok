def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
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
            else:
                # Extract class attributes from the <html> tag
                html_start = lowercase_input.find('<html')
                html_end = lowercase_input.find('>', html_start)
                if html_start != -1 and html_end != -1:
                    html_tag = lowercase_input[html_start:html_end+1]
                    classes = []
                    for attr in html_tag.split():
                        if attr.startswith('class='):
                            classes = attr[7:-1].split() if attr.startswith("class=\"") else attr[6:].split()
                            break
                    if classes:
                        return f"generic html document detected with classes: {', '.join(classes)}"
                    else:
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
                # If it's a single item, check if it's a number or not
                try:
                    # Attempt to convert to float
                    float(input_data)
                    return input_data.lower()  # If it's a number, return as is but lowercase
                except ValueError:
                    # If it's not a number, return with first letter capitalized
                    return input_data.strip().capitalize()
        else:
            # If it's not a string, return a lowercase string representation
            return str(input_data).lower()