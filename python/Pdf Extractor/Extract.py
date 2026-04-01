import fitz  # PyMuPDF
import re

# Function to convert color to a more readable format (e.g., RGB or hex)
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

# Open the PDF file
doc = fitz.open("./progit.pdf")

# Define the color threshold for separating
highlight_colors = {
    'light_blue': [0.5, 0.8, 0.9],
    'pink': [0.9, 0.6, 0.8],
    'green': [0.4, 0.9, 0.4], 
    'yellow': [1.0, 0.9, 0.4],
    'red':[0.9, 0.2, 0.2]  # RGB for yellow
    # Add other colors as needed
}

# Loop through all the pages
with open('text.md', 'w', encoding='utf-8') as f:
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Extracting the annotations
        for annot in page.annots():
            if annot.type[0] == 8:  # Type 8 is for highlight annotations
                highlight_color = annot.colors["stroke"]  # Color of the highlight (stroke color)
                # Get the rectangle (bounding box) of the highlight
                rect = annot.rect
                
                # Extract the text within the rectangle
                highlight_text = page.get_text("text", clip=rect)
                highlight_text = ' '.join(highlight_text.split())
                # print(highlight_color)
                # Check which color it is (this may need tuning depending on precision)
                color_code = ''
                for color_name, color_value in highlight_colors.items():
                    if (abs(highlight_color[0] - color_value[0]) < 0.1 and
                        abs(highlight_color[1] - color_value[1]) < 0.1 and
                        abs(highlight_color[2] - color_value[2]) < 0.1):
                        
                        color_code = color_name

                if(color_code != ''):
                    if(color_code == 'light_blue'):
                        highlight_text = '\n' + '## ' + highlight_text + '\n'
                    elif(color_code == 'pink'):
                        highlight_text = '\n' + '### ' + highlight_text + '\n'
                    elif(color_code == 'green'):
                        pattern = r'\b\w+\.'
                        texts = highlight_text.split()
                        if texts[-1][-1] != ":":
                            for i in range(len(texts)-1, 0, -1):
                                if re.search(pattern, texts[i]):
                                    break
                                texts.pop()

                        highlight_text = ' '.join(texts)
                        
                        highlight_text = '\n' + highlight_text + '\n'
                    elif(color_code == 'yellow'):
                        highlight_text = '\n' + '>' + highlight_text + '\n'
                    elif(color_code == 'red'):
                        print(highlight_text)
                        highlight_text = '\n' + '```bash' + '\n' + highlight_text + '\n' +  '```' + '\n'

                print(f'color of the text {color_code} : {highlight_text}')
                f.write(highlight_text)
