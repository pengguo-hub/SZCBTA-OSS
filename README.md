# Joint optimization of spatial zoning, continuous batching, and task allocation in overhead sorting systems

This repository provides the instance-generation code, computational instances, and corresponding experimental results accompanying the paper **“Joint optimization of spatial zoning, continuous batching, and task allocation in overhead sorting systems.”**

The materials are shared to support inspection of the experimental data, verification of the reported results, and further research on overhead sorting systems.



##### instance\_generate.py:

The generation code creates instances according to the parameters specified in the script. Use the supplied instance files when comparing with the published results; generating new instances may produce different inputs unless the same parameters and random seeds are used.

To generate additional instances:

1. Install the Python version and packages required by the generator.
2. Set the instance parameters, output directory, and random seed as supported by the code.



##### json\_order:

The provided example files contain the input data for the computational experiments. When interpreting the data, refer to the generator and the content of the paper together. These correspond to the examples in Tables 6–8.



##### result:

The results file reports the experimental results for the corresponding instances. The results can only be compared if the instance data, algorithm settings, termination conditions, and computational environment are exactly the same. These results correspond to the three-stage algorithm instance results in Tables 6–8.



##### case\_instances:

These data are consistent with the case study examples presented in the paper.



##### case\_results:

These results are consistent with those obtained using the three-stage algorithm in the case studies presented in the paper.

