# Legal-amendment Project README

## Project Overview

This repository contains Data Transfer Agreements (DTAs) for the HE²AT Center Project, with amendments related to cloud storage, external researcher access, and post-project data use. The documents are prepared for University of Cape Town (UCT) and Wits Health Consortium (WHC) with tracked changes showing all modifications.

## Repository Structure

### Main Document Groups
- **RP1_UCT_New**: UCT-specific RP1 documents
- **RP1_WHC_New**: WHC-specific RP1 documents
- **RP2_WHC**: WHC RP2 documents
- **RP1_Old**: Original WHC RP1 document with amendments

### Document Formats
- **Markdown Files**: Each document group contains markdown files with HTML-style tracked changes
  - Blue text = additions
  - Red strikethrough text = deletions
- **Word Documents**: Corresponding Word documents with tracked changes for each document group

### Key Folders
- **/Final_Word_Documents/**: Main working directory with all finalized versions
- **/Amendment_docs/**: Contains the LaTeX amendment template (Amendment.tex)
- **/Lawyer_Editable_Word_Docs/**: Lawyer-editable Word documents with tracked changes

### Analysis Documents
- **amendment_changes_table.md**: Table summarizing all changes made to each document
- **Legal_Document_Amendments_Visualization.drawio**: Visualization diagram of changes

### Utility Scripts
- **convert_markdown_to_word.py**: Script to convert markdown with tracked changes to Word format
- Other utility scripts for document processing and reorganization

## Key Amendments

All documents incorporate the following key amendments:

1. **New Definitions**: Azure Cloud Platform, Cloud Migration, Data Access Committee, etc.
2. **Agreement Term Change**: Extended for perpetual Post-Project Data Use
3. **Cloud Migration Authorization**: Permission to migrate data to Azure Cloud
4. **External Researcher Access**: Authorization for controlled access by external researchers
5. **Post-Project Data Use**: Long-term data retention at different access levels
6. **Enhanced Security Provisions**: Cloud-specific security measures
7. **Survival Clause**: Ensuring certain provisions survive agreement termination

## Working with the Documents

### For Legal Teams
The documents in the **/Lawyer_Editable_Word_Docs/** folder are specifically formatted for legal review with:
- Proper tracked changes
- Consistent formatting across all documents
- Section numbering aligned with the original agreements

### For Technical Teams
- The markdown files in **/Final_Word_Documents/** provide a clean, version-controlled view of changes
- The python scripts allow for automated processing and conversion

## Special Notes on Section Numbering
- RP1_UCT and RP1_WHC use placeholder section numbers (2.Y, 2.Z)
- RP2_WHC and RP1_Old_WHC use specific section numbers (2.20, 2.21)
- All documents maintain consistent content despite numbering differences

## Amendment Effective Date
All documents refer to an "Amendment Effective Date" which will be the date of signature of the last Party to sign the Amendment.
