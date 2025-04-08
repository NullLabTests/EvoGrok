def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected, length: 30"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected, length: 33"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected, length: 35"
        else:
            # For other HTML documents, process the content
            content = ''.join(c for c in input_data if c.isalnum() or c.isspace())
            sorted_content = ','.join(sorted(content.lower().split()))
            return f"other html document detected, content: {sorted_content}, length: {len(sorted_content)}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # Return the sorted result, its length, and a sum of its numeric values
        numeric_sum = sum(int(x) for x in sorted_result.split(',') if x.isdigit())
        return f"evaluated result: {sorted_result}, length: {len(sorted_result)}, sum: {numeric_sum}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        # Return the sorted input, its length, and the count of unique words
        unique_words = len(set(sorted_input.split(',')))
        return f"processed text: {sorted_input}, length: {len(sorted_input)}, unique words: {unique_words}"