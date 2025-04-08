def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
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
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items, similar to Parent2
            sorted_items = sorted(input_data.split(','))
            # Check if all items are numeric
            if all(item.strip().replace('.', '', 1).isdigit() for item in sorted_items):
                # If all numeric, calculate the average
                numbers = [float(item.strip()) for item in sorted_items]
                average = sum(numbers) / len(numbers)
                return f"average: {average:.2f}"
            else:
                # If not all numeric, return sorted and joined items
                return ','.join(sorted_items)
        else:
            # If no commas, check if the input is a single number
            try:
                number = float(input_data.strip())
                return f"single number: {number:.2f}"
            except ValueError:
                # If not a number, return the input as a lowercase string
                return str(input_data).lower()