#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import itertools
from contextlib import contextmanager

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection failed")

@contextmanager 
def get_cursor():
    """
    Query helper function using context lib. Creates a cursor from a database
    connection object, and performs queries using that cursor.
    """
    DB = connect()
    cursor = DB.cursor()
    try:
        yield cursor
    except:
        raise
    else:
        DB.commit()
    finally:
        cursor.close()
        DB.close()        

def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute("TRUNCATE matches;")

def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM players;")
def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM players;")
        total = cursor.fetchall()
        for row in total:
            return row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO players (name) VALUES (%s);",(name,))

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as cursor:
        query = """SELECT players.id,players.name,winners_record.wins,matches_played.matches FROM players
                            LEFT JOIN winners_record ON players.id = winners_record.player
                            LEFT JOIN matches_played ON players.id = matches_played.player
                            GROUP BY players.id,players.name,winners_record.wins,matches_played.matches
                            ORDER BY winners_record.wins DESC;
                """
        cursor.execute(query)
        standings = cursor.fetchall()
        return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as cursor:
        query = "INSERT INTO matches (winner_ids,loser_ids) VALUES (%s,%s);"
        params = (winner,loser)
        cursor.execute(query,params)
        
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    iter_pair = itertools.izip(*[iter(standings)]*2) # iterates every 2 values from standings
    next_pairs = []  # list that contains pairs of next round
    pairings = list(iter_pair)
    for pair in pairings:
        id1 = pair[0][0]
        name1 = pair[0][1]
        id2 = pair[1][0]
        name2 = pair[1][1]
        matchup = (id1, name1, id2, name2)
        next_pairs.append(matchup)
    return next_pairs
