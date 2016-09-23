--
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
-- Table contains registered players names
CREATE TABLE players ( id SERIAL PRIMARY KEY,
                    name TEXT );

-- Table contains winners and losers of every match
CREATE TABLE matches ( match_ids SERIAL PRIMARY KEY,
                        winner_ids INTEGER REFERENCES players(id),
                        loser_ids INTEGER REFERENCES players(id) );    
-- Table contains winning record of every player
CREATE VIEW winners_record as SELECT players.id as player ,count(matches.winner_ids) as wins 
                              FROM players LEFT JOIN matches
                              ON players.id = matches.winner_ids
                              GROUP BY players.id,matches.winner_ids ;   
-- Table contains record of players who lose the match(optional)                               
CREATE VIEW losers_record as SELECT players.id as player ,count(matches.loser_ids) as lose 
                              FROM players LEFT JOIN matches
                              ON players.id = matches.loser_ids
                              GROUP BY players.id,matches.loser_ids ;                                                             
-- Table contains how many matches played by each player
CREATE VIEW matches_played as SELECT players.id as player,count(matches.match_ids) as matches
                                FROM players LEFT JOIN matches
                                ON (players.id = matches.winner_ids) or (players.id = matches.loser_ids)
                                GROUP BY players.id
                                ORDER BY players.id ASC;