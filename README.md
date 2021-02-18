# TradeRepublic-Overview

![Python application](https://github.com/Giebisch/TradeRepublic-Overview/workflows/Python%20application/badge.svg)

## Why was this made ?

Currently there is no web/desktop app for Trade Republic, meaning it's pretty hard to follow your depot without your phone. With this application
it's really convenient to watch your depot grow while working on your computer.

## What does it do ?

There are two options to read in your depot, one is to specify a folder with all your pdf you exported out of Trade Republic. It then automatically
parses them for their ISINs and quantity. Other option is to specify a .csv file where you can explicitly state your positions. After the positions are read
it periodically displays your positions with their current price and total worth.

## How do I use it ?

Run the script with `-h` or `--help` to get following message:

    usage: traderep [-h] [--parse PARSE] [--value VALUE]

    optional arguments:
    -h, --help     show this help message and exit
    --parse PARSE  Specify folder you want to parse the pdfs in
    --value VALUE  Specify the folder you previously parsed

## What format does the .csv file have to have ?

    ISIN;QUANTITY;PRICE;
    IE00B4L5Y983;50.0;62.28
    ...