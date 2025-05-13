"""
Script to create a complete markdown file with tracked changes for RP1_Old document.
"""

import os
import re

def create_full_markdown(input_file, output_file):
    """
    Create a complete markdown document with all tracked changes applied.
    """
    try:
        # Read the original text
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert text to markdown
        markdown = "# " + content.strip().replace("\n\n", "\n\n## ").replace("\n\n##", "\n\n# ")
        
        # Function to find a section using regex
        def find_section(pattern, text):
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(0)
            return None
        
        # Function to insert content after a pattern
        def insert_after(text, pattern, new_content):
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                start, end = match.span()
                return text[:end] + "\n\n" + new_content + text[end:]
            return text
        
        # Function to replace text
        def replace_text(text, pattern, replacement, deletion=True):
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                matched_text = match.group(0)
                if deletion:
                    replacement_text = f"~~<span style='color: red'>{matched_text}</span>~~ <span style='color: blue'>{replacement}</span>"
                else:
                    replacement_text = f"{matched_text} <span style='color: blue'>{replacement}</span>"
                return text.replace(matched_text, replacement_text)
            return text
        
        # Update markdown with all tracked changes
        
        # 1. Find definitions section and add new definitions
        pattern_definitions = r"DEFINITIONS"
        new_definitions = """

## <span style='color: blue'>1.21 "Azure Cloud Platform" means the Microsoft Azure cloud computing service that will serve as the HE²AT Center Primary Repository.

1.22 "Cloud Migration" means the process of transferring the Original Study Data and any derived data sets from the existing on-premises infrastructure to the Azure Cloud Platform.

1.23 "Data Access Committee or DAC" means the committee established by the HE²AT Center to review and approve data access requests from external researchers according to established criteria and protocols, which shall continue to function after the conclusion of the HE²AT Center Project.

1.24 "Data Access Levels" means the tiered access system implemented by the HE²AT Center consisting of:
• Level 0: Original Study Data - Raw, unprocessed data with restricted access to Core Data Team only
• Level 1: Consortium Shared Data - Processed data shared only among HE²AT Center Consortium partners
• Level 2: De-identified Data - Retained by HE²AT Center for approved external researcher access
• Level 3: Inferential Data - Aggregated and anonymized data available for open access

1.25 "External Researcher" means any qualified researcher who is not a member of the HE²AT Center Consortium but who has been approved by the Data Access Committee to access Level 2 data for specific research purposes.

1.26 "Post-Project Data Use" means the continued storage, access, and use of the data after the conclusion of the HE²AT Center Project in accordance with this Amendment.

1.27 "Successor Governance Entity" means any entity or institution that assumes responsibility for the governance, maintenance, and oversight of the Post-Project Data Repository after the conclusion of the HE²AT Center Project.</span>"""
        markdown = insert_after(markdown, pattern_definitions, new_definitions)
        
        # 2. Replace agreement duration text
        pattern_duration = r"shall terminate on"
        new_duration = "~~<span style='color: red'>shall terminate on completion of the HE²AT Project</span>~~ <span style='color: blue'>shall remain in effect in perpetuity with respect to the Post-Project Data Use provisions set forth in Section 2.12 of this Amendment, unless terminated earlier in accordance with the provisions of this Agreement. The Data Provider specifically acknowledges and agrees that the Post-Project Data Use provisions shall survive the termination of the HE²AT Center Project</span>"
        markdown = markdown.replace("shall terminate on completion of the HE²AT Project", new_duration)
        
        # 3. Add enhanced data rights after Section 2.4
        pattern_data_ownership = r"2\.4"
        enhanced_rights = """

<span style='color: blue'>The Data Provider hereby grants the Data Recipient a perpetual, irrevocable, worldwide, non-exclusive license to store the Original Study Data in the Azure Cloud Platform as part of the HE²AT Center's Cloud Migration.

The Data Provider hereby authorizes the Data Recipient to process and transform the Original Study Data to create derived data sets at Levels 1, 2, and 3.

The Data Provider hereby authorizes the Data Recipient to retain the derived data sets for Post-Project Data Use as specifically authorized in this Amendment.

The Data Provider hereby authorizes the Data Recipient to grant access to Level 2 data to External Researchers in accordance with the procedures set forth in this Amendment.

This expanded license does not transfer ownership of the Original Study Data, which remains with the Data Provider.</span>"""
        markdown = insert_after(markdown, pattern_data_ownership, enhanced_rights)
        
        # 4. Replace Core Team reference
        core_team_text = "Core Team for purposes of"
        if core_team_text in markdown:
            new_core_team = "~~<span style='color: red'>Core Team for purposes of</span>~~ <span style='color: blue'>Core HE²AT Center Data Management Team for purposes of</span>"
            markdown = markdown.replace(core_team_text, new_core_team)
        
        # 5. Add Level 0 classification info at the end of Section 2.5
        data_mgmt_plan_text = "HE²AT Center Data Management Plan."
        if data_mgmt_plan_text in markdown:
            level0_info = "HE²AT Center Data Management Plan. <span style='color: blue'>Following the Cloud Migration, the Original Study Data will be classified as Level 0 data in the Azure Cloud Platform's tiered data access system and will remain accessible only to the Core Data Team.</span>"
            markdown = markdown.replace(data_mgmt_plan_text, level0_info)
        
        # 6. Add new sections 2.19-2.21 before section 3
        pattern_section_3 = r"GENERAL"
        new_sections = """

## <span style='color: blue'>2.19 Cloud Storage Infrastructure and Data Migration Authorization

2.19.1 The Data Provider hereby irrevocably authorizes the Data Recipient to:
(a) migrate the Original Study Data from on-premises infrastructure to the Azure Cloud Platform;
(b) store and process the Original Study Data and all derived data sets in the Azure Cloud Platform; and
(c) implement the tiered Data Access Levels system described in this Amendment.

## 2.20 External Researcher Access Authorization

2.20.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission for appropriately de-identified data derived from the Original Study Data (Level 2 Data) to be made available to External Researchers who are not members of the HE²AT Center Consortium, subject to the following conditions:
(a) All External Researcher access requests must be reviewed and approved by the Data Access Committee.
(b) External Researchers must sign a legally binding Data Use Agreement.
(c) External Researchers must commit to appropriate citation of both the HE²AT Center and the original data sources.
(d) External Researchers will only have access to Level 2 data (de-identified).
(e) All External Researcher access will be monitored and logged.
(f) The Data Access Committee shall maintain the right to revoke access for any External Researcher.

## 2.21 Post-Project Data Use and Long-Term Data Retention Authorization

2.21.1 The Data Provider hereby explicitly and irrevocably authorizes and grants permission that the data derived from the Original Study Data shall be retained and may continue to be used beyond the conclusion of the HE²AT Center Project as follows:
(a) Level 0 Data (Original Study Data): Shall be retained for a period of 5 (five) years.
(b) Level 1 Data (Consortium Shared Data): Shall be retained for a period of 10 (ten) years.
(c) Level 2 Data (De-identified Data): Shall be retained indefinitely as a scientific resource.
(d) Level 3 Data (Inferential Data): Shall be retained indefinitely as an open scientific resource.</span>"""
        markdown = insert_after(markdown, pattern_section_3, new_sections)
        
        # 7. Add new survival clause after Section 12.5
        pattern_survival = r"12\.5"
        new_clause = """

## <span style='color: blue'>12.6 The Parties expressly acknowledge and agree that the provisions of Sections 2.20 and 2.21 of this Amendment regarding External Researcher Access and Post-Project Data Use shall survive the termination of the Agreement and the conclusion of the HE²AT Center Project.</span>"""
        markdown = insert_after(markdown, pattern_survival, new_clause)
        
        # 8. Renumber 12.6 to 12.7
        if "12.6" in markdown:
            markdown = markdown.replace("12.6", "~~<span style='color: red'>12.6</span>~~ <span style='color: blue'>12.7</span>")
        
        # 9. Change Effective Date to Amendment Effective Date
        if "the Effective Date" in markdown:
            amendment_date = "~~<span style='color: red'>the Effective Date</span>~~ <span style='color: blue'>the Amendment Effective Date</span>"
            markdown = markdown.replace("the Effective Date", amendment_date)
        
        # Add a header with explanation of tracked changes
        header = """# DATA TRANSFER AGREEMENT WITH TRACKED CHANGES - RP1 OLD VERSION

**Legend:**
- ~~<span style='color: red'>Red strikethrough text</span>~~ = deleted text
- <span style='color: blue'>Blue text</span> = added text

---

"""
        markdown = header + markdown
        
        # Write the markdown to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Created complete markdown with tracked changes for RP1_Old: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error creating markdown: {e}")
        return False

# Define base directories
base_dir = "/Users/craig/Desktop/Legal-amendment"
input_dir = os.path.join(base_dir, "Markdown_With_Changes", "RP1_Old")
output_dir = os.path.join(base_dir, "Full_Markdown_With_Changes", "RP1_Old")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Process RP1_Old document
input_file = os.path.join(input_dir, "RP1_WHC_Original.txt")
output_file = os.path.join(output_dir, "RP1_WHC_Original_Complete_With_Changes.md")

if os.path.exists(input_file):
    success = create_full_markdown(input_file, output_file)
    if success:
        # Copy to Final_Word_Documents
        final_dir = os.path.join(base_dir, "Final_Word_Documents", "RP1_Old")
        os.makedirs(final_dir, exist_ok=True)
        import shutil
        shutil.copy2(output_file, os.path.join(final_dir, "RP1_WHC_Original_Complete_With_Changes.md"))
        print(f"Copied markdown file to {final_dir}")
    else:
        print("Failed to create markdown with tracked changes for RP1_Old")
else:
    print(f"Error: Input file {input_file} not found")
