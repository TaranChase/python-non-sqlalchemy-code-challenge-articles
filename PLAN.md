# Implementation Plan for Articles Code Challenge

## Domain Model
- **Author** has many Articles
- **Magazine** has many Articles  
- **Article** belongs to both Author and Magazine (many-to-many between Author and Magazine)

## Implementation Order (Recommended)

### Phase 1: Basic Classes & Initializers
1. **Article class** - Basic initializer with author, magazine, title
2. **Author class** - Basic initializer with name
3. **Magazine class** - Basic initializer with name, category
4. Add `Article.all = []` class variable to track all articles

### Phase 2: Properties
1. Article.title property (immutable, validates 5-50 chars)
2. Author.name property (immutable, validates non-empty string)
3. Magazine.name property (mutable, validates 2-16 chars)
4. Magazine.category property (mutable, validates non-empty string)
5. Article.author property (mutable, returns Author)
6. Article.magazine property (mutable, returns Magazine)

### Phase 3: Object Relationship Methods
1. Author.articles() - Returns list of articles for author
2. Magazine.articles() - Returns list of articles for magazine
3. Author.magazines() - Returns unique list of magazines author contributed to
4. Magazine.contributors() - Returns unique list of authors for magazine

### Phase 4: Aggregate & Association Methods
1. Author.add_article(magazine, title) - Creates and returns new Article
2. Author.topic_areas() - Returns unique list of category strings
3. Magazine.article_titles() - Returns list of title strings
4. Magazine.contributing_authors() - Returns authors with >2 articles

### Phase 5: Testing & Refinement
1. Run pytest to check implementation
2. Fix any failing tests
3. Clean up code if time permits

## Key Implementation Details

### Track All Articles
```python
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
```

### Author Methods
```python
def articles(self):
    return [article for article in Article.all if article.author == self]

def magazines(self):
    return list(set(article.magazine for article in self.articles()))

def add_article(self, magazine, title):
    return Article(self, magazine, title)

def topic_areas(self):
    articles = self.articles()
    if not articles:
        return None
    return list(set(article.magazine.category for article in articles))
```

### Magazine Methods
```python
def articles(self):
    return [article for article in Article.all if article.magazine == self]

def contributors(self):
    return list(set(article.author for article in self.articles()))

def article_titles(self):
    articles = self.articles()
    if not articles:
        return None
    return [article.title for article in articles]

def contributing_authors(self):
    articles = self.articles()
    if not articles:
        return None
    author_counts = {}
    for article in articles:
        author_counts[article.author] = author_counts.get(article.author, 0) + 1
    contributing = [author for author, count in author_counts.items() if count > 2]
    return contributing if contributing else None
```

## Testing Strategy
1. Start with `python lib/debug.py` to test manually
2. Run `pytest` to see test results
3. Fix failing tests one by one
4. Ensure all tests pass before submission

