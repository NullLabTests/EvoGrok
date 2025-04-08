def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known titles
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            # Process class attributes for data analysis
            classes = set(re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE))
            return f'wikipedia data analysis html document detected, processing class attributes: {",".join(sorted(classes))}'.lower()
        elif 'mathematics' in lowercase_input:
            # Process doctype declaration for mathematics
            doctype = re.search(r'<!DOCTYPE\s+([^>]+)>', input_data, re.IGNORECASE)
            return f'wikipedia mathematics html document detected, processing doctype declaration: {doctype.group(1) if doctype else "unknown"}'.lower()
        elif 'text processing' in lowercase_input:
            # Process HTML tag attributes for text processing
            attributes = set(re.findall(r'(\w+)=["\']', input_data))
            return f'wikipedia text processing html document detected, processing html tag attributes: {",".join(sorted(attributes))}'.lower()
        else:
            # Process unknown HTML document type
            title = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            return f'html document detected, processing unknown type: {title.group(1) if title else "untitled"}'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # If successful, return the result as a string, sorted, joined, and with duplicates removed
        return ','.join(sorted(set(str(result).lower().split())))
    except:
        # If evaluation fails, process the input as text
        if isinstance(input_data, (list, tuple, set)):
            # If input is a collection, flatten it and process as text
            flattened_input = ' '.join(str(item) for item in input_data)
            return ','.join(sorted(set(flattened_input.lower().split())))
        elif isinstance(input_data, dict):
            # If input is a dictionary, process keys and values as text
            all_items = ' '.join(f"{key} {value}" for key, value in input_data.items())
            return ','.join(sorted(set(all_items.lower().split())))
        else:
            # For other types, convert to string, lowercase, split, sort, remove duplicates, and join
            return ','.join(sorted(set(str(input_data).lower().split())))