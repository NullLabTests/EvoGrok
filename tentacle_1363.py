import json
import keyword
import statistics

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values, then lowercase
            sorted_values = sorted(input_data.split(','))
            # Check if all values are numeric
            if all(value.strip().replace('.', '').isdigit() for value in sorted_values):
                # If numeric, calculate the sum, average, standard deviation, and median
                values = [float(value.strip()) for value in sorted_values]
                total = sum(values)
                average = total / len(values)
                std_dev = statistics.stdev(values)
                median = statistics.median(values)
                return f"numeric input: sum={total:.2f}, average={average:.2f}, std_dev={std_dev:.2f}, median={median:.2f}"
            else:
                # If not numeric, return sorted values with a prefix and count unique values
                unique_count = len(set(sorted_values))
                return f"string list: {','.join(sorted_values).lower()}, unique_count={unique_count}"
        else:
            # Check if the input is a valid Python identifier
            if input_data.isidentifier():
                # If it's an identifier, check if it's a built-in function or keyword
                if input_data in dir(__builtins__):
                    return f"python built-in: {input_data.lower()}"
                elif input_data in keyword.kwlist:
                    return f"python keyword: {input_data.lower()}"
                else:
                    return f"python identifier: {input_data.lower()}"
            # Check if the input is a valid JSON string
            try:
                json_data = json.loads(input_data)
                return f"json data: {json.dumps(json_data).lower()}"
            except json.JSONDecodeError:
                # If not JSON, return the input as a lowercase string with a prefix
                return f"string input: {str(input_data).lower()}"