class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = None
        self.title = title  # Use property setter for validation
        self._author = None
        self.author = author
        self._magazine = None
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Validate title is a string and length is 5-50 characters
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = None
        # Set name directly without going through setter to bypass immutability check
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name is immutable - silently ignore any attempts to change it
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = set()
        for article in self.articles():
            unique_magazines.add(article.magazine)
        return list(unique_magazines)

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        unique_categories = set()
        for magazine in magazines:
            unique_categories.add(magazine.category)
        return list(unique_categories)


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Use property setter for validation
        self.category = category  # Use property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Validate name is a string and length is 2-16 characters
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Validate category is a string and length > 0
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_authors = set()
        for article in self.articles():
            unique_authors.add(article.author)
        return list(unique_authors)

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
        
        author_count = {}
        for article in articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        contributing = [author for author, count in author_count.items() if count > 2]
        if not contributing:
            return None
        return contributing

