def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known content
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected".lower()
        elif 'text processing' in input_data.lower():
            return "text processing html document detected".lower()
        else:
            return "generic html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort its characters, and join them
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, process the input as text
        if isinstance(input_data, str):
            # Split the input string by commas, sort the resulting list, and join it back
            return ','.join(sorted(input_data.split(',')))
        else:
            # If input is not a string, convert it to a string and return it lowercase
            return str(input_data).lower()