import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on known titles
        if 'data analysis' in lowercase_input:
            # Process class attributes for data analysis
            classes = set(re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE))
            # Count the number of unique classes
            class_count = len(classes)
            return f'wikipedia data analysis html document detected, {class_count} unique class attributes processed: {",".join(sorted(classes))}'.lower()
        
        elif 'mathematics' in lowercase_input:
            # Process doctype declaration and extract math-related tags for mathematics
            doctype = re.search(r'<!DOCTYPE\s+([^>]+)>', input_data, re.IGNORECASE)
            math_tags = set(re.findall(r'<(math|sup|sub|var)>', input_data, re.IGNORECASE))
            return f'wikipedia mathematics html document detected, doctype: {doctype.group(1) if doctype else "unknown"}, math-related tags processed: {",".join(sorted(math_tags))}'.lower()
        
        elif 'text processing' in lowercase_input:
            # Process HTML tag attributes and extract text-related tags for text processing
            attributes = set(re.findall(r'(\w+)=["\']', input_data))
            text_tags = set(re.findall(r'<(p|span|div|h[1-6])>', input_data, re.IGNORECASE))
            return f'wikipedia text processing html document detected, {len(attributes)} html tag attributes processed: {",".join(sorted(attributes))}, text-related tags processed: {",".join(sorted(text_tags))}'.lower()
        
        else:
            # Process unknown HTML document type
            title = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            # Extract all tags in the document
            all_tags = set(re.findall(r'</?(\w+)', input_data, re.IGNORECASE))
            return f'html document detected, unknown type: {title.group(1) if title else "untitled"}, {len(all_tags)} unique tags processed: {",".join(sorted(all_tags))}'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # If successful, return the result as a string, sorted, joined, with duplicates removed, and with numeric values rounded to 2 decimal places
        processed_result = []
        for item in str(result).lower().split():
            try:
                processed_result.append(f"{float(item):.2f}")
            except ValueError:
                processed_result.append(item)
        return ','.join(sorted(set(processed_result)))
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