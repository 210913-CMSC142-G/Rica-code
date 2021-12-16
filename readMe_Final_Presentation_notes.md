**NP-complete problem: Paint by Numbers (Nonogram) - readMe file**

Rica Bernadine M. Calbario
CMSC 142 G

**What is a nonogram?**

This puzzle has many names that you may be familiar with, such as: Hanjie, Paint by Numbers, Picross, Griddlers, and Pic-a-Pix. A **nonogram** is a Japanese logical puzzle where an encrypted image is revealed by coloring blocks of a grid based on the numbers hinted at the top and left sides. It can be a simple black and white image, or a fully colored image.

**This is how the puzzle works.**
- **Hint numbers** are given at the top and on the left sides of the grid, which are used as guides on how to color the puzzle. These numbers indicate **how many boxes are to be filled** in that specific row or column.
- The **order** of the numbers at the sides of the grid determines the **order of placement** for each set of blocks of color.
- For black and white puzzles, each set of blocks are separated by **AT LEAST one** empty space/cell, which is usually filled with an X (to mark the spaces that are not a part of the solution and to avoid confusion). 
- As for the colored puzzles, the same rule may also be applied, but there are also instances where adjoining blocks do not have any spaces in between. This happens when two neighboring blocks have different colors, thus, they can still be easily distinguished as compared to a standard B&W puzzle.

**Why is a nonogram an NP-complete problem?**
Remember that NP-complete problems are hard problems that can be reduced using an already solved problem. It makes use of verified guesses, which in our case is verified by the hint numbers.
Also note that each nonogram puzzle designed for humans displays a different encrypted image. Thus, this requires different approaches to solve each puzzle. Which means that there is no “good” or efficient solution to solve these nonograms. Again, we rely on the hints given at the sides of the grid to solve the puzzle. But then, there are also puzzles with multiple or no solutions at all. For example, the 2x2 puzzle presented in the slides. This is a pattern referred to as an elementary switching component.

**How do we solve a nonogram?**
*There are two possible solutions. Note that these are not necessarily the best and most effective solutions, but it gets the job done.*

The first possible solution is the depth-first search, exhaustive search, or backtracking algorithm. This is a slow execution process since the computer goes through every possible combination and placements of the colored blocks.
Here’s a link to a GIF that I found online (https://lihautan.com/solving-nonogram-with-code/7bfbcf67e3276087.gif) that visualizes how backtracking on a nonogram puzzle looks like once coded.

The second strategy is using an algorithm that implements a priority queue. Here, lines with hints of a longer set of colored blocks are prioritized first. Once the queue becomes empty, the computer then looks for a contradiction using the breadth-first search algorithm, which is faster than going through all of the cells repeatedly.
*GIF Visualization: https://www.alphabetagamer.com/pictopix-beta-demo/*

**Demo using Nonograms Pro (can be downloaded on Windows from the Microsoft Store)**
*Other free nonogram apps can be found online (here's one you can take a look at: https://www.nonograms.org) or through Google Playstore/Apple App Store*

**References:**
1. What is Nonogram? – nonogram. (n.d.). Retrieved from https://nonogram.easybrain.com/hc/en-us/articles/360025363971-What-is-Nonogram-. 
2. MilanB. (2021, December 3). Japanese crossword "Avokado". Colour Japanese crossword "Avokado". Retrieved from https://www.nonograms.org/nonograms2/i/50864. 
3. RaoraDJ. (2021, November 25). Japanese crossword "have a pear-fect day". Black and white Japanese crossword "Have a pear-fect day". Retrieved from https://www.nonograms.org/nonograms/i/50550.
4. Robertson, K. J. (2016, November 9). Pictopix – beta demo: Alpha beta gamer. Alpha Beta Gamer | Free Video Game Alpha &; Beta Tests. The Worlds Biggest Beta Testing Site. Retrieved from https://www.alphabetagamer.com/pictopix-beta-demo/. 
5. Benton, J., Snow, R., & Wallach, N. (2005, March 21). A combinatorial problem associated with nonograms . UCSD Mathematics. Retrieved from http://math.ucsd.edu/~nwallach/row-column-new.pdf. 
6. GeeksforGeeks. (2021, November 29). NP-completeness: Set 1 (introduction). Retrieved from https://www.geeksforgeeks.org/np-completeness-set-1/. 
7. Moss, A. (2020, April 30). Solving hard instances of Nonograms. Medium. Retrieved from https://medium.com/smith-hcv/solving-hard-instances-of-nonograms-35c68e4a26df. 
8. Yu, C.-H., Lee, H.-L., & Chen, L.-H. (2009, November 13). An efficient algorithm for solving nonograms - applied intelligence. SpringerLink. Retrieved from https://link.springer.com/article/10.1007/s10489-009-0200-0. 

