"""
Extract text from Word documents and convert to markdown with tracked changes
"""

import os
import re
import sys
import docx
from docx import Document

def extract_text_from_docx(file_path):
    """Extract text from a Word document"""
    try:
        doc = Document(file_path)
        full_text = []
        
        for para in doc.paragraphs:
            full_text.append(para.text)
            
        return '\n\n'.join(full_text)
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return None

def save_text_file(text, output_path):
    """Save text to a file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved text to {output_path}")
        return True
    except Exception as e:
        print(f"Error saving to {output_path}: {e}")
        return False

def create_markdown_with_changes(original_text, changes):
    """
    Create a markdown file with tracked changes
    Args:
        original_text: The original text content
        changes: List of change dictionaries with:
                - 'type': 'deletion' or 'addition'
                - 'search_text': Text to find
                - 'replacement': Text to add (for additions)
    """
    # Make a copy of the text that we'll modify
    modified_text = original_text
    
    # Apply the changes one by one
    for change in changes:
        change_type = change.get('type')
        search_text = change.get('search_text')
        replacement = change.get('replacement', '')
        
        if search_text not in modified_text:
            print(f"WARNING: Could not find '{search_text[:40]}...' in the text")
            continue
            
        if change_type == 'deletion':
            # Format as red strikethrough in markdown
            modified_text = modified_text.replace(
                search_text, 
                f"~~<span style='color: red'>{search_text}</span>~~"
            )
        elif change_type == 'addition':
            # Format as blue text in markdown
            if search_text:  # If we're replacing something
                modified_text = modified_text.replace(
                    search_text,
                    f"~~<span style='color: red'>{search_text}</span>~~ <span style='color: blue'>{replacement}</span>"
                )
            else:
                # Just adding new text
                modified_text = modified_text.replace(
                    search_text,
                    f"<span style='color: blue'>{replacement}</span>"
                )
    
    return modified_text

def main():
    """Main function to process the files"""
    base_dir = "/Users/craig/Desktop/Legal-amendment"
    input_dir = os.path.join(base_dir, "Final_Word_Documents")
    output_dir = os.path.join(base_dir, "Markdown_With_Changes")
    
    # Create output directories with the same structure
    for subdir in os.listdir(input_dir):
        subdir_path = os.path.join(input_dir, subdir)
        if os.path.isdir(subdir_path):
            os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)
    
    # Define the changes for our documents
    changes = [
        # Section 1 changes - Definitions
        {
            'type': 'addition',
            'search_text': '1.20 "Consortium Shared Data" means',
            'replacement': '\n\n1.21 "Azure Cloud Platform" means the Microsoft Azure cloud computing service that will serve as the HE²AT Center Primary Repository.\n\n1.22 "Cloud Migration" means the process of transferring the Original Study Data and any derived data sets from the existing on-premises infrastructure to the Azure Cloud Platform.\n\n1.23 "Data Access Committee or DAC" means the committee established by the HE²AT Center to review and approve data access requests from external researchers according to established criteria and protocols, which shall continue to function after the conclusion of the HE²AT Center Project.\n\n1.24 "Data Access Levels" means the tiered access system implemented by the HE²AT Center consisting of:\n• Level 0: Original Study Data - Raw, unprocessed data with restricted access to Core Data Team only\n• Level 1: Consortium Shared Data - Processed data shared only among HE²AT Center Consortium partners\n• Level 2: De-identified Data - Retained by HE²AT Center for approved external researcher access\n• Level 3: Inferential Data - Aggregated and anonymized data available for open access\n\n1.25 "External Researcher" means any qualified researcher who is not a member of the HE²AT Center Consortium but who has been approved by the Data Access Committee to access Level 2 data for specific research purposes.\n\n1.26 "Post-Project Data Use" means the continued storage, access, and use of the data after the conclusion of the HE²AT Center Project in accordance with this Amendment.\n\n1.27 "Successor Governance Entity" means any entity or institution that assumes responsibility for the governance, maintenance, and oversight of the Post-Project Data Repository after the conclusion of the HE²AT Center Project.'
        },
        # Section 2.1 changes
        {
            'type': 'deletion',
            'search_text': 'This Agreement shall commence on the Commencement Date and shall terminate on completion of the HE²AT Project',
            'replacement': 'This Agreement shall commence on the Commencement Date and shall remain in effect in perpetuity with respect to the Post-Project Data Use provisions set forth in Section 2.12 of this Amendment, unless terminated earlier in accordance with the provisions of this Agreement. The Data Provider specifically acknowledges and agrees that the Post-Project Data Use provisions shall survive the termination of the HE²AT Center Project'
        },
        # Add section after 2.4
        {
            'type': 'addition',
            'search_text': '2.4 Data Provider retains ownership of the Original Study Data and retains all rights to distribute the Original Study Data to other third parties.',
            'replacement': '\n\nThe Data Provider hereby grants the Data Recipient a perpetual, irrevocable, worldwide, non-exclusive license to store the Original Study Data in the Azure Cloud Platform as part of the HE²AT Center\'s Cloud Migration.\n\nThe Data Provider hereby authorizes the Data Recipient to process and transform the Original Study Data to create derived data sets at Levels 1, 2, and 3.\n\nThe Data Provider hereby authorizes the Data Recipient to retain the derived data sets for Post-Project Data Use as specifically authorized in this Amendment.\n\nThe Data Provider hereby authorizes the Data Recipient to grant access to Level 2 data to External Researchers in accordance with the procedures set forth in this Amendment.\n\nThis expanded license does not transfer ownership of the Original Study Data, which remains with the Data Provider.'
        },
        # Add text in 2.5
        {
            'type': 'deletion',
            'search_text': 'The Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the Core Team for purposes of',
            'replacement': 'The Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the Core HE²AT Center Data Management Team for purposes of'
        },
        # Add text to end of 2.5
        {
            'type': 'addition',
            'search_text': 'as set out in the HE²AT Center Data Management Plan.',
            'replacement': ' as set out in the HE²AT Center Data Management Plan. Following the Cloud Migration, the Original Study Data will be classified as Level 0 data in the Azure Cloud Platform\'s tiered data access system and will remain accessible only to the Core Data Team.'
        },
        # New sections 2.19-2.21
        {
            'type': 'addition',
            'search_text': '2.18 The Data Provider',
            'replacement': '\n\n2.19 Cloud Storage Infrastructure and Data Migration Authorization\n\n2.19.1 The Data Provider hereby irrevocably authorizes the Data Recipient to:\n(a) migrate the Original Study Data from on-premises infrastructure to the Azure Cloud Platform;\n(b) store and process the Original Study Data and all derived data sets in the Azure Cloud Platform; and\n(c) implement the tiered Data Access Levels system described in this Amendment.\n\n2.20 External Researcher Access Authorization\n\n2.20.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission for appropriately de-identified data derived from the Original Study Data (Level 2 Data) to be made available to External Researchers who are not members of the HE²AT Center Consortium, subject to the following conditions:\n(a) All External Researcher access requests must be reviewed and approved by the Data Access Committee.\n(b) External Researchers must sign a legally binding Data Use Agreement.\n(c) External Researchers must commit to appropriate citation of both the HE²AT Center and the original data sources.\n(d) External Researchers will only have access to Level 2 data (de-identified).\n(e) All External Researcher access will be monitored and logged.\n(f) The Data Access Committee shall maintain the right to revoke access for any External Researcher.\n\n2.21 Post-Project Data Use and Long-Term Data Retention Authorization\n\n2.21.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission that the data derived from the Original Study Data shall be retained and may continue to be used beyond the conclusion of the HE²AT Center Project as follows:\n(a) Level 0 Data (Original Study Data): Shall be retained for a period of 5 (five) years.\n(b) Level 1 Data (Consortium Shared Data): Shall be retained for a period of 10 (ten) years.\n(c) Level 2 Data (De-identified Data): Shall be retained indefinitely as a scientific resource.\n(d) Level 3 Data (Inferential Data): Shall be retained indefinitely as an open scientific resource.\n\n2.18 The Data Provider'
        },
        # Add new clause in Section 12
        {
            'type': 'addition',
            'search_text': '12.5 The provisions of this Agreement that by their nature are intended to survive termination or expiration of the Agreement shall survive such termination or expiration and shall remain in full force and effect.',
            'replacement': '\n\n12.6 The Parties expressly acknowledge and agree that the provisions of Sections 2.20 and 2.21 of this Amendment regarding External Researcher Access and Post-Project Data Use shall survive the termination of the Agreement and the conclusion of the HE²AT Center Project.'
        },
        # Renumber clause in Section 12
        {
            'type': 'deletion',
            'search_text': '12.6 The Data Recipient hereby acknowledges',
            'replacement': '12.7 The Data Recipient hereby acknowledges'
        }
    ]
    
    # Process each document that needs tracked changes
    for subdir in ['RP1_UCT_New', 'RP1_WHC_New', 'RP2_WHC']:
        subdir_path = os.path.join(input_dir, subdir)
        if not os.path.isdir(subdir_path):
            continue
            
        # Find the original docx file
        for file in os.listdir(subdir_path):
            if 'Original' in file and file.endswith('.docx'):
                # Extract text from the Word document
                docx_path = os.path.join(subdir_path, file)
                print(f"Processing {docx_path}...")
                
                original_text = extract_text_from_docx(docx_path)
                if not original_text:
                    continue
                
                # Save the original text
                text_filename = file.replace('.docx', '.txt')
                text_path = os.path.join(output_dir, subdir, text_filename)
                save_text_file(original_text, text_path)
                
                # Create markdown with tracked changes
                markdown_text = create_markdown_with_changes(original_text, changes)
                markdown_filename = file.replace('Original', 'Tracked_Changes').replace('.docx', '.md')
                markdown_path = os.path.join(output_dir, subdir, markdown_filename)
                save_text_file(markdown_text, markdown_path)
                
                # Also create a plain text version with simple markers for track changes
                simple_tracked_filename = file.replace('Original', 'Tracked_Simple').replace('.docx', '.txt')
                simple_tracked_path = os.path.join(output_dir, subdir, simple_tracked_filename)
                
                # Create a simplified version with basic markers
                simple_text = original_text
                for change in changes:
                    if change['type'] == 'deletion':
                        simple_text = simple_text.replace(
                            change['search_text'],
                            f"[DELETED: {change['search_text']}]"
                        )
                    elif change['type'] == 'addition':
                        if change['search_text']:
                            simple_text = simple_text.replace(
                                change['search_text'],
                                f"[DELETED: {change['search_text']}] [ADDED: {change['replacement']}]"
                            )
                
                save_text_file(simple_text, simple_tracked_path)
                
                print(f"Created tracked changes versions for {file}")

if __name__ == "__main__":
    # Create the output directory
    os.makedirs("/Users/craig/Desktop/Legal-amendment/Markdown_With_Changes", exist_ok=True)
    main()
    print("Conversion complete!")
