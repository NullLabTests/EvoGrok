def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            content = lower_input.split('>', 1)[1].split('<', 1)[0]
            word_count = len(content.split())
            complexity = calculate_complexity(content)
            return f"data analysis html document detected, word count: {word_count}, complexity: {complexity:.2f}, wikipedia: true".lower()
        elif 'mathematics' in lower_input:
            content = lower_input.split('>', 1)[1].split('<', 1)[0]
            word_count = len(content.split())
            complexity = calculate_complexity(content)
            return f"mathematics html document detected, word count: {word_count}, complexity: {complexity:.2f}, wikipedia: true".lower()
        elif 'text processing' in lower_input:
            content = lower_input.split('>', 1)[1].split('<', 1)[0]
            word_count = len(content.split())
            complexity = calculate_complexity(content)
            return f"text processing html document detected, word count: {word_count}, complexity: {complexity:.2f}, wikipedia: true".lower()
        else:
            # For unknown HTML documents, process the content
            content = lower_input.split('>', 1)[1].split('<', 1)[0]
            word_count = len(content.split())
            complexity = calculate_complexity(content)
            return f"unknown html document detected, word count: {word_count}, complexity: {complexity:.2f}, wikipedia: unknown".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # Calculate complexity based on the number of unique elements
        complexity = calculate_complexity(sorted_result)
        # Return the sorted result, its length, word count, and complexity
        return f"{sorted_result}, length: {len(sorted_result)}, word count: {len(str(result).split())}, complexity: {complexity:.2f}, mathematical expression: true"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        # Calculate complexity based on the number of unique words
        complexity = calculate_complexity(sorted_input)
        # Return the sorted input, its length, word count, and complexity
        return f"{sorted_input}, length: {len(sorted_input)}, word count: {len(str(input_data).split())}, complexity: {complexity:.2f}, mathematical expression: false"

def calculate_complexity(text):
    # Calculate complexity based on the number of unique words or elements
    words = text.split(',')
    unique_count = len(set(words))
    total_count = len(words)
    return unique_count / total_count if total_count > 0 else 0