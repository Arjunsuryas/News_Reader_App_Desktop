from datetime import datetime
from typing import List

# Assuming NewsArticle is already imported from previous dataclass definition

mock_articles: List[NewsArticle] = [
    NewsArticle(
        id="7",
        title="Major Tech Companies Announce Collaboration on Quantum Computing",
        description="Leading technology firms join forces to accelerate quantum computing research and development for commercial applications.",
        content="In an unprecedented move, major tech companies have announced a collaborative effort to advance quantum computing technology, potentially revolutionizing computing power and capabilities.",
        author="Lisa Wang",
        source="Tech Innovation News",
        published_at="2024-01-15T02:15:00Z",
        image_url="https://images.pexels.com/photos/8566526/pexels-photo-8566526.jpeg?auto=compress&cs=tinysrgb&w=800",
        category="technology",
        url="https://example.com/quantum-computing",
        reading_time=4
    ),
    NewsArticle(
        id="8",
        title="Economic Growth Projections Exceed Expectations for 2024",
        description="Financial analysts revise growth forecasts upward as key economic indicators show stronger than expected performance.",
        content="Economic experts are optimistic about the year ahead as multiple indicators point to sustained growth and improved market conditions across various sectors.",
        author="David Park",
        source="Economic Review",
        published_at="2024-01-15T01:45:00Z",
        image_url="https://images.pexels.com/photos/7681091/pexels-photo-7681091.jpeg?auto=compress&cs=tinysrgb&w=800",
        category="business",
        url="https://example.com/economic-growth",
        reading_time=3
    )
]
