# CompOT
----

This is a work-in-progress repository for various Computational Optimality Theory scripts and documents. Here you'll find an overview of this project's set theory framework and algorithmic methods for generative candidate selection and evaluation.


## Set-Based Formalism

This project uses a set-theoretic framework to formalize Computational Optimality Theory (CompOT). Below, we define the primary sets, functions, and structures.

### Sets

- **$\textbf{Can}$:** The infinite set of all possible candidates.
  
   $$\textbf{Can} = \\{ c_1, c_2, c_3, \dots \\}$$

- **$\textbf{Con}$:** The finite set of all constraints, hierarchically ranked.

   $$\textbf{Con} = \\{ k_1, k_2, \dots, k_m \\} \quad \text{with } k_1 \succ k_2 \succ \dots \succ k_m$$

- **$\textbf{C}$:** The finite set of chosen candidates used in evaluation. 
   
   $$\textbf{C} \subset \textbf{Can}$$

### Functions

1. **Evaluation Function** $E$:
   The evaluation function maps each pair of constraint $k_i \in \textbf{Con}$ and candidate $c \in \textbf{Can}$ to a binary value indicating satisfaction ($0$) or violation ($1$).

   $$E: \textbf{Con} \times \textbf{Can} \rightarrow \{0, 1\}$$

   $$E(k_i, c) = \begin{cases} 1 & \text{if } c \text{ violates } k_i, \\
   0 & \text{if } c \text{ satisfies } k_i.
   \end{cases}$$

2. **First Violation Function** $F(c)$:
   The first violation function identifies the first constraint violated by a candidate $c \in \textbf{Can}$:
   
   $$F: \textbf{Can} \rightarrow \{1, 2, \dots, m\} \cup \{\infty\}$$

   $$F(c) =
   \begin{cases}
   \min \{ i \mid E(k_i, c) = 1 \} & \text{if such } i \text{ exists,} \\
   \infty & \text{if } E(k_i, c) = 0 \text{ for all } i.
   \end{cases}$$

### Level Sets

The candidate space is partitioned into **level sets** based on $F(c)$, the first violated constraint:

$$\mathcal{L}_i = \{ c \in \textbf{Can} \mid F(c) = i \}, \quad i = 1, 2, \dots, m$$

- The **minimal level set** $\mathcal{L}_{\min}$ contains candidates that violate the same highest-ranked constraint $k_i$.
- The winning candidate is determined by lexicographically comparing violation profiles within $\mathcal{L}_{\min}$ and across higher-ranked levels as needed.



## Generative Candidate Selection

This algorithm generates a finite, sufficient subset of candidates for evaluation.


### Process:

1. **Initialization:**
   Start with:
   - The winning candidate $c_w$ with its violation profile $V(c_w)$.
   - The fully faithful candidate $c_f$ (the candidate with no violations).

2. **Iterative Generation:**
   - For a given candidate $c_n$:
     1. Identify the first unviolated constraint $k_i \in \textbf{Con}$.
     2. Generate a new candidate $c_{n+1}$ designed to violate $k_i$.
     3. Compute the violation profile $V(c_{n+1})$ by applying $E(k_j, c_{n+1})$ for all $k_j \in \textbf{Con}$.
     4. Check which constraints remain unviolated.

   - Repeat this process until every constraint in $\textbf{Con}$ has been violated at least once.

3. **Termination:**
   The process stops when the generated set of candidates $\textbf{C}$ contains sufficient candidates to:
   - Lexicographically evaluate $c_w$.
   - Prove $c_w$'s optimality against all potential competitors.


## Development Roadmap

1. Implement basic generative candidate selection.
2. Create evaluation algorithms for lexicographic comparison and level-set pruning.
3. Extend the system for multi-candidate generation and efficiency testing.
4. Develop user-friendly interfaces and visualizations.
5. Provide detailed documentation and tutorials.


## Usage

Usage instructions will be added as the repository develops.


## Contributions

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

Please ensure that your code adheres to project guidelines and is well-documented.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
