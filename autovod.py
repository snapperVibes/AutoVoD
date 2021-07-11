from dataclasses import dataclass
import click
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from openpyxl import load_workbook


@dataclass
class Match:
    p1: str
    p2: str
    _start: str
    _end: str

    def _to_time(self, time):
        h, m, s = time.split(":")
        return (h * 3600) + (m * 60) + s

    @property
    def start_time(self) -> int:
        return self._to_time(self._start)

    @property
    def end_time(self) -> int:
        return self._to_time(self._end)

    @property
    def title(self) -> str:
        return f"{self.p1} vs {self.p2}"


@click.command("autovod")
@click.option("--data")
@click.option("--vod")
def cli(data, vod):
    # Load data
    wb = load_workbook(data)
    sheet = wb.active
    matches = []
    for row in sheet.iter_rows():
        matches.append(Match(*[data.value for data in row]))

    # Split the videos
    for match in matches:
        ffmpeg_extract_subclip(
            vod, match.start_time, match.end_time, targetname=f"{match.title}.mp4"
        )


if __name__ == "__main__":
    cli()
