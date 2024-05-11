#TODO: C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”
#1.  Create an identifying comment within the first line of a file named “main.py” that includes your student ID.
#2.  Include comments in your code to explain both the process and the flow of the program.

#DijkstraShortestPath(startV) {
#   for each vertex currentV in graph {
#      currentV⇢distance = Infinity
#      currentV⇢predV = 0
#      Enqueue currentV in unvisitedQueue
#   }
#
#   // startV has a distance of 0 from itself
#   startV⇢distance = 0
#
#   while (unvisitedQueue is not empty) {
#      // Visit vertex with minimum distance from startV
#      currentV = DequeueMin unvisitedQueue
#
#      for each vertex adjV adjacent to currentV {
#         edgeWeight = weight of edge from currentV to adjV
#         alternativePathDistance = currentV⇢distance + edgeWeight
#            
#         // If shorter path from startV to adjV is found,
#         // update adjV's distance and predecessor
#         if (alternativePathDistance < adjV⇢distance) {
#            adjV⇢distance = alternativePathDistance
#            adjV⇢predV = currentV
#         }
#      }
#   }
#}