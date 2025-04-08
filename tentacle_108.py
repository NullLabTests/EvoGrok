def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML
        title_start = input_data.lower().find('<title>')
        title_end = input_data.lower().find('</title>')
        
        if title_start != -1 and title_end != -1:
            title = input_data[title_start+7:title_end].strip().lower()
            
            if 'data analysis' in title:
                return "data analysis html document detected"
            elif 'mathematics' in title:
                return "mathematics html document detected"
            elif 'text processing' in title:
                return "text processing html document detected"
        
        # If no specific title is found, return a generic message
        return "html document detected"
    
    try:
        # Attempt to sort and join the input data
        return ','.join(sorted(input_data.split(',')))
    except:
        try:
            # If sorting and joining fails, attempt to evaluate the input as a mathematical expression
            result = eval(input_data)
            # Convert the result to a string and lowercase it
            return str(result).lower()
        except:
            # If evaluation fails, return the input as a lowercase string
            return str(input_data).lower()