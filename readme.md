# Analyzing Historical MLB Trends

1. When I first downloaded Sean Lahman's historical baseball data I wasn't exactly sure what was looking for. So I created a way to search the data for interesting statistics. I printed out some lists and found that most of the records I searched either occurred before 1900, or in recent history. This led me toward analying how the game has changed since the 1800s and what that means for todays' game. 
 1. ![Search](Images/search.png)
2. I decided that the easiest way to move forward with my analyzation was to import pandas to work with the data. This was a unique challenge because I had never used Pandas before. I also imported matplotlib in order to make some plot later on which is something I wasnted to learn how to do.  
3. After playing with data.head() for a while to get familiar with indexing in pandas, I chose three statistics associated with hitting, and three with pitching, and used yearID as the common column. 
 3a. ![New Chart](Images/sub_heads.png)
4. I wrote each of these shrunken versions of the original csv files into new csv's call hit_sub and pitch_sub in order to start plotting. 
5. After failing to create a histogram, I realized that I could make subplots that ould serve perfectly for presenting the time data for both pitching and hitting. 
6. Below are my subplots to display the change in hitting and pitching statistics. The order of these stats are correct in the title of each graph.
## Hitting
![Hitting](Images/hitting.png)
## Pitching
![Pitching](Images/pitching.png)
### Analysis of Subplot Data
- Looking at these figures, we can see that home runs and strikeouts went up for hitters while innings pitched, complete games, and shutouts went down for pitchers. 
- These are interesting stats because we can also see that runs scored did not change by much. 
- This means that the game is changing in terms of the product we see on the field. Less balls are being put in play which leads to less defensive plays being made. This has been one of the main compaints made by baseball purists. They argue that the game is worse because of the increase in strikeouts. Analytics people will be quick to point out that runs have been constant and home runs increasing makes the game more exciting, therefore; the game hasn't been made worse. I can see it from both sides. Pitchers and hitters have been in a battle for over 140 years, but they have always found a way to respond to the adjustments the other side is making. This is how runs have remained relatively contstant. I would tend to agree with the purists that the game is less visually appealing because less balls are being put in play.   
### Tableau Visualization
I used Tableau to create this graph that combines the previous subplots.
![New Chart](Images/tbl.png)