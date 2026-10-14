
<!-- PAGE 1 -->
![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000000_cfc028af990a7c714565578d9997a9eb76f14c02e4a83a81cc03f39aa5bc9532.png)

Article

## Dynamics of a Fishery Management Model with Predation-Induced Fear Effect, Impulsive Nonlinear Harvesting Prey and Predator Seasonally Migrating Between Two Patches

Bingying Gao, Jianjun Jiao Zeli Zhou and Shirui Zhang

School of Mathematics and Statistics , Guizhou University of Finance and Economics, Guiyang 550025, China Correspondence: jiaojianjun@mail gufe.edu.cn

## Abstract

This paper proposes a novel management model that integrates three critical ecological factors: the prey (fish) fear effect, impulsive nonlinear harvesting, and predator seasonal migration. It is demonstrated that all solutions of the proposed system are uniformly ultimately bounded. We establish the conditions for the local and global asymptotic stability of the prey-extinction periodic solution; derive the permanence criteria for the system, and determine the threshold condition for prey extinction. Numerical simulations are conducted to validate the theoretical These simulations also help identify the parameters influencing the threshold condition and reveal the complex dynamics of the The results provide significant insights for fishery management, suggesting that regulating harvesting intensity and as well as considering predator migration mortality, are crucial for sustaining fish populations and preventing overexploitation. fishery findings. key system. timing harvesting; large-scale migration; global asymptotic stability; permanence

MSC: 34A37; 34D05; 34D23; 34E05; 37MO5

## 1. Introduction

Fisheries constitute a economic driver; supported by a complete industrial chain that encompasses the entire process from fishing and aquaculture to processing and sales [1]. Fisheries sustain employment and livelihoods for millions, worldwide. Nevertheless , combined pressures from population growth and demand for aquatic products are intensifying the strain on global resources [2,3] Overfishing and a lack of scientific planning deplete fish stocks, disrupt aquatic food webs, and threaten biodiversity: The urgent implementation of science-based management is thus essential to ensure the long-term sustainability of fishery resources [4,5]. key rising fishery

The long-distance migrations undertaken by many birds under climatic and other influences have been comprehensively explored in studies such as [6-8]. Empirical evidence confirms that large-scale bird migration impacts fish resources. Regional studies of Lake Erie (North America) the Dal River (Sweden) Norway; and South Africa demonstrate that migratory birds alter fish population size, distribution; and ecological balance through differential predation pressure [9\_11] Given that these birds predate economically valuable

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000001_e1069a8128cb69e8af192403d64fc05aa2628c4993fc15a53bd8f25c040c5b9b.png)

Academic Editor: Hari Mohan Srivastava

Revised: 22 December 2025

Accepted: 29 December 2025

Publis
<!-- PAGE 2 -->
hed: 31 December 2025

Copyright: @ 2025 by the authors

Licensee MDPI, Basel, Switzerland.

This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.

Axioms 2026, 15, 32

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000002_1d857ae610518ae23d759de2c756add235dedcc7e02f21797dda1baff4f73bbc.png)

fishery management models should integrate the impacts of bird migration, necessitating the development of suitable biological models to describe this critical predator-prey dynamic [13]

Biodynamic systems, recognized for their accurate prediction of biological population trends, have attracted considerable worldwide interest [14]. Such systems with impulsive effects are now widely applied across various fields. For instance, Liu et al. [15] examined Holling-I functional response predator-prey system subject to impulsive linear pesticide spraying and predator release:

$$\begin{array} { r l } & { \frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) ( r - a x _ { 1 } ( t ) - b x _ { 2 } ( t ) ) , } \\ & { \frac { d x _ { 2 } ( t ) } { d t } = x _ { 2 } ( t ) ( - d + c x _ { 1 } ( t ) ) , } \\ & { \Delta x _ { 1 } ( t ) = - p _ { 1 } x _ { 1 } ( t ) , \quad t = n T } \\ & { \Delta x _ { 2 } ( t ) = - p _ { 2 } x _ { 2 } ( t ) + \mu , } \end{array}$$

where x1 (t) stands for the prey (pest) population and x2(t) for the predator (natural enemy) population   During the non-impulsive phase, the prey population x1 (t) grows at an intrinsic rate r &gt; 0. It is restricted by the intraspecific competition coefficient a 0 and the predation rate b 0 of predators. Meanwhile, the predator population x2(t) a natural mortality rate d &gt; 0 and grows through predation with a conversion rate 0. Impulsive events occur periodically with T.At these moments , pesticides are sprayed, instantly reducing the prey population by proportion 0 p1 1 and the predator population by proportion 0 &lt; p2 1 &gt; 0 predators are artificially added. Ultimately, the global asymptotic stability condition for the prey-extinction periodic solution; the persistence condition of the system; and the existence and stability criteria for the positive periodic solution are derived. In [16], a fishery model with impulsive linear harvesting was explored, establishing the global asymptotic stability conditions for the prey extinction periodic solution and the criteria for system permanence. Jiao et al. [17] investigated an impulsive predator-prey model incorporating seasonal large-scale migration of predators. Other related studies can be found in [18-23]. In terms of nonlinear impulses, Li [24,25] incorporated nonlinear impulsive control into pest management models, and Cheng [26] studied nonlinear impulsive control in a phytoplankton-fish system. has period

Predator-prey interactions extend beyond direct killing: In reality, prey perceiving threats (fish) may alter their behaviors increased concealment) , which in turn may affect predators (birds) in terms of search efficiency or handling time: Incorporating such bidirectional behavioral feedback into the model will undou
<!-- PAGE 3 -->
btedly make the model more (e.g'

Most models with impulsive effects in fisheries use linear harvesting   In contrast, impulsive density-dependent nonlinear harvesting has received less attention; despite its direct relevance to the population monitoring central to effective management [27-29]Harvesting efforts should therefore be regulated by monitoring fish population levels. Furthermore, while most existing studies on impulsive predator-prey models rely on Holling-I or Holling-II functional responses that depend solely on prey density; a more ecologically realistic framework requires functional responses influenced by both prey and predator densities [30]. The large-scale migration of piscivorous birds impacts fish populations and fisheries due to their energy dependence on this prey. This interaction, which is bidirectional as fish resource availability indirectly influences bird numbers , is modeled the Beddington-DeAngelis functional response.  This response depends on the densities of both species and quantifies the inhibitory effect of predator interference on predation rates , leading to more accurate predictions that have been validated in several cases [31] using

ecologically realistic. However; due to significant challenges in quantifying these trophiclevel bidirectional behavioral interactions in modeling and parameter estimation; as preliminary theoretical exploration; we intentionally focus on the core, well-documented direct effect of fear the growth rate of the prey population (fish) . Long-term fear stress induced by predators can significantly alter prey physiology; life history; and reproduction: This phenomenon is now central to ecological research [32]. This is demonstrated by diverse cases: wolves altering elk metabolism [33], odors of mantises causing harm to fruit flies [34], and predator cues causing PTSD-like (post-traumatic stress disorder) impairments that compromise reproduction in chickadees [35]. Beyond traditional predators , the large-scale migration of birds constitutes a significant source of fear stress for aquatic prey like fish [36]: This stress elicits a physiological response, elevating cortisol and other stress hormones via the HPA axis (hypothalamic-pituitary-adrenal axis) , which consequently impairs immune function, disrupts reproductive hormones , and suppresses reproduction [37,38]. Prolonged exposure can also alter metabolic scope, hinder growth, and ultimately lead to reduced birth rates [39]. Evidence shows that the predation threat from migratory birds can disrupt fish metabolism and behavior; impair reproduction through energetic and hormonal pathways, and ultimately reduce reproductive success [40-42]. The fear effect on fish is still overlooked in models, unlike other ecological factors. on fishery

Based on this, this paper establishes a novel Beddington-DeAngelis functional response fishery management system with fear effect; predator large-scale migration and impulsive density-dependent nonlinear harvesting prey (fish),

$$\supsetsup [ \text {pulsive density-dependent nonlinear harvesting prey (fish)} , \\ \frac { d x _ { t } ( t ) } { d t } = x _ { 0 } ( t ) ( a _ { 1 } - b _ { 1 0 } x _ { 0 } ( t ) ) , \\ \frac { d x _ { 1 } (
<!-- PAGE 4 -->
 t ) } { d t } = x _ { 1 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 1 } ( t ) ) , \\ \Delta x _ { 0 } ( t ) = - \frac { h _ { m } x _ { 0 } } { a _ { 0 } + x _ { 0 } ( t ) } x _ { 0 } ( t ) , \\ \Delta x _ { 1 } ( t ) = - a _ { 0 } x _ { 1 } ( t ) , \\ \frac { d x _ { 0 } ( t ) } { d t } = x _ { 0 } ( t ) \left ( \frac { a _ { 2 0 } } { 1 + a _ { 1 } x _ { 1 } } - b _ { 2 0 } x _ { 0 } ( t ) \right ) - \frac { \zeta _ { 0 } x _ { 0 } ( t ) x _ { 1 } ( t ) } { 1 + A _ { 0 } x _ { 0 } ( t ) + B _ { 0 } x _ { 1 } ( t ) } , \\ \frac { d x _ { 1 } ( t ) } { d t } = - d x _ { 1 } ( t ) + \frac { c _ { 0 } z _ { 0 } x _ { 0 } ( t ) x _ { 1 } ( t ) } { 1 + A _ { 0 } x _ { 0 } ( t ) + B _ { 0 } x _ { 1 } ( t ) } , \\ \Delta x _ { 0 } ( t ) = 0 , \quad \left \{ t = ( n + 1 ) P \\ \Delta x _ { 1 } ( t ) = - d _ { 1 } x _ { 1 } ( t ) , \right \} \\ \intertext { s u p s } A se a l $ m a t r i g n a t i m s a s u m e d $ for p e r a d o r s m i v e n t h e v e e t h a n d p e r a t i o n $ }$$

A seasonal migration is assumed for predators moving between 1 and 2. The density xo(t) describes the prey population, which is confined to 2 The predator population density is represented by x1 (t). For prey population xo(t) in 2 over (nP, (n + 0)P] , a10 0 corresponds to the inherent growth rate; similarly, b1o 0 represents the intraspecific competition coefficient:. density-dependent nonlinear harvesting of prey (fish) at time t = (n + 0)P. The coefficient where 0, represents the maximum harvest amount:. That is, prey harvesting happens right before predators move in large numbers seasonally from patch 1 to 2 This happens at time t = (n + 0)P. Furthermore, the maximum amount of prey (fish) is harvested when the prey quantity xo(t) approaches infinity: On the contrary, no harvest is made when the prey quantity approaches 0. The mortality coefficient do (0 do 1) governs the population loss that predators x1 (t) undergo their seasonal migration from 1 to 2 at time t = (n + 0)P. In 2 over 0 denotes the inherent growth rate of prey xo(t), while b2o 0 denotes its intraspecific competition coefficient in the same period.  The fear effect is characterized by the birth patch pattern patch patch patch hmax hmax' patch during patch patch patch

rate term 020 with &amp; 0 quantifying the fear level.  Consequently  an increase in &amp; leads to a reduction in the prey birth rate\_ The term Zoxo(t)x (t) characterizes the Beddington-DeAngelis functional response, capturing how predator capture ability depends on both prey(fish) and predator densities , rather than prey density alone. Over the interval (n + 0)P, (n + 1)P] Ço &gt; 0 quantifies the prey capture ability by predators in 2, and co 0 denotes the associated conversion rate into predator growth. Ao 0 represents the handling time on the feeding rate and Bo 0 characterizes the intensity of interference among predators. The coefficient d1 (0 &lt; d1 1) represents the mortality rate during the seasonal large-scale migration of predators x1 (t) from 2 to patch 1 at t = (n + 1)P. These migratory events occur periodically every P time units, where P 0 is a constant and 0 &lt; 0 1. Additionally; the differences (t) and (t) are defined as Ax(t) = xo(t+) - xo(t) and (t) = x
<!-- PAGE 5 -->
1 (t+) x1 (t) , respectively. patch patch

## 2. Preliminaries

Remark 1. In (2) , the dynamics of the predator population x1(t) in 2 are affected by its seasonal immigration and emigration (characterized by impulses) as well as local mortality: The prey-extinction periodic solution (0,ñ1(t) ) focused on in this paper describes the state of the predator population after the collapse of the fish resource xo(t) in 2 Mathematically , this solution arises from the subsystem (3) when xo(t) = 0, where predator dynamics are driven solely by intrinsic growth the migration-free (nP,(n + 0)P] natural mortality during the predation The condition (1 \_ do)(1 \_ 1ensures a solution ñ1 (t ) , which is sustained not by local prey but by the balance between growth in 1and mortality during migration. This mathematical construct is used to model the ecological scenario where predators are sustained by external resources other prey in 1) and continue to exert periodic predation pressure on 2 even after local prey From a biological perspective, the sustained oscillations of x1 (t) in this solution do not imply that predators can persist independently of local fish resources for a time, but rather reflect the following after the depletion of the target fishery population (prey) , the predation pressure from migratory populations outside the will still periodically occur. In fishery management models , the core purpose of analyzing the stability of this solution is to accurately define the critical threshold at which the target fish population moves towards commercial extinction (unable to support sustainable fishing)  rather than predicting the long-term independent survival of the predator population. patch system patch during period period periodic patch patch (e8 collapse. patch long reality: system

Consider system (2), whose right-hand side defines a vector mapping p (p1 p2) Let R+ = [0,0) and R2 {(m1,m2) M1 &gt; O,m2 &gt; 0} A solution to this system can be expressed as F(t) = (xo(t),x1(t))P, where the domain is R+ and the range belongs to R2 This solution is continuous on the intervals (nP, (n + 0)P] and ((n + 0)P, (n + 1)P] (n € Z+) , and possesses right limits at (n+1)P+X1(t). Thus, F(t) is a piecewise continuous function. According to the descrip tion in [43], the p is smooth, ensuring global uniqueness of solutions to the system (2). We state several lemmas that form the basis for our subsequent theoretical developments. pulse limt &gt;C key

Lemma 1. If the solution F(t) of system (2) satisfies F(O+) 0, then F(t) 0 for all t 0. Additionally, if F(0+) &gt; 0, then F(t) 0 for all t 0

Lemma 2 There exists a constant J1 0 such that xo(t) &lt; J1 and x1 (t) J1 for all sufficiently large t, where (xo(t),x1 (t)) denotes a solution of system (2).

Proof: the upper right Dini derivative of V(t) , we obtain

$$V ( t ) & = c _ { 0 } ( a _ { 1 0 } + d ) x _ { 0 } ( t ) - c _ { 0 } b _ { 1 0 } x _ { 0 } ^ { 2 } ( t ) + ( a _ { 1 1 } + d ) x _ { 1 } ( t ) \\ & = - c _ { 0 } b _ { 1 0 } \left ( x _ { 0 } ( t ) - \frac { a _ { 1 0 } + k } { 2 b _ { 1 0 } } \right ) ^ { 2 } + \frac { c _ { 0 } ( a _ { 1 0 } + k ) ^ { 2 } } { 4 b _ { 1 0 } } \\ & - b _ { 1 1 } \left ( x _ { 1 } ( t ) - \frac { a _ { 1 1 } + k }
<!-- PAGE 6 -->
 { 2 b _ { 1 1 } } \right ) ^ { 2 } + \frac { ( a _ { 1 1 } + k ) ^ { 2 } } { 4 b _ { 1 1 } } \\ & \leqslant \frac { c _ { 0 } ( a _ { 1 0 } + k ) ^ { 2 } } { 4 b _ { 1 0 } } + \frac { ( a _ { 1 1 } + k ) ^ { 2 } } { 4 b _ { 1 1 } } ,$$

when t = (n + 0)P ,

$$V ( t ^ { + } ) = c _ { 0 } x _ { 0 } ( t ) \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } + x _ { 0 } ( t ) } \right ) + ( 1 - d _ { 0 } ) x _ { 1 } ( t ) \leqslant V ( t ) ,$$

when t € ((n + 0)P , (n + 1)P]

$$D ^ { + } V ( t ) + k V ( t ) & = - c _ { 0 } b _ { 2 0 } x _ { 0 } ^ { 2 } ( t ) + c _ { 0 } x _ { 0 } ( t ) \left ( \frac { a _ { 2 0 } } { 1 + \alpha x _ { 1 } ( t ) } + k \right ) + ( k - d ) x _ { 1 } ( t ) \\ & \leq - c _ { 0 } b _ { 2 0 } x _ { 0 } ^ { 2 } ( t ) + c _ { 0 } x _ { 0 } ( t ) ( a _ { 2 0 } + k ) \\ & = - c _ { 0 } b _ { 2 0 } \left ( x _ { 0 } ( t ) - \frac { a _ { 2 0 } + k } { 2 b _ { 2 0 } } \right ) ^ { 2 } + \frac { c _ { 0 } ( a _ { 2 0 } + k ) ^ { 2 } } { 4 b _ { 2 0 } } ,$$

$$V ( t ^ { + } ) = c _ { 0 } x _ { 0 } ( t ) + ( 1 - d _ { 1 } ) x _ { 1 } ( t ) \leqslant V ( t ) .$$

Letting M = minCo Co we derive 4620 (a1o (a20 4b1o 4b11

$$\begin{cases} V ( t ) + k V ( t ) \leqslant M & , t \in ( n P , ( n + 1 ) P ] \\ V ( t ^ { + } ) \leqslant V ( t ) & , t = ( n + 1 ) P \end{cases} .$$

By applying the comparison theorem for impulsive differential equations, we derive

$$V ( t ) \leqslant \left ( V ( 0 ^ { + } ) - \frac { M } { k } \right ) e x p ( - n k P ) + \frac { M } { k } \to \frac { M } { k } ( t \to \infty )$$

Consequently, it can be deduced that V(t) is uniformly ultimately bounded. Fur thermore, by the definition of V(t) , xo(t) and x1 (t) possess an upper bound J1 such that Xo(t) J1 and x1 (t) &lt; J1.

xo(t) = 0, the subsystem of system (2) can be obtained as follows: Letting

$$\begin{cases} \frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 1 } ( t ) ) & , t \in ( n P , ( n + \theta ) P ] \\ \Delta x _ { 1 } ( t ) = - d _ { 0 } x _ { 1 } ( t ) & , t = ( n + \theta ) P \\ \frac { d x _ { 1 } ( t ) } { d t } = - d x _ { 1 } ( t ) & , t \in ( ( n + \theta ) P , ( n + 1 ) P ] \\ \Delta x _ { 1 } ( t ) = - d _ { 1 } x _ { 1 } ( t ) & , t = ( n + 1 ) P \end{cases} .$$

The analytical solution follows

$$x _ { 1 } ( t ) = \begin{cases} \frac { a _ { 1 1 } x _ { 1 } ( n P ^ { + } ) e ^ { \rho _ { 1 1 } ( t - n h ) } } { a _ { 1 1 } + b _ { 1 1 } x _ { 1 } ( n P ^ { + } ) ( e ^ { \rho _ { 1 1 } ( t - n h ) } - 1 ) } & , t \in ( n P , ( n + \theta ) P ] \\ \gamma _ { 1 } ( ( n + \theta ) P ^ { + } ) e ^ { - d ( t - ( n + \theta ) P ) } & t \in ( ( n + \theta ) P \ P \ ( n + 1 ) P ] ^ { . } \end{cases} .$$

Equation (4) has a trivial fixed X* 0 Moreover; under the condi tion (1 = do)(1 1, it also admits a positive fixed a11 ((1\_do)(l\_d1 The periodic solution of system (3) is point point

$$\widetilde { x } _ { 1 } ( t ) = \begin{cases} \frac { a _ { 1 1 } x ^ { * } e ^ { a _ { 1 1 } ( t - n P ) } } { a _ { 1 1 } + b _ { 1 1 } x ^ { * } ( e ^ { a _ { 1 1 } ( t - n P ) } - \overline { 1 } ) } & , t \in ( n P , ( n + \theta ) P ] \\ x ^ { * * } e ^ { - d ( t - ( n + \theta ) P ) } & , t \in ( ( n + \theta ) P , ( n + 1 ) P ] \end{cases} .$$

where

W
<!-- PAGE 7 -->
hen x 0,

$$\left | \frac { d f ( x _ { n } ) } { d x _ { n } } \right | _ { x _ { n } = x ^ { * } } \right | = ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a }$$

if (1 \_ do)(1 \_ d)eanoP-d(1-0)P 1. When x* + 0,

$$\left | \frac { d f ( x _ { n } ) } { d x _ { n } } \right | _ { x _ { n } = x ^ { * } } \right | = \frac { 1 } { ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } } < 1 ,$$

if (1 \_ do)(1 \_ 1. Next, will prove the global stability: We have we

$$| x _ { n + 1 } - 0 | = \frac { a _ { 1 1 } ( 1 - a _ { 0 ) } ) ( 1 - a _ { 1 } ) e ^ { x _ { n } } } { a _ { 1 1 } + b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta P } - 1 ) x _ { n } } \leqslant ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } x _ { n } .$$

That the trivial fixed 1. point is,

For the positive fixed point; we have

$$\begin{array} { r } { x ^ { * } = \frac { a _ { 1 1 } ( ( 1 - a _ { 0 } ) ( 1 - a _ { 1 } ) e ^ { \prime } e ^ { 1 1 ^ { * } } - a _ { 1 } ) e ^ { ( 1 - a _ { 1 } ) } } { b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta ^ { p } } - 1 ) } } \end{array}$$

Lemma 3. (i) The trivial fixed is globally asymptotically stable when point

$$1 .$$

(ii) The positive fixed point x* is globally asymptotically stable when

$$( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } > 1 .$$

Proof. Letting Xn x1 (nP+ ) , the stroboscopic map of system (2) is

$$x _ { n + 1 } & = \frac { ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) a _ { 1 1 } e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } x _ { n } } { a _ { 1 1 } + b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta P } - 1 ) x _ { n } } \\ & = f ( x _ { n } ) , \\ \frac { d f ( x _ { n } ) } { d x _ { n } } & = \frac { a _ { 1 1 } ^ { 2 } ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } } { ( a _ { 1 1 } + b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta P } - 1 ) x _ { n } ) ^ { 2 } } .$$

$$x _ { n }$$

$$\frac { d x _ { n } } { d x _ { n } }$$

$$\left | \frac { 1 } { x _ { n + 1 } } - \frac { 1 } { x ^ { * } } \right | & = \left | \frac { a _ { 1 1 } + b _ { 1 1 } \left ( e ^ { a _ { 1 1 } \theta P } - 1 \right ) x _ { n } } { ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } x _ { n } } - \frac { a _ { 1 1 } + b _ { 1 1 } \left ( e ^ { a _ { 1 1 } \theta P } - 1 \right ) x ^ { * } } { ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } x ^ { * } } \right | \\ & = \frac { 1 } { ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } } \right | \frac { 1 } { x _ { n } } - \frac { 1 } { x ^ { * } } \right | \to 0 \ a s \ n \to \infty .$$

Therefore, the positive fixed point x* is globally asymptotically stable if (1 do) (1 \_ 1

Similar to Ref. [25], we can obtain the following lemma:

Lemma 4. The periodic solution ñ1(t) becomes globally asymptotically stable when the condition

$$> 1$$

is satisfied.

$$i s \, s a t i s f i e . \\ \quad \text {Consider the following conditions} \\ ( H _ { 1 } ) \, ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 } \theta P - d ( 1 - \theta ) P } & > 1 , \\ ( H _ { 2 } ) \left ( 1 - \frac { H _ { \max } } { a _ { 0 } } \right ) \exp ( a
<!-- PAGE 8 -->
 _ { 1 0 } \theta P + d ( 1 - \theta ) P + M ) & < 1 , \\ ( H _ { 2 } ^ { \prime } ) \left ( 1 - d _ { 0 } \right ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P - 2 \ln \frac { a _ { 1 1 } + b _ { 1 1 } x ^ { * } ( e ^ { a _ { 1 1 } \theta P } - 1 ) } { a _ { 1 1 } } } & < 1 , \\ ( H _ { 3 } ) \left ( 1 - \frac { H _ { \max } } { a _ { 0 } + b } \right ) \exp ( a _ { 1 0 } \theta P + d ( 1 - \theta ) P + M ^ { \prime } ) & < 1 , \\ ( H _ { 4 } ) \left ( 1 - \frac { H _ { \max } } { a _ { 0 } } \right ) \exp ( a _ { 1 0 } \theta P + d ( 1 - \theta ) P + M ) & > 1 , \\ \text {with} & \quad M = \ln \frac { 1 + \alpha x ^ { * * } e ^ { - d ( 1 - \theta ) P } } { 1 + \alpha x ^ { * * } } + \frac { \xi _ { 0 } } { d B _ { 0 } } \ln \frac { 1 + B _ { 0 } x ^ { * * } e ^ { - a ( 1 - \theta ) P } } { 1 + B _ { 0 } x ^ { * * } } , \\ M ^ { \prime } = \ln \frac { 1 + \alpha x ^ { * * } e ^ { - d ( 1 - \theta ) P } } { 1 + \alpha x ^ { * * } } + \frac { \zeta _ { 0 } } { d B _ { 0 } } \ln \frac { 1 + A _ { 0 } b + B _ { 0 } x ^ { * * } e ^ { - d ( 1 - \theta ) P } } { 1 + A _ { 0 } b + B _ { 0 } x ^ { * * } } . \\ \intertext { s a t i s f i e . } 3 . \text { Main Results} \\ \intertext { \text {in bio-dynamical systems, involving the stability of the prevac-extinction periodicity} } \intertext { \text {in bio-dynamical systems, involving the stability of the prevac-extinction periodicity} }$$

## 3. Main Results

In bio-dynamical systems , investigating the stability of the prey-extinction periodic solution is not aimed at achieving such a state, but rather to pinpoint the critical threshold at which the system collapses , thereby providing an early warning for irreversible ecological or economic consequences. This section focuses on analyzing the stability of the prey-extinction periodic solution (0,ñ1 (t) ) of system (2): if this solution is stable, it implies that once the prey population density falls below a certain critical level; the system will irreversibly decline toward prey extinction: Notably; the periodic dynamics of the predator population in this solution characterize the ecological reality that external predation pressure still persists periodically even after the depletion of the target fish resource This is mathematically represented by the predator subsystem (3), which is decoupled from prey dynamics and sustained by migration-driven growth and mortality balance, rather than local prey consumption. Consequently, the stability condition of this solution corresponds to a core threshold for preventing the collapse of the target fish population in management practice, offering crucial early warning support for fishery resource risk management.

## 3.1. Stability

To mathematically define the extinction threshold for the prey population; we analyze the stability of the boundary periodic solution (0,ñ1(t)). The stability of this solution implies that once the prey density falls below a critical level due to overharvesting or predation pressure, the system will irreversibly converge to a state where the prey is extinct\_~a scenario that must be avoided in management.

H) hold, then the periodic solution (0,ñ1(t)) of (2) is locally asymptotically stable. system

Pro
<!-- PAGE 9 -->
of: Define u(t) xo(t)  v(t) x1(t) = ñ1(t), the following linear approximation system is obtained for system (2)

$$\left ( \begin{array} { c } \frac { d u ( t ) } { d t } \\ \frac { d v ( t ) } { d t } \end{array} \right ) = \left ( \begin{array} { c c } a _ { 1 0 } & 0 \\ 0 & a _ { 1 1 } - 2 b _ { 1 1 } \widetilde { x } _ { 1 } ( t ) \end{array} \right ) \left ( \begin{array} { c } u ( t ) \\ v ( t ) \end{array} \right ) , t \in ( n P , ( n + \theta ) P ] ,$$

and

$$\left ( \begin{array} { c } \frac { d u ( t ) } { d t } \\ \frac { d v ( t ) } { d t } \end{array} \right ) = \left ( \begin{array} { c c } \frac { a _ { 2 0 } } { 1 + \alpha \widetilde { x } _ { 1 } } - \frac { \zeta _ { 0 } \widetilde { x } _ { 1 } ( t ) } { 1 + B _ { 0 } \widetilde { x } _ { 1 } ( t ) } & 0 \\ \frac { c _ { 0 } \zeta _ { 0 } \widetilde { x } _ { 1 } ( t ) } { 1 + B _ { 0 } \widetilde { x } _ { 1 } ( t ) } & - d \end{array} \right ) \left ( \begin{array} { c } u ( t ) \\ v ( t ) \end{array} \right ) , t \in ( 0 , 1 )$$

For t € (nP,(n + 0)P] the fundamental solution matrix can be readily calculated

$$( t ) = \begin{pmatrix} \exp ( a _ { 1 0 } ( t - n P ) ) & 0 \\ & \ast \end{pmatrix} _ { * } \quad \exp \left ( \int _ { n P } ^ { t } ( a _ { 1 1 } - 2 b _ { 1 1 } )$$

For t € ((n + 0)P , (n + 1)P]  the fundamental solution matrix is as follows

$$Y _ { 2 } ( t ) = \begin{pmatrix} \exp \left ( \int _ { ( n + \theta ) P } ^ { t } \left ( \frac { a _ { 2 0 } } { 1 + \alpha \tilde { x } _ { 1 } ( s ) } - \frac { \zeta _ { 0 } \tilde { x } _ { 1 } ( s ) } { 1 + \beta _ { 0 } \tilde { x } _ { 1 } ( s ) } \right ) d s \right ) & 0 \\ & \exp ( - d ( t - ( n + \theta ) P ) ) \end{pmatrix} .$$

Since the specific expression denoted by * is not used in the subsequent analysis, it is omitted. The linearization of the third and fourth equations in system (2) is given by

$$\begin{pmatrix} u ( ( n + \theta ) P ^ { + } ) \\ v ( ( n + \theta ) P ^ { + } ) \end{pmatrix} = \begin{pmatrix} 1 - \frac { h _ { \max } } { \alpha _ { 0 } } & 0 \\ 0 & 1 - d _ { 0 } \end{pmatrix} \begin{pmatrix} u ( ( n + \theta ) P ) \\ v ( ( n + \theta ) P ) \end{pmatrix} ,$$

and the linearization of the seventh and eighth equations in system (2) is given by

$$\begin{pmatrix} u ( ( n + 1 ) P ^ { + } ) \\ v ( ( n + 1 ) P ^ { + } ) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 - d _ { 1 } \end{pmatrix} \begin{pmatrix} u ( ( n + 1 ) P ) \\ v ( ( n + 1 ) P ) \end{pmatrix} .$$

The local stability of the prey-extinction periodic solution (0,ñ1 (t) ) can be determined by the eigenvalues of the matrix

$$G & = \begin{pmatrix} 1 & 0 \\ 0 & 1 - d _ { 1 } \end{pmatrix} Y _ { 2 } ( P ) \begin{pmatrix} 1 - \frac { h _ { \max } } { \alpha _ { 0 } } & 0 \\ 0 & 1 - d _ { 0 } \end{pmatrix} Y _ { 1 } ( \theta P ) \\ & = \begin{pmatrix} 1 & 0 \\ 0 & 1 - d _ { 1 } \end{pmatrix} \begin{pmatrix} \exp \left ( \int _ { \theta P } ^ { \int _ { P } } \left ( \frac { a _ { 2 0 } } { 1 + \alpha _ { 1 } ^ { 2 } ( s ) } - \frac { \zeta _ { 0 } \tilde { x } _ { 1 } ( s ) } { 1 + B _ { 0 } \tilde { x } _ { 1 } ( s ) } \right ) d s \right ) & 0 \\ & \exp ( - d ( 1 - \theta ) P ) \end{pmatrix} \\ & \times \begin{pmatrix} 1 - \frac { h _ { \max } } { \alpha _ { 0 } } & 0 \\
<!-- PAGE 10 -->
 0 & 1 - d _ { 0 } \end{pmatrix} \begin{pmatrix} \exp ( a _ { 1 0 } \theta P ) & 0 \\ 0 & \exp \left ( \int _ { 0 } ^ { \theta P } ( a _ { 1 1 } - 2 b _ { 1 1 } \tilde { x } _ { 1 } ( s ) ) d s \right ) \end{pmatrix} \\ & = \begin{pmatrix} \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) \exp \left ( \int _ { \theta P } ^ { P } \left ( \frac { a _ { 2 0 } } { 1 + \alpha _ { 1 } ^ { \tilde { x } _ { 1 } } ( s ) } - \frac { \zeta _ { 0 } \tilde { x } _ { 1 } ( s ) } { 1 + B _ { 0 } \tilde { x } _ { 1 } ( s ) } \right ) d s + a _ { 1 0 } \theta P \right ) & 0 \\ & \ast \end{pmatrix} _ { G _ { 2 2 } } , \\ \intertext { where } G _ { 2 2 } & \equiv \left ( 1 - a _ { 0 } \right ) ( 1 - d _ { 1 } ) \exp \left ( \int _ { 0 } ^ { \theta P } ( a _ { 1 1 } - 2 b _ { 1 1 } \tilde { x } _ { 1 } ( s ) ) d s - d ( 1 - \theta ) P \right ) .$$

where G22 (1 \_ do)(1 \_ d1) exp

It is straightforward to determine that the matrix G possesses two eigenvalues

$$\lambda _ { 1 } = \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) \exp \left ( \int _ { \theta P } ^ { P } \left ( \frac { a _ { 2 0 } } { 1 + \alpha \widetilde { x } _ { 1 } ( s ) } - \frac { \zeta _ { 0 } \widetilde { x } _ { 1 } ( s ) } { 1 + B _ { 0 } \widetilde { x } _ { 1 } ( s ) } \right ) d s + a _ { 1 0 } \theta P \right ) ,$$

and

Subsequently;

$$\begin{cases} \frac { d x _ { 0 } ( t ) } { t } \leqslant a _ { 1 } x _ { 0 } ( t ) & , t \in ( n P , ( n + \theta ) P ] \\ \Delta x _ { 0 } ( t ) \leqslant - \frac { h _ { \max } } { a _ { 0 } + b + \epsilon } x _ { 0 } ( t ) & , t = ( n - + \theta ) P \\ \frac { d x _ { 0 } ( t ) } { t } \leqslant \frac { a _ { 0 } x _ { 0 } ( t ) } { 1 + ( \tilde { x } _ { 1 } ( t ) - \varepsilon _ { 1 } ) } - \frac { \zeta _ { 0 } ( \tilde { x } _ { 1 } ( t ) - \varepsilon _ { 1 } ) x _ { 0 } ( t ) } { 1 + A _ { 0 } ( b + \epsilon ) + B _ { 0 } ( \tilde { x } _ { 1 } ( t ) - \varepsilon _ { 1 } ) } & , t \in ( ( n + \theta ) P , ( n + 1 ) P ] \\ \Delta x _ { 0 } ( t ) = 0 & , t = ( n + 1 ) P \end{cases}$$

$$\left ( \int _ { 0 } ^ { \theta P } ( a _ { 1 1 } - 2 b _ { 1 1 } \widetilde { x } _ { 1 } ( s ) ) d s - d ( 1 - \theta ) P \right ) .$$

When the condition specified in Theorem 1. By virtue of the Floquet theorem [43], the boundary periodic solution (0,ñ1(t) ) is locally asymptotically stable.

Denote

$$\rho _ { 0 } = a _ { 1 0 } \theta P + \int _ { ( n + \theta ) P } ^ { ( n + 1 + \theta ) P } \left ( \frac { a _ { 2 0 } } { 1 + \alpha ( \widetilde { x } _ { 1 } ( s ) - \varepsilon _ { 1 } ) } - \frac { \zeta _ { 0 } ( \widetilde { x } _ { 1 } ( s ) - \varepsilon _ { 1 } ) } { 1 + A _ { 0 } ( b + \epsilon ) + B _ { 0 } ( \widetilde { x } _ { 1 } ( s ) - \varepsilon _ { 1 } ) } \right ) d s .$$

Theorem 2. The global asymptotic stability of (0,ñ1(t)) is guaranteed when conditions H1) (H2) and ( H3 hold simultaneously.

Proof.  We demonstrate the global attraction of the solution. Lemma 4 implies that for any 0, there exists noP 0 satisfying

$$x _ { 1 } ( t ) \geqslant \widetilde { x } _ { 1 } ( t ) - \varepsilon _ { 1 } , \quad \forall t > n _ { 0 } P .$$

Define b max 920 We choose €1 0 and d 0 to ensure p 1 with 0 = ePo Now, considering system (2), the following inequal
<!-- PAGE 11 -->
ity holds

$$\frac { d x _ { 0 } } { d t } \leqslant x _ { 0 } \left ( a _ { 1 0 } - b _ { 1 0 } x _ { 0 } - \frac { h _ { \max } } { \alpha _ { 0 } + b + \varepsilon _ { 1 } } \right ) .$$

Thus, we obtain the inequality

$$x _ { 0 } ( ( n + 1 + \theta ) P ^ { + } ) \leqslant \rho x _ { 0 } ( ( n + \theta ) P ^ { + } ) .$$

This implies that for any integer ko 0,

$$x _ { 0 } ( ( n _ { 1 } + k _ { 0 } + \theta ) P ) \leqslant e ^ { k _ { 0 } \rho } x _ { 0 } ( ( n _ { 1 } + \theta ) P ^ { + } ) .$$

As ko ~ +0, the right-hand side tends to 0, thus ,

$$x _ { 0 } ( t ) \rightarrow 0 \ \ a s \ \ t$$

We now prove that X1 (t) ~ ñ1(t) as t = +0. For any € 0 with 0 &lt; € &lt; there exists 0 such that for all t n1P , we have xo(t) €. n1P

From system (2), we derive the following equations:

$$\begin{cases} \frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 1 } ( t ) ) & , t \in ( n P , ( n + \theta ) P ] \\ \Delta x _ { 1 } ( t ) = - d _ { 0 } x _ { 1 } ( t ) & , t = ( n + \theta ) P \\ \frac { d x _ { 1 } ( t ) } { d t } \leq \left ( - d + \frac { c _ { 0 } \zeta _ { 0 } \varepsilon } { 1 + A _ { 0 } \varepsilon } \right ) x _ { 1 } ( t ) & , t \in ( ( n + \theta ) P , ( n + 1 ) P ] ^ { \cdot } \\ \Delta x _ { 1 } ( t ) = - d _ { 1 } x _ { 1 } ( t ) & , t = ( n + 1 ) P \end{cases} .$$

Applying the comparison theorem of impulsive differential equations [43], we arrive at the following system of equations:

$$\begin{array} { r l } & { \frac { d x _ { 3 } ( t ) } { d t } = x _ { 3 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 3 } ( t ) ) \quad , t \in ( n P , ( n + \theta ) P ] } \\ & { \Delta x _ { 3 } ( t ) = - d _ { 0 } x _ { 3 } ( t ) , \quad , t = ( n + \theta ) P } \\ & { \frac { d x _ { 3 } ( t ) } { d t } = \left ( - d + \frac { c _ { 0 } \zeta _ { 0 } \varepsilon } { 1 + A _ { 0 } \varepsilon } \right ) x _ { 3 } ( t ) \quad , t \in ( ( n + \theta ) P , ( n + 1 ) P ] ^ { \cdot } } \\ & { \Delta x _ { 3 } ( t ) = - d _ { 1 } x _ { 3 } ( t ) \quad , t = ( n + 1 ) P } \end{array}$$

Consequently, the periodic solution ñ3(t) of the above system is derived as follows:

$$\widetilde { x } _ { 3 } ( t ) = \begin{cases} \frac { a _ { 1 1 } x _ { 3 } ^ { * } e ^ { a _ { 1 1 } ( t - n P ) } } { a _ { 1 1 } + b _ { 1 1 } x _ { 3 } ^ { * } ( e ^ { a _ { 1 1 } ( t - n P ) } - 1 ) } & , t \in ( n P , ( n + \theta ) P ] \\ x _ { 3 } ^ { * * } e ^ { ( - d t + \frac { C _ { 0 } \xi _ { 0 } ^ { e } } { 1 + A _ { 0 } e } ) ( t - ( n + \theta ) P ) } & , t \in ( ( n + \theta ) P , ( n + 1 ) P ] \end{cases} .$$

where

$$\begin{cases} x _ { 3 } ^ { * } = \frac { Q a _ { 1 1 } } { b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta P } - 1 ) } & \quad a _ { 1 1 } x _ { 3 } ^ { * } e ^ { a _ { 1 1 } \theta P } \\ x _ { 3 } ^ { * * } = ( 1 - d _ { 0 } ) \frac { a _ { 1 1 } x _ { 3 } ^ { * } e ^ { a _ { 1 1 } \theta P } } { a _ { 1 1 } + b _ { 1 1 } x _ { 4 } ^ { * } ( e ^ { a _ { 1 1 } \theta P } - 1 ) } & \quad \cdot \\ \end{cases}$$

Based on the &gt; 0, there exists 0 such that when t the inequality X1 (t) &gt; ñ1(t) = €1 holds. For any €2 0, there exists t1 such that when t &gt; t1, noP noP ,

$$\widetilde { x } _ { 1 } ( t ) - \varepsilon _ { 1 } \leqslant x _ { 1 } ( t ) \leqslan
<!-- PAGE 12 -->
t \mathfrak { s l }$$

Let € = 0. Then, for large t,

$$\varepsilon _ { 1 } < x _ { 1 } ( t ) < \widetilde { x } _ { 1 } ( t ) + \varepsilon _ { 1 } ,$$

SO +0 The is complete. proof

Proving the permanence of the system, on the other hand , ensures that all populations can be maintained within a positive density range over the long term, enabling sustainable coexistence\_ This corresponds to the ideal objectives of ecosystem health and sustainable resource utilization. Together; these two aspects delineate both the safety boundaries and sustainable pathways for ecological management.

## 3.2. Permanence

Complementary to the extinction analysis, it is crucial to identify the positive conditions for sustainable management. Permanence ensures that all population densities remain positive in the term, corresponding to the desired state of sustainable resource utiliza tion. This subsection aims t0 establish the mathematical criteria for system permanence, thereby defining the safe operating space for management interventions. long

Theorem 3. Under conditions H1) and H4) , system (2) exhibits permanence.

Proof. An application of Lemma yields

$$- \varepsilon _ { 1 } \geqslant x ^ { * * } e ^ { - d ( 1 - \theta ) P } - \varepsilon _ { 1 } = c$$

Select 03 0 such that 03 min and p2 1, where

$$\rho _ { 2 } = ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } ) e ^ { ( a _ { 1 0 } - b _ { 1 0 } \omega _ { 3 } ) I P + \int _ { ( n + \theta ) P } ^ { ( n + 1 + \theta ) P } \left ( \frac { a _ { 2 0 } } { 1 + \alpha _ { 0 } ( \tilde { x } _ { 4 } ( s ) + \epsilon ) } - b _ { 2 0 } \omega _ { 3 } - \frac { \zeta _ { 0 } ( \tilde { x } _ { 4 } ( s ) + \epsilon ) } { 1 + \beta _ { 0 } ( \tilde { x } _ { 4 } ( s ) + \epsilon ) } \right ) \mathrm d s } { \alpha _ { 0 } } .$$

We now establish a uniform positive lower bound for the prey population: there exists 01 0 such that xo(t) 01 holds for all large t.

forward, our task is to prove that there exist t1 0, ensuring that xo(t1) Otherwise, for all t &gt; 0, we have Xo(t) (3, based on system (2), we can Moving gain

$$\begin{cases} \frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 1 } ( t ) ) & , t \in ( m P , ( n + \theta ) P ) \\ \Delta x _ { 1 } ( t ) = - d _ { 0 } x _ { 1 } ( t ) & , t = ( m + \theta ) P \\ \frac { d x _ { 1 } ( t ) } { d t } \leqslant \left ( - d + \frac { c _ { 0 } \zeta _ { 0 } \omega _ { 3 } } { 1 + A _ { 0 } \omega _ { 3 } } \right ) x _ { 1 } ( t ) & , t \in ( ( n + \theta ) P , ( n + 1 ) ) \\ \Delta x _ { 1 } ( t ) = - d _ { 1 } x _ { 1 } ( t ) & , t = ( m + 1 ) P \end{cases}$$

$$\begin{cases} \frac { d x _ { 4 } ( t ) } { d t } = x _ { 4 } ( t ) ( a _ { 1 1 } - b _ { 1 1 } x _ { 4 } ( t ) ) & , t \in ( n P , ( n + \theta ) P ) \\ \Delta x _ { 4 } ( t ) = - d _ { 0 } x _ { 4 } ( t ) & , t = ( n + \theta ) P \\ \frac { d x _ { 4 } ( t ) } { d t } = \left ( - d _ { 1 } + \frac { c _ { 0 } z _ { 0 } \theta _ { 3 } } { 1 + A _ { 0 } \omega _ { 3 } } \right ) x _ { 4 } ( t ) & , t \in ( ( n + \theta ) P , ( n + 1 ) P ) \\ \Delta x _ { 4 } ( t ) = - d _ { 1 } x _ { 4 } ( t ) & , t = ( n + 1 ) P \end{cases} .$$

Therefore, the periodic solution ñ4(t) of system (6) is derived as follows:

$$\w
<!-- PAGE 13 -->
idetilde { x } _ { 4 } ( t ) = \begin{cases} \frac { a _ { 1 1 } x _ { 4 } ^ { * } e ^ { a _ { 1 1 } ( t - n P ) } } { a _ { 1 1 } + b _ { 1 1 } x _ { 4 } ^ { * } ( e ^ { a _ { 1 1 } ( t - n P ) } - 1 ) } & , t \in ( n P , ( n + \theta ) P ) \\ x _ { 4 } ^ { * * } e ^ { \left ( - d + \frac { c _ { 0 } \xi _ { 0 } \omega _ { 3 } } { 1 + A _ { 0 } \omega _ { 3 } } \right ) ( t - ( n + \theta ) P ) } & , t \in ( ( n + \theta ) P , ( n + 1 ) P ) \end{cases} .$$

where

$$\begin{cases} x _ { 4 } ^ { * } = \frac { P a _ { 1 1 } } { b _ { 1 1 } ( e ^ { a _ { 1 1 } \theta P } - 1 ) } \\ x _ { 4 } ^ { * * } = ( 1 - d _ { 0 } ) \frac { } { a _ { 1 1 } } \end{cases}$$

The periodic solution 74(t) is globally asymptotically stable from Lemma 4. Therefore , according to comparison theorem of impulsive differential equations [43], for any &gt; 0, there exists a to such that for t to, X1 (t) X4 (t) ñ4(t) + e. From system (2) again; we get

$$\begin{cases} \frac { d x _ { 0 } } { d t } \geqslant x _ { 0 } ( t ) ( a _ { 1 0 } - b _ { 1 0 } \omega _ { 3 } ) & , t \in ( n P , ( n + \theta ) P ) \\ \Delta x _ { 0 } \geqslant - \frac { h _ { m a x } } { a _ { 0 } } x _ { 0 } & , t = ( n + \theta ) P \\ \frac { d x _ { 0 } } { d t } \geqslant x _ { 0 } \left ( \frac { a _ { 2 0 } } { 1 + a ( \tilde { x } _ { 4 } ( t ) + \varepsilon ) } - b _ { 2 0 } \omega _ { 3 } - \frac { \zeta _ { 0 } ( \tilde { x } _ { 4 } ( t ) + \varepsilon ) } { 1 + B _ { 0 } ( \tilde { x } _ { 4 } ( t ) + \varepsilon ) } \right ) & , t \in ( ( n + \theta ) P , ( n + 1 ) P ) \end{cases}$$

Then xo( (n +1 + P)P+) fore, xo((n1 + k1 + 0)P) k1p2' xo((n1 + 0)P+) +0 as k1 +0, which implies xo(t) +0 as 4 +0, which is contradiction. Thus there exists a t1 0 such that Xo(t1) &gt; 03.

If xo(t) 03 for all t &gt; t1, then our objective is achieved. We therefore consider only those solutions whose trajectories leave and later re-enter the region defined by R = {x € R2 Xo = {xo(t) 03} Then xo(t) 03 for t € [t1, t* ) . inftzt1

Case A: with t* (n2 + 0)P. Select natural numbers n3, n4 € Nsuch that

$$\rho _ { 3 } = \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) ^ { n _ { 3 } } e ^ { n _ { 3 } \delta _ { 3 } P } \rho _ { 2 } ^ { n _ { 4 } } >$$

with the conditions 61 = 010 b1ow3 &lt; 0, 82 @20 b2ow3 0, and 1+b2oJi 0. Let 83 = max {81,82} and P1 (n3 + n4)P . Then there exists t2 € [t* ,t* + P1] such that xo(t2) If instead xo(t) Equation (6) holds. That is, for sufficiently t, we have large

$$\zeta \, x _ { 4 } ( t ) \, \leqslant$$

Furthermore, Equation holds on the interval [t* + n3P,t* + P1]. Therefore,

$$x _ { 0 } ( ( n _ { 2 } + n _ { 3 } + n _ { 4 } + \theta ) P ^ { + } ) \geqslant \rho _ { 2 } ^ { n }$$

From system (2), we obtain the following:

$$\begin{cases} \frac { d x _ { 0 } } { d t } \geqslant x _ { 0 } ( t ) \delta _ { 3 } & , t \neq ( n + \theta ) P \\ \Delta x _ { 0 } \geqslant - \frac { h \max } { \alpha _ { 0 } } x _ { 0 } & , t = ( n + \theta ) P \end{cases}$$

On the interval [t* ,t* + n3P], integrate the system (8), we have

$$x _ { 0 } ( ( n _ { 2 } + n _ { 3 } + \theta ) P ^ { + } ) \geqslant \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) ^ { n _ { 3 } } x _ { 0 } ( ( n _ { 2 }$$

In conclusi
<!-- PAGE 14 -->
on; the following inequality can obtain

$$x _ { 0 } ( ( n _ { 2 } + n _ { 3 } + n _ { 4 } + \theta ) P ^ { + } ) \geq \rho _ { 2 } ^ { n _ { 4 } } \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) ^ { n _ { 3 } } x _ { 0 } ( ( n _ { 2 } + \theta ) P ^ { + } ) e ^ { n _ { 3 } \delta _ { 3 } P } = \rho _ { 3 } \omega _ { 3 } > \omega _ { 3 } ,$$

Let {xo(t) W3, then, by integrating (8) on interval [t* , tx ) , we xo(t) 1 e(n2+n3)83P = (1. For t tì , the same Qo t1 (3. inftzt* hmax gain

Case B(a): For all t € we have Xo(t) W3Following the approach in Case A, there exists t2 € [(n2 + 0 + 1)P, (n2 + n3 + n4 + 1 + 0)P] such that xo(t2) 2 This is omitted here. Define t2 03} For any t € (t* ,t2 ) , we have xo(t) Integrating Equation (8) over (t* ,t2) gives xo(t) &gt; xo(t*) (1 \_ "max proof (u3.

Case B: t* # (n2 + 0)P . Assume t* ((n2 + 0)P, (n2 + 0 + 1)P] The following analysis presents possible outcomes in this scenario.

Case B(b): There exists t0 Define t3 = {xo(t) 03} Then for all t € (t*,t3), we have xo(t) Integrating Equation (8) over the interval (t* ,t3) yields xo(t) = W3, the same argument applies for t t3. Therefore, xo(t) W1 for all t &gt; t1. This completes the proof. inftzt

## 4. Numerical Simulation and Discussion

This section employs numerical simulations to achieve three progressive the first is to visually validate the theoretical results of Section 3, demonstrating both extinction and permanence scenarios (Figures 1 and 2). In Figure 1, panels (a) (b) and (c) illustrate the prey population's decay to zero, the predator' s convergence to a periodic oscillation, and the phase portrait converging to the boundary solution (0,ñ1(t) ) , respectively; thereby visually confirming Theorem 2. Conversely, Figure 2 shows sustained oscillations of both populations , confirming Theorem 2 The second aim is to identify the management levers by quantifying the influence of major parameters on the extinction threshold condition Ro through sensitivity analysis (Figures 3-5). Figure 3 (the PRCC plot) ranks parameter sensitivity; while Figures 4 and 5 illustrate two-parameter interactions, demonstrating how P, and d1 jointly modulate Ro. The third aim is to explore complex dynamics bethe stable regimes , revealing potential risks (e-g-, chaotic fluctuations) that may arise from suboptimal management, thereby extending the theoretical findings to more realistic contexts (Figures 6-13). Figures 6-13 systematically reveal bifurcations, period-doubling cascades, chaotic transitions, and the coexistence of attractors as parameters (P, Q, d1) are varied, providing a dynamical map of potential management outcomes. goals: key hmax' yond key hmax'

First, to validate the global stability condition in Theorem 2, we select parameters satisfying (H1), (H2) , and H3) . The following numerical simulations, conducted using MATLAB R2O24a, validate the established theoretical results. The parameter values used in our model are 010 2 0.6, b1o 0.8,011 2 0.25, 0.76, do 2 0.11, 020 0.4, b2o 0.2, &amp; = 0.05, Bo = 1,d = 0.25, co 0.85, d1 0.11, P = 2,0 = 0.25. The calculations yield the following values: hmax

$$H _ { 1 } = ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \th
<!-- PAGE 15 -->
eta ) P } = 2 . 4 3 9 8 > 1 ,$$

$$( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P - 2 \ln \frac { a _ { 1 1 } + b _ { 1 1 } x ^ { * } ( e ^ { a _ { 1 1 } \theta F _ { - 1 } } - 1 ) } { a _ { 1 1 } } } = 0 . 9 3 3 8 < 1 ,$$

$$H _ { 3 } = \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } + b } \right ) \exp ( a _ { 1 0 } \theta P + d ( 1 - \theta ) P + \mathbf M ) = 0 . 2 3 2 7 < 1 .$$

and

These results satisfy the conditions of Theorem 2 We therefore conclude that the periodic solution (0,ñ1(t)) of system (2) is globally asymptotically stable (see Figure 1)

As shown in Figure 1, when the parameters satisfy the conditions of Theorem 2 the system exhibits typical prey-extinction dynamics. Specifically, Figure 1a shows that the prey population x0(t) rapidly decays to zero. Meanwhile, Figure 1b demonstrates that the predator population x1 (t) tends toward a stable periodic oscillation; this behavior is manifested in the phase portrait in Figure Ic as the system trajectory converges to the boundary periodic solution (0,ñ1(t)). When the parameters satisfy the conditions of Theorem 2, the system trajectory converges to the boundary periodic solution (0,ñ1(t) ) , the prey population goes extinct while the predator population exhibits periodic fluctuations. This numerically verifies the theoretically derived extinction threshold. From a management perspective  this state simulates the ecological scenario where, after the collapse of the target fish resource, predation pressure though at a low level\_still recurs periodically due to the existence of migratory sources, thereby highlighting the extreme importance of maintaining the fish population above the extinction threshold. ie

Figure 1. This figure validates the global asymptotic stability of the prey-extinction periodic solution (0,ñ1(t)) as stated in Theorem 2 Panel (a) shows the time series of the prey population xo(t) , which rapidly decays to zero, confirming prey extinction. Panel (b) displays the time series of the predator population x1 (t) , which converges to a stable periodic oscillation; this oscillation is driven by the predator's intrinsic growth during migration-free periods and mortality during migration, as described by subsystem (3). Panel (c) presents the phase portrait, where the trajectory converges to the boundary periodic solution (0,ñ1(t) ) , visually confirming the stability of the prey extinct state: The basic parameters are a10 0.6, b1o 0.8,011 = 3, b11 0.25, 0.76, do 0.11, 020 0.4, b2o 0.8, Ao 0.05, Bo 1,d = 0.25, Co 0.85, d1 0.11, P = 2,0 = 0.25 system hmax 0.2,

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000003_38cf962ef6045be4b8df1baaa3bafa89e42660c3c26db706bfaaaee59c0ba81d.png)

Next, to demonstrate the permanence condition in Theorem 3, a different parameter set is used. Setting the model parameters as a10 0.8, b1o 2 0.15, 0.9, b11 0.27, 0.9, do 0.5, b2o 0.22, &amp; 0.9, Ço = 0.4, Ao 0.04, Bo 0.3,d = 0.2, co 0.1,d1 0.27, P = 3, 0 0.35, then 011 hmax

$$H _ { 1 } = ( 1 - d _ { 0 } ) ( 1 - d _ { 1 } ) e ^ { a _ { 1 1 } \theta P - d ( 1 - \theta ) P } = 1 . 4 2 8 4 > 1 ,$$

$$H _ { 4 } = \left ( 
<!-- PAGE 16 -->
1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) \exp ( a _ { 1 0 } \theta P + d ( 1 - \theta ) P + M ^ { \prime } ) = 5 3 2 9 8 > 1 ,$$

and which implies that Theorem 3 is satisfied; therefore, system (2) is permanent (see Figure 2)

To systematically rank the impact of parameters on the extinction threshold Ro, we perform PRCC (Partial Rank Correlation Coefficient) analysis.  This leads us to determine key

$$R _ { 0 } = \left ( 1 - \frac { h _ { \max } } { \alpha _ { 0 } } \right ) e$$

Figure 2 This figure demonstrates the permanence of system (2) as established in Theorem 3 Panel (a) shows the time series of the prey population xo(t) , which persists at positive levels with oscillations. Panel (b) shows the corresponding predator population x1 (t) also persisting with oscillations. Panel (c) displays the phase portrait in which the trajectory remains bounded within a positive region of the state space, confirming the long-term coexistence of both populations. The basic parameters are 010 0.8, b1o 0.15, 011 0.9,b11 = 0.27 , 0.9,do 0.13,020 0.5, b2o 0.22, &amp; 0.4, Ao 0.04, Bo = 0.3,d = 0.2, co 0.1,d1 0.27, P = 3, and 0 0.35. hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000004_8a43e95d1b0cf0b95e9145eb82ca3929defb0091fb16c392273a10fed4e1ff3f.png)

Predator fear levels toward prey a, predator migration mortality rate d1, prey capture amount period P, and the inter-predator interference coefficient Bo are selected as research parameters. To thoroughly explore the interactions among parameters and their combined effects on the system's threshold condition Ro, we conduct a systematic sensitivity analysis of P , hmax, d1, and Bo in this section: The PRCC values between each parameter and the prey extinction condition Ro are calculated to evaluate their sensitivity: In this process, the LHS (Latin Hypercube Sampling) method is used to estimate the PRCC values, thereby accurately identifying the parameters that play a decisive role in the prey extinction threshold condition Ro [44] pulse hmax, key

Figure 3. The PRCCs of the parameters (a , d1, hmax, P, Bo) for the prey extinction threshold 5, b1o = 0.5, 011 2, b11 0.5, 6 =4, b2o 0.1, d1 0.2, P = 3 and 0 0.1. key hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000005_db5262c1810c28333995ab8992c25b509aaf9da1c74fc72dde7057335c125839.png)

As observed in Figure 3, the period P and the predator interference coefficient Bo are positively correlated with the prey extinction threshold condition Ro. It has been Or Bo raises Ro, which in turn contributes to an increase in prey density   Conversely, prey fear level &amp;, predator migration mortality d1, and maximum prey harvest hmax show negative correlations with Ro. An increase in these parameters decreases Ro  which ultimately reduces prey density  Further PRCC results indicate that the parameters d1, P, and Bo all demonstrate substantial correlation pulse hmax'

strengths, with absolute values exceeding 0.4. This demonstrates that these four parameters significantly influence Ro, thus serving as ke
<!-- PAGE 17 -->
y regulators of prey population density From a biological perspective, elevated predator migration mortality d1 initially leads to temporary decline in predator abundance: This reduction in density-dependent stress subsequently increases reproductive success and juvenile survival; ultimately triggering a compensatory population surge in the following The reinvasion of these recovered predators into prey habitats consequently drives prey population suppression through intensified predation pressure: year.

Figure 4. The importance of predator migration mortality rate d1, prey capture amount and impulsive P on the threshold condition Ro. (a) Effect of predator migration mortality rate d1 and impulsive period P on Ro with hmax 5.9 (b) Effect of prey capture amount and impulsive P on Ro with d1 0.9 hmax' period hmax period

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000006_39093e3f2a394d78e9d6ae30a982c6c2bcdc2dc213342bd31f157daeaa410f5c.png)

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000007_6146cae582f4180b9507dece2fe88c0beecd5cc0fa1f5316d68e5c738eebdc09.png)

As shown in Figure 4, the impulsive P , maximum prey harvest amount and predator migration mortality rate d1 strongly influence the threshold condition A higher impulsive period P leads to a higher Ro. A higher predator migration mortality rate d1 also increases Ro. In contrast; a lower maximum prey harvest amount decreases Ro. Therefore, harvesting prey less frequently helps to maintain a larger prey population. The two-parameter analysis (Figure 4) demonstrates that the positive effect of the P on Ro is more pronounced at low d1 or high This finding suggests that the frequency of management interventions (P) is of particular importance in contexts characterized by low predator migration mortality or intense pressure: period hmax' hmax pulse period hmax tuning fishing

Figure 5 reveals that increasing the predator interference coefficient Bo significantly mitigates top-down control on prey populations. The magnitude of this effect is strongly modulated by predator migration mortality d1, with minimal mortality leading to maximal prey survival benefits. Ecological interpretation suggests that low d1 maintains robust predator populations wherein interference competition Bo becomes particularly effective at reducing per-capita predation rates. This parameter interaction creates a novel ecological scenario where prey thrive most when predator populations experience both low migration mortality and strong intra-specific interference, highlighting non-linear dependencies in food web regulation. The one-parameter analysis (Figure 5) and its interaction trend with d1 demonstrate that the regulatory role of predator intraspecific interference Bo in population dynamics is highly dependent on the intrinsic pressure of the predator population (as indicated by d1), uncovering the nonlinear nature of top-down control processes. The sensitivity and two-parameter analyses collectively demonstrate that the effects of management levers P, d1) are rarely independent
<!-- PAGE 18 -->
. Their interactions can amplify or mitigate each other's impact on the extinction threshold Ro, underscoring the necessity for integrated , multi-parameter management strategies rather than isolated adjustments of single factor. key (e.g hmax'

Figure 5. Parameter dependence of the threshold condition Ro  Setting the model parameters as 5, b1o 0.5, =2, b11 = 0.5, = 6,do 4, b2o = 0.2, &amp; 0.3, Ço 0.1, Ao 0.5,d = 0.2, co 0.1, P = 3,0 = 0.1. hmax 010 011

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000008_1a1018386fb296ba25c2689e30a2ec2039c855cabe23ef6299635743610561bf.png)

we explore the complex dynamical behaviors that can emerge outside the stability regimes, taking the pulse Pas a representative example. We proceed to analyze several significant parameters governing the behavioral dynamics of system (2). The following analysis focuses on the role of the impulse Pin governing the dynamics of system (2). Setting the parameters as 0.5, b1o 0.1, 011 0.3, b11 0.3, 0.2, Qo = 0.5, do 0.15, 020 3, b2o 0.5, 3.5, Ao = 0.2, Bo = 0.3, d 0.1, Co = 0.3, d1 = 0.15, and 0 = 0.3, we can derive the bifurcation diagrams of predator-prey model (2) with a bifurcation parameter P from 0.01 to 15. Finally period period hmax 010

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000009_046c166eb6221e6ce89b1bd73cc8e88e4645855e765b874d75f0095976c7219a.png)

Figure 6. Bifurcation diagrams of system (2) with 0 P 15. (a) Bifurcation diagram of xo(t) 0.5, b1o 0.1, 0.3, b11 = 0.3, 0.5, do 3, b2o 0.1, Ço = 3.5, Ao 0.2, Bo 0.3, d = 0.1, Co = 0.3, d1 = 0.15, and 0 0.3 011 hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000010_a241d50dd510a31614e8e25015fe3d24c867025278268c8a38c659610a282b73.png)

Figure 6 illustrates the complex bifurcation scenario of system (2) under varying impulsive periods P. An increase in P triggers a classical route to chaos through successive period-doubling bifurcations, followed by a reverse sequence of period-halving (inverse period-doubling) bifurcations that restore system order:. This complete bifurcation cascade demonstrates the fundamental role of the impulsive period in regulating system dynamics between order and chaos. Notably, chaos emerges in the system when P increases to approximately 12.8 (Figure 8a); as P further rises to 15, the system reverts to a stable P-periodic solution via inverse period-doubling bifurcation. This indicates that there exists a 'chaotic window' for the interval of management (P), where an inappropriate interval may lead to unpredictable drastic fluctuations in population size: Supplementary Figures 7 and 8 provide concrete examples of the characteristic behaviors observed during these transitions , numerically verifying the theoretical predictions. pulses

Figure 7. A period-doubling cascade transitions the from a P-periodic solution to a 4P-periodic solution.  (a) Phase portrait of P-periodic solution when P = 4. (b) Phase portrait of 2P-periodic solution when P = 8. (c) Phase po
<!-- PAGE 19 -->
rtrait of 4P-periodic solution when P = 9.6. (d) Phase portrait of chaos when P 12 system

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000011_5840c7a173361f71f8fff65c3f63fc070ef9ea5eddc41361187035aa49adc145.png)

Figure 8. Period-halving bifurcation reduces the to a P-periodic solution. (a) Phase portrait exhibiting chaotic behavior when P = 12.8. (b) Phase portrait of the 4P-periodic solution when P 13.5. (c) Phase portrait of the 2P-periodic solution when P 14.5. (d) Phase portrait of the P-periodic solution when P = 15. system

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000012_45b212935b11d1cbc2b0379dcdcb6d15be0ccc0dea0d81df4fa381dd585af614.png)

Next; we investigate the influence harvesting ability of the prey for (2) Set the parameters of system (2) as a10 = 0.4, b1o 0.1, 011 = 0.25, 0.9, do = 2.8, b2o = 0.15, &amp; 2.5, Ao 0.2, Bo 1, d 0.1, Co = 0.32, hmax system b11

d1 = 0.1, P = 1, 0 = 0.2, with xo(0) = 0.6, X1 (0) = 0.4. Figure 9 shows the bifurcation diagrams of system (2) based on the bifurcation parameter 0. hmax

Figure 9. Bifurcation diagrams of system (2) with the maximum harvest amount as the bifur cation parameter (for 0.01 1). (a) Bifurcation diagram of xo(t) for bifurcation parameter 0.01 (b) Bifurcation diagram of x1 (t) for bifurcation parameter 0.01 Set the parameters of system (2) as 0.4, b1o = 0.1, 011 0.25, b11 0.9, do = 0.1, 020 2.8, b2o 0.15, &amp; 0.2, Ço = 2.5, Ao = 0.2, Bo = 1,d = 0.1,co = 0.32,d1 = hmax hmax hmax: 010

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000013_cb1a66bd6bdcb4c59e6cd02e0575ab8d7d13fe71d715376fd2810457fb052b1f.png)

As shown in the bifurcation diagram; the maximum amplitude of system dynamics remains relatively stable. Figure 10 shows that with the increase in intensity hmax, the system undergoes an abrupt transition from a P-periodic solution to chaotic behavior; which represents the occurrence of a crisis-induced chaotic transition. Specifically; when exceeds the critical value (~0.6), the system completely loses stability, ultimately This result provides a dynamical basis for setting the 'maximum allowable catch" in management. fishing hmax key fishery

Figure 10. System (2) suddenly changes from a P-periodic solution to chaos. (a) Phase portrait of P-periodic solution when 0.5. (b) Phase portrait of chaos when 0.7 hmax hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000014_a05ee672dceb8b0b37138c902ccdd20bd01f4cb1b7e1dc556b81e945fbb58188.png)

Suppose the parameters of system (2) are a10 5, b1o 0.1, 0.5, b11 0.1, 0.1, Qo 0.5, do 0.08, a20 = 2, b2o 0.5, Ço = 5, Ao 0.01, Bo 1, d 0.1, Co = 0.5,d1 0.15, P = 15,0 = 0.2 Bifurcation diagrams of system (2) are computed for parameter &amp; in the range [0.01, 15] (see Figure 11). Figure 11 shows that different attractors will coexist for the same fear level alpha. Figure 12 demonstrates that strange attractors coexist w
<!-- PAGE 20 -->
ith a 4P-periodic solution at &amp; = 3.72. 011 hmax

Figure 11. Bifurcation diagram of system (2) with fear level &amp; as the bifurcation parameter: (a) Bifurcation diagram of xo(t). (b) Bifurcation diagram of x1 (t). Suppose the parameters of (2) are 010 5, b1o = 0.1,011 = 0.5, b11 = 0.1, 0.1, Q0 0.5, do 0.08, 020 2, b2o 0.5, Ço = 5, Ao 0.01, Bo = 1,d = 0.1, co 0.5,d1 0.15, P = 15, and 0 = 0.2 system hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000015_8487407e200c75a53dd54725e82dc57c81226c186b1dd1a3d9584af00bc4cde8.png)

12

Figure 12 When œ = 3.72, the 4P-periodic solution and P-periodic solution coexist:. (a) Time series of x1 (t) with (xo(0),X1 (0) (0.6,0.4)) (b) The solution with (xo(0),x1 (0) (0.6,0.4)) tends to = (2,2)). (d) The solution with Xo(0) = 2,x1 (0) = 2 tends to a 4P-periodic solution.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000016_922e3c28288addd4a24787f76eeb3fba7995c711605cc29cbfd3f60d022463b8.png)

= 1, 0.2, 0.1, b11 = 0.1, = 0.5, do 0.1, 020 = 2, b2o = 0.01, &amp; 1, Ço 2, Ao = 0.2, Bo = 0.3, d = 0.1, co = 0.1, P = 1, and 0 =0.1. We obtained the bifurcation diagram of system (2) with respect to the bifurcation parameter d1 ranging from 0.01 to 1 (see Figure 13). Figure 13 shows that as the predator migration mortality rate d1 increases , the system transition from chaos to a P-periodic solution. b1o hmax 011 will

Figure 13. Bifurcation diagrams of (2) with the predator migration mortality rate d1 as the bifurcation parameter (for 0.01 d1 1). (a) Bifurcation diagram of xo(t) for the bifurcation parameter d1. (b) Bifurcation diagram of x1 (t) for the bifurcation parameter d1. Set the model parameters as 010 1, b1o 0.2, 011 = b11 0.1, 0.5, do = 0.1, 020 = 2, b2o = 0.3,d = 0.1, co 0.1, P = 1,and 0 =0.1. system 0.1, hmax

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\axioms-15-00032-v3\axioms-15-00032-v3_output_artifacts\image_000017_320afdb02b0ed732b85bdbbb8f7d8af70ed9f2d861187edc5f2a0a62eab91745.png)

When the mortality rate of predators , denoted by d1, is minimal, predators exert a substantial influence on their prey: The population dynamics of both species demonstrate chaotic behaviour. When the value of d1 exceeds the critical value of approximately 0.47 , significant proportion of predators The growth rate of prey populations increases exponentially before stabilising, a phenomenon that can be attributed to a significant decrease in predation pressure: A decline in population numbers or even extinction is often the consequence of excessively high mortality rates perish.

In summary, the exploration beyond stable regimes reveals that the system can exhibit rich dynamics , including periodic doubling, chaos, and the coexistence of attractors, par ticularly when parameters like the P , harvesting intensity or fear level &amp; exceed certain ranges. These findings provide crucial additional insights: (1) delineate "danger zones" in parameter space where management outcomes become highly unpredictable or sensitive to initial conditions. (2) Th
<!-- PAGE 21 -->
e presence of chaotic or high-periodic oscillations implies that even in the absence of extinction; populations may undergo severe tive management must consider not only the extinction threshold but also the broader dynamical landscape to avoid inadvertently pushing the system into a volatile, though persistent; state: period key7 pulse hmax, They

From management perspective; the discovery of complex dynamical behaviors bifurcations and chaos) carries significant implications. It indicates that within specific parameter regions , the long-term evolutionary behavior of the system is highly sensitive to initial conditions and parameter perturbations , which significantly increases the difficulty and potential risks of practical management. Therefore, in the practice of fishery resource management; efforts should be made to avoid setting system parameters within these "sensitive regions" to reduce the unpredictability of population dynamics. (e.g

## 5. Conclusions

This study formulates a predator-prey model with a Beddington-DeAngelis functional response that incorporates prey fear; large-scale predator migration; and impulsive density dependent nonlinear harvesting: Through theoretical analysis and numerical simulations, it provides theoretical support for sustainable resource management. The main contributions of this work are threefold: first, we theoretically derive explicit extinction and permanence thresholds (Theorems 1-3), which provide mathematically rigorous boundaries for sustainable harvesting: Second, through systematic numerical exploration (Figures 1-13), we

identify and quantify the parameters (P, d1, Bo, &amp;) that govern system dynamics , highlighting their interactions and nonlinear effects. Third, we uncover complex dynamical regimes (bifurcations, chaos) that emerge outside stability boundaries , revealing previously unrecognized risks in fishery management: These findings collectively advance the field of impulsive bioeconomic modeling by integrating multiple ecological mechanisms (fear; migration; nonlinear harvesting) and by providing both theoretical benchmarks and practi cal insights for adaptive management. Specifically; the results suggest that management strategies should simultaneously regulate harvesting intensity (hmax), timing (P), and con sider predator migration mortality (d1) to maintain populations within safe dynamical regimes , thereby preventing both extinction and economically destabilizing fluctuations. The results demonstrate that the scientific and coordinated regulation of the maximum harvesting intensity hmax and the management intervention frequency period P is the pathway to steering the system towards permanence and avoiding the risk of prey extinction. Here, establishes the foundation for an adaptive harvesting strategy based on population density; while P serves as a crucial temporal lever for balancing short-term economic benefits with long-term ecological stability: Future management practices should strive to integrate this theoretical framework with field monitoring data to develop more precise and sustainable harvesting strategies. key hmax, pulse key hmax fishery

We first prove the uniform boundedness of all solutions. Subsequ
<!-- PAGE 22 -->
ently; we establish the local and global asymptotic stability conditions for the prey-extinction periodic solution (0,ñ1 (t) ) , derive the criteria for system permanence, and determine the precise threshold condition for prey extinction. Second, numerical simulations were conducted. These not only confirmed the validity of the theoretical results but also identified the core influencing factors.  Specifically, sensitivity analysis revealed four parameters. The prey extinction threshold condition is primarily governed by four critical parameters: the predator migration mortality rate d1, the maximum prey capture amount the period P and the inter-predator interference coefficient Bo. A two-parameter sensitivity analysis demonstrated that both the period P and interference coefficient Bo are positively correlated with this threshold . Consequently, increasing either parameter strengthens the threshold condition; thereby enhancing the likelihood of prey population persistence. The predator migration mortality rate d1 and maximum prey capture amount hmax showed a negative correlation with the prey extinction threshold Ro. Increases in these parameters pushed the prey population closer to extinction. These results suggest that extending the period P and strengthening predator interference Bo can improve prey survival chances. In contrast, high predator migration mortality d1 or increased prey capture will markedly elevate extinction risk. Therefore, management strategies should maintain appropriate intervals and mitigate predator interference while avoiding excessive migration mortality and overharvesting   Finally, this study analyzed four parameters including fear level 4 , predator migration mortality rate d1, maximum prey capture amount and period P. These parameters significantly influenced the system state, with the period P a particularly strong effect. A suitable value of P could stabilize the population dynamics of both prey and predators. In addition; through systematic parameter interaction analysis, we found that the effect of the period P is closely correlated with predator mortality d1 and intensity which underscores the necessity of integrated management strategies. Exploration of the dynamics outside the stability domain revealed the existence of bifurcation and chaotic behaviors in the system, alerting us to the risk that inappropriate management may trigger unpredictable drastic fluctuations in populations. In summary, these results provide reliable theoretical support for fishery management:. offer guidance for scientifically regulating effort, key hmax' pulse pulse pulse hmax pulse key pulse hmax' pulse having pulse fishing hmax' They fishing

## References

- 1 Hicks, C.; Cohen, P; Graham, N. Harnessing global fisheries to tackle micronutrient deficiencies. Nature 2019, 574, 95-98 [CrossRef] [PubMed]
- 2 Global food insecurity and famine from reduced crop, marine fishery and livestock production due to climate disruption from nuclear war soot injection. Nat. Food 2022, 3, 586-596. [CrossRef]
- 3 R; et al. Expanding ocean food production under climate change: Nature 2022, 605, 490-496. [CrossRef]
- 4 Science 2024, 385, 860-865. [CrossRef]
- 5 Rethinking sustainability of
<!-- PAGE 23 -->
 marine fisheries for a fast-changing planet:. npj Ocean Sustain: 2024, 3,41. [CrossRef]
- 6 Dänhardt, J ; Lindström,  . Optimal departure decisions of songbirds from an experimental stopover site and the significance of weather Anim. Behav. 2001, 62, 235-243. [CrossRef]
- 7 Gu, Z.; Dixon, A.; Zhan, X. Genetics and evolution of bird migration. Annu. Rev. Anim. Biosci. 2024, 12, 21-43. [CrossRef]
8. Dingle, H.; Drake, VA. What Is Migration? BioScience 2007, 57,113-121. [CrossRef]

protecting biodiversity, preventing overfishing, and ensuring the sustainable supply of fishery resources.

Building on these limitations, many meaningful questions remain for future research For example, how can we determine the pulse control period P to achieve an appropriate balance between harvesting yield and ecological risk? If we consider stage structure in predators or prey, what kind of dynamic behavior will the system exhibit? If stochastic variability is introduced into capture intensity, migration loss, or fear responses , and additional mechanisms such as adaptive fear responses or cooperative hunting are incorporated, what kind of dynamic behavior will the system exhibit? Meanwhile, the current model primarily considers the impact of the fear effect on the prey population. In reality, the fear effect may also significantly influence predator behavior and functional response param eters. Investigating how fear shapes predator foraging strategies remains a meaningful direction for future research optimal

It should be emphasized that all of the above conclusions are derived under several simplifying assumptions, including deterministic impulsive harvesting, a fixed predator gration mortality rate, and a time-invariant representation of the prey fear response: These assumptions make it possible to obtain explicit extinction thresholds, stability domains, and bifurcation structures , but they inevitably restrict the range of dynamical behaviours that the model can capture: In real ecosystems, stochastic fluctuations in harvesting effort; migration losses, or behavioural responses may strongly interact with nonlinear functional responses and impulsive effects, thereby shifting extinction thresholds , modifying system robustness, and generating richer short-term dynamics such as noise-induced oscillations, transient nence and bifurcation results obtained here should be interpreted as baseline predictions for systems in which environmental and management variability are moderate, and caution is required when extrapolating these findings to strongly stochastic settings. mi-

Author   Contributions: Conceptualization, Writ authors have read and agreed to the published version of the manuscript:.

Funding: This work is supported by National Natural Science Foundation of China (No. 12261018), Graduate Program of Guizhou University of Finance and Economics, China (No. 2025BAZYSY198).

Data Availability Statement: No new data were created or analyzed in this study.

Conflicts of Interest: The authors declare no conflict of interest

- 9 Österblom, H; et al. Seabird-induced natural mortality of fish varies with fish abundance: Evidence from five ecosystems Fish Fish. 2021, 22, 262-279. [CrossRef] forage
- 10 B
<!-- PAGE 24 -->
oström, MK; Lunneryd, S.-G.; Karlsson; L.; Ragnarsson, B. Cormorant impact on trout Salmo trutta) and salmon (Salmo salar) migrating from the river Dalälven emerging in the Baltic Sea Fish. Res. 2009, 98, 16-21. [CrossRef]
11. 213-227. [CrossRef]
12. Food and Agriculture Organization of the United Nations. The State of World Fisheries and Aquaculture 2022: Towards Blue Transformation; FAO: Rome, Italy, 2022. [CrossRef]
- 13 G.J; et al. switching and consumption by seabirds in the central California Current upwelling ecosystem: Implications for forage fish management. J.Mar. Syst. 2018, 185, 25-39. [CrossRef] Prey
14. Xiao, Y; Chen, L. Modeling and analysis of a predator-prey model with disease in the prey:  Math. Biosci. 2001, 171, 59-82. [CrossRef] [PubMed]
15. Liu, B.; Zhang, Y; Chen, L\_ The dynamical behaviors of a Lotka-Volterra predator-prey model concerning integrated pest management Nonlinear Anal. Real World Appl. 2005, 6, 227-243. [CrossRef]
17. Jiao, J.; Quan, Q ; Dai, X. Dynamics of a new impulsive predator-prey model with predator population seasonally large-scale migration. Appl. Math. Lett. 2022, 132, 108096. [CrossRef]
16. an impulsive mathematical model. AIMS Math. 2022, 7, 1-24. [CrossRef] using
18. Jiao, J ; Xiao, Y; Jiao, H. Dynamics of a switched predator-prey breeding management model with impulsive nonlinear releasing and age-selective harvesting predator: Adv. Contin: Discret. Model. 2025, 2025, 101. [CrossRef]
20. Zhou, Z; Jiao, J ; Dai, X; Wu, L. Dynamics of a Predator-Prey System with Impulsive Stocking and Nonlinear Harvesting Predator at Different Moments. Mathematics 2024, 12, 2369. [CrossRef] Prey
19. Quan, Q. Dynamics of pest-nature enemy model for IPM with repeatedly releasing natural enemy and impulsively spraying pesticides. Adv: Contin. Discret. Model. 2025, 2025, 52. [CrossRef]
- 21 . M; Jiao, J. Dynamics of a predator-prey fishery model with birth pulse, impulsive releasing and harvesting on prey: J. Appl. Math. Comput. 2024, 70, 3011-3031. [CrossRef] Wang'
- 23 Zhao, T.; S. Impulsive harvesting and by-catch mortality for the theta logistic model.  Appl. Math.  Comput.  2011, 217, 9412-9423. [CrossRef] Tang
22. Liu, Y; Guo, L.; Liu, X. Dynamical Behaviors in a Stage-Structured Model with a Birth Pulse: Mathematics 2023, 11,3321. [CrossRef]
24. Li, C. D; X.; Liu, M. Complex dynamics of a nonlinear impulsive control predator-prey model with Leslie-Gower and B-D functional response: AIMS Math. 2024, 9, 14454-14472. [CrossRef] Cheng Feng
26. H;Xu, H; Fu, J. Dynamic analysis of a phytoplankton-fish model with the impulsive feedback control depending on the fish density and its changing rate. Math. Biosci. 2023, 20, 8103-8123. [CrossRef] [PubMed] Cheng' Eng;
25. Li, C.; S. Analyzing a generalized pest-natural enemy model with nonlinear impulsive control. Open Math. 2018, 16, 1390-1411. [CrossRef] Tang'
- 27 . Follana-Berná, G.; Arechavala-Lopez, P; Ramirez-Romero, E.; Koleva, E.; Grau, A.; Palmer; M Mesoscale assessment of sedentary coastal fish density using vertical underwater cameras Fish. Res. 2022, 253, 106362. [CrossRef]
28. young-of-year brown trout (Salmo trutta) in a boreal river in northern Sweden. Fish. Manag: Ecol. 2023, 31, e12658. [CrossRef
<!-- PAGE 25 -->
] large
30. Zhang, H; Georgescu, P; Chen, L. On the impulsive controllability and bifurcation of a predator-pest model of IPM. Biosystems 2008, 93, 151-171. [CrossRef]
29. Lamberg, A.; Imsland, AKD. Using Merged Pre-Fishery Abundance as a Parameter Evaluating the Status of Atlantic Salmon and Anadromous Brown Trout Populations: A Norwegian Case Study. Fishes 2022, 7, 264. [CrossRef]
31. Zhou, Z.; Quan, Q ; Jiao, J ; Dai, X. Bifurcation dynamics of a predator-prey model with impulsive density-dependent nonlinear pesticide spraying and predator release\_
32. free-living wildlife reduces population growth over generations Proc . Natl. Acad. Sci. USA 2022, 119,e2112404119. [CrossRef]
- 33 predator-induced stress on the global metabolism of an ungulate prey using fecal metabolomic fingerprinting: Sci. 2021, 11, 6129. [CrossRef] [PubMed] Rep.
34. and reproduction: J. Anim: Ecol. 2016, 85, 507-515. [CrossRef] [PubMed]

35. changes in the brains and behaviour of wild animals. Sci. 2019, 9, 11474. [CrossRef] [PubMed] Rep.
36. Kolecek, J ; Reif, J.; Sálek, M; Hanzelka, J ; Sottas, C.; Kubelka, V. Global population trends in shorebirds: Migratory behaviour makes species at risk. Sci. Nat. 2021, 108, 9. [CrossRef]
3. 37 . response of rainbow trout (Oncorhynchus mykiss) myotubes challenged with Piscirickettsia salmonis. Vet. Immunol.  Immunopathol. 2021, 237, 110240. [CrossRef]
38. Tabata, YA.de Oliveira, C.; Takahashi, N.S.; Hattori, RS. Early warming stress on rainbow trout juveniles impairs male reproduction but contrastingly elicits intergenerational thermotolerance: Sci. 2021, 11, 17053. [CrossRef] Rep.
39. Barton, B.A.; Iwama; G.K. Physiological changes in fish stress in aquaculture with emphasis on the response effects of corticosteroids. Annu. Rev. Fish Dis. 1991, 1, 3-26. [CrossRef] from and
40. air-water interface
41. Escaping Perceived predation risk affects migratory propensity: Biol. Lett. 2015, 11, 20150466. [CrossRef] peril:
8. 43 Lakshmikantham, V; Bainov, D.D.; Simeonov, PS. of Impulsive Differential Equations; World Scientific: Singapore, 1989. Theory
42. Courbin, N.; Pichegru, L.; Seakamela, M; Makhado, A.; Meÿer, M; Kotze, PG.; Mc Cue, S.A.; Péron; C. Seascapes of fear and competition shape regional seabird movement ecology: Commun. Biol. 2022, 5, 208. [CrossRef]
44. Liu, B.; BL; Tao, FM; Hu, G. Modelling the Effects of Pest Control with Development of Pesticide Resistance: Acta Math: Appl. Sin. Engl. Ser. 2021, 37, 109-125. [CrossRef] Kang'
11. 46 Tian, Y; Tang, S.; Cheke, RA. Dynamic complexity of predator-prey model for IPM with nonlinear impulsive control incorporating a regulatory factor for predator releases. Math. Model. Anal. 2019, 24, 134-154. [CrossRef]
45. C.J ; Kirschner; D.E. methodology for performing global uncertainty and sensitivity analysis in systems J. Theor. Biol. 2008, 254, 178-196. [CrossRef] [PubMed] Ray,

DisclaimerlPublisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and /or the editor(s) . MDPI and /or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content:.