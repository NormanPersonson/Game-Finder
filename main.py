from drafter import *
from dataclasses import dataclass
from games_library import Game, INITIAL_GAMES
import random
@dataclass 
class State:
    all_games:list[Game]
    user_genre:str=""
    backup_genre:str=""
    max_price:str=""
    min_rating:str=""
    selected_platform:str=""

@route("/")
def index(state:State)-> Page:
    return Page(
        state,
        Div(
            Header("Game Finder"),
            Paragraph("Find games that fit your special preferences"),
            Button("Start Finding Games", "preferences"),
            Button("About This App", "about")
        )
    )
@route("/preferences")
def preferences_page(state:State)->Page:
    genres=["Action", "RPG", "Simulation", "Strategy", "Platformer", "Adventure", "Puzzle"]
    platforms=["PC", "PlayStation", "Xbox", "Switch"]
    return Page(
        state,
        Div(
            Header("Enter Preferences"),
            
            "Primary Genre:",
            SelectBox("user_genre",genres),
            "Backup Genre (if primary has no matches):",
            SelectBox("backup_genre", genres),
            "Platform:",
            SelectBox("selected_platform", platforms),
            "Maximum Price ($):",
            TextBox("max_price"),
            "Minimum Rating (0 to 5):",
            TextBox("min_rating"),

            Button("Review & Confirm", "confirmation"),
            Button("Back to Home", "index")
        )
    )
@route("/confirmation")
def confirmation_page(state: State, user_genre: str, backup_genre: str, selected_platform: str, max_price: str, min_rating: str) -> Page:
    # Save everything to state so the results page can use it
    state.user_genre = user_genre
    state.backup_genre = backup_genre
    state.selected_platform = selected_platform
    state.max_price = max_price
    state.min_rating = min_rating
    chosen_word=random.choice(["Awesome", "Brilliant", "Fantastic", "Wonderful", "Superb", "Excellent", "Amazing", "Inconceivable", "Fabulous", "Fantabulous", "Killer", "Dude... That right there was an abolutely unexpected but awesome", "That was such AWESOMNENERNFWKRNEKNRKJNV"])
    
    return Page(
        state,
        Div(
            Header(f"{chosen_word} Choice!"),
            Paragraph(f"{chosen_word}! Your selection has been successfully saved."),
            Paragraph("Please review your preferences below:"),
            Paragraph(f"Current Platform Filter: <strong>{state.selected_platform or 'None'}</strong>"),
            Paragraph(f"Primary Genre: <strong>{state.user_genre or 'None'}</strong>"),
            Paragraph(f"Backup Genre: <strong>{state.backup_genre or 'None'}</strong>"),
            Paragraph(f"Max Price: <strong>${state.max_price if state.max_price.strip() else 'No limit'}</strong>"),
            Paragraph(f"Min Rating: <strong>{state.min_rating if state.min_rating.strip() else 'None'} / 5.0</strong>"),
            
            Button("Find My Matching Game", "results"),
            Button("Change Preferences", "preferences"),
            Button("Back to Home", "index")      
        )
    )
@route("/results")
def results_page(state: State) -> Page:
    # Convert strings to floats here for filtering (with default fallbacks if empty)
    price_limit = float(state.max_price) if state.max_price.strip() else 999.99
    rating_limit = float(state.min_rating) if state.min_rating.strip() else 0.0

    matching_games = []
    for game in state.all_games:
        if (state.selected_platform in game.platform and
            game.genre == state.user_genre and
            game.price <= price_limit and
            game.rating >= rating_limit):
            matching_games.append(game)

    used_genre = state.user_genre

    if len(matching_games) == 0:
        for game in state.all_games:
            if (state.selected_platform in game.platform and
                game.genre == state.backup_genre and
                game.price <= price_limit and
                game.rating >= rating_limit):
                matching_games.append(game)
        used_genre = state.backup_genre

    best_game = None
    if len(matching_games) > 0:
        best_game = matching_games[0]
        for g in matching_games:
            if g.rating >= best_game.rating:
                best_game = g

    if best_game is not None:
        return Page(
            state,
            Div(
                Header("Your Recommended Game!"),
                Paragraph(f"We found a great match using your genre choice: <strong>{used_genre}</strong>"),
                Div(
                    Header(best_game.title),
                    Paragraph(f"Platform(s): {', '.join(best_game.platform)}"),
                    Paragraph(f"Genre: {best_game.genre}"),
                    Paragraph(f"Price: ${best_game.price:.2f}"),
                    Paragraph(f"Rating: {best_game.rating} / 5.0")
                ),
                Button("Search Again", "preferences"),
                Button("View Full Catalog", "catalog"),
                Button("Home", "index")
            )
        )
    else:
        return Page(
            state,
            Div(
                Header("No Matches Found"),
                Paragraph("We couldn't find anything matching your filters."),
                Button("Go to Fallback Options", "fallback"),
                Button("Try Again", "preferences")
            )
        )

@route("/fallback")
def fallback_page(state: State) -> Page:
    return Page(
        state,
        Div(
            Header("No Exact Matches Found"),
            Paragraph(f"We couldn't find any games matching your exact primary genre and budget."),
            Paragraph("Here are all our available games, or you can try adjusting your preferences:"),
            Button("Change Preferences", "preferences"),
            Button("Browse Full Catalog", "catalog"),
            Button("Back to Home", "index")
        )
    )

@route("/catalog")
def catalog_page(state:State)->Page:
    game_cards=[]
    for game in state.all_games:
        game_cards.append(
            Div(
                Header(game.title),
                Paragraph(f"Platform: {', '.join(game.platform)} | Genre: {game.genre}"),
                Paragraph(f"Price: ${game.price:.2f} | Rating: {game.rating}/5.0")
            )
        )
        
    return Page(
        state,
        Div(
            Header("Complete Game Catalog"),
            Paragraph("Here are all the games available in our dataset:"),
            game_cards,
            Button("Back to Home", "index")
        )
    )

@route("/about")
def about_page(state:State)-> Page:
    return Page(
        state,
        Div(
            Header("About this application"),
            Paragraph("This video game recommendation tool helps players find games that match their exact platform, budget, andgenre preferences without getting overwelmed by choices."),
            Button("Back to Home", "index")
        )
    )
if __name__ == "__main__":
    start_server(State(all_games=INITIAL_GAMES))
