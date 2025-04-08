import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and class attributes
        html_type = None
        if 'data analysis' in lowercase_input:
            html_type = 'data analysis'
        elif 'mathematics' in lowercase_input:
            html_type = 'mathematics'
        elif 'text processing' in lowercase_input:
            html_type = 'text processing'
        
        if html_type:
            # Extract classes from the HTML
            classes = re.findall(r'class="([^"]*)"', lowercase_input)
            all_classes = ' '.join(classes).lower()
            
            if 'wikipedia' in all_classes:
                return f"wikipedia {html_type} html document detected, classes: {all_classes}"
            else:
                return f"{html_type} html document detected, classes: {all_classes}"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Check if the result is a number
        if isinstance(result, (int, float)):
            # Convert the result to a string and lowercase it
            return f"mathematical result: {str(result).lower()}"
        else:
            # If the result is not a number, process it as a string
            return f"evaluated expression: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, and join it back together
            sorted_items = sorted(input_data.split(','))
            processed_items = ','.join(item.strip().lower() for item in sorted_items if item.strip())
            
            # Check if the processed items contain specific keywords
            if 'data' in processed_items and 'analysis' in processed_items:
                return f"{processed_items}, data analysis detected"
            elif any(keyword in processed_items for keyword in ['math', 'equation', 'number', 'calculation']):
                return f"{processed_items}, mathematics detected"
            elif 'text' in processed_items and 'processing' in processed_items:
                return f"{processed_items}, text processing detected"
            else:
                # If no specific keywords are found, return the processed items
                return processed_items
        else:
            # If it's not a string, return a lowercase string representation
            return f"non-string input: {str(input_data).lower()}"