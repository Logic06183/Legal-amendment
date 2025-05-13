"""
Script to fix the tracked changes in the RP1_Old markdown document.
"""

import re

# Path to the markdown file
markdown_file = "/Users/craig/Desktop/Legal-amendment/Final_Word_Documents/RP1_Old/RP1_WHC_Complete_With_Changes.md"

# Read the current content
with open(markdown_file, 'r', encoding='utf-8') as file:
    content = file.read()

# 1. Fix Agreement Duration (Section 2.1)
content = content.replace(
    "2.1\tThis Agreement shall commence on the Commencement Date and shall terminate on completion of the HE2AT Project.",
    "2.1\tThis Agreement shall commence on the Commencement Date and ~~<span style='color: red'>shall terminate on completion of the HE2AT Project</span>~~ <span style='color: blue'>shall remain in effect in perpetuity with respect to the Post-Project Data Use provisions set forth in Section 2.12 of this Amendment, unless terminated earlier in accordance with the provisions of this Agreement. The Data Provider specifically acknowledges and agrees that the Post-Project Data Use provisions shall survive the termination of the HE²AT Center Project</span>."
)

# 2. Fix Core Team Reference (Section 2.5)
content = re.sub(
    r"2\.5\s*The Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the Core HE²AT Data Management Team for purposes",
    "2.5\tThe Data Provider acknowledges and agrees that initially the Original Study Data shall be accessible only to the ~~<span style='color: red'>Core Team</span>~~ <span style='color: blue'>Core HE²AT Center Data Management Team</span> for purposes",
    content
)

# 3. Fix Renumbering (12.6 to 12.7)
content = re.sub(
    r"12\.6\s*The Data Recipient hereby acknowledges",
    "~~<span style='color: red'>12.6</span>~~ <span style='color: blue'>12.7</span>\tThe Data Recipient hereby acknowledges",
    content
)

# 4. Fix Amendment Effective Date
content = re.sub(
    r"IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Effective Date",
    "IN WITNESS WHEREOF, the Parties have executed this Agreement as of the ~~<span style='color: red'>Effective Date</span>~~ <span style='color: blue'>Amendment Effective Date</span>",
    content
)

# Write the updated content
with open(markdown_file, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"Fixed tracked changes in {markdown_file}")
