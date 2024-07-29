# Top 10 Movies Website

This is a Flask-based web application that allows users to manage their top 10 favorite movies. Users can add, edit, rate, and delete movies, with movie data fetched from The Movie Database (TMDb) API. The application uses SQLAlchemy for database management and Flask-WTF for form handling, with Bootstrap for styling.

## Features

- Add movies by searching from the TMDb API.
- Edit movie details such as rating and review.
- Delete movies from the list.
- Automatically update the ranking of movies based on their ratings.

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Migrate
- WTForms
- Bootstrap-Flask
- The Movie Database (TMDb) API

## Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- pip

## Installation

1. Clone the repository:

```sh
git clone https://github.com/Prathamesh326/Top-10-Movies-Website.git
cd Top-10-Movies-Website
```

2. Install the required packages:

```sh
pip install -r requirements.txt
```

3. Set up the database:

```sh
flask db upgrade
```

4. Run the application:

```sh
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## Configuration

Ensure you have a valid API key from [The Movie Database (TMDb)](https://www.themoviedb.org/) and set it in your `main.py` file:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

## Project Structure

```
Top-10-Movies-Website/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── select.html
│
├── static/
│   └── css/
│       └── styles.css
│
├── main.py
├── requirements.txt
└── README.md
```

## Usage

1. Navigate to the homepage to see the list of top 10 movies.
2. Click "Add Movie" to search and add a new movie to the list.
3. Click "Update" on a movie card to edit the movie's rating and review.
4. Click "Delete" on a movie card to remove the movie from the list.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please reach out to [Prathamesh326](https://github.com/Prathamesh326).
