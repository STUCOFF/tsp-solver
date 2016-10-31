## Solving TSP with Tabu-Search and Simulated Annealing



## Environment
- OS: Arch linux 
- CPU: Intel(R) Core(TM) i5-3337U CPU @ 1.80GHz
- RAM: 8GB



## Implementation
- Python 3
- numpy (1.11.2)
- Implemeted by US



## Parameters of TS
- The neighbor was defined that swap the order of two city
- Max loop: 10,000
- Size of Tabu list: 500
- Termination condition: 100 no change




## Parameters of SA
- Update temperature (t): t = a * t,  (a = 0.5)
- Intitial temperature: 50
- Minimum temperature: 0.000001
- Equilibrium state: 10 (= Q) times transitions
- Max loop: 10,000
- Termination condition: 100 no change



## Experiment 1



![graph](img/graph_01.png)



## Result: Path cost and time 
## TS
|          |         MAX |         MIN |         AVE |
|:---------|------------:|------------:|------------:|
| Cost     | 14          | 10          | 11.3        |
| Time [s] |  0.00970888 |  0.00899458 |  0.00927832 |

## SA
|          |        MAX |        MIN |        AVE |
|:---------|-----------:|-----------:|-----------:|
| Cost     | 14         | 10         | 10.8       |
| Time [s] |  0.0105474 |  0.0102334 |  0.0103969 |



## Result: Memory usage of TS
```txt
Answer
Path: [4, 2, 0, 5, 3, 1] , Cost: 12
Filename: tabu_search.py

Line #    Mem usage    Increment   Line Contents
================================================
    11   28.359 MiB    0.000 MiB   @profile
    12                             def tabu_search(graph, tabu_max=500, step=10000, count_max=100):
    13   28.359 MiB    0.000 MiB       count = 0
    14   28.359 MiB    0.000 MiB       tabu_list = []
    15   28.359 MiB    0.000 MiB       n = len(graph)
    16   28.359 MiB    0.000 MiB       s = np.random.permutation(n).tolist()  # initil solution
    17   28.359 MiB    0.000 MiB       tabu_list.append(s)
    18                             
    19   28.359 MiB    0.000 MiB       for i in range(step):
    20                             
    21   28.359 MiB    0.000 MiB           feisible_list = []
    22   28.359 MiB    0.000 MiB           neighbors = get_neighbors(s)
    23                             
    24   28.359 MiB    0.000 MiB           for x in neighbors:
    25   28.359 MiB    0.000 MiB               if not x in tabu_list:
    26   28.359 MiB    0.000 MiB                   feisible_list.append(x)
    27                             
    28   28.359 MiB    0.000 MiB           s_next = find_better_solusion(feisible_list, s, graph)
    29                             
    30   28.359 MiB    0.000 MiB           if s == s_next:
    31   28.359 MiB    0.000 MiB               count += 1
    32                                     else:
    33   28.359 MiB    0.000 MiB               count = 0
    34                             
    35   28.359 MiB    0.000 MiB           s = s_next
    36                             
    37   28.359 MiB    0.000 MiB           if not s in tabu_list:
    38   28.359 MiB    0.000 MiB               tabu_list.append(s)
    39                             
    40   28.359 MiB    0.000 MiB           if len(tabu_list) > tabu_max:
    41                                         tabu_list.pop(0)
    42                             
    43   28.359 MiB    0.000 MiB           if count > count_max:
    44   28.359 MiB    0.000 MiB               return s
    45                             
    46                                 return s
```



## Result: Memory usage of SA
```txt
Answer
Path: [4, 5, 3, 1, 0, 2] , Cost: 10
Filename: simulated_annealing.py

Line #    Mem usage    Increment   Line Contents
================================================
    13   28.117 MiB    0.000 MiB   @profile
    14                             def simulated_anealing(graph, step=10000, a=0.5, q=1000, t=50, t_min=0.000001, count_max=100):
    15   28.117 MiB    0.000 MiB       count = 0
    16   28.117 MiB    0.000 MiB       n = len(graph)
    17   28.117 MiB    0.000 MiB       s = np.random.permutation(n).tolist()  # initil solution
    18                             
    19   28.117 MiB    0.000 MiB       for i in range(step):
    20   28.117 MiB    0.000 MiB           s_next = find_better_solusion(get_neighbors(s), s, graph)
    21                             
    22   28.117 MiB    0.000 MiB           e = get_cost(s, graph)
    23   28.117 MiB    0.000 MiB           e_next = get_cost(s_next, graph)
    24                             
    25   28.117 MiB    0.000 MiB           if s == s_next:
    26   28.117 MiB    0.000 MiB               count += 1
    27                                     else:
    28   28.117 MiB    0.000 MiB               count = 0
    29                             
    30   28.117 MiB    0.000 MiB           if e_next < e:
    31   28.117 MiB    0.000 MiB               s = s_next
    32                                     else:
    33   28.117 MiB    0.000 MiB               if random.random() <= probability(e, e_next, t):
    34   28.117 MiB    0.000 MiB                   s = s_next
    35                             
    36   28.117 MiB    0.000 MiB           if i % q == 0:  # Equilibrium state
    37   28.117 MiB    0.000 MiB               t = a * t
    38                             
    39   28.117 MiB    0.000 MiB           if count > count_max:
    40   28.117 MiB    0.000 MiB               return s
    41                             
    42                                 return s
```



## Experiment 2


![graph](img/graph_03.png)



## Result: Path cost and time

## TS
|          |        MAX |        MIN |        AVE |
|:---------|-----------:|-----------:|-----------:|
| Cost     | 20         | 13         | 17.3       |
| Time [s] |  0.0990255 |  0.0883646 |  0.0946415 |

## SA
|          |        MAX |        MIN |        AVE |
|:---------|-----------:|-----------:|-----------:|
| Cost     | 24         | 20         | 21.5       |
| Time [s] |  0.0909619 |  0.0871007 |  0.0883519 |



## Result: Memory usage of TS
```txt
Answer
Path: [14, 4, 9, 3, 1, 6, 13, 5, 7, 11, 10, 2, 8, 0, 12] , Cost: 21
Filename: tabu_search.py

Line #    Mem usage    Increment   Line Contents
================================================
    11   28.367 MiB    0.000 MiB   @profile
    12                             def tabu_search(graph, tabu_max=500, step=10000, count_max=100):
    13   28.367 MiB    0.000 MiB       count = 0
    14   28.367 MiB    0.000 MiB       tabu_list = []
    15   28.367 MiB    0.000 MiB       n = len(graph)
    16   28.367 MiB    0.000 MiB       s = np.random.permutation(n).tolist()  # initil solution
    17   28.367 MiB    0.000 MiB       tabu_list.append(s)
    18                             
    19   28.367 MiB    0.000 MiB       for i in range(step):
    20                             
    21   28.367 MiB    0.000 MiB           feisible_list = []
    22   28.367 MiB    0.000 MiB           neighbors = get_neighbors(s)
    23                             
    24   28.367 MiB    0.000 MiB           for x in neighbors:
    25   28.367 MiB    0.000 MiB               if not x in tabu_list:
    26   28.367 MiB    0.000 MiB                   feisible_list.append(x)
    27                             
    28   28.367 MiB    0.000 MiB           s_next = find_better_solusion(feisible_list, s, graph)
    29                             
    30   28.367 MiB    0.000 MiB           if s == s_next:
    31   28.367 MiB    0.000 MiB               count += 1
    32                                     else:
    33   28.367 MiB    0.000 MiB               count = 0
    34                             
    35   28.367 MiB    0.000 MiB           s = s_next
    36                             
    37   28.367 MiB    0.000 MiB           if not s in tabu_list:
    38   28.367 MiB    0.000 MiB               tabu_list.append(s)
    39                             
    40   28.367 MiB    0.000 MiB           if len(tabu_list) > tabu_max:
    41                                         tabu_list.pop(0)
    42                             
    43   28.367 MiB    0.000 MiB           if count > count_max:
    44   28.367 MiB    0.000 MiB               return s
    45                             
    46                                 return s
```



## Result: Memory usage of SA
```txt
Answer
Path: [6, 1, 10, 11, 5, 4, 9, 3, 2, 12, 13, 0, 8, 7, 14] , Cost: 22
Filename: simulated_annealing.py

Line #    Mem usage    Increment   Line Contents
================================================
    13   28.359 MiB    0.000 MiB   @profile
    14                             def simulated_anealing(graph, step=10000, a=0.5, q=1000, t=50, t_min=0.000001, count_max=100):
    15   28.359 MiB    0.000 MiB       count = 0
    16   28.359 MiB    0.000 MiB       n = len(graph)
    17   28.359 MiB    0.000 MiB       s = np.random.permutation(n).tolist()  # initil solution
    18                             
    19   28.359 MiB    0.000 MiB       for i in range(step):
    20   28.359 MiB    0.000 MiB           s_next = find_better_solusion(get_neighbors(s), s, graph)
    21                             
    22   28.359 MiB    0.000 MiB           e = get_cost(s, graph)
    23   28.359 MiB    0.000 MiB           e_next = get_cost(s_next, graph)
    24                             
    25   28.359 MiB    0.000 MiB           if s == s_next:
    26   28.359 MiB    0.000 MiB               count += 1
    27                                     else:
    28   28.359 MiB    0.000 MiB               count = 0
    29                             
    30   28.359 MiB    0.000 MiB           if e_next < e:
    31   28.359 MiB    0.000 MiB               s = s_next
    32                                     else:
    33   28.359 MiB    0.000 MiB               if random.random() <= probability(e, e_next, t):
    34   28.359 MiB    0.000 MiB                   s = s_next
    35                             
    36   28.359 MiB    0.000 MiB           if i % q == 0:  # Equilibrium state
    37   28.359 MiB    0.000 MiB               t = a * t
    38                             
    39   28.359 MiB    0.000 MiB           if count > count_max:
    40   28.359 MiB    0.000 MiB               return s
    41                             
    42                                 return s
```



### Comparison: Experiment 1
|         |  TS     |        SA | 
|--------:|--------:|----------:|
| Result  |         |   o       |
| Time    |  o      |           |
| Memory  |         |    o      |



### Comparison: Experiment 2
|         |  TS     |        SA | 
|--------:|--------:|----------:|
| Result  |  o      |           |
| Time    |  o      |    o      |
| Memory  |  o      |    o      |



### Discussion & Conclusion
- In TS and SA, the performance were almost same.
- The memory useage is based on importing python library.
- If we implent by basic lang like C, the result will be changed.
- The parameter of SA was not proper.
- We need to try experiment more and change parameters.



### Thank you
