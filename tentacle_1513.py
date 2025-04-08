def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        # Determine the type of Wikipedia HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            # If it's an HTML document but doesn't match specific patterns, check for other keywords
            if 'science' in lowercase_input:
                return "wikipedia science html document detected"
            elif 'history' in lowercase_input:
                return "wikipedia history html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        if isinstance(result, (int, float)):
            # If the result is a single number, return it with a description
            return f"evaluated expression result: {result:.2f}"
        elif isinstance(result, list):
            # If the result is a list, process it further
            if all(isinstance(item, (int, float)) for item in result):
                # Calculate and return statistics for a list of numbers
                average = sum(result) / len(result)
                minimum = min(result)
                maximum = max(result)
                return f"list of numbers detected. average: {average:.2f}, min: {minimum:.2f}, max: {maximum:.2f}"
            else:
                # For a list of non-numeric items, return the sorted list
                return f"sorted list: {sorted(result)}"
        else:
            # For other types of results, convert to string and lowercase
            return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        input_str = str(input_data).strip()
        
        if ',' in input_str:
            # Process comma-separated values
            values = [value.strip() for value in input_str.split(',')]
            numeric_values = []
            non_numeric_values = []
            
            for value in values:
                try:
                    numeric_values.append(float(value))
                except ValueError:
                    non_numeric_values.append(value)
            
            results = []
            
            if numeric_values:
                average = sum(numeric_values) / len(numeric_values)
                results.append(f"average of numeric values: {average:.2f}")
            
            if non_numeric_values:
                sorted_non_numeric = sorted(non_numeric_values)
                results.append(f"sorted non-numeric values: {', '.join(sorted_non_numeric)}")
            
            return '; '.join(results) if results else input_str.lower()
        else:
            # For single string inputs, convert to lowercase
            return input_str.lower()