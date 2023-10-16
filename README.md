# Chess PGN Recorder

## Overview
The Chess PGN Recorder is a Python-based program designed to assist chess players and enthusiasts in recording, documenting, and saving their games in the Portable Game Notation (PGN) format. With a user-friendly command-line interface, this program not only captures individual moves, but also allows users to document meta information about the game, such as event, date, players, and more.

## Features

1. **Record Game Moves**:
    - Record individual moves for both White and Black.
    - The move recording format supports standard chess notations.
    - Special move notations (e.g., checks, castling, en passant) are recognized and can be included in the statistics.
    - Users can add comments to specific moves.

2. **Add Game Information**:
    - Store meta information of the chess game including: 
        - Event
        - Site
        - Date
        - Round
        - White player's name
        - Black player's name
        - Result (e.g., 1-0, 0-1, 1/2-1/2)

3. **Statistics**:
    - Generate statistics based on the recorded moves. For instance, it can count the number of checks, castling moves, good/bad move annotations, and more for each player.
    
4. **Export to PGN File**:
    - Once a game has been fully recorded, users have the option to export and save the game in the standard PGN file format. This PGN file can be opened with most chess software for analysis or replay.

5. **Helpful Menus**:
    - The program provides clear and straightforward menus to guide users through the process, making it easy for users to navigate and use the software effectively.

## How to Use

1. **Main Menu**:
    - **Create game**: Begin the process of recording a new game.
    - **Information**: Provides an overview of the program and its functionalities.
    - **Exit program**: Safely close the program.

2. **Game Menu**:
    - **Record game moves**: Enter moves for both White and Black in standard chess notation.
    - **Add game information**: Document the meta information of the game.
    - **Statistics**: View statistics based on the recorded moves.
    - **Create .pgn file**: Export the recorded game and its information to a PGN file.
    - **Return to main menu**: Go back to the main menu.

3. **Input Notations**:
    When recording moves, standard chess notations are accepted. Some special notations include:
    - `+` for Check
    - `#` for Checkmate
    - `!` for Good move
    - `!!` for Excellent move
    - `?` for Bad move
    - `??` for Very bad move
    - `0-0` for Short castling (Kingside castling)
    - `0-0-0` for Long castling (Queenside castling)
    - `a.p` for En passant capture
