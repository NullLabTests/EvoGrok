def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Check for specific HTML document types
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort any comma-separated values
        result_str = str(result).lower()
        if ',' in result_str:
            return ','.join(sorted(result_str.split(',')))
        return result_str
    except:
        # If evaluation fails, process the input string
        input_str = str(input_data).lower()
        
        # Check if the input contains numbers and perform basic calculations
        import re
        numbers = re.findall(r'\d+', input_str)
        if numbers:
            numbers = [int(num) for num in numbers]
            return f"sum: {sum(numbers)}, average: {sum(numbers)/len(numbers):.2f}"
        
        # If input contains commas, sort and join
        if ',' in input_str:
            return ','.join(sorted(input_str.split(',')))
        
        # If no special processing applies, return the input as a lowercase string
        return input_str