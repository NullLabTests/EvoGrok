def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"data analysis html document detected, length: {len(sorted_content)}, content: {sorted_content}, title: Data analysis"
        elif 'mathematics' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"mathematics html document detected, length: {len(sorted_content)}, content: {sorted_content}, title: Mathematics"
        elif 'text processing' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"text processing html document detected, length: {len(sorted_content)}, content: {sorted_content}, title: Text processing"
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
        
        # Calculate the length of the original input and the processed result
        original_length = len(str(input_data))
        processed_length = len(sorted_result)
        
        # Attempt to process the result as if it were an HTML document
        if isinstance(result, str) and result.strip().lower().startswith('<!doctype'):
            lowercase_result = result.lower()
            
            # Determine the type of HTML document based on the title
            if 'data analysis' in lowercase_result:
                content = ' '.join(lowercase_result.split()[2:])  # Remove DOCTYPE and first tag
                sorted_content = ','.join(sorted(content.split()))
                return f"data analysis html document detected from calculation, length: {len(sorted_content)}, content: {sorted_content}, title: Data analysis, original result: {result}, original input length: {original_length}"
            elif 'mathematics' in lowercase_result:
                content = ' '.join(lowercase_result.split()[2:])  # Remove DOCTYPE and first tag
                sorted_content = ','.join(sorted(content.split()))
                return f"mathematics html document detected from calculation, length: {len(sorted_content)}, content: {sorted_content}, title: Mathematics, original result: {result}, original input length: {original_length}"
            elif 'text processing' in lowercase_result:
                content = ' '.join(lowercase_result.split()[2:])  # Remove DOCTYPE and first tag
                sorted_content = ','.join(sorted(content.split()))
                return f"text processing html document detected from calculation, length: {len(sorted_content)}, content: {sorted_content}, title: Text processing, original result: {result}, original input length: {original_length}"
            else:
                # If no specific type is detected, process the content
                content = ' '.join(lowercase_result.split()[2:])  # Remove DOCTYPE and first tag
                sorted_content = ','.join(sorted(content.split()))
                return f"html document detected from calculation, length: {len(sorted_content)}, content: {sorted_content}, original result: {result}, original input length: {original_length}"
        
        # If the result is not an HTML document, return the processed result
        return f"{sorted_result}, processed length: {processed_length}, original result: {result}, original input length: {original_length}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        
        # Calculate the length of the original input and the processed result
        original_length = len(str(input_data))
        processed_length = len(sorted_input)
        
        # Return the sorted input, its length, and the original input length
        return f"{sorted_input}, processed length: {processed_length}, original input length: {original_length}"