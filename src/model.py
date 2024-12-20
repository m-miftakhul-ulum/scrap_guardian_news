from dataclasses import dataclass, asdict


@dataclass
class News:
    title: str
    url: str
    content: str