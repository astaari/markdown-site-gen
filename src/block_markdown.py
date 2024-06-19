

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    result = []
    for s in block_strings:
        if not s:
            continue
        result.append(s.strip())
    return result 


def block_to_block_type(block):
    import re
    lines = block.split("\n")


    if re.match("^[(#)]{1,6}",block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                print(line)
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("1."):
        itr = 2
        for line in lines[1:]:
            if not line.startswith(f"{itr}."):
                return block_type_paragraph
            itr+=1
        return block_type_ordered_list
    return block_type_paragraph

