def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML
        title_start = input_data.lower().find('<title>')
        if title_start != -1:
            title_end = input_data.lower().find('</title>', title_start)
            if title_end != -1:
                title = input_data[title_start+7:title_end].strip().lower()
                
                # Identify the type of HTML document based on the title
                if 'data analysis' in title:
                    return "data analysis html document detected"
                elif 'mathematics' in title:
                    return "mathematics html document detected"
                elif 'text processing' in title:
                    return "text processing html document detected"
                else:
                    return "unknown html document detected"
        
        # If title couldn't be extracted, return a generic HTML detection message
        return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a comma-separated list
        if isinstance(input_data, str):
            items = [item.strip() for item in input_data.split(',')]
            return ','.join(sorted(items))
        else:
            # If input is not a string, return its string representation
            return str(input_data).lower()