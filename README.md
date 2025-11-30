
# Project-3-Tree-Applications---AJTenn-JerrickLittle
Project 3: Tree Applications

## Project Title and Description

### Tree Choice: B-Tree

### Application Details
The application generates data that is similar to a company contact manager, with a bunch of "client" names and their respective companies, and some other basic information about them. As discussed later, this is done in the data generation and contact.py files, and the contact information can be extended to add more fields if wanted. With this generated data, the B-Tree implementation initializes and builds the B-Tree. Finally, the user is able to interact with the tree, with 5 basic interactions: 
1: Show Whole Traversal
2: Search for a contact by last name
3: Insert a contact
4: Delete a contact by last name
5: Exit

### Use-Case
The Use-Case would be for data scientists, sales, and other workers within a company that have full access to a database of clients, and want to maybe contact them, or learn more about them using this contact manager system.

## Team Members: AJ Tennathur & Jerrick Little

## Installation & Setup

### Prerequisites (Python version, libraries, etc.)
Faker Python Library IS REQUIRED for the data generation code to run. If not installed, you must install this before it will work.

### Step-by-step setup instructions
Have the following files loaded: 
- B_Tree_Imply.py
- contact.py
- data_generation.py

Then follow the following instructions in the Usage Guide. 

## Usage Guide

### How To Use
Steps: 
1: Go to the data generation file. Scroll to the line: contacts = generate_contacts(50). In the submitted project, this means that the data set will have 50 contacts. You can adjust this depending on what you would like, or you can keep this, as it works perfectly well with 50 contacts. 
2. RUN THE data_generation.py file. This is essential as it will create a csv file within the folder, that has the data that the BTree needs in order to build the tree.
3. Run the B_Tree_Impl.py file. You now have the 5 options discussed above to choose from. Proceed from there. 

Important: When inserting a contact, include all the information as guided by the prompts. 

## Example Command & Expected Input/Output

Contact Manager B-Tree Options:
1: Show Whole Traversal
2: Search for a contact by last name
3: Insert a contact
4: Delete a contact by last name
5: Exit
Enter your choice: 1

All contacts in B-tree (in order):
Contact(0, Michele, Dennis, Freeman-Carter, 3696541514)
Contact(1, Alicia, Burgess, Miller, Powell and Richardson, 1565715979)
Contact(2, Joshua, Lopez, Briggs-Johnson, 8151753679)
Contact(3, Jonathan, Hamilton, Perez-Stark, 0520431365)
Contact(4, Eileen, Reed, George, Sutton and Beck, 7840442660)
Contact(5, Nicholas, Martinez, Chaney-Carroll, 8466225324)
Contact(6, David, Clark, Brewer Ltd, 7448498520)
Contact(7, Kathryn, Gomez, Harmon Group, 9180262104)
Contact(8, Emily, Mendoza, Lopez Inc, 0859193540)
Contact(9, Alexander, Mcconnell, Whitney and Sons, 8685921241)
Contact(10, Christopher, Taylor, Romero-Smith, 2087026090)
Contact(11, Dustin, Smith, Hurley, Bowen and Lee, 8937380419)
Contact(12, Stephanie, Hoover, Miller Inc, 3801143788)
Contact(13, Gerald, English, Chapman-Rogers, 1354180096)
Contact(14, Teresa, Gillespie, Thompson Inc, 3305757556)
Contact(15, Kyle, Wallace, Taylor, Solomon and Leblanc, 4057936811)
Contact(16, Jason, Cruz, Hicks-Tucker, 0157700707)
Contact(17, Chloe, Huang, Thomas-Johnson, 8055311382)
Contact(18, James, Smith, Lopez-Bailey, 9853309221)
Contact(19, Chris, Sellers, Turner PLC, 5670577504)
Contact(20, Christopher, Harris, Torres, Ramirez and Sanford, 1412271251)


Contact Manager B-Tree Options:
1: Show Whole Traversal
2: Search for a contact by last name
3: Insert a contact
4: Delete a contact by last name
5: Exit
Enter your choice: 2
Enter last name to search: Hoover
Found contacts:
Contact(12, Stephanie, Hoover, Miller Inc, 3801143788)

## Screenshots/Demos
- See screenshots in Example_Screenshots Folder for example usage.

## Tree Implementation Details

### How the B-Tree Works
The B-Tree data structure efficiently stores, searches, inserts, deletes, and traverses contact records. Each contact is stored as a key-value pair, where the key is the `contact_id` and the value is a `Contact` object. The B-Tree is a balanced tree that maintains sorted data and allows operations in logarithmic time by splitting and merging nodes when needed. 

Important:

- The B-Tree is implemented from scratch, supporting all the major/important operations (insert, delete, search, range query, traversal).
- Contacts are stored as objects, allowing for easy extension of contact fields.

### Time & Space Complexity (Big O)
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)
- Traversal: O(n)
- Space Complexity: O(n), where n is the number of contacts stored. Each node contains up to `2t-1` keys and up to `2t` children, where `t` is the minimum degree of the tree. This is by definition of the B-tree structure.

### Interesting Implementation Choices
- The application supports user interaction for searching, inserting, and deleting contacts by last name, making it user-friendly.
- The data generation code utilizes Python's Faker library to create "realistic" contact data (names, company names) for testing and demonstration. This is so that when the user interacts, they are seeing realistic names, and then can search/delete names. 

## Interface Evolution

### Initial Design Differences
- The initial design used randomly generated, non-realistic names and company data for contacts, making the dataset less practical for real-world scenarios and user testing.
- The Contact class was duplicated in both the data generation and B-Tree implementation files, leading to redundancy.
- The user interface was limited to simple print statements and did not allow for interactive searching, insertion, or deletion of contacts. It only included the base viewing of the whole tree traversal.
- The B-Tree was built from randomly generated data each time, rather than from a persistent dataset (CSV file). This is because the data generation code was within the implementation, so each time, a new dataset of randomly generated data was used to build the B-Tree.

### Reason for changes
- Realistic data generation was added using Python's Faker library to make the application more useful for demonstration and testing.
- The Contact class became a shared module to avoid redundancy and ensure consistency.
- A command-line interface was implemented to allow users to interactively search, insert, and delete contacts, making the application more user-friendly and actually applicable.
- The use of a CSV file for data storage allows for persistent datasets and easier testing, rather than regenerating random data on each run. The data generation code was also moved to another file.

### What I Learned
- Importance of having well-structured data. 
- Not having redundant classes in order to optimize space complexity. 
- B-Trees are very efficient, but all the implementations need to work well for the B-Tree to be built effectively, be able to search, insert, or delete. 

## Challenges/Future Enhancements
- Ensuring all B-Tree operations (insert, delete, search) work correctly and efficiently for all edge cases was challenging, especially for deletion and rebalancing.
- Maintaining data consistency and avoiding redundancy required careful refactoring (e.g., moving the Contact class to a shared module).
- Handling user input validation and error cases in the command-line interface.

- The application could be enhanced by supporting additional search options (like searching by company or phone number).
- For even better performance with large datasets, I can consider implementing a B+ Tree, which is optimized for disk-based storage and range queries.
- Adding a GUI or web interface could make the application more accessible and user-friendly. Currently uses CLI.
- Implementing authentication or access control for sensitive contact data. This would be especially useful in order to protect "client" information and only provide access to specific users and maintain that privacy boundary.



README.md
Displaying contacts_BTree.csv.