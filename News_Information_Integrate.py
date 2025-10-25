from dataclasses import dataclass, field
from typing import List, Literal, Optional

@dataclass
class NewsArticle:
    id: str
    title: str
    description: str
    content: str
    author: str
    source: str
    published_at: str
    image_url: str
    category: str
    url: str
    reading_time: int

@dataclass
class NewsCategory:
    id: str
    name: str
    slug: str
    color: str

@dataclass
class NewsFilters:
    category: str
    search: str
    sort_by: Literal['newest', 'oldest', 'popular'] = 'newest'

@dataclass
class NewsState:
    articles: List[NewsArticle] = field(default_factory=list)
    categories: List[NewsCategory] = field(default_factory=list)
    loading: bool = True
    error: Optional[str] = None
    filters: NewsFilters = field(default_factory=lambda: NewsFilters(category='all', search=''))
    bookmarks: List[str] = field(default_factory=list)
