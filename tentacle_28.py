def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML
        title_start = input_data.lower().find('<title>')
        title_end = input_data.lower().find('</title>')
        if title_start != -1 and title_end != -1:
            title = input_data[title_start+7:title_end].strip().lower()
            
            # Identify the topic based on the title
            if 'data analysis' in title:
                return "data analysis html document detected"
            elif 'mathematics' in title:
                return "mathematics html document detected"
            elif 'text processing' in title:
                return "text processing html document detected"
            else:
                return "unknown topic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If the input contains commas, sort and join it
        if ',' in str(input_data):
            return ','.join(sorted(str(input_data).split(',')))
        # Otherwise, return the input as a lowercase string
        else:
            return str(input_data).lower()