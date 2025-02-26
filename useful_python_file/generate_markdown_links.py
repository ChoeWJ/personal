def generate_markdown_links(start, end, middle_text, output_file):
    """
    Generate markdown image links with incremental numbers and custom middle text.
    Save the result to a specified output file.
    
    :param start: Start of the range for numbering (inclusive).
    :param end: End of the range for numbering (inclusive).
    :param middle_text: Custom middle text to include in file names.
    :param output_file: Path to the output file to save the results.
    """
    try:
        with open(output_file, 'w') as file:
            for num in range(start, end + 1):
                link = f"![{middle_text}_{num:03}](../images/{middle_text}/{num:03}.png)"
                file.write(link + '\n')
        print(f"Markdown links successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    print("Generate markdown image links")
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    middle_text = input("Enter the middle text (e.g., Algorithm_Paradigm): ")
    output_file = input("Enter the output file path (e.g., output.txt): ")
    
    generate_markdown_links(start, end, middle_text, output_file)
