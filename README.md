
How to Run the Project
----------------------

The main library this project uses is wikipedia. The source code for this is included in the repository because we actually modified some of the source code to suppress warning in our program. In case other libraries are needed, type 'pip install --user -r requirements.txt'. To run the program, simply type 'python wikipedia-bot.py "SOURCEPAGE" "DESTPAGE"'. The program will output a path between the two articles in text form.


External Sources Used
----------------------

http://stackoverflow.com/questions/24413563/how-do-i-know-if-a-process-has-timedout-in-bash
http://stackoverflow.com/questions/687948/timeout-a-command-in-bash-without-unnecessary-delay

Benchmarking Results
--------------------



| Source                         | Destination                    | #Links, Time(1) | #Links, Time(2) | #Links, Time(3) | Average    |
|--------------------------------|--------------------------------|-----------------|-----------------|-----------------|------------|
| Chicago Cubs                   | Wrigley Field                  | 1, 4.01533      | 1, 3.82206      | 1, 3.70731      | 1, 3.84823 |
| University of Notre Dame       | Knute Rockne                   | 1, 3.06576      | 1, 3.00064      | 1, 3.22876      | 1, 3.09839 |
| Chocolate                      | Brain                          | 2, 7.56347      | 2, 3.47812      | 2, 6.51746      | 2, 5.85302 |
| Orange (fruit)                 | Purple                         | 2, 8.22610      | 2, 10.3709      | 2, 8.17634      | 2, 8.92445 |
| Telephone                      | Whistle                        | 2, 3.51836      | 2, 3.45852      | 2, 3.56073      | 2, 3.51254 |
| Peanuts                        | George H W Bush                | 3, 16.3124      | 3, 23.4242      | 3, 19.7249      | 3, 19.8205 |
| Peanut                         | Cupcake                        | 4, 15.0667      | 4, 16.7509      | 4, 15.5669      | 4, 15.7948 |
| Adele                          | Malik Zaire                    | 4, 9.30975      | 4, 15.4758      | 4, 10.7803      | 4, 11.8553 |
| Somali lark                    | Battle of Great Bridge         | 4, 17.8890      | 4, 22.3818      | 8, 48.0684      | 5, 29.4464 |
| Socks                          | Wierd Al                       | 6, 31.7290      | 5, 18.4056      | 7, 50.9891      | 6, 33.7079 |
| Mirror Image                   | Dell                           | 4, 12.8211      | 3, 14.3931      | 4, 15.9633      | 3, 14.3925 |
| Telephone                      | Grasshopper                    | 9, 67.1147      | 8, 50.4769      | 8, 51.1647      | 8, 56.2521 |
| Jesus                          | Johnnie Cochran                | 6, 34.2885      | 21, 124.447      | 33, 190.617      | 20, 116.451 |

