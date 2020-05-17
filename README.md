# Heuristic Global Optimization
Global optimization attempts to find the global minima / maxima of a function or set of functions. The functions may have more than one local minima and hence global optimization differs from local optimization in that it cannot be easily solved by using something like gradient descent. Moreover, in a lot of cases explicitly calculating the derivatives of the functions may be intractable.

**Heuristic** Global Optimization aims to solve the global optimization problem using heuristics to find an approximate solution, unlike classical algorithms which aim to find exact solutions. This repository aims to be a collection of such algorithms, providing both the theory behind the algorithms as well as Python implementations.

## Currently Implemented Algorithms:
* Greedy Search / Random Search / Random Walk
* Simulated Annealing (with and without automatic parameter selection)
* Genetic Algorithms for Path Finding and Travelling Salesman Problem
* Multi Objective Optimization using Elitist Non-Dominated Sorting Genetic Algorithm (NSGA-II)
* Tabu Search for Travelling Salesman Problem and Capacitated Vehicle Routing Problem

## Some visualizations
* **Simulated Annealing:** Below we see the comparison between simulated annealing (SA) and greedy search (GS) on an example objective. The search algorithm attempts to minimize the function based on two variables. In the image, green areas are maximas and purple areas are minimas, with the intensity representing magnitude.
  
![Simulated Annealing example](Images/simulated_annealing.png)

* **Genetic Algorithsm**: Below shows the evolution of the solutions for two problems solved using genetic algorithms: path finding and travelling salesman problem:
  
<center>

 Path Finding          |  Travelling Salesman Probem
:-------------------------:|:-------------------------:
![Path finding using genetic algorithm](Images/GA_PathFinding.gif)  |  ![TSP using genetic algorithms](Images/GA_TSP.gif)
</center>

* **NSGA II**: Below shows the evolution of the pareto front for two benchmark multi objective optimization problems: Kursawe function and Viennet function (look at `6. Multi Objective Optimization & NSGA II.ipynb` for more details).
  
  
<center>

 Kursawe Function          |  Viennet Function
:-------------------------:|:-------------------------:
![Path finding using genetic algorithm](Images/nsga_kursawe.gif)  |  ![TSP using genetic algorithms](Images/nsga_viennet.gif)
</center>

* **Tabu Search**: Below compares an optimal solution found using Tabu search vs. greedy search for the [Vehicle Routing Problem](https://en.wikipedia.org/wiki/Vehicle_routing_problem).

<center>

 Greedy Search          |  Tabu Search
:-------------------------:|:-------------------------:
![VRP optimal solution using Greedy search](Images/vrp_greedy.png)  |  ![VRP optimal solution using Tabu search](Images/vrp_tabu.png)
</center>
  
## Running the Code
The code is available as separate Jupyter notebooks, which can be run independent on one another.

## Acknowledgements
The theoretical details for the algorithms have been taken from the course [Surrogate and Metaheuristic Global Optimization](https://ivle.nus.edu.sg/V1/lms/public/view_moduleoutline.aspx?CourseID=1D86508F-95B6-4BD2-AC09-6A895C581EBF&ClickFrom=StuViewBtn) offered in [NUS](http://www.nus.edu.sg), taught by [Prof. Christine Shoemaker](https://www.eng.nus.edu.sg/isem/staff/christine-a-shoemaker/)