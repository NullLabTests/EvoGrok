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
                return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result as a string
        result_str = str(result).lower()
        
        # If the result is a number, return it as a string
        if result_str.replace('.', '').isdigit():
            return result_str
        
        # Otherwise, split into words, remove empty strings, sort, and join
        words = [word for word in result_str.split() if word]
        return ','.join(sorted(words))
    except:
        # If evaluation fails, process the input as text
        input_str = str(input_data).lower()
        
        # Check for HTML-like structure
        if input_str.strip().startswith('<') and input_str.strip().endswith('>'):
            content = input_str.split('>', 1)[-1].split('<', 1)[0]
            if content:
                # Split the content into words, remove empty strings, sort, and join
                words = [word for word in content.split() if word]
                return ','.join(sorted(words))
            else:
                return "html-like structure detected"
        
        # If not HTML-like, process as regular text
        words = [word for word in input_str.split() if word]
        return ','.join(sorted(words))