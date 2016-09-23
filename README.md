## This project contains 3 files.
>> tournament.sql
>> tournament.py
>> tournament_test.py

## Tournament DATABASE Tables
>> players : Contains the registered names
>> matches : Contains the each match winners and losers
>> winners_record(VIEW) : Contains the winning record of each Players
>> losers_record(VIEW) : Contains the record of matches lost by each person
>> matches_played(VIEW) : contains the matches played by each person
     
# To initiate the Tournament Database 
# Run the following commands
>> psql
>> \i tournament.sql
>> \q 

## To run the project 
>> python tournament_test.py
