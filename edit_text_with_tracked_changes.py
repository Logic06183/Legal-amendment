"""
Script to edit the extracted text files with tracked changes markers.
This will use more accurate text matching based on the actual content.
"""

import os
import re

def add_tracked_changes_to_file(input_file, output_file):
    """
    Add tracked changes to text file
    Args:
        input_file: Path to input text file
        output_file: Path to output text file with tracked changes
    """
    try:
        # Read the original text
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Make a copy that we'll modify
        modified = content
        
        # Function to find and replace text with regex pattern
        def find_and_replace(pattern, replacement, text, is_deletion=False, add_markers=True):
            match = re.search(pattern, text, re.DOTALL)
            if match:
                matched_text = match.group(0)
                if is_deletion:
                    # For deletions, wrap in [DELETED: ]
                    if add_markers:
                        replacement_text = f"[DELETED: {matched_text}] [ADDED: {replacement}]"
                    else:
                        replacement_text = replacement
                else:
                    # For additions, just add the new text after
                    if add_markers:
                        replacement_text = f"{matched_text} [ADDED: {replacement}]"
                    else:
                        replacement_text = f"{matched_text}{replacement}"
                        
                return text.replace(matched_text, replacement_text)
            return text
        
        # 1. Find section with Consortium Shared Data definition to add new definitions (1.21-1.27)
        consortium_pattern = r'["\']?Consortium Shared Data["\']?\s*means\s*[^.]+\.'
        new_definitions = """

1.21 "Azure Cloud Platform" means the Microsoft Azure cloud computing service that will serve as the HE²AT Center Primary Repository.

1.22 "Cloud Migration" means the process of transferring the Original Study Data and any derived data sets from the existing on-premises infrastructure to the Azure Cloud Platform.

1.23 "Data Access Committee or DAC" means the committee established by the HE²AT Center to review and approve data access requests from external researchers according to established criteria and protocols, which shall continue to function after the conclusion of the HE²AT Center Project.

1.24 "Data Access Levels" means the tiered access system implemented by the HE²AT Center consisting of:
• Level 0: Original Study Data - Raw, unprocessed data with restricted access to Core Data Team only
• Level 1: Consortium Shared Data - Processed data shared only among HE²AT Center Consortium partners
• Level 2: De-identified Data - Retained by HE²AT Center for approved external researcher access
• Level 3: Inferential Data - Aggregated and anonymized data available for open access

1.25 "External Researcher" means any qualified researcher who is not a member of the HE²AT Center Consortium but who has been approved by the Data Access Committee to access Level 2 data for specific research purposes.

1.26 "Post-Project Data Use" means the continued storage, access, and use of the data after the conclusion of the HE²AT Center Project in accordance with this Amendment.

1.27 "Successor Governance Entity" means any entity or institution that assumes responsibility for the governance, maintenance, and oversight of the Post-Project Data Repository after the conclusion of the HE²AT Center Project."""
        modified = find_and_replace(consortium_pattern, new_definitions, modified)
        
        # 2. Find section 2.1 to modify agreement duration
        agreement_duration_pattern = r'This Agreement shall commence on the Commencement Date and shall terminate on completion of the HE.AT Project'
        new_duration = """This Agreement shall commence on the Commencement Date and shall remain in effect in perpetuity with respect to the Post-Project Data Use provisions set forth in Section 2.12 of this Amendment, unless terminated earlier in accordance with the provisions of this Agreement. The Data Provider specifically acknowledges and agrees that the Post-Project Data Use provisions shall survive the termination of the HE²AT Center Project"""
        modified = find_and_replace(agreement_duration_pattern, new_duration, modified, is_deletion=True)
        
        # 3. Find section 2.4 to add enhanced data rights
        data_ownership_pattern = r'2\.4.*?Data Provider retains ownership of the Original Study Data.*?third parties\.'
        enhanced_rights = """

The Data Provider hereby grants the Data Recipient a perpetual, irrevocable, worldwide, non-exclusive license to store the Original Study Data in the Azure Cloud Platform as part of the HE²AT Center's Cloud Migration.

The Data Provider hereby authorizes the Data Recipient to process and transform the Original Study Data to create derived data sets at Levels 1, 2, and 3.

The Data Provider hereby authorizes the Data Recipient to retain the derived data sets for Post-Project Data Use as specifically authorized in this Amendment.

The Data Provider hereby authorizes the Data Recipient to grant access to Level 2 data to External Researchers in accordance with the procedures set forth in this Amendment.

This expanded license does not transfer ownership of the Original Study Data, which remains with the Data Provider."""
        modified = find_and_replace(data_ownership_pattern, enhanced_rights, modified)
        
        # 4. Find section 2.5 to update Core Team reference
        core_team_pattern = r'The Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the Core Team for purposes of'
        core_team_replacement = """The Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the Core HE²AT Center Data Management Team for purposes of"""
        modified = find_and_replace(core_team_pattern, core_team_replacement, modified, is_deletion=True)
        
        # 5. Add the Level 0 classification information
        data_mgmt_plan_pattern = r'as set out in the HE.AT Center Data Management Plan\.'
        level0_info = """ as set out in the HE²AT Center Data Management Plan. Following the Cloud Migration, the Original Study Data will be classified as Level 0 data in the Azure Cloud Platform's tiered data access system and will remain accessible only to the Core Data Team."""
        modified = find_and_replace(data_mgmt_plan_pattern, level0_info, modified, add_markers=False)
        
        # 6. Add new sections 2.19-2.21
        # Try to find section 2.18 or 2.17 or similar
        section_pattern = r'2\.1[78]\s+.*'
        new_sections = """

2.19 Cloud Storage Infrastructure and Data Migration Authorization

2.19.1 The Data Provider hereby irrevocably authorizes the Data Recipient to:
(a) migrate the Original Study Data from on-premises infrastructure to the Azure Cloud Platform;
(b) store and process the Original Study Data and all derived data sets in the Azure Cloud Platform; and
(c) implement the tiered Data Access Levels system described in this Amendment.

2.20 External Researcher Access Authorization

2.20.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission for appropriately de-identified data derived from the Original Study Data (Level 2 Data) to be made available to External Researchers who are not members of the HE²AT Center Consortium, subject to the following conditions:
(a) All External Researcher access requests must be reviewed and approved by the Data Access Committee.
(b) External Researchers must sign a legally binding Data Use Agreement.
(c) External Researchers must commit to appropriate citation of both the HE²AT Center and the original data sources.
(d) External Researchers will only have access to Level 2 data (de-identified).
(e) All External Researcher access will be monitored and logged.
(f) The Data Access Committee shall maintain the right to revoke access for any External Researcher.

2.21 Post-Project Data Use and Long-Term Data Retention Authorization

2.21.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission that the data derived from the Original Study Data shall be retained and may continue to be used beyond the conclusion of the HE²AT Center Project as follows:
(a) Level 0 Data (Original Study Data): Shall be retained for a period of 5 (five) years.
(b) Level 1 Data (Consortium Shared Data): Shall be retained for a period of 10 (ten) years.
(c) Level 2 Data (De-identified Data): Shall be retained indefinitely as a scientific resource.
(d) Level 3 Data (Inferential Data): Shall be retained indefinitely as an open scientific resource."""
        modified = find_and_replace(section_pattern, new_sections, modified)
        
        # 7. Add new survival clause in Section 12
        survival_pattern = r'12\.5\s+The provisions of this Agreement that by their nature.*?force and effect\.'
        new_clause = """

12.6 The Parties expressly acknowledge and agree that the provisions of Sections 2.20 and 2.21 of this Amendment regarding External Researcher Access and Post-Project Data Use shall survive the termination of the Agreement and the conclusion of the HE²AT Center Project."""
        modified = find_and_replace(survival_pattern, new_clause, modified)
        
        # 8. Renumber 12.6 to 12.7
        renumber_pattern = r'12\.6\s+The Data Recipient hereby acknowledges'
        new_number = """12.7 The Data Recipient hereby acknowledges"""
        modified = find_and_replace(renumber_pattern, new_number, modified, is_deletion=True)
        
        # 9. Change Effective Date to Amendment Effective Date
        effective_date_pattern = r'IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Effective Date\.'
        amendment_date = """IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Amendment Effective Date."""
        modified = find_and_replace(effective_date_pattern, amendment_date, modified, is_deletion=True)
        
        # Write the modified content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(modified)
            
        print(f"Added tracked changes to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        return False

def main():
    # Define base directories
    base_dir = "/Users/craig/Desktop/Legal-amendment"
    text_dir = os.path.join(base_dir, "Markdown_With_Changes")
    
    # Create a folder for text files with tracked changes
    tracked_changes_dir = os.path.join(base_dir, "Text_With_Tracked_Changes")
    os.makedirs(tracked_changes_dir, exist_ok=True)
    
    # Process each document folder
    for folder_name in ['RP1_UCT_New', 'RP1_WHC_New', 'RP2_WHC']:
        folder_path = os.path.join(text_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue
            
        # Create corresponding output folder
        output_folder = os.path.join(tracked_changes_dir, folder_name)
        os.makedirs(output_folder, exist_ok=True)
        
        # Find original text files
        for file in os.listdir(folder_path):
            if 'Original' in file and file.endswith('.txt'):
                input_path = os.path.join(folder_path, file)
                output_path = os.path.join(output_folder, file.replace('Original', 'Tracked_Changes'))
                
                # Process the file
                success = add_tracked_changes_to_file(input_path, output_path)
                if success:
                    print(f"Successfully created tracked changes for {file}")
                else:
                    print(f"Failed to create tracked changes for {file}")

if __name__ == "__main__":
    main()
    print("Tracked changes processing complete!")
