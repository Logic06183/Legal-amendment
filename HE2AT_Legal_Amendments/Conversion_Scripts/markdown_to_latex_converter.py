"""
Markdown to LaTeX Converter
Converts markdown files with tracked changes to professionally formatted LaTeX documents
that preserve strikethrough and colors for legal document review.
"""

import os
import re
import sys
import subprocess
import shutil

def convert_markdown_to_latex(markdown_file, output_tex, output_pdf):
    """
    Convert a markdown file with tracked changes to a LaTeX file and PDF.
    
    Args:
        markdown_file: Path to markdown file with HTML-style tracked changes
        output_tex: Path to save the LaTeX file
        output_pdf: Path to save the PDF file
    """
    print(f"Converting {markdown_file} to {output_tex} and {output_pdf}...")
    
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract the document title
    first_line = content.split('\n', 1)[0].strip('# ')
    
    # Create the LaTeX document structure
    latex_content = []
    latex_content.append("\\documentclass[12pt,letterpaper]{article}")
    latex_content.append("\\usepackage[margin=1in]{geometry}")
    latex_content.append("\\usepackage{xcolor}")
    latex_content.append("\\usepackage{ulem}")  # For strikethrough
    latex_content.append("\\usepackage{titlesec}")
    latex_content.append("\\usepackage{enumitem}")
    latex_content.append("\\usepackage{fancyhdr}")
    latex_content.append("\\usepackage{lastpage}")
    latex_content.append("\\usepackage{setspace}")
    
    # Define colors
    latex_content.append("\\definecolor{deletecolor}{RGB}{255,0,0}")  # Red for deletions
    latex_content.append("\\definecolor{addcolor}{RGB}{0,0,255}")  # Blue for additions
    
    # Custom commands for tracked changes
    latex_content.append("\\newcommand{\\deleted}[1]{\\textcolor{deletecolor}{\\sout{#1}}}")
    latex_content.append("\\newcommand{\\added}[1]{\\textcolor{addcolor}{#1}}")
    
    # Set up page style with headers and footers
    latex_content.append("\\pagestyle{fancy}")
    latex_content.append("\\fancyhf{}")
    latex_content.append("\\renewcommand{\\headrulewidth}{0pt}")
    latex_content.append("\\fancyfoot[C]{Page \\thepage\\ of \\pageref{LastPage}}")
    
    # Title formatting
    latex_content.append("\\titleformat{\\section}{\\normalfont\\Large\\bfseries}{\\thesection}{1em}{}")
    latex_content.append("\\titleformat{\\subsection}{\\normalfont\\large\\bfseries}{\\thesubsection}{1em}{}")
    
    # Document begins
    latex_content.append("\\begin{document}")
    latex_content.append("\\onehalfspacing")
    
    # Center the title
    latex_content.append("\\begin{center}")
    latex_content.append(f"\\textbf{{\\Large {first_line}}}")
    latex_content.append("\\end{center}")
    
    # Add a legend
    latex_content.append("\\textbf{LEGEND:} \\deleted{Red strikethrough text} = deleted text; \\added{Blue text} = added text")
    latex_content.append("\\vspace{0.5cm}")
    latex_content.append("\\hrule")
    latex_content.append("\\vspace{0.5cm}")
    
    # Process the markdown content line by line
    lines = content.split('\n')
    skip_lines = 7  # Skip title and legend lines that we've already processed
    in_paragraph = False
    current_text = ""
    
    # Process each line
    for i, line in enumerate(lines):
        if i < skip_lines:
            continue
            
        # Check if the line is empty - it marks the end of a paragraph
        if not line.strip():
            if in_paragraph:
                # Process and add the current paragraph
                processed_para = process_paragraph_latex(current_text)
                latex_content.append(processed_para)
                latex_content.append("")  # Add empty line
                current_text = ""
                in_paragraph = False
            continue
        
        # Check for headers
        if line.strip().startswith('#'):
            if in_paragraph:
                processed_para = process_paragraph_latex(current_text)
                latex_content.append(processed_para)
                latex_content.append("")  # Add empty line
                current_text = ""
                in_paragraph = False
            
            # Count header level and extract text
            header_level = 0
            for char in line:
                if char == '#':
                    header_level += 1
                else:
                    break
            
            header_text = line.lstrip('#').strip()
            
            # Create appropriate LaTeX header
            if header_level == 1:
                latex_content.append(f"\\section*{{{header_text}}}")
            elif header_level == 2:
                latex_content.append(f"\\subsection*{{{header_text}}}")
            else:
                latex_content.append(f"\\subsubsection*{{{header_text}}}")
            
            latex_content.append("")  # Add empty line
            continue
        
        # Start a new paragraph or continue with the current one
        if not in_paragraph:
            in_paragraph = True
            current_text = line
        else:
            current_text += " " + line
    
    # Process the last paragraph if any
    if current_text:
        processed_para = process_paragraph_latex(current_text)
        latex_content.append(processed_para)
    
    # End the document
    latex_content.append("\\end{document}")
    
    # Write the LaTeX file
    with open(output_tex, 'w', encoding='utf-8') as tex_file:
        tex_file.write('\n'.join(latex_content))
    
    # Compile LaTeX to PDF
    compile_latex_to_pdf(output_tex)
    
    print(f"Successfully created: {output_tex} and {output_pdf}")
    return True

def process_paragraph_latex(text):
    """
    Process a single paragraph of text to convert markdown tracked changes to LaTeX commands.
    """
    # First deal with strikethrough deletions
    text = re.sub(r'~~(.*?)~~', r'\\deleted{\1}', text)
    
    # Deal with blue additions
    text = re.sub(r'<span style=\'color: blue\'>(.*?)</span>', r'\\added{\1}', text)
    
    # Deal with red deletions
    text = re.sub(r'<span style=\'color: red\'>(.*?)</span>', r'\\deleted{\1}', text)
    
    # Special characters that need escaping in LaTeX
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde ')
    text = text.replace('^', '\\textasciicircum ')
    
    return text

def compile_latex_to_pdf(tex_file):
    """
    Compile a LaTeX file to PDF using pdflatex.
    """
    try:
        # Get the directory of the tex file
        tex_dir = os.path.dirname(tex_file)
        tex_filename = os.path.basename(tex_file)
        
        # Run pdflatex twice to ensure references are correct
        # Use -interaction=nonstopmode to keep going when errors are encountered
        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename], 
                      check=True, cwd=tex_dir)
        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename], 
                      check=True, cwd=tex_dir)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX: {e}")
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define input and output paths
    input_dirs = [
        os.path.join(base_dir, "Final_Word_Documents", "RP1_UCT_New"),
        os.path.join(base_dir, "Final_Word_Documents", "RP1_WHC_New"),
        os.path.join(base_dir, "Final_Word_Documents", "RP2_WHC"),
        os.path.join(base_dir, "Final_Word_Documents", "RP1_Old")
    ]
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(base_dir, "Legal_Review_LaTeX")
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each directory
    for input_dir in input_dirs:
        dir_name = os.path.basename(input_dir)
        output_subdir = os.path.join(output_dir, dir_name)
        os.makedirs(output_subdir, exist_ok=True)
        
        # Find all markdown files
        for file_name in os.listdir(input_dir):
            if file_name.endswith("_With_Changes.md"):
                markdown_file = os.path.join(input_dir, file_name)
                
                # Create output file names
                base_name = file_name.replace("_With_Changes.md", "")
                tex_file = os.path.join(output_subdir, f"{base_name}_Legal.tex")
                pdf_file = os.path.join(output_subdir, f"{base_name}_Legal.pdf")
                
                # Convert the file
                convert_markdown_to_latex(markdown_file, tex_file, pdf_file)
    
    print("\nConversion complete! Legal review LaTeX documents and PDFs have been created in:")
    print(output_dir)
    print("\nThese documents include:")
    print("1. Professional legal document formatting with proper margins and spacing")
    print("2. Red strikethrough text for deletions")
    print("3. Blue text for additions")
    print("4. Page numbers in the footer")
    print("5. Consistent legal document styling")
    
    # Explain comparison with Word
    print("\nComparison with Word documents:")
    print("- LaTeX PDFs provide more consistent formatting across all systems")
    print("- PDF formatting is generally more polished and professional")
    print("- Word documents allow direct editing by lawyers")
    print("- Both formats preserve the tracked changes with colors and strikethrough")

if __name__ == "__main__":
    main()
