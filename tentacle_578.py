def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return "data analysis html document detected".lower()
        elif 'mathematics' in lower_input:
            return "mathematics html document detected".lower()
        elif 'text processing' in lower_input:
            return "text processing html document detected".lower()
        else:
            # If no specific type is detected, process the content
            content = lower_input.split('>', 1)[-1].split('<', 1)[0]
            if content:
                # Sort and join the unique words in the content
                words = sorted(set(content.split()))
                return ','.join(words)
            else:
                return "generic html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join unique elements
        result_str = str(result)
        elements = sorted(set(result_str.split()))
        return ','.join(elements)
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join unique elements
        lower_input = str(input_data).lower()
        elements = sorted(set(lower_input.split()))
        return ','.join(elements)