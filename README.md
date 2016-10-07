# Tournament results project for Udacity Nanodegree Program

## This project contains 3 files.
- tournament.sql
- tournament.py
- tournament_test.py

## Tournament DATABASE Tables
- players : Contains the registered names
- matches : Contains the each match winners and losers
- winners_record(VIEW) : Contains the winning record of each Players
- losers_record(VIEW) : Contains the record of matches lost by each person
- matches_played(VIEW) : contains the matches played by each person

## To run locally(make sure you expert of theese)
- You need to run this application in virtual machine.
- Download and install Vagrant application [here](https://www.vagrantup.com/).
- You also need [Virtual Box](https://www.virtualbox.org/).
- Clone this repository using git shell.
- Change your directory to cloned repository.
- Now type below commands in your shell.
```bash
$vagrant up
```
```bash
$vagrant ssh
```
 
## To initiate the Tournament Database 
### Run the following commands
```bash
$ psql 
```
```bash
> \i tournament.sql
```
```bash
> \q
```
### To run the project 
```bash
$ python tournament_test.py
```
