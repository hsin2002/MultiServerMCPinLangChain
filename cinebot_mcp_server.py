from fastmcp import FastMCP

mcp = FastMCP("CineBot")

@mcp.tool()
def check_showtimes(movie_title: str) -> str:
    """
    Check showtimes for a given movie title.
    """
    fake_showtimes = {
        "Inception": "10:00 AM, 1:00 PM, 4:00 PM, 7:00 PM",
        "The Matrix": "11:00 AM, 2:00 PM, 5:00 PM, 8:00 PM",
        "Interstellar": "12:00 PM, 3:00 PM, 6:00 PM, 9:00 PM",
    }
    return fake_showtimes.get(movie_title.lower(), "No showtimes available for this movie.")


if __name__ == "__main__":
    mcp.run()
