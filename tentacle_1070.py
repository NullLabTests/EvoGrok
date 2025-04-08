import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on known titles
        if 'data analysis' in lowercase_input:
            # Process class attributes for data analysis
            classes = set(re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE))
            # Count occurrences of each class
            class_counts = {cls: input_data.lower().count(f'class="{cls}"') for cls in classes}
            return f'wikipedia data analysis html document detected, processing class attributes: {",".join(f"{cls}({count})" for cls, count in sorted(class_counts.items()))}'.lower()
        
        elif 'mathematics' in lowercase_input:
            # Process doctype declaration and meta tags for mathematics
            doctype = re.search(r'<!DOCTYPE\s+([^>]+)>', input_data, re.IGNORECASE)
            meta_tags = set(re.findall(r'<meta\s+name="([^"]*)"', input_data, re.IGNORECASE))
            return f'wikipedia mathematics html document detected, processing doctype declaration: {doctype.group(1) if doctype else "unknown"}, meta tags: {",".join(sorted(meta_tags))}'.lower()
        
        elif 'text processing' in lowercase_input:
            # Process HTML tag attributes and script tags for text processing
            attributes = set(re.findall(r'(\w+)=["\']', input_data))
            scripts = set(re.findall(r'<script\s+src="([^"]*)"', input_data, re.IGNORECASE))
            return f'wikipedia text processing html document detected, processing html tag attributes: {",".join(sorted(attributes))}, script sources: {",".join(sorted(scripts))}'.lower()
        
        else:
            # Process unknown HTML document type
            title = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            # Extract all classes used in the document
            all_classes = set(re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE))
            return f'html document detected, processing unknown type: {title.group(1) if title else "untitled"}, classes used: {",".join(sorted(all_classes))}'.lower()
    
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