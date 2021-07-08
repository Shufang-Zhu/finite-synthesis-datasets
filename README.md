# Finite-synthesis-datasets

The datasets for finite-synthesis consists of two classes:
* The first class of datasets is the **Random** family, composed of 1000 LTLf formulas formed by random conjunction, generated as described in [ZTLPV17](https://arxiv.org/pdf/1705.08426.pdf).
* The second one is from [TV19](https://www.ijcai.org/Proceedings/2019/0777.pdf) and [BLTV20](https://arxiv.org/pdf/1911.08145.pdf), which describes two-player games, split into the **Single-Counter**, **Double-Counters** and **Nim** dataset families.


Moreover, for each family, there are two versions referring to which player (agent or environment) moves first.

## Random family

The **Random** datasets are constructed from basic cases taken from LTL synthesis datasets [Lily](https://www.react.uni-saarland.de/tools/unbeast/) and [Load balancer](https://www.react.uni-saarland.de/tools/unbeast/). Formally, a random conjunction formula <img alt="RC(L)" src="https://render.githubusercontent.com/render/math?math=RC%28L%29" style="transform: translateY(20%);" /> has the form:
<img alt="RC(L) = \bigwedge_{1\leq i\leq L}P_i(v_1,v_2,...,v_k)," src="https://render.githubusercontent.com/render/math?math=RC%28L%29%20%3D%20%5Cbigwedge_%7B1%5Cleq%20i%5Cleq%20L%7DP_i%28v_1%2Cv_2%2C...%2Cv_k%29%2C" style="transform: translateY(20%);" />
where <img alt="L" src="https://render.githubusercontent.com/render/math?math=L" style="transform: translateY(20%);" /> is the number of conjuncts, or the length of the formula, and <img alt="P_i" src="https://render.githubusercontent.com/render/math?math=P_i" style="transform: translateY(20%);" /> is a randomly selected basic case. Variables <img alt="v_1,v_2,...,v_k" src="https://render.githubusercontent.com/render/math?math=v_1%2Cv_2%2C...%2Cv_k" style="transform: translateY(20%);" /> are chosen randomly from a set of <img alt="m" src="https://render.githubusercontent.com/render/math?math=m" style="transform: translateY(20%);" /> candidate variables. Given <img alt="L" src="https://render.githubusercontent.com/render/math?math=L" style="transform: translateY(20%);" /> and <img alt="m" src="https://render.githubusercontent.com/render/math?math=m" style="transform: translateY(20%);" /> (the size of the candidate variable set), we generate a formula <img alt="RC(L)" src="https://render.githubusercontent.com/render/math?math=RC%28L%29" style="transform: translateY(20%);" /> in the following way:
* Randomly select <img alt="L" src="https://render.githubusercontent.com/render/math?math=L" style="transform: translateY(20%);" /> basic cases;
* For each case <img alt="\phi" src="https://render.githubusercontent.com/render/math?math=%5Cphi" style="transform: translateY(20%);" />, substitute every variable <img alt="v" src="https://render.githubusercontent.com/render/math?math=v" style="transform: translateY(20%);" /> with a random new variable <img alt="v'" src="https://render.githubusercontent.com/render/math?math=v%27" style="transform: translateY(20%);" /> chosen from <img alt="m" src="https://render.githubusercontent.com/render/math?math=m" style="transform: translateY(20%);" /> atomic propositions.
If <img alt="v" src="https://render.githubusercontent.com/render/math?math=v" style="transform: translateY(20%);" /> is an environment-variable in <img alt="\phi" src="https://render.githubusercontent.com/render/math?math=%5Cphi" style="transform: translateY(20%);" />, then <img alt="v'" src="https://render.githubusercontent.com/render/math?math=v%27" style="transform: translateY(20%);" /> is also an environment-variable in <img alt="RC(L)" src="https://render.githubusercontent.com/render/math?math=RC%28L%29" style="transform: translateY(20%);" />. The same applies to the agent-variables.

## Single-Counter family

This dataset family is a simple example where the behavior of the system is completely determined by the actions of the environment. Therefore, the challenge in this family lies mostly in proving that the specification is realizable. The system stores an <img alt="n" src="https://render.githubusercontent.com/render/math?math=n" style="transform: translateY(20%);" />-bit counter (where <img alt="n" src="https://render.githubusercontent.com/render/math?math=n" style="transform: translateY(20%);" /> is the scaling parameter) which it must increment upon a signal by the environment. The system wins if the counter eventually overflows to <img alt="0" src="https://render.githubusercontent.com/render/math?math=0" style="transform: translateY(20%);" />. To guarantee that the game is winning for the system, the specification assumes that the environment will send the increment signal at least once every two timesteps.

## Double-Counter family

This dataset family is similar to the Single-Counter one, except that in this case there are two <img alt="n" src="https://render.githubusercontent.com/render/math?math=n" style="transform: translateY(20%);" />-bit counters, one incremented by the environment and another by the system. The goal of the system is for its counter to eventually catch up with the environment’s counter. To guarantee that this is achievable, the specification assumes that the environment cannot increment its counter twice in a row.

## Nim family

This dataset family describes a generalized version of the game of Nim [Bouton1901](https://paradise.caltech.edu/ist4/lectures/Bouton1901.pdf) with <img alt="n" src="https://render.githubusercontent.com/render/math?math=n" style="transform: translateY(20%);" /> heaps of <img alt="m" src="https://render.githubusercontent.com/render/math?math=m" style="transform: translateY(20%);" /> tokens each. The environment and the system take turns removing any number of tokens from one of the heaps, and the player who removes the last token loses.
