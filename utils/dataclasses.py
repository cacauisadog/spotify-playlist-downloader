from dataclasses import dataclass


@dataclass
class Song:
    artist: str
    name: str

    def track(self):
        return f"{self.name} - {self.artist}"
