# Report Guide — Stacks Implementation

Use the assignment's specified format: **Tahoma, 10 pt, 1.15 line spacing, justified alignment**. The assignment does not state a required page count. Replace placeholders with your actual details and insert screenshots from your own successful run.

## 1. Title Page
- Institution: Limkokwing University of Creative Technology, Sierra Leone
- Module: Data Structures and Algorithms
- Assignment: Stacks Implementation
- Student name: [Your name]
- Student ID: [Your ID, if required]
- Semester: September 2026–February 2027
- Submission date: [Date]

## 2. Introduction
Explain the purpose of the program: to read arithmetic expressions from `input.txt`, evaluate them using stacks, and write results to `output.txt` while preserving separator lines.

## 3. Data Structures Used
Describe the Stack class and its LIFO behavior. Explain `push`, `pop`, `peek`, `is_empty`, and `size`. Explain why two stacks are used: one for operands and one for operators.

## 4. Program Design
Describe each source file:
- `stack.py`: stack operations
- `tokenizer.py`: identifies numbers and symbols
- `expression_evaluator.py`: precedence and parentheses
- `file_handler.py`: input/output processing
- `main.py`: command-line entry point

Include a flowchart or pseudocode if useful. Explain that the evaluator does not use Python's `eval()`.

## 5. Testing and Results
Run the program and unit tests. Insert screenshots of:
1. The project files in VS Code.
2. The sample `input.txt`.
3. The terminal showing `python main.py`.
4. The generated `output.txt`.
5. The test suite results.

Discuss the supplied examples and additional cases: precedence, parentheses, nested parentheses, decimal numbers, negative results, malformed expressions, and division by zero. Report only results you actually observed.

## 6. Conclusion
Summarize what the program demonstrates about stack operations, expression evaluation, operator precedence, file handling, and testing. Mention limitations and possible future improvements.

## 7. GitHub
Include the repository URL after uploading your project. Add the lecturer as a collaborator as instructed by the assignment.

## 8. References
List only resources you actually consulted, using the citation style your lecturer expects if one was specified.
