from flask import Flask, render_template, request
import requests

# Initialize Flask application
app = Flask(__name__)

# GIPHY API key
API_KEY = "P8p9BnUx95Q8nySurPYrp7wWtVS1noQ2"

# Home route: handles GET and POST
@app.route("/", methods=["GET", "POST"])
def index():
    gif_urls = []

    if request.method == "POST":
        # Capture search term from form
        search_term = request.form.get("search")

        # Build GIPHY API request URL
        api_url = (
            f"https://api.giphy.com/v1/gifs/search"
            f"?api_key={API_KEY}&q={search_term}&limit=10"
        )

        # Send request to GIPHY
        response = requests.get(api_url)

        # If successful, extract GIF URLs
        if response.status_code == 200:
            data = response.json()
            gif_urls = [item["images"]["original"]["url"] for item in data["data"]]

    # Render HTML template with GIFs
    return render_template("index.html", gifs=gif_urls)

# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def index():
    gif_urls = []
    error_message = None

    if request.method == "POST":
        search_term = request.form.get("search")

        if not search_term:
            error_message = "Please enter a search term."
        else:
            api_url = (
                f"https://api.giphy.com/v1/gifs/search"
                f"?api_key={API_KEY}&q={search_term}&limit=10"
            )
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                if data["data"]:
                    gif_urls = [item["images"]["original"]["url"] for item in data["data"]]
                else:
                    error_message = f"No GIFs found for '{search_term}'."
            else:
                error_message = "Failed to fetch GIFs. Please try again later."

    return render_template("index.html", gifs=gif_urls, error=error_message)
