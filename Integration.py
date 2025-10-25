[tool.poetry]
name = "news_reader_app"
version = "0.0.0"
description = "Python equivalent of a news reader app"
authors = ["Your Name <you@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.11"
streamlit = "^1.29.0"  # For UI similar to React
requests = "^2.31.0"   # Fetch news from APIs
pydantic = "^2.3.1"     # For typed data models

[tool.poetry.dev-dependencies]
black = "^23.12.0"         # Code formatter (like Prettier)
flake8 = "^6.1.0"          # Linting (like ESLint)
isort = "^6.4.0"            # Import sorting
mypy = "^1.5.1"             # Static type checking (like TypeScript)
pytest = "^7.4.3"           # Testing

[build-system]
requires = ["poetry-core>=1.6.0"]
build-backend = "poetry.core.masonry.api"
