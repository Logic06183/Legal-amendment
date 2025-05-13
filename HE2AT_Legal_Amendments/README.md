# HE²AT Center Legal Amendments Package

This package contains the complete set of legal amendment documents for the HE²AT Center Data Transfer Agreements with enhanced formatting and styling. All documents maintain tracked changes for legal review.

## Folder Structure

This package is organized into the following folders:

```
HE2AT_Legal_Amendments/
├── Word_Documents/ - Professional Word documents with tracked changes (for legal review)
├── LaTeX_Documents/ - LaTeX files and PDFs (for archival and reference)
├── Source_Documents/ - Original markdown files with tracked changes
├── Conversion_Scripts/ - Tools for converting between formats
├── Diagrams/ - Visual representations of the amendment process
├── amendment_changes_table.md - Complete matrix of all changes
└── README.md - This guide
```

## Document Overview

The package includes the following key documents:

### Word Documents (Ready for Legal Review)

All Word documents have been professionally styled with:
- Times New Roman font
- Proper legal document margins (1.25" sides, 1" top/bottom)
- Header with "HE²AT CENTER" branding
- Page numbers in footer
- Tracked changes clearly shown (red strikethrough for deletions, blue text for additions)

Key documents:
- `RP1_UCT_Enhanced_Legal.docx` - University of Cape Town agreement (RP1 - latest version)
- `RP1_WHC_Enhanced_Legal.docx` - Wits Health Consortium agreement (RP1 - latest version)
- `RP2_WHC_Enhanced_Legal.docx` - Wits Health Consortium agreement (RP2 version)
- `RP1_Old_WHC_Enhanced_Legal.docx` - Wits Health Consortium original agreement with amendments

## Document Organization by Institution and Research Project

The HE²AT Center manages multiple data transfer agreements (DTAs) across different research projects and institutions. Below is a clear explanation of what each document represents:

### By Institution

**University of Cape Town (UCT) Documents**
- `RP1_UCT_Enhanced_Legal.docx` - The UCT agreement for Research Project 1 with all tracked amendments

**Wits Health Consortium (WHC) Documents**
- `RP1_WHC_Enhanced_Legal.docx` - The WHC agreement for Research Project 1 (new version)
- `RP2_WHC_Enhanced_Legal.docx` - The WHC agreement for Research Project 2
- `RP1_Old_WHC_Enhanced_Legal.docx` - The original WHC agreement for Research Project 1 (previous version)

### By Research Project

**Research Project 1 (RP1)**
- `RP1_UCT_Enhanced_Legal.docx` - UCT version
- `RP1_WHC_Enhanced_Legal.docx` - WHC current version
- `RP1_Old_WHC_Enhanced_Legal.docx` - WHC original version

**Research Project 2 (RP2)**
- `RP2_WHC_Enhanced_Legal.docx` - WHC version

### Version Timeline

**Original/Old Versions**
- `RP1_Old_WHC_Enhanced_Legal.docx` - The initial WHC agreement for RP1

**Current/New Versions**
- `RP1_UCT_Enhanced_Legal.docx` - Current UCT agreement for RP1
- `RP1_WHC_Enhanced_Legal.docx` - Updated WHC agreement for RP1
- `RP2_WHC_Enhanced_Legal.docx` - Current WHC agreement for RP2

### LaTeX Documents

The LaTeX folder contains professionally typeset documents:
- `Amendment.tex/pdf` - The formal amendment document template
- `Cover letter.tex/pdf` - Cover letter to accompany amendments
- `FAQ.tex/pdf` - Frequently asked questions document

### Visual Diagrams

The `Diagrams` folder contains:
- `Legal_Document_Amendments_Overview.drawio` - High-level overview of the amendment process
- `Legal_Document_Amendments_Visualization.drawio` - Visual relationships between documents and changes

### Amendment Table

The `amendment_changes_table.md` file provides a complete matrix of all changes across all document versions, making it easy to:
- Compare changes across different document versions
- Identify specific sections that were modified
- Track which changes apply to which institutional agreements

### Source Documents

Original markdown files with tracked changes that serve as the source for the Word and LaTeX conversions.

## Amendment Changes Summary

| Section | Change Description | RP1_UCT | RP1_WHC | RP2_WHC | RP1_Old_WHC |
|---------|-------------------|---------|---------|---------|---------|
| **Definitions** | Added "Azure Cloud Platform" | ✓ | ✓ | ✓ | ✓ |
| | Added "Cloud Migration" | ✓ | ✓ | ✓ | ✓ |
| | Added "Data Access Committee" | ✓ | ✓ | ✓ | ✓ |
| | Added "Data Access Levels" | ✓ | ✓ | ✓ | ✓ |
| | Added "External Researcher" | ✓ | ✓ | ✓ | ✓ |
| | Added "Post-Project Data Use" | ✓ | ✓ | ✓ | ✓ |
| | Added "Successor Governance Entity" | ✓ | ✓ | ✓ | ✓ |
| **Agreement Term** | Modified to allow perpetual Post-Project Data Use | ✓ (Section 2.1) | ✓ (Section 2.1) | ✓ (Section 2.1) | ✓ (Section 2.1) |
| **Data Rights** | Extended license for cloud storage | ✓ | ✓ | ✓ | ✓ |
| | Authorization for data transformation | ✓ | ✓ | ✓ | ✓ |
| | Authorization for External Researcher access | ✓ | ✓ | ✓ | ✓ |
| **Cloud Migration** | Authorization to migrate to Azure | ✓ (Section 2.X) | ✓ (Section 2.X) | ✓ (Section 2.19) | ✓ (Section 2.19) |
| | Security measures in Azure Cloud | ✓ | ✓ | ✓ | ✓ |
| | Data security methods by Access Level | ✓ | ✓ | ✓ | ✓ |
| **External Researcher Access** | Terms for external access authorization | ✓ (Section 2.Y) | ✓ (Section 2.Y) | ✓ (Section 2.20) | ✓ (Section 2.20) |
| | DAC approval requirement | ✓ | ✓ | ✓ | ✓ |
| | Data Use Agreement requirement | ✓ | ✓ | ✓ | ✓ |
| **Post-Project Data Use** | Data retention periods by level | ✓ (Section 2.Z) | ✓ (Section 2.Z) | ✓ (Section 2.21) | ✓ (Section 2.21) |
| | Level 0 (5 years) | ✓ | ✓ | ✓ | ✓ |
| | Level 1 (10 years) | ✓ | ✓ | ✓ | ✓ |
| | Levels 2-3 (indefinite) | ✓ | ✓ | ✓ | ✓ |
| **Security Provisions** | Enhanced cloud security safeguards | ✓ (Section 6) | ✓ (Section 6) | ✓ (Section 6) | ✓ (Section 6) |
| | Extended security breach notification | ✓ (Section 7) | ✓ (Section 7) | ✓ (Section 7) | ✓ (Section 7) |

## Conversion Tools

The `Conversion_Scripts` folder contains several Python scripts for converting between different formats:

1. `enhanced_legal_styling.py` - Latest tool with professional legal document styling
   ```
   python enhanced_legal_styling.py input_markdown.md output_docx.docx
   ```

2. `convert_single_markdown.py` - Converts a single markdown file to Word
   ```
   python convert_single_markdown.py input_markdown.md output_docx.docx
   ```

3. `markdown_to_latex_converter.py` - Converts markdown to LaTeX/PDF
   ```
   python markdown_to_latex_converter.py input_markdown.md output_directory
   ```

4. `enhanced_word_converter.py` - Previous version of the Word converter

## Usage Instructions

### For Legal Review
1. Share the Word documents in the `Word_Documents` folder with legal team
2. All tracked changes are clearly marked with red strikethrough (deletions) and blue text (additions)
3. Include the LaTeX PDF files for reference if desired

### For Creating New Versions
1. Update the source markdown files in `Source_Documents`
2. Use the conversion scripts to generate new Word or LaTeX documents

## Key Amendment Details

1. **Cloud Migration**: Authorization to migrate data to Azure Cloud Platform with enhanced security
2. **External Researcher Access**: Framework for sharing de-identified data with qualified researchers
3. **Post-Project Data Use**: Data retention periods based on sensitivity levels
4. **Enhanced Security**: Additional safeguards for cloud-based storage and access

## Notes for Legal Team

- All amendments preserve data ownership rights of the original data providers
- Level 0 (raw) data will be deleted after 5 years unless explicitly approved for longer retention
- External researcher access limited to de-identified (Level 2) data only
- All access governed by Data Access Committee with comprehensive audit trails
