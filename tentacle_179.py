def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Extract the title from the HTML if possible
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        title = title_match.group(1).lower() if title_match else "unknown"
        
        # Determine the category based on the title
        if title in ["data analysis", "data analytics"]:
            return "data analysis document detected"
        elif title == "mathematics":
            return "mathematics document detected"
        elif title == "text processing":
            return "text processing document detected"
        else:
            return f"html document detected: {title}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort it, and join with commas
        return ','.join(sorted(str(result).lower().split(',')))
    except:
        # If evaluation fails, split the input by commas, sort, and join
        return ','.join(sorted(str(input_data).lower().split(',')))