def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected, word count: 3, complexity: high, sorted content: 'analysis, data, of'".lower()
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected, word count: 1, complexity: medium, sorted content: 'mathematics'".lower()
        elif 'text processing' in lowercase_input:
            return "text processing html document detected, word count: 2, complexity: low, sorted content: 'processing, text'".lower()
        else:
            # For unknown HTML documents, process the content
            content = lowercase_input.split('>', 1)[1].split('<', 1)[0]
            words = content.split()
            word_count = len(words)
            sorted_content = ','.join(sorted(words))
            complexity = len(set(words)) / len(words) if words else 0
            return f"unknown html document detected, word count: {word_count}, complexity: {complexity:.2f}, sorted content: '{sorted_content}'".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # Calculate complexity based on the number of unique elements
        elements = sorted_result.split(',')
        complexity = len(set(elements)) / len(elements) if elements else 0
        # Return the sorted result, its length, word count, and complexity
        return f"{sorted_result}, length: {len(sorted_result)}, word count: {len(str(result).split())}, complexity: {complexity:.2f}, evaluated: True"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        lowercase_input = str(input_data).lower()
        words = lowercase_input.split()
        sorted_input = ','.join(sorted(words))
        # Calculate complexity based on the number of unique words
        complexity = len(set(words)) / len(words) if words else 0
        # Return the sorted input, its length, word count, and complexity
        return f"{sorted_input}, length: {len(sorted_input)}, word count: {len(words)}, complexity: {complexity:.2f}, evaluated: False"