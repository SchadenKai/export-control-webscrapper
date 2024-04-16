system_message = """
    You are an export data engineer. 
    You are tasked to create a clean dataset for my AI chat agent that has no missing values or flaws.
    The dataset will be represented in table format. 
"""

def generate_prompt(content=''):
    prompt = f"""
    As a data engineer, I need to create a clean dataset for my AI chat agent. Provide a table structure based on the given content below with the following columns:

    Category: This column represents the category of the item. Categories are denoted as Category 0, Category 1, ..., Category 9. If the category cannot be seen directly, it's represented as the first character of the 5-character code of the item.

    Subcategory: This column represents both the category and the subcategory. Each subcategory is represented by a combination of the category and a letter from A to E, where A = Systems, equipment, and components; B = test, inspection, and production equipment; C = materials; D = software; E = technology. If the subcategory cannot be directly identified, it's represented as the first two characters of the 5-character code of the item.

    Item: This column represents the specific item. It includes variations of the 5-character code for specific items, sub-items (represented by a letter), sub-sub-items (represented by a number), or sub-sub-sub-items (represented by a letter). Variations of the 5-character code are also included, such as 1B233.

    Description: This column contains a description of the item. It's derived from the direct paragraph associated with the 5-character code, its sub-item (represented by a letter), sub-sub-item (represented by a number), or sub-sub-sub-item (represented by a letter). Descriptions include details about the item.

    Technical Note/Note/N.B.: This column contains additional notes related to a specific item. It includes content found after the text "Technical Note / Note / N.B." and provides extra information about the item.

    When recording an item or entry in the table, ensure to fill in the Category and Subcategory columns based on its parent category and subcategory, as this is important for identification purposes.
    
    This is the content below: 
    {content}
    """
    return prompt

# def generate_prompt(content, topic):
#     prompt = f"""
#     As a data engineer, I want to create a clean dataset for my AI chat agent. Provide a table structure of the given content below with the following columns which will be the clean dataset for my AI chat agent:

#     Category: e.g. Category 0, Category 1, ... Category 9. If the Category cannot be seen, it can be seen represented as the first character of the 5 character code of the item.
#     Subcategory: e.g. 0A, 0B, 0C, etc. This column represents both the category, which is the first character plus the subcategory it is, which is the second character that is letters from A - E. Each letter from A - E represents different components under that category such as A = Systems, equipment, and components; B = test, inspection, and production equipment; C = materials; D = software; E = technology. If cannot be seen or identified, it can be seen as the first two characters of the 5 character code of the item
#     Item: e.g. 0A001, 0A001.a, 0A001.i.1. This represents other variations of the 5 character code for specific items of a category and subcategory.
#     Description: for 0A that would be "Systems, Equipment and Components", for 0A001 that would be "Nuclear reactors" and specially designed or prepared equipment and components therefor, as follows:, for 0A001.a that would be "Nuclear reactors"; and for 0A001.i.1 that would be "Heat exchangers as follows Steam generators specially designed or prepared for the primary, or intermediate, coolant circuit of a "nuclear reactor";". This will be coming from the direct paragraph a 5 character code, its sub item (represented by a letter. ex. 0A001.a), sub sub item (represented by a number. ex. 0A001.a.1), or sub sub sub item (represented by a letter. ex. 0A00A.a.1.a). There are also different variation of combinations of that 5 character code such as 1B233.
#     Technical Note/Note/N.B.: e.g. In 0A001.h. 'nuclear reactor internals' means any major structure within a reactor vessel which has one or more functions such as supporting the core, maintaining fuel alignment, directing primary coolant flow, providing radiation shields for the reactor vessel, and guiding in-core instrumentation. This is the text content which is after the following side note text: Technical Note / Note / N.B. This contains additional notes in regards to a specific item.

#     This is the content below:
#     {content}
#     """
#     return prompt

# def generate_prompt(content):
#     prompt = f"""
#     As a data engineer, I want to create a clean dataset for my ai chat agent. Provide a table structure of the given content below with the following columns which will be the clean dataset for my ai chat agent:

#     Category: e.g. Category 0, Category 1, ... Category 9. If the Category cannot be seen, it can be seen represented as the first character of the 5 character code of the item.
#     Subcategory: e.g. 0A, 0B, 0C, etc. This column represents both the category, which is the first character plus the subcategory it is, which is the second character that is letters from A - E. Each letters from A - E represent different components under that category such as A = Systems, equipment, and components; B = test, inspection, and production equipment; C = materials; D = software; E = technology. If cannot be seen or identified, it can be seen as the first two characters of the 5 character code of the item
#     Item: e.g. 0A001, 0A001.a, 0A001.i.1. This represents other variations of the 5 character code for specific items of a category and sub category. 
#     Description: for 0A that would be "Systems, Equipment and Components", for 0A001 that would be "Nuclear reactors"and specially designed or prepared equipment and components therefor, as follows:, for 0A001.a that would be "Nuclear reactors"; and for 0A001.i.1 that would be "Heat exchangers as follows Steam generators specially designed or prepared for the primary, or intermediate, coolant circuit of a "nuclear reactor";". This will be coming from the direct paragraph a 5 character code, its sub item (represented by a letter. ex. 0A001.a), sub sub item (represented by a number. ex. 0A001.a.1), or sub sub sub item (represented by a letter. ex. 0A00A.a.1.a). There are also different variation of combinations of that 5 character code such as 1B233.
#     Technical Note/Note/N.B.: e.g. In 0A001.h. 'nuclear reactor internals' means any major structure within a reactor vessel which has one or more functions such as supporting the core, maintaining fuel alignment, directing primary coolant flow, providing radiation shields for the reactor vessel, and guiding in-core instrumentation. This is the text content which is after the following side note text: Technical Note / Note / N.B. This contains additional notes in regards to a specific item. 

#     This is the content below:
#     {content}

#     If an item is being recorded in the table, you need to fill in also the Category and Subcategory, since this is important for identification purposes.
#     """