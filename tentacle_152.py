def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML if possible
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).lower()
            if title in ['data analysis', 'mathematics', 'text processing']:
                return f"{title} wikipedia page detected"
            else:
                return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort its characters, and join them
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, split the input by commas, sort, and join
        return ','.join(sorted(str(input_data).lower().split(',')))