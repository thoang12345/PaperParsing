

{0}------------------------------------------------

## **HYBRID POWERTRAIN OPTIMIZATION FOR REGIONAL AIRCRAFT INTEGRATING HYDROGEN FUEL CELLS AND ALUMINUM AIR BATTERIES**

**Harshal Kaushik<sup>1</sup> , Ali Mahboub Rad<sup>1</sup> , Korebami Adebajo<sup>2</sup> , Sobhan Badakhshan<sup>1</sup> , Nathaniel Cooper<sup>2</sup> , Austin Downey<sup>2</sup> , Jie Zhang1**,<sup>∗</sup>

<sup>1</sup>University of Texas at Dallas, Richardson, TX

<sup>2</sup>University of South Carolina, Columbia, SC

### **ABSTRACT**

*With the increasing demand for air travel and the urgency to reduce emissions, transitioning from fossil fuel-based propulsion systems is a critical step toward sustainable aviation. While batteries are widely used in urban air mobility, their long charging durations limit their feasibility for consecutive flights. Hybrid propulsion systems, which integrate fuel cells and batteries, offer a promising alternative due to their higher energy density and improved efficiency. This paper presents a novel hybrid powertrain architecture for regional aircraft, incorporating a hydrogen fuel cell, a lithium-ion battery, and an auxiliary aluminum-air battery. The proposed system is evaluated using real-world power demand data from a Cessna 208 aircraft. The hydrogen fuel cell acts as the primary power source, ensuring continuous operation, while the lithium-ion battery manages transient power fluctuations to enhance system stability. The aluminum-air battery is introduced as a high-energy emergency backup, providing extended endurance during critical situations. A mixed-integer optimization model is formulated for system sizing and power scheduling, ensuring optimal energy distribution among the power sources. Multiple operational scenarios are analyzed to evaluate system performance, particularly under emergency conditions, where power reliability is crucial. The results highlight the feasibility and effectiveness of the proposed hybrid architecture in improving energy efficiency and flight safety for regional aircraft applications.*

**Keywords:** Hybrid-electric aircraft propulsion; Mixedinteger programming; Hydrogen fuel cell; Lithium-ion battery; Aluminum-air battery.

# **1. INTRODUCTION**

The shift toward sustainable, dependable energy sources is paramount in tackling global environmental challenges and mitigating climate change. The transportation sector significantly contributes to greenhouse gas emissions, accounting for roughly 2.5% of global emissions; within this sector, aviation alone is responsible for nearly 12% of transportation-related emissions, as reported in [\[1\]](#page-6-0). As air travel demand continues to rise, adopting cleaner and more efficient energy alternatives is vital to minimizing aviation's environmental footprint and ensuring long-term sustainability.

Hydrogen has emerged as a promising alternative to fossil fuels in aviation, primarily due to its high gravimetric energy density. Research into hydrogen-based aviation has been ongoing for more than five decades, highlighting its potential as a cleaner energy carrier [\[2\]](#page-6-1). Among hydrogen technologies, fuel cells stand out for their high efficiency, minimal noise, and zero harmful emissions, producing only water vapor [\[3\]](#page-6-2). However, as noted by Jarry et al. [\[4\]](#page-6-3), fuel cell systems face notable challenges such as slower dynamic response, limited power density, and accelerated aging, which hinder their standalone implementation in aviation.

Lithium-ion (Li-ion) batteries offer rapid response times, enhanced operational flexibility under dynamic conditions, and higher power density. However, their lower gravimetric energy density can compromise weight efficiency and reduce an aircraft's payload capacity [\[5\]](#page-6-4). Numerous studies have examined all-electric battery-powered aircraft, with most focusing on shortrange commuter flights due to battery energy density limitations. The study conducted by [\[6\]](#page-6-5) highlights power constraints as a major challenge, emphasizing payload reductions for short-term viability and the need for battery advancements for long-term feasibility. Similarly, Bærheim et al. [\[7\]](#page-6-6) explore battery-electric aviation for regional flights up to 400 km, finding that while new aircraft designs meet operational needs, retrofitted models require improved battery energy density. In addition, Ebersberger et al. [\[8\]](#page-6-7) assess an all-electric propulsion system for small commuter aircraft, analyzing power distribution, battery technologies, and energy storage while addressing efficiency, reliability, and safety considerations.

\*Corresponding author: jiezhang@utdallas.edu

{1}------------------------------------------------

Fuel cell-battery hybridization, integrating both fuel cell and battery technologies into in a single power system has emerged as a promising approach to leverage their strengths while mitigating their weaknesses [\[9\]](#page-6-8).However, hybridization introduces challenges in energy management and sizing methodologies. As discussed in [\[10\]](#page-6-9), these challenges can be formulated as an optimization problem, with sizing strategies and predictive algorithms ensuring seamless power allocation under varying operational conditions.

Energy management and sizing optimization of fuel cellbattery hybrid-powered aircraft have received extensive research. For instance, Donateo et al. [\[9\]](#page-6-8) investigate the retrofitting of ultralight aircraft with a fuel cell, lithium battery, and hydrogen storage system, optimizing hybridization ratios and comparing charge-depleting and charge-sustaining modes to assess their impact on fuel cell performance and hydrogen consumption. A refined sizing approach for fuel cell-battery hybrid systems is presented in [\[11\]](#page-6-10), introducing a weight estimation model and conducting sensitivity analyses to determine the optimal power balance for enhanced aircraft performance. The study by Lei et al. [\[12\]](#page-6-11) classifies energy management strategies into rule-based, intelligent-based, and optimization-based approaches, evaluating their efficiency and feasibility while analyzing trade-offs between fuel cells, batteries, and ultra-capacitors for unmanned aerial vehicle applications. Later in [\[13\]](#page-6-12), a comprehensive mathematical model has been formulated to optimize fuel cell performance across different scales, highlighting the importance of balancing hydrogen storage and electrochemical efficiency to enhance system reliability. Additionally, Hoenicke et al. [\[14\]](#page-6-13) introduce a novel Power Management module to optimize energy distribution in hybrid propulsion, ensuring efficient fuel cell operation during cruise and battery support during high-power phases such as takeoff. Furthermore, this module integrates passive and active charging strategies to reduce battery size, improve reliability, and enhance overall safety.

Emergency energy reserves remain a challenge for hybrid fuel cell–battery systems because Li-ion batteries add significant weight when used solely for reserve capacity, and hydrogen-based systems do not scale effectively for this purpose. Consequently, increasing reserve capacity often encroaches upon the already limited usable range of these aircraft. In addition to hydrogen and battery-based hybrid solutions, alternative energy resources are now being explored for aviation and broader transportation applications. Among these, Aluminum–air (Al-air) batteries have garnered attention due to their high energy density, lightweight design, and long duration power supply capabilities. Their ability to deliver reliable emergency power makes them especially suitable for main energy source failures or divergence missions, where extended flight time or safe landing requires additional power. As noted in [\[15\]](#page-7-0), Al-air batteries offer significant weight savings and a higher theoretical energy density compared to Liion batteries, rendering them an appealing option for auxiliary aviation use. Furthermore, aluminum is approximately 4050 times more abundant than lithium in the Earth's crust [\[16\]](#page-7-1), suggesting a more sustainable and widely available resource for energy storage. Nonetheless, issues such as anode corrosion, hydrogen evolution side reactions, and electrolyte degradation can compromise efficiency and lifespan. Moreover, as pointed out in [\[17\]](#page-7-2), the non-rechargeable nature of Al-air batteries necessitates anode and electrolyte replacement, limiting their practicality for continuous operation in primary energy applications. Despite these drawbacks, ongoing advancements in battery management, material engineering, and electrolyte optimization have the potential to bolster their viability for backup power and emergency energy support in aviation [\[18\]](#page-7-3). However, only a few studies have investigated energy management and sizing optimization for Al–air–powered aircraft. One such study [\[19\]](#page-7-4) examines the design and optimization of short-range, Al–air–powered aircraft for regional transport, analyzing weight, operating costs, and performance trade-offs. Recognizing that Al–air batteries offer high specific energy but low power output, the authors propose hybridizing them with Li-ion batteries to overcome power constraints and improve operational feasibility.

This paper extends the optimization model proposed in [\[13,](#page-6-12) [14\]](#page-6-13) by incorporating aluminum air battery as an emergency backup power source and optimizing for sizing and energy management. We investigate this integration and assess aircraft performance in critical scenarios. Our key contributions are outlined as follows:

- We formulate a mixed-integer programming (MIP) model for optimal system sizing and power management, ensuring efficient energy distribution and hybridization ratio optimization.
- We introduce the integration of an aluminum-air battery within a hybrid powertrain consisting of a hydrogen fuel cell and a Li-ion battery. The aluminum-air battery serves as a backup power source, ensuring continued operation in the event of a fuel cell failure or providing additional power during unexpected scenarios such as rerouting or operational challenges.
- We derive the power curves for the Cessna 208 based on real-time flight data provided by pilots. Utilizing these power profiles, we design three distinct scenarios: normal operation, reduced hydrogen availability, and flight diversion. Each scenario is analyzed to ensure the aircraft can safely complete its mission and land securely.

The remainder of the paper is structured as follows. Section [2](#page-1-0) presents the MIP formulation for system sizing, optimal power management, and hybridization ratio. Section [3](#page-3-0) gives the experimental set up and Section [4](#page-4-0) explores numerical case studies, detailing different experiments and analyzing the corresponding results. Finally, the paper concludes with a discussion of key findings in Section [5.](#page-6-14)

#### <span id="page-1-0"></span>**2. MATHEMATICAL MODEL**

In this section, we explain the proposed mixed-integer programming model for optimal sizing and power management.

## **2.1. Objective Function**

The objective of this study is to optimize the size of the hybrid powertrain to minimize costs while ensuring that the aircraft's 

{2}------------------------------------------------

weight constraints are not exceeded. The analysis is based on the weight and volume constraints of the Cessna 208, which will be discussed in detail later in Section 3. Considering the removal of the original Pratt and Whitney PT6A-114A turboprop engine and the existing fuel storage, the available weight allocation for the fuel cell and battery system is estimated at 1200 kg. This serves as a key design constraint, defining the maximum allowable weight for integrating the hybrid power system.

Next, we define the design variables, which represent the energy requirements for the flight. The objective is to determine the optimal sizing of the hydrogen tank (L), fuel cell capacity (kWh), Li-ion battery capacity (kWh), and aluminum-air battery capacity (kWh). These variables are denoted as ��H, ��fc, ��Li, and ��Al, respectively. The first component of objective function is formulated as the minimization of the total weight of all hydrogen storage and power generation components. Thus, the optimization problem aims to minimize the following:

$$C_H^{\text{wt}} V_H + C_{\text{FC}}^{\text{wt}} E_{\text{fc}} + C_{\text{Li}}^{\text{wt}} E_{\text{Li}} + C_{\text{Al}}^{\text{wt}} E_{\text{Al}}, \quad (1)$$

where the weight coefficients are finalized for batteries and fuel cell and listed in TABLE [1.](#page-2-0)

<span id="page-2-0"></span>**TABLE 1: WEIGHT COEFFICIENT VALUES**

|              | $C_H^{\text{wt}}$<br>(kg/L) | $C_f^{\text{wt}}$<br>(kg/kWh) | $C_{Li}^{\text{wt}}$<br>(kg/kWh) | $C_{Al}^{\text{wt}}$<br>(kg/kWh) |
|--------------|-----------------------------|-------------------------------|----------------------------------|----------------------------------|
| <b>Value</b> | 1/11000                     | 1.5                           | 4                                | 0.1234                           |

A second component of objective function is designed to collectively minimize the power expenditure of both the fuel cell and the batteries at every time instance ��. The goal is to ensure that power consumption is minimized while meeting all operational constraints, thus maximizing the system's overall efficiency. Following is the second part of the objective function, where we seek to minimize the total power expenditure for both the fuel cell and the batteries across all time instances, formulated as:

$$\sum_{t \in T} P_{\text{fc}}^t + P_{\text{Li}}^t + P_{\text{Al}}^t. \quad (2)$$

While the power demand profile is indeed a fixed input derived from real flight data and must be fully satisfied at every time step (enforced by the power balance constraint Equation [\(4\)](#page-2-1)), we include the power supplied by the fuel cell, lithium-ion battery, and aluminum-air battery in the objective function to enable optimal energy management. This formulation allows the model to strategically allocate power among the available sources, selecting combinations that not only satisfy demand but also minimize fuel consumption and enhance overall system efficiency. This integrated objective supports the design of a hybrid powertrain that is both energy-efficient and operationally sustainable.

#### **2.2. Weight Constraints**

Next, we introduce the constraint sets, beginning with the weight constraint. This constraint ensures that the total weight of the combined power generation components and the hydrogen tank remains within the allowable weight limit. The hybrid energy system in the Cessna 208 is set to have the maximum allowable weight of 1200 kg.

$$C_H^{\text{wt}} V_H + C_{\text{FC}}^{\text{wt}} E_{\text{fc}} + C_{\text{Li}}^{\text{wt}} E_{\text{Li}} + C_{\text{Al}}^{\text{wt}} E_{\text{Al}} \leq 1200, \quad (3)$$

where the weight coefficients are mentioned earlier in TABLE [1.](#page-2-0) As we described earlier, even though the objective function aims to minimize the total weight of the proposed hybrid powertrain, we explicitly include this maximum weight constraint to ensure compatibility with the baseline configuration of the Cessna 208, which is originally powered by a Pratt & Whitney PT6A-114A turboprop engine. This constraint ensures that our replacement powertrain of hydrogen fuel cell and battery does not exceed the weight capacity allocated to the original propulsion system, thereby preserving the aircraft's structural integrity, center-ofgravity limits, and aerodynamic balance. As the Cessna 208 airframe and performance characteristics are tightly coupled with its existing powertrain weight, our design prioritizes a modular retrofit without making significant modifications to the aircraft body. The weight constraint thus serves as a critical boundary condition, enforcing feasibility within the physical and regulatory limits of the original airframe.

#### **2.3. Power Demand Satisfaction Constraint**

This constraint focuses on scheduling the power distribution to ensure that load requirements are met at every time instance while preventing any power generation unit, including the fuel cell and Li-ion battery, from being overloaded. The fuel cell and Li-ion battery serve as the primary hybrid power sources, whereas the aluminum-air battery functions as a reserved power supply, utilized only in emergency scenarios. The decision variables for this stage are �� t fc, �� t Li, and �� t Al, representing the power generated by the fuel cell, Li-ion battery, and aluminum-air battery at each time instance ��, respectively. The total flight duration is denoted as ��, which, for simplicity, represents the set of all discretized time steps ranging from 0 to the end of the flight.

We begin by formulating the constraint that ensures the total power demand is met by the available power sources, namely the fuel cell, Li-ion battery, and aluminum-air battery. Mathematically, this condition can be expressed as follows:

<span id="page-2-1"></span>
$$P_{\text{fc}}^t + P_{\text{Li}}^t + P_{\text{Al}}^t = P_{\text{dem}}^t, \quad \forall t \in T, \quad (4)$$

where �� �� dem is the demand at an instant ��. The power demand data for the Cessna 208 has been gathered from the fuel flowdata provided by the pilots. By incorporating all these instances, we ensure that the power output sufficiently meets the load requirements under normal operating conditions. For exceptional extreme scenarios, a detailed discussion is provided later to assess and guarantee that the aircraft possesses adequate energy reserves for safe landings.

## **2.4. Fuel Cell Constraints**

The third set of constraints ensures that the available hydrogen supply is adequate to sustain the fuel cell's energy requirements throughout the entire flight duration.

$$V_H \ \eta_{\text{fc}} \ H_{\text{LHV}} \ H_{\text{mass}} \geq E_{\text{fc}}, \quad (5)$$

{3}------------------------------------------------

where ���� �� is the efficiency of fuel cell, ��LHV is the lowest heating value of hydrogen, and ��mass is the mass to volume ratio for hydrogen. Values for these are mentioned in TABLE [2.](#page-3-1)

**TABLE 2: HYDROGEN FUEL CELL PROPERTIES**

<span id="page-3-1"></span>

|              | <b>Coefficient</b> | $\eta_{fc}$ | $H_{LHV}$<br>(kWh/kg) | $H_{mass}$<br>(kg/L) |
|--------------|--------------------|-------------|-----------------------|----------------------|
| <b>Value</b> |                    | 0.55        | 33.33                 | 0.09                 |

Next, we impose a constraint on the ramp rate of the fuel cell. We assume that there is a ramp rate limiting the change in the fuel cell's power output from �� ��1 fc to �� ��2 fc . For the current scenario, we assume that within the time interval Δ��, the fuel cell can increase its power by 0.1��fc. This can be formulated as:

$$P_{\text{fc}}^{t_1} - P_{\text{fc}}^{t_2} \leq 0.1 E_{\text{fc}}, \quad \forall t_1, t_2 \in T, \quad (6)$$

where ��<sup>1</sup> and ��<sup>2</sup> represent consecutive time instances within ��.

## **2.5. Battery Constraint**

The state of charge (SOC) constraint on the Li-ion battery ensures that the battery's energy levels are properly tracked throughout the flight. This constraint is essential for maintaining energy balance and preventing over-discharge or overcharging, which could compromise the performance and longevity of the battery. Mathematically, it enforces that the energy stored in the battery at any time step ��<sup>1</sup> is equal to the energy available at a subsequent time step ��2, adjusted for the power drawn from the battery over that interval.

$$SOC_{Li}^{t_i} E_{Li} = SOC_{Li}^{t_2} E_{Li} - P_{Li}^{t_1} \Delta t, \quad \forall t_1, t_2 \in T. \quad (7)$$

Here, �� ��1 Li represents the power supplied by the Li-ion battery at time ��1, whileΔ�� accounts for the duration over which this power is drawn. Similarly, the SOC equation for the aluminum-air battery is formulated in the same manner, establishing a relationship between ��������<sup>1</sup> Al, ��Al, and �� ��1 Al. This ensures that the aluminum-air battery's energy dynamics are accurately represented, enabling its role as an auxiliary power source during critical flight scenarios.

We enforce the battery charge/discharge rate constraints implicitly by adopting a 1C rate limit for both the lithium-ion and aluminum-air batteries. Technically, a 1C rate implies that a battery can be fully charged or discharged within one hour. This constraint ensures that the battery's power output or input at any time stays within its nominal capacity. The proposed methodology is compactly illustrated in the flowchart shown in Fig. [1.](#page-3-2)

### <span id="page-3-0"></span>**3. EXPERIMENTAL SET-UP**

In this section we introduce the selected aircraft (Cessna 208) followed by a detailed discussion of the power curves, including the methodology used to obtain them.

## **3.1. Aircraft Specifications**

We utilize power curves derived from the Cessna 208 aircraft for a Columbia South Carolina, USA to Richmond North Carolina, USA flight, which has an approximate duration of 130 minutes [\[20\]](#page-7-5). Our objective is to power the same aircraft with a

![](_page_3_Diagram_15.jpeg)

<span id="page-3-2"></span>**FIGURE 1: THE PROPOSED ALGORITHM FOR OPTIMAL SIZ-ING AND POWER MANAGEMENT.**

zero-emission propulsion system using a hydrogen fuel cell and batteries while maintaining its aerodynamic performance, shape, size, and weight characteristics. To achieve this, we replace the conventional engine and fuel system with a hydrogen fuel cell and a combination of Li-ion and aluminum-air batteries, ensuring that the fundamental aircraft design remains unchanged.

The Cessna 208 has a fuel capacity of approximately 1000 kg and an engine (PT6A-114A) weighing around 200 kg. By eliminating these components, we allocate a total of 1200 kg to integrate the fuel cell, hydrogen storage, Li-ion battery, and aluminum-air battery required to sustain the entire flight. The fuel cell serves as the primary power source due to its high power density, efficiently driving the propeller. However, since fuel cells struggle with dynamic load variations, a Li-ion battery is incorporated to handle transient power demands. Additionally, an aluminum-air battery is included as an emergency energy source, ensuring sufficient power for a safe landing at the nearest airport in the event of a fuel cell failure. The precise capacities of all components will be determined through the experiments, explained next.

### **3.2. Power Curves**

Multiple power curves have been obtained for the Columbiato-Richmond flight, specifically for a conventionally powered Cessna 208 aircraft, illustrated in Fig. [2.](#page-4-1) These power curves capture various flight phases, including takeoff, climb, cruise, descent, and taxi. To facilitate optimized power system sizing and scheduling, we consider an average power curve that represents the overall power demand throughout the flight.

Information on the power curves for various flights was obtained from fuel flow data recorded and provided by aircraft pilots. This data, sourced from Flightdata [\[21\]](#page-7-6), was converted to power used by the engine. The specific energy of the fuel commonly used in piston-powered aircraft was used to calculate the energy produced from the fuel consumed. By factoring in the engine's efficiency at different points in time, this energy was then converted into usable power for the aircraft. During taxi, cruise, and descent, efficiency was assumed to be 30%, while during takeoff, it was assumed to be 19%, as these engines are typically less efficient at high power demands, such as during takeoff.

{4}------------------------------------------------

![](_page_4_Figure_0.jpeg)

<span id="page-4-1"></span>**FIGURE 2: CESSNA 208 POWER PROFILES FROM COLUMBIA TO RICHMOND.**

Due to the dynamic power variations during takeoff and climb, batteries play a crucial role in meeting the high transient power demands during these phases. Once the power requirement stabilizes during cruise, the fuel cell becomes the primary power source, while the battery usage is adjusted accordingly. The Li-ion battery is utilized to smooth out power fluctuations, ensuring stable operation, whereas the aluminum-air battery primarily serves as a backup energy source for safety, providing emergency power in the event of unexpected failures.

In the following subsections, we conduct experiments to analyze the aircraft powertrain's response under varying flight conditions and determine the required component sizing. Three experimental case studies are considered: the first examines a configuration utilizing only hydrogen and Li-ion batteries; the second evaluates powertrain performance under low hydrogen volume conditions; and the third investigates the aircraft's ability to execute a safe landing while accounting for rerouting requirements.

#### <span id="page-4-0"></span>**4. NUMERICAL EXPERIMENTS AND RESULTS**

In this section, we present the simulation experiments conducted using a real aircraft dataset as well as outline the experimental setup and discuss results.

#### **4.1. Experiment 1: Li-ion Battery Handling the Power Demand Fluctuations**

![](_page_4_Figure_8.jpeg)

<span id="page-4-2"></span>**FIGURE 3: SIMULATION RESULTS OF EXPERIMENT 1**

produced with a combination of a hydrogen fuel cell and a Li-ion battery. The fuel cell serves as the primary power source, supplying the majority of the power demand, particularly during the climb and cruise phases, where power requirements remain relatively stable. Minor perturbations in power demand are efficiently managed by the battery during those phases. Fig. [3\(](#page-4-2)a) illustrates the power output ratio between the fuel cell and the battery. During takeoff, there is a significant surge in power demand, which is primarily handled by the Li-ion battery. During the descent phase, power requirements are minimal and are efficiently met through the combined operation of the fuel cell and the battery. It is important to note that the fuel cell's deceleration response is relatively slow; therefore, any excess power generated is utilized to recharge the battery. Additionally, Fig. [3\(](#page-4-2)b) depicts the depletion of hydrogen storage over time, while Fig. [3\(](#page-4-2)c) presents the state of charge (SOC) of the battery throughout the flight. Table [3](#page-5-0) presents the sizing results for the fuel cell, hydrogen storage vessel, and Li-ion battery.

#### **4.2. Experiment 2: Aluminum-air Battery Activation at Low Hydrogen Levels**

{5}------------------------------------------------

<span id="page-5-0"></span>**TABLE 3: SIZING CONFIGURATIONS FOR HYBRID ENERGY SYSTEM COMPONENTS**

|            | Experiment | Fuel Cell capacity (kWh) | Li-ion Battery capacity (kWh) | Aluminum-air battery capacity | Hydrogen (kWh) volume (L) | Powertrain weight (kg) |
|------------|------------|--------------------------|-------------------------------|-------------------------------|---------------------------|------------------------|
| Experiment | 1          | 458                      | 100                           | 0                             | 320                       | 1200                   |
| Experiment | 2          | 480                      | 80                            | 450                           | 370                       | 1142                   |
| Experiment | 3          | 480                      | 80                            | 450                           | 370                       | 1142                   |

![](_page_5_Figure_2.jpeg)

![](_page_5_Figure_3.jpeg)

![](_page_5_Figure_4.jpeg)

<span id="page-5-1"></span>**FIGURE 4: SIMULATION RESULTS OF EXPERIMENT 2**

![](_page_5_Figure_6.jpeg)

![](_page_5_Figure_7.jpeg)

![](_page_5_Figure_8.jpeg)

risk to the flight. The key question addressed is how to ensure a safe flight continuation in such a situation. This is where the aluminum-air battery plays a crucial role. For this experiment, we assume that a safe hydrogen volume threshold is greater than 10% of the total capacity (the aluminum-air battery is triggered below 100 L here in Figs. [4](#page-5-1) and [5](#page-5-2) for better illustration).

As in the previous case, power is initially supplied through a combination of a hydrogen fuel cell and a Li-ion battery. The fuel cell serves as the primary power source during the climb and cruise phases, where power demands remain relatively stable, while minor fluctuations are managed by the Li-ion battery.

However, once the hydrogen volume drops below 10% of the tank capacity, the aluminum-air battery is activated, and the fuel cell is shut down. At this stage, the aluminum-air battery becomes

<span id="page-5-2"></span>**FIGURE 5: SIMULATION RESULTS OF EXPERIMENT 3**

the primary power source, ensuring flight continuation and a safe landing. Furthermore, Fig. [4\(](#page-5-1)b) illustrates the depletion of hydrogen storage over time, while Fig. [4\(](#page-5-1)c) presents the SOC of the Li-ion battery throughout the flight. Table [3](#page-5-0) presents the sizing results for the fuel cell, hydrogen storage vessel, Li-ion battery, and aluminum-air battery.

## **4.3. Experiment 3: Flight Rerouting Analysis**

In this third experiment, our primary objective is to analyze the flight behavior in the event of a rerouting scenario. There are situations where the aircraft may need to execute a go-around maneuver and return for landing due to missed approach, low visibility, or adverse environmental conditions.

As in the previous cases, the takeoff, climb, and cruise phases

{6}------------------------------------------------

are powered by the combined operation of the fuel cell and the Li-ion battery, as shown in Fig. [5\(](#page-5-2)a). However, during rerouting, the aircraft descends with lower hydrogen reserves, and the aluminum-air battery is activated to meet the additional energy demands required for the diversion. The aluminum-air battery is capable of sustaining this extra operation efficiently. Furthermore, Fig. [5\(](#page-5-2)b) illustrates the depletion of hydrogen storage over time, while Fig. [5\(](#page-5-2)c) presents the SOC of the Li-ion battery throughout the flight.

#### **4.4. Optimal Sizing Results**

The sizing outcomes for the fuel cell, hydrogen storage vessel, Li-ion battery, and aluminum-air battery are summarized in Table [3.](#page-5-0) These results represent the optimum quantity of lithium ion battery energy, fuel cell energy, hydrogen volume, and aluminium air battery energy required to complete the flight in the emergency situations. These quantities are selected by obeying the weight constraints, sizing constraints, and operational constraints.

#### <span id="page-6-14"></span>**5. CONCLUSION**

<span id="page-6-7"></span>A comprehensive analysis of a hybrid powertrain for a regional aircraft, i.e., the Cessna 208, integrating a hydrogen fuel cell, a Li-ion battery, and an aluminum-air battery is performed to enhance operational resilience. A mixed-integer programming model is formulated for optimal system sizing and power management, ensuring efficient energy distribution and hybridization optimization. Through the use of real-world flight data, we evaluate power demands under various scenarios, including nominal operation, reduced hydrogen availability, and flight diversion. Findings highlight the critical role of the aluminum-air battery in ensuring flight safety during emergency conditions, particularly in cases of fuel cell failure or unexpected rerouting. This study provides valuable insights into powertrain sizing and scheduling, with plans to expand the dataset by incorporating additional flight profiles for enhanced robustness.

<span id="page-6-9"></span><span id="page-6-8"></span>Potential future work will involve developing a stochastic sizing model incorporating diverse origin-destination datasets to enhance hybrid-electric propulsion for regional aircraft.

### **ACKNOWLEDGMENTS**

<span id="page-6-11"></span><span id="page-6-10"></span>This material is based in part upon work supported by the Air Force Office of Scientific Research (AFOSR) through award no. FA9550-21-1-0083. This work is also partly supported by the National Science Foundation (NSF) grant number 2237696. This project is also partially supported by the University of South Carolina Office of Undergraduate Research through the Magellan Scholar Program. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation, the United States Air Force, or the University of South Carolina.

#### **REFERENCES**

<span id="page-6-13"></span><span id="page-6-12"></span><span id="page-6-0"></span>[1] M. Sparano, M. Sorrentino, G. Troiano, G. Cerino, G. Piscopo, M. Basaglia, and C. Pianese, "The future technological potential of hydrogen fuel cell systems for aviation and

<span id="page-6-6"></span><span id="page-6-5"></span><span id="page-6-4"></span><span id="page-6-3"></span><span id="page-6-2"></span><span id="page-6-1"></span>preliminary co-design of a hybrid regional aircraft powertrain through a mathematical tool," *Energy Conversion and Management*, vol. 281, p. 116822, 2023. [2] T. Kadyk, C. Winnefeld, R. Hanke-Rauschenbach, and U. Krewer, "Analysis and design of fuel cell systems for aviation," *Energies*, vol. 11, no. 2, p. 375, 2018. [3] A. V. Geliev, I. O. Kiselev, V. S. Zakharchenko, I. O. Kiselev, and D. I. Zhuravlev, "Conceptual design of an electric propulsion system based on fuel cells for an ultralight manned aircraft," in *2019 IEEE Conference*. IEEE, 2019. [4] T. Jarry, F. Lacressonnière, A. Jaafar, C. Turpin, and M. Scohy, "Optimal sizing of a passive hybridization fuel cell – battery," in *Proc. of the International Conference on Electrical, Computer and Energy Technologies (ICECET)*. Cape Town, South Africa: IEEE, 2021. [5] S. Li, C. Gu, M. Xu, J. Li, P. Zhao, and S. Cheng, "Optimal power system design and energy management for more electric aircrafts," *Journal of Power Sources*, vol. 512, p. 230473, 2021. [6] M. A. Anker, C. Hartmann, and J. K. Nøland, "Feasibility of battery-powered all-electric propulsion for short-haul commuter aircraft," *IEEE Access*, vol. 13, pp. 32 260–32 275, 2025. [7] T. Bærheim, J. J. Lamb, J. K. Nøland, and O. S. Burheim, "Potential and limitations of battery-powered all-electric regional flights—a norwegian case study," *IEEE Transactions on Transportation Electrification*, vol. 9, no. 1, pp. 1809– 1825, 2023. [8] J. Ebersberger, L. Fauth, R. Keuter, Y. Cao, Y. Freund, R. Hanke-Rauschenbach, B. Ponick, A. Mertens, and J. Friebe, "Power distribution and propulsion system for an all-electric short-range commuter aircraft – a case study," *IEEE Access*, vol. 10, pp. 12–34, 2022. [9] T. Donateo, A. Ficarella, and L. Lecce, "Retrofitting of ultralight aircraft with a fuel cell power system," *European Transport Studies*, vol. 1, p. 100002, 2024. [10] T. Donateo and H. Çınar, "Conceptual design and sizing optimization based on minimum energy consumption of lift-cruise type evtol aircraft powered by battery and fuel cell for urban air mobility," *Journal of Physics: Conference Series*, vol. 2385, p. 012072, 2022. [11] J. Park, D. Lee, D. Lim, and K. Yee, "A refined sizing method of fuel cell-battery hybrid system for evtol aircraft," *Applied Energy*, vol. 328, p. 120160, 2022. [12] T. Lei, Z. Yang, Z. Lin, and X. Zhang, "State of art on energy management strategy for hybrid-powered unmanned aerial vehicle," *Chinese Journal of Aeronautics*, vol. 32, no. 6, pp. 1488–1503, 2019. [13] M. C. Massaro, S. Pramotton, P. Marocco, A. H. A. Monteverde, and M. Santarelli, "Optimal design of a hydrogenpowered fuel cell system for aircraft applications," *Energy Conversion and Management*, vol. 306, p. 118266, 2024. [14] P. Hoenicke, D. Ghosh, A. Muhandes, S. Bhattacharya, C. Bauer, J. Kallo, and C. Willich, "Power management control and delivery module for a hybrid electric aircraft using fuel cell and battery," *Energy Conversion and Management*, vol. 244, p. 114445, 2021.

{7}------------------------------------------------

- <span id="page-7-0"></span>[15] S. Yang and H. Knickle, "Design and analysis of aluminum/air battery system for electric vehicles," *Journal of Power Sources*, vol. 112, pp. 162–173, 2002. [16] Y. Xue, J. Yuan, X. Yu, S. Sun, H. Zhang, W. Zhou, J. Zhang, and Y. Xia, "Air-breathing cathode for aluminum–air battery: From architecture to fabrication and evaluation," *Materials Science & Engineering R*, vol. 163, p. 100942, 2025. [17] Y. Chen, Y. Liu, W. Du, Q. Li, H. Wang, Q. Li, Q. Wu, and
- <span id="page-7-6"></span><span id="page-7-5"></span><span id="page-7-4"></span><span id="page-7-3"></span><span id="page-7-2"></span><span id="page-7-1"></span>G. Qin, "Identification of the parameters of the aluminumair battery with regard to temperature," *Journal of Energy Storage*, vol. 88, p. 111397, 2024. [18] C. S. Pawlak, E. A. Lory, and P. J. Ansell, "Aluminum-air batteries for aircraft applications," in *AIAA SciTech Forum*, 2025. [19] J. M. Vegh and J. J. Alonso, "Design and optimization of short-range aluminum-air powered aircraft," in *54th AIAA Aerospace Sciences Meeting*. San Diego, California, USA: American Institute of Aeronautics and Astronautics, 2016. [20] ARTS Laboratory, "Realistic southeastern flight operations data," 2024. [Online]. Available: [https://github.com/ARTS-Laboratory/](https://github.com/ARTS-Laboratory/Realistic-Southeastern-Flight-Operations-Data/tree/main) [Realistic-Southeastern-Flight-Operations-Data/tree/main](https://github.com/ARTS-Laboratory/Realistic-Southeastern-Flight-Operations-Data/tree/main) [21] Flight Data Systems, "Flight data systems – aviation data solutions," 2024. [Online]. Available: [https:](https://www.flightdata.com/) [//www.flightdata.com/](https://www.flightdata.com/)