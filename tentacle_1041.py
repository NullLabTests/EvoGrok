def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If no specific type is detected, process the content
            content = lowercase_input.split('>', 1)[-1].split('<', 1)[0]
            if content:
                # Split the content into words, remove empty strings, sort, and join
                words = [word for word in content.split() if word]
                return ','.join(sorted(words))
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            return f"numeric result: {result:.2f}".lower()
        elif isinstance(result, str):
            words = [word for word in result.split() if word]
            return ','.join(sorted(words))
        else:
            return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove empty strings, sort, and join
        words = [word for word in str(input_data).lower().split() if word]
        return ','.join(sorted(words))