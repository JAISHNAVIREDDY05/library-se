# TRACEABILITY MATRIX

This document provides traceability between user stories, source code,
unit tests, and Git release tags.

| Sprint | User Story ID | Description | Source Code | Test Case | Git Tag |
|-------|---------------|-------------|-------------|-----------|---------|
| Sprint-1 | US-01 | Add a book with ID, title, and author |src/library.py:add_book()    | tests/test_library.py:test_add_book_success   |v0.1  |
| Sprint-1 | US-02 | Reject duplicate Book IDs |  |  |  |
| Sprint-2 | US-03 | Borrow and return books |src/library.py:borrow_book(), return_book()  | tests/test_library.py:test_borrow_available_book, test_return_book|v0.2  |
| Sprint-3 | US-04 | Generate library report |  |  |  |

