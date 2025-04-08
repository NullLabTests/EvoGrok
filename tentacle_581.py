def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected".lower()
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected".lower()
        elif 'text processing' in lowercase_input:
            return "text processing html document detected".lower()
        else:
            # If no specific type is detected, process the content
            content = lowercase_input.split('>', 1)[1].split('<', 1)[0]
            words = content.split()
            # Sort words by length, then alphabetically
            sorted_words = sorted(words, key=lambda x: (len(x), x))
            return ','.join(sorted_words)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it by length and then alphabetically, and join it
        words = str(result).split()
        sorted_words = sorted(words, key=lambda x: (len(x), x))
        return ','.join(sorted_words)
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort by length and then alphabetically, and join
        words = str(input_data).lower().split()
        sorted_words = sorted(words, key=lambda x: (len(x), x))
        return ','.join(sorted_words)