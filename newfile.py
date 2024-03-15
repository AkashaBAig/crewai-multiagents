import openai
import PyPDF2
import os

# Set your OpenAI API key here
openai.api_key = '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'  # Replace with your actual OpenAI API key

# Define your custom prompt for the GPT model
custom_prompt = "Your task involves transforming technical information about Veeder-Root TLS systems, which are integral to fuel management and environmental monitoring at gas stations. The objective is to refine and simplify this content, ensuring it is suitable for feeding into a retrieval augmented generation pipeline. When processing the text, adhere to the following steps: Concept Identification: Grasp and contextualize the key concepts within the content. Clear Explanation: Rephrase these concepts using easy-to-understand language. Prioritize conveying practical insights over delving into technical specifics. Visual Interpretation: For any content that includes visual elements like images, figures, or tables, offer detailed descriptions to make them comprehensible without visual reference. Detailed Elaboration: Where concepts are not immediately clear, provide additional information to clarify. The primary aim is to make this specialized content about Veeder-Root TLS systems comprehensible and actionable for use in a retrieval augmented generation pipeline."

# Paths for the PDF file and the output text file
pdf_file_path = r'C:\Users\Test\Downloads\new.pdf'  # Update this to the actual path of your PDF file
output_text_file_path = r'C:\Users\Test\Downloads.txt'  # Update this to where you want to save the output

# Function to use OpenAI's GPT model for rewriting text
def rewrite_text_with_gpt(text, prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Adjust model as needed
            prompt=prompt + text,
            max_tokens=2048
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None


# Function to process the PDF file
def process_pdf(file_path, output_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    try:
        # Open the PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            # Process each page
            all_text = ''
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                # Rewrite the extracted text using OpenAI's model with the custom prompt
                rewritten_text = rewrite_text_with_gpt(text, custom_prompt)

                all_text += rewritten_text + "\n"

            # Save the rewritten text to the specified output file
            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(all_text)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_pdf(pdf_file_path, output_text_file_path)
