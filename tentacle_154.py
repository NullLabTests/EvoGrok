def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML content
        title_start = input_data.lower().find('<title>')
        title_end = input_data.lower().find('</title>')
        if title_start != -1 and title_end != -1:
            title = input_data[title_start+7:title_end].strip()
            
            # Process the title based on known Wikipedia page topics
            if title == "data analysis":
                return "data analysis detected"
            elif title == "mathematics":
                return "mathematics detected"
            elif title == "text processing":
                return "text processing detected"
            else:
                return "unknown wikipedia page detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort its characters, and join them
        return ','.join(sorted(str(result)))
    except:
        # If evaluation fails, split the input by commas, sort the parts, and join them
        return ','.join(sorted(input_data.split(',')))