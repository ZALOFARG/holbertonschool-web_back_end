# Pagination

### 0. Simple helper function

Write a function named index_range that takes two integer arguments\
page and page_size.

The function should return a tuple of size two containing a start\
index and an end index corresponding to the range of indexes to\
return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

### 1. Simple pagination

Copy index range from the previous task and the following class\
into your code

### 2. Hypermedia pagination 

Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and \
defaults) as get_page and returns a dictionary containing the \
following key-value pairs:

Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

### 3. Deletion-resilient hypermedia pagination

The goal here is that if between two queries, certain rows are \
removed from the dataset, the user does not miss items from \
dataset when changing page.
