# Plan for Many-to-Many Relationship Implementation

## Analysis Summary

From reading the test files and requirements, I need to implement:

### Article Class

- `__init__(self, author, magazine, title)` - Initialize with author, magazine, title
- `title` property (immutable, str, 5-50 chars)
- `author` property (mutable, type Author)
- `magazine` property (mutable, type Magazine)
- Class attribute `Article.all = []` (for tracking all articles)

### Author Class

- `__init__(self, name)` - Initialize with name
- `name` property (immutable, str, > 0 chars)
- `articles()` - Returns list of Article objects
- `magazines()` - Returns unique list of Magazine objects
- `add_article(magazine, title)` - Creates and returns new Article
- `topic_areas()` - Returns unique list of category strings

### Magazine Class

- `__init__(self, name, category)` - Initialize with name and category
- `name` property (mutable, str, 2-16 chars)
- `category` property (mutable, str, > 0 chars)
- `articles()` - Returns list of Article objects
- `contributors()` - Returns unique list of Author objects
- `article_titles()` - Returns list of title strings
- `contributing_authors()` - Returns authors with > 2 articles

## Implementation Order

1. **Article Class** - Basic properties and validation
2. **Author Class** - Basic properties and validation
3. **Magazine Class** - Basic properties and validation
4. **Article relationships** - Link to author and magazine
5. **Author relationships** - articles() and magazines()
6. **Magazine relationships** - articles() and contributors()
7. **Aggregate methods** - add_article, topic_areas, article_titles, contributing_authors

## Key Implementation Notes

- Use private attributes with properties for validation
- Need to append articles to `Article.all` list
- Use set() for unique results where needed
- Handle None returns when no articles exist

---

# Implementation TODO List

## Step 1: Implement Article Class

- [x] Add Article class with `__init__` method
- [x] Add `_title` private attribute
- [x] Add `title` property (immutable, validate str, 5-50 chars)
- [x] Add `author` property (mutable, store \_author)
- [x] Add `magazine` property (mutable, store \_magazine)
- [x] Add `Article.all = []` class attribute
- [x] Append new article to Article.all in **init**

## Step 2: Implement Author Class

- [x] Add Author class with `__init__` method
- [x] Add `_name` private attribute
- [x] Add `name` property (immutable, validate str, > 0 chars)
- [x] Implement `articles()` method (filter Article.all)
- [x] Implement `magazines()` method (unique magazines from articles)
- [x] Implement `add_article(magazine, title)` method
- [x] Implement `topic_areas()` method (unique categories from magazines)

## Step 3: Implement Magazine Class

- [x] Add Magazine class with `__init__` method
- [x] Add `_name` private attribute
- [x] Add `_category` private attribute
- [x] Add `name` property (mutable, validate str, 2-16 chars)
- [x] Add `category` property (mutable, validate str, > 0 chars)
- [x] Implement `articles()` method (filter Article.all)
- [x] Implement `contributors()` method (unique authors from articles)
- [x] Implement `article_titles()` method (return titles list or None)
- [x] Implement `contributing_authors()` method (authors with >2 articles)

## Step 4: Test Implementation

- [x] Run pytest to verify all tests pass
- [x] Test edge cases
