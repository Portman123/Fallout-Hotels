# Fallout Hotels
An interactive map of hotel locations and nuclear powerplant locations + explosion radii. This can be used to recommend the most vulnerable and dangerous hotels, helping customers to expose themselves to more nuclear radiation in the hopes of gaining cool superpowers.

Made for nuclear fallout themed GreatUniHack 2021.

## Inspiration
The nuclear fallout theme of the hackathon & Peak.ai challenge asking us to build something that helps people make bad decisions.

## What it does
We assumed a post-apocalyptic world in which radiation is rife - all nuclear power plants have exploded and all major cities have been bombed. This web app displays a map with the radiation sources and the extent of their blast/fallout. However, not all good things in life are gone, and for those citizens wishing to choose their post-apocalyptic holiday destination, we have displayed a selection of hotels together with their danger rating. High danger ratings mean increased exposure to radiation, offering the unquestionable benefit of obtaining an interesting superpower (subject to purchasing our 1 or 2 week Atomic Package Deal for as little as 1499.99, T&Cs apply). Please browse freely.

In addition to the above, we added the option to adjust certain settings to view the world in alternative danger scenarios.

## How we built it
We used datasets found on Kaggle for the nuclear power plant and cities data, Google API for hotel locations and Reddit API for our bad super powers list. All the back end work was done in Python via Google Colab, using pandas for data manipulation and folium to build the map. We used Flask to set up the web app, with HTML and CSS on the front end. 

## Challenges we ran into
The first hotel dataset we tried contained 3000 hotels, all exclusively in India. We also tried to use a machine learning model to predict fallout areas, but lacked suitable information or datasets (nuclear power plant disasters are exceedingly rare). 

## Accomplishments that we're proud of
Successfuly building the function that calculated the number of danger zones based on location.

## What's next
Adding more interactive features, including a field to input chosen holiday destination (e.g. city, country) which would re-focus the map and display highest-danger locations.

## Credits
* Radioactive icon made by [WesleyV](https://www.flaticon.com/authors/wesleyv) from [Flaticon](https://www.flaticon.com/).
* Skull icon [source](https://en.m.wikipedia.org/wiki/File:Skull-Icon.svg)
* [r/shittypowers](https://www.reddit.com/r/shittysuperpowers/) for crowd-sourced bad super powers. 
