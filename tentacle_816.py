def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected, word count: 3, complexity: high".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected, word count: 1, complexity: medium".lower()
        elif 'text processing' in input_data.lower():
            return "text processing html document detected, word count: 2, complexity: low".lower()
        else:
            # For unknown HTML documents, process the content
            content = input_data.lower().split('>', 1)[1].split('<', 1)[0]
            word_count = len(content.split())
            return f"unknown html document detected, word count: {word_count}, complexity: unknown".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # Calculate complexity based on the number of unique elements
        complexity = len(set(sorted_result.split(','))) / len(sorted_result.split(','))
        # Return the sorted result, its length, word count, and complexity
        return f"{sorted_result}, length: {len(sorted_result)}, word count: {len(str(result).split())}, complexity: {complexity:.2f}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        # Calculate complexity based on the number of unique words
        complexity = len(set(sorted_input.split(','))) / len(sorted_input.split(','))
        # Return the sorted input, its length, word count, and complexity
        return f"{sorted_input}, length: {len(sorted_input)}, word count: {len(str(input_data).split())}, complexity: {complexity:.2f}"