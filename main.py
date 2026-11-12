from drafter import *
from dataclasses import dataclass
import random
@dataclass
class Game:
    title:str
    platform:list[str]
    genre:str
    price:float
    rating:float

INITIAL_GAMES = [
    # Action & Adventure
    Game("Hades", ["PC", "Switch", "PlayStation", "Xbox"], "Action", 24.99, 4.9),
    Game("Hades II", ["PC"], "Action", 29.99, 4.8),
    Game("God of War Ragnarok", ["PlayStation", "PC"], "Action", 69.99, 4.9),
    Game("Marvel's Spider-Man 2", ["PlayStation"], "Action", 69.99, 4.8),
    Game("Elden Ring", ["PC", "PlayStation", "Xbox"], "RPG", 59.99, 4.9),
    Game("Bloodborne", ["PlayStation"], "Action", 19.99, 4.7),
    Game("Monster Hunter World", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.6),
    Game("Devil May Cry 5", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.7),
    Game("Sekiro: Shadows Die Twice", ["PC", "PlayStation", "Xbox"], "Action", 59.99, 4.8),
    Game("Ghost of Tsushima", ["PlayStation", "PC"], "Action", 49.99, 4.8),
    Game("Horizon Zero Dawn", ["PC", "PlayStation"], "Action", 19.99, 4.5),
    Game("Horizon Forbidden West", ["PC", "PlayStation"], "Action", 49.99, 4.7),
    Game("Batman: Arkham City", ["PC", "PlayStation", "Xbox"], "Action", 19.99, 4.6),
    Game("Control", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.4),
    Game("Bayonetta 3", ["Switch"], "Action", 59.99, 4.5),
    Game("Metal Gear Rising: Revengeance", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.6),
    Game("Grand Theft Auto V", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.3),
    Game("Red Dead Redemption 2", ["PC", "PlayStation", "Xbox"], "Action", 59.99, 4.9),
    Game("Sleeping Dogs", ["PC", "PlayStation", "Xbox"], "Action", 19.99, 4.5),
    Game("Cyberpunk 2077", ["PC", "PlayStation", "Xbox"], "RPG", 49.99, 4.1),

    # RPGs
    Game("The Witcher 3", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 39.99, 4.7),
    Game("Baldur's Gate 3", ["PC", "PlayStation", "Xbox"], "RPG", 59.99, 5.0),
    Game("Persona 5 Royal", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 59.99, 4.9),
    Game("Final Fantasy VII Remake", ["PlayStation", "PC"], "RPG", 39.99, 4.6),
    Game("Final Fantasy XVI", ["PlayStation", "PC"], "RPG", 69.99, 4.5),
    Game("Disco Elysium", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 39.99, 4.7),
    Game("Divinity: Original Sin 2", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 44.99, 4.8),
    Game("Chrono Trigger", ["PC", "Switch"], "RPG", 14.99, 4.9),
    Game("Skyrim", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 39.99, 4.5),
    Game("Fallout: New Vegas", ["PC", "PlayStation", "Xbox"], "RPG", 9.99, 4.8),
    Game("Dark Souls III", ["PC", "PlayStation", "Xbox"], "RPG", 39.99, 4.7),
    Game("Dragon Age: Inquisition", ["PC", "PlayStation", "Xbox"], "RPG", 19.99, 4.2),
    Game("Octopath Traveler II", ["PC", "PlayStation", "Switch"], "RPG", 59.99, 4.6),
    Game("Xenoblade Chronicles 3", ["Switch"], "RPG", 59.99, 4.7),
    Game("Yakuza: Like a Dragon", ["PC", "PlayStation", "Xbox"], "RPG", 59.99, 4.6),
    Game("Star Wars Jedi: Survivor", ["PC", "PlayStation", "Xbox"], "Action", 69.99, 4.2),
    Game("NieR: Automata", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 39.99, 4.8),
    Game("Paper Mario: The Thousand-Year Door", ["Switch"], "RPG", 59.99, 4.7),
    Game("Sea of Stars", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 34.99, 4.4),
    Game("The Outer Worlds", ["PC", "PlayStation", "Xbox", "Switch"], "RPG", 29.99, 4.0),

    # Simulation & Strategy
    Game("Stardew Valley", ["PC", "PlayStation", "Xbox", "Switch"], "Simulation", 14.99, 4.8),
    Game("Minecraft", ["PC", "PlayStation", "Xbox", "Switch"], "Simulation", 29.99, 4.6),
    Game("Animal Crossing: New Horizons", ["Switch"], "Simulation", 59.99, 4.5),
    Game("Cities: Skylines", ["PC", "PlayStation", "Xbox", "Switch"], "Simulation", 29.99, 4.2),
    Game("Planet Zoo", ["PC"], "Simulation", 44.99, 4.4),
    Game("Sims 4", ["PC", "PlayStation", "Xbox"], "Simulation", 0.00, 3.8),
    Game("RimWorld", ["PC"], "Simulation", 34.99, 4.9),
    Game("Factorio", ["PC", "Switch"], "Simulation", 35.00, 4.9),
    Game("Oxygen Not Included", ["PC"], "Simulation", 24.99, 4.6),
    Game("PowerWash Simulator", ["PC", "PlayStation", "Xbox", "Switch"], "Simulation", 24.99, 4.5),
    Game("Civilization VI", ["PC", "PlayStation", "Xbox", "Switch"], "Strategy", 29.99, 4.3),
    Game("Age of Empires II: Definitive Edition", ["PC", "Xbox"], "Strategy", 19.99, 4.7),
    Game("XCOM 2", ["PC", "PlayStation", "Xbox", "Switch"], "Strategy", 39.99, 4.5),
    Game("Total War: Warhammer III", ["PC"], "Strategy", 59.99, 4.1),
    Game("Stellaris", ["PC", "PlayStation", "Xbox"], "Strategy", 39.99, 4.3),
    Game("Into the Breach", ["PC", "Switch"], "Strategy", 14.99, 4.7),
    Game("Frostpunk", ["PC", "PlayStation", "Xbox"], "Strategy", 29.99, 4.5),
    Game("Slay the Spire", ["PC", "PlayStation", "Xbox", "Switch"], "Strategy", 24.99, 4.9),
    Game("Balatro", ["PC", "PlayStation", "Xbox", "Switch"], "Strategy", 14.99, 4.9),
    Game("Northgard", ["PC", "PlayStation", "Xbox", "Switch"], "Strategy", 29.99, 4.2),

    # Platformers & Indie
    Game("Celeste", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 19.99, 4.8),
    Game("Super Mario Odyssey", ["Switch"], "Platformer", 59.99, 4.9),
    Game("Super Mario Bros. Wonder", ["Switch"], "Platformer", 59.99, 4.8),
    Game("Hollow Knight", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 14.99, 4.9),
    Game("Ori and the Will of the Wisps", ["PC", "Xbox", "Switch"], "Platformer", 29.99, 4.8),
    Game("Dead Cells", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 24.99, 4.7),
    Game("Cuphead", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 19.99, 4.7),
    Game("Crash Bandicoot 4", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 39.99, 4.3),
    Game("Sonic Mania", ["PC", "PlayStation", "Xbox", "Switch"], "Platformer", 19.99, 4.5),
    Game("Pizza Tower", ["PC"], "Platformer", 19.99, 4.8),
    Game("Outer Wilds", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 24.99, 4.9),
    Game("Subnautica", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 29.99, 4.7),
    Game("Tunic", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 29.99, 4.5),
    Game("Journey", ["PC", "PlayStation", "Switch"], "Adventure", 14.99, 4.6),
    Game("Inside", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 19.99, 4.8),
    Game("A Short Hike", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 7.99, 4.7),
    Game("Return of the Obra Dinn", ["PC", "PlayStation", "Xbox", "Switch"], "Puzzle", 19.99, 4.8),
    Game("Portal 2", ["PC"], "Puzzle", 9.99, 5.0),
    Game("Tetris Effect: Connected", ["PC", "PlayStation", "Xbox", "Switch"], "Puzzle", 39.99, 4.7),
    Game("The Witness", ["PC", "PlayStation", "Xbox"], "Puzzle", 39.99, 4.2),

    # Shooters & Multiplayer
    Game("Counter-Strike 2", ["PC"], "Action", 0.00, 3.9),
    Game("Apex Legends", ["PC", "PlayStation", "Xbox", "Switch"], "Action", 0.00, 4.0),
    Game("Overwatch 2", ["PC", "PlayStation", "Xbox", "Switch"], "Action", 0.00, 3.5),
    Game("Valorant", ["PC"], "Action", 0.00, 4.1),
    Game("Halo: The Master Chief Collection", ["PC", "Xbox"], "Action", 39.99, 4.6),
    Game("Doom Eternal", ["PC", "PlayStation", "Xbox", "Switch"], "Action", 39.99, 4.7),
    Game("Titanfall 2", ["PC", "PlayStation", "Xbox"], "Action", 19.99, 4.9),
    Game("Helldivers 2", ["PC", "PlayStation"], "Action", 39.99, 4.5),
    Game("Left 4 Dead 2", ["PC"], "Action", 9.99, 4.9),
    Game("Deep Rock Galactic", ["PC", "PlayStation", "Xbox"], "Action", 29.99, 4.8),
    Game("It Takes Two", ["PC", "PlayStation", "Xbox", "Switch"], "Adventure", 39.99, 4.8),
    Game("Portal", ["PC"], "Puzzle", 9.99, 4.8),
    Game("Terraria", ["PC", "PlayStation", "Xbox", "Switch"], "Simulation", 9.99, 4.9),
    Game("Valheim", ["PC", "Xbox"], "Simulation", 19.99, 4.6),
    Game("Palworld", ["PC", "Xbox"], "Simulation", 29.99, 4.2),
    Game("Phasmophobia", ["PC"], "Simulation", 13.99, 4.5),
    Game("Vampire Survivors", ["PC", "PlayStation", "Xbox", "Switch"], "Action", 4.99, 4.9),
    Game("Dave the Diver", ["PC", "PlayStation", "Switch"], "Adventure", 19.99, 4.7),
    Game("Sniper Elite 5", ["PC", "PlayStation", "Xbox"], "Action", 49.99, 4.1)
]
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
