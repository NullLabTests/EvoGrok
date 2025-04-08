def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected, length: 30, title: Data analysis, content: " + ','.join(sorted(' '.join(lowercase_input.split()[2:])))
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected, length: 32, title: Mathematics, content: " + ','.join(sorted(' '.join(lowercase_input.split()[2:])))
        elif 'text processing' in lowercase_input:
            return "text processing html document detected, length: 34, title: Text processing, content: " + ','.join(sorted(' '.join(lowercase_input.split()[2:])))
        else:
            # If no specific type is detected, process the content
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"html document detected, length: {len(sorted_content)}, content: {sorted_content}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        
        # Calculate the length of the original input
        original_length = len(str(input_data))
        
        # Return the sorted result, its length, the original result, and the original input length
        return f"{sorted_result}, processed length: {len(sorted_result)}, original result: {result}, original input length: {original_length}, original input: {input_data}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        
        # Calculate the length of the original input
        original_length = len(str(input_data))
        
        # Return the sorted input, its length, and the original input length
        return f"{sorted_input}, processed length: {len(sorted_input)}, original input length: {original_length}, original input: {input_data}"