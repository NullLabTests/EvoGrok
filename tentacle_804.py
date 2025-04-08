def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        title_start = lowercase_input.find('<title>')
        title_end = lowercase_input.find('</title>')
        if title_start != -1 and title_end != -1:
            title = lowercase_input[title_start+7:title_end].strip()
            
            if 'data analysis' in title:
                return "data analysis html document detected"
            elif 'mathematics' in title:
                return "mathematics html document detected"
            elif 'text processing' in title:
                return "text processing html document detected"
            else:
                return f"html document detected: {title}"
        
        # If no title found, extract class attributes from the <html> tag
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
                    float_value = float(input_data)
                    # If it's a number, return it with two decimal places and lowercase
                    return f"{float_value:.2f}".lower()
                except ValueError:
                    # If it's not a number, return with first letter capitalized and rest lowercase
                    return input_data.strip().capitalize().lower()[1:]
        else:
            # If it's not a string, return a lowercase string representation
            return str(input_data).lower()