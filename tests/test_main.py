from lrclib_picard import get_client


def test_get():
    client = get_client()
    result = client.get(
        artist_name="Borislav Slavov",
        track_name="I Want to Live",
        album_name="Baldur's Gate 3 (Original Game Soundtrack)",
        duration=233,
    )

    assert result.id == 3396226
