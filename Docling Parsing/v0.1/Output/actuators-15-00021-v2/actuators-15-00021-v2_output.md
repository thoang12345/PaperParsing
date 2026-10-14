
<!-- PAGE 1 -->
![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000000_a5006b3f62a9ecae0827d004d62bc7ec8fccedfb5a61669a05096cbcc32c9319.png)

Article

## Bionic Design Based on McKibben Muscles and Elbow Flexion and Extension Assist Device

Hong Jiang Qingyi Zeng, Yang Jiang, Zihao Zuo and Yanhong Peng of Mechanical Engineering, Chongqing University of Technology, Chongqing 400054, China Correspondence: yhpeng@nagoya-u jp College ~

## Abstract

The increasing aging population and the rise in sports injuries have led to greater demand for elbow function rehabilitation and daily assistance. To address the limitations of tradi tional rigid rehabilitation aids and existing flexible assistive systems, this paper designs a wearable elbow-assist robot that arranges pneumatic muscles based on the distribution of human elbow muscles. By integrating bionic experimental research, and mathematical modeling, the proposed approach determines the optimal scheme through comparative experiments on material structures and provides supporting data; while the mathematical model describes the force characteristics of the pneumatic muscles. Final experiments verify that the system can effectively assist elbow movement and significantly enhance flexion torque: design,

Keywords: McKibben pneumatic muscle; wearable elbow-assist robot; bionic contraction ratio; versatility design;

## 1. Introduction

In recent years, the prevalence of upper-limb functional impairments has increased due to population aging and the rising incidence of sports-related injuries. Approximately one-quarter of stroke survivors experience persistent upper-limb dysfunction, such as limited elbow flexion-extension or spastic rigidity, which significantly affects daily activities and independent [1] In addition to stroke  postoperative elbow rehabilitation; sarcopenia, amyotrophic lateral sclerosis [2], and radial nerve injuries also require term mechanical assistance: living long

Conventional rigid exoskeletons can provide strong structural support but often lack adaptability, wearing comfort; and stability, particularly when accommodating diverse body geometries while preserving natural joint motion [3]. In contrast, soft robotic technologies have emerged as a promising alternative. For example, Mao et al. developed a biomimetic flexible defecation robot system that demonstrates the advantages of soft robots in safe human-machine interaction and biological compatibility [4]. Related studies have further shown that soft pneumatic actuators can successfully reproduce complex organlevel deformation,underscoring the suitability of soft actuators for simulating intricate biological motions in biomedical applications [5]. Soft wearable devices are also better suited for prolonged daily use; however; still face limitations in actuation capability dynamic response speed, and control precision due to strong nonlinearities and external disturbances , which may reduce clinical effectiveness [6,7]. they

Among various soft actuation approaches, McKibben pneumatic artificial muscles (PAMs) are considered highly promising for wearable assistive systems owing to their high


<!-- PAGE 2 -->
![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000001_acd3cda202116f845b3e3d63ed5868f4f2a237974efbd6417dc2dc3e2cf5fb0e.png)

Academic Editors: Zhixing Ge and Xingyue Hu

Received: 6 November 2025 Revised: 20 December 2025

Accepted: 25 December 2025

Published: 31 December 2025

Copyright: @ 2025 by the authors.

Licensee MDPI, Basel , Switzerland

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000002_1f2ca256908ab99b33631afe73bbe4acaf0945e57b4be3083ee292e03350b4aa.png)

power-to-weight ratio, intrinsic compliance, and muscle-like contraction behavior [8,9] Significant progress has been made in PAM modeling, materials , and control; with several studies exploring their application in elbow and upper-limb assistance [10,11]: Never theless , existing systems still face challenges , including imperfect anatomical alignment; limited durability; and insufficient adaptability to individual anthropometry: Moreover; current models and control methods struggle to balance real-time performance and mechanical accuracy during complex motions , limiting long-term comfort; clinical reliability, and widespread adoption. Building upon the aforementioned clinical needs and technological gaps, this study proposes a bio-inspired flexible elbow assistive system actuated by McKibben pneumatic artificial muscles. Unlike previous McKibben-based elbow assistive systems, this work introduces hybrid-material actuators and a four-node weaving design to enhance durability; torque stability; and anatomical alignment:. The research focuses on the systematic design and evaluation of an elbow-assist device: First, the actuator configuration was optimized according to anatomical muscle distribution and elbow biomechanics, ensuring that the actuation pathway aligns with natural joint motion. Subsequently through structural refinement and material comparison experiments , improvements were made in flexibility, sealing integrity; and long-term durability of the McKibben actuators, which in turn directly enhanced usability metrics. Specifically, the optimized fabric weaving and compliant actuation increased wearer comfort by reducing localized pressure and improving conformity to the arm Improved sealing and consistent torque ensured high repeatability across multiple inflation-deflation Furthermore, the robust and reinforced materials decreased the likelihood of air leakage and material wear; thereby reducing maintenance requirements. An adjustable attachment mechanism was also designed to accommodate diverse user anthropometrics and further enhance comfort and wearability: Experimental results demonstrated that the proposed system can provide stable elbow flexion assistance with a controllable output torque ranging from 5 to 50 Nmm, confirming its operational effectiveness and applica tion potential. Overall, this work aims to deliver a soft, wearable rehabilitation device with muscle-like compliant 
<!-- PAGE 3 -->
actuation; specifically designed to support elbow flexion-extension recovery. The proposed system provides assistive rehabilitation for individuals with impaired upper-limb motor function, particularly stroke survivors experiencing muscle imbalance and older adults with age-related neuromuscular decline: gain sealing cycles.

## 2. A Review of McKibben Pneumatic Muscle Research

2.1. Development History of McKibben Pneumatic Muscles

McKibben pneumatic artificial muscles were first introduced in the 1950s by J. . McKibben in the context of prosthetic research. Their basic structure consists of an inner rubber bladder encased within an outer braided sleeve When pressurized , the bladder expands radially, inducing axial contraction of the actuator: With ongoing advances in materials science, manufacturing techniques , and control strategies , the application scope of McKibben muscles has expanded from early prosthetic studies to biomimetic robotics and wearable assistive devices.

The effective utilization of McKibben PAMs relies heavily on a thorough understanding of their mechanical behavior and the development of appropriate control strategies. Soleymani and Khajehsaeid proposed a continuum mechanics-based model that describes the stiffness characteristics, free contraction behavior; blocked force output, and dead-zone pressure effects of McKibben muscles, while also capturing the Mullins softening nomenon observed during initial inflation-deflation cycles [12]. Owing to the pronounced nonlinear and hysteretic characteristics of McKibben muscles , achieving precise control remains challenging; Closed-loop feedback control systems typically improve performance by adjusting the inflation pressure in real time according to motion states and load dephe-

mands, while machine learning-based approaches further optimize control parameters to enhance adaptability and robustness. Chou and Hannaford analyzed the length-tension relationship of McKibben muscles and derived linearized models that facilitate controller design [13]. Meanwhile, Mao et al. demonstrated that data-driven approaches can signifi cantly improve control precision in rehabilitation applications , indicating that combining classical modeling techniques with modern algorithms is an effective strategy for managing the complex dynamics of McKibben muscles.

Experimental studies play a critical role in validating control methods and optimizing structural By measuring force-displacement characteristics , dynamic responses, and energy consumption, theoretical models and control strategies can be systematically evaluated. Numerical simulation methods, such as finite element analysis, are widely employed to predict mechanical behavior and structural optimization: Antonelli et al. developed a three-dimensional nonlinear model and validated it through quasi-static experiments [14]. In addition; the development of prototype systems and user trials is essential for practical deployment. Jeong et al. demonstrated that a soft wearable elbow robot significantly improved joint torque output and range of motion; providing valuable guidance for subsequent design refinement [15] design. guide

## 2.2. Progress of McKibben Pneumatic Muscles

Wearabl
<!-- PAGE 4 -->
e assistive devices driven by McKibben muscles generally outperform traditional systems in terms of output force, range of motion; and response speed, with tions spanning robotics, biomedical engineering, and industrial automation. Representative examples include the Pneuborn robots developed at Osaka University and the soft rehabili tation gloves and humanoid robots produced by FESTO. et al. proposed a biomimetic forearm wearable system termed Funabot-Sleeve, which integrates McKibben PAMs to deliver natural proprioceptive feedback and seamless human-machine interaction [16]. Building on this concept, the Funabot-Suit further extended McKibben-based actuation to the torso by integrating thin artificial muscles directly into conventional garments , allowing users to perceive bending and twisting motions in a natural and intuitive manner:.  This line of work highlights the scalability and configurational flexibility of McKibben-driven wearable systems across different body segments [17]. In addition; several compact pneumatic muscle sleeves and bending actuators are capable of generating torques exceeding 4 N-m while maintaining thin, wearable form factors [18], further demonstrating the versatility of McKibben-driven systems in both single-joint and whole-limb assistive applications. ent limitations. Their nonlinear deformation behavior and time-dependent characteristics complicate precise control, while end constraints can make contraction behavior difficult to predict accurately: Consequently, the design of biomimetic joints based on McKibben muscles requires careful trade-offs in material selection and mechanical configuration, which inevitably increases the overall complexity of system design and control. applica Peng

## 3. System Design and Concept

## 3.1. Overall Structural Design Concept

In the design; the arrangement of muscles involved in human elbow movement was fully utilized , mimicking the coordinated action of multiple muscle groups to enable flexible and precise elbow movement. The robot adopts McKibben pneumatic muscles arranged according to the human elbow structure, designed to closely replicate natural human elbow motion and provide intuitive assistance.

Considering the significant variation in users' body shapes , the bionic design of the wearable robot based on McKibben muscles, and to ensure the elbow assistance system

can accommodate diverse users, was informed by extensive literature and case studies on wearable devices. Through comparative analysis, an optimal scheme was identified. Adjustable connection methods were implemented to link the McKibben pneumatic muscles , allowing the joint connections to accommodate variations in arm circumference, length, and individual wearing preferences.   This ensures proper fit across various body types without discomfort or overly tight fixation that could compromise user experience. More over; the design allows the McKibben pneumatic muscles to better conform to human motion. During elbow movements, these connections automatically make fine adjustments in response to body motion, enabling the pneumatic muscles to deliver assistance that aligns with the user 's posture. This enhances both the effectiveness of the robotic 
<!-- PAGE 5 -->
assistance and the wearing experience, accommodating diverse user requirements.

## Antagonistic McKibben Tendon Design

The elbow assistance system based on McKibben muscles generally consists of two antagonistically arranged McKibben muscles , simulating the synergistic operation of human elbow muscles [19] As shown in Figure 1, elbow flexion and extension are produced by the coordinated work of the biceps brachii and triceps brachii muscles, with the biceps acting as the flexor and the triceps as the extensor: The precise coordination between these muscle groups allows humans to perform diverse multi-degree-of-freedom (DoF) movements \_

Figure 1. Anatomical diagram of human arm muscles.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000003_28f6ba0bb4be813670e0a025badd85bfc2f87c5958917ca08b0b8ea2cc61390a.png)

This study employs a bionic design based on McKibben muscles, inspired by the structure and movement patterns of human muscles. Previous work by and Yu demonstrated a 7-DoF humanoid robotic arm based on McKibben PAMs, where reverse symmetric PAM structures and Bowden cables were used to replace the human muscletendon-ligament arrangement. By setting appropriate degrees of freedom and properly arranging the Bowden cables, the shoulder; elbow; and wrist joints intersect at a single config uration without interference between joint motions , facilitating humanoid motion control:. Gong

Building on this concept, a wearable elbow flexion and extension assistive exoskeleton for upper-limb rehabilitation was developed, and its mechanical structure is shown in Figure 2 Each end of the McKibben muscles is fixed using iron bands to replace human muscle attachments and mounted onto a wearable layer made of flexible  waterproof material, facilitating comfortable donning and removal. This wearable provides layer

comfort during use while preventing pressure points normal movement. The material' s inherent waterproof properties further allow operation in diverse environments, expanding the products usability: during

Figure 2. Geometric configuration of the McKibben pneumatic muscle actuator:

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000004_694f474cf361446dfcd9cb3e16d47f164e1186a548e652a845a9434decec9ccd.png)

Each muscle unit in the McKibben wearable robot consists of four woven McKibben muscles. A single McKibben muscle is primarily composed of a balloon or stretchable rubber tube, encased in a nylon braided sleeve: For operation; air is supplied to this assembly via a pump, with precise control of airflow provided by solenoid valves. Pressure sensors installed in the air circuit monitor the internal pressure of each McKibben muscle, providing critical data for system operation and informing subsequent control strategies, ensuring stable and reliable muscle performance under varying conditions. ong

Importantly, to address the inability of McKibben muscles to provide support under tensile conditions , the muscle groups are arranged antagonistically to achieve coordinated elbow flexion and extensio
<!-- PAGE 6 -->
n. During common assisted arm flexion; one muscle group relaxes while the opposing group contracts This synergistic pattern mirrors the functional principle of human flexors and extensors, providing effective elbow assistance and improving the user s overall movement experience.

## 3.2. Mathematical Model

## 3.21. Modeling of the McKibben Pneumatic Muscle Actuator

Ideal static model and geometric parameters.   According to reference [20] an ideal static mathematical model of the braided pneumatic muscle is established based on the law of energy conservation:

$$F = \pi$$

$$\alpha = \frac { 3 \pi D _ { 0 } ^ { 2 } } { 4 \tan ^ { 2 } \theta _ { 0 } } , \quad b = \frac { \pi D _ { 0 } ^ { 2 } } { 4 \sin ^ { 2 } \theta _ { 0 } }$$

In the equation, represents the contraction ratio of the pneumatic muscle; F is the contraction force of the pneumatic muscle; and p is the internal air pressure of the pneumatic muscle.

In practical actuators, force equilibrium of the braided structure and geometric constraints must be considered to eliminate internal variables such as fiber tension and instantaneous radius. By combining these effects , the static force of the pneumatic muscle can be expressed as

$$F = \frac { p } { 4 \pi n ^ { 2 } } \left ( 3 L ^ { 2 } - l ^ { 2 } \right ) + \sigma _ { z } \frac { V _ { B } } { L } - \frac { \sigma _ { x } t L ^ { 2 } } { 2 \pi n ^ { 2 } R }$$

Material nonlinearity and parameter identification.  The strain-energy equation struc ture can be represented as a polynomial equation with constant stress [21], then the axial and circumferential stresses of the bladder are:

$$\sum _ { k = 1 } ^ { M }$$

In the equation; M is the highest order of the polynomial; €o is the strain of the bladder; and Ek is the empirical coefficient:.

In Equation (4), the empirical coefficient needs to be optimized. The least-squares error between the theoretical output force of the braided pneumatic muscle and the experimental output force is:

$$\Delta F _ { W } = \sum _ { i } \left ( \frac { F _ { i } - F _ { r i } } { F _ { r i } } \right ) ^ { 2 }$$

In the equation; F; represents the output force at time i from the model, and Fri represents the output force at time i measured experimentally.

Substituting the material model into the static force expression yields

To minimize the least-squares error between the theoretical output force of the pneumatic muscle and the experimentally measured output force, the empirical coefficient Ek is designed trust-region algorithm with global convergence properties [22]. The initial values of the empirical coefficients were selected within physically reasonable ranges reported in pneumatic muscle studies to ensure numerical stability: The optimization process was considered converged when the relative change in the objective function between successive iterations became sufficiently small or when the trust-region radius was reduced to its minimum allowable value: This procedure provided stable convergence and consistent parameter identification across repeated experiments. using prior

$$F = \frac { p } { 4 \pi n ^ { 2 } } \left ( 3 \tilde { L } ^ { 2 } - l ^ { 2 } \right ) + \left [ \frac { V _ { B } } { L _ { 0 } } \sum _ { k = 1 } ^ { M } 
<!-- PAGE 7 -->
E _ { k } \left ( \frac { L } { L _ { 0 } } - 1 \right ) ^ { k } - \frac { t L ^ { 2 } } { 2 \pi n ^ { 2 } R } \sum _ { k = 1 } ^ { M } E _ { k } \left ( \frac { R } { R _ { 0 } } - 1 \right ) ^ { k } \right ]$$

Equation (6) can be written as:

$$F = F _ { G } + F _ { N }$$

Friction and dead-zone pressure effects. The friction between the braided mesh and the bladder during the inflation and deflation of the braided pneumatic muscle is an important factor contributing to its hysteresis. Experimental results show that the magnitude of the friction force is related to the axial force applied to the pneumatic muscle. The empirical friction coefficient is considered to be 0.12 [23]. The friction force is given by:

$$F _ { f } = - k _ { f } ( F _ { G } + F _ { N } ) \ s g n ( V )$$

In the equation; kf is the empirical friction coefficient; and sgn(V) is the sign function. During the initial inflation of the braided pneumatic muscle, the presence of a dead zone causes the internal air pressure to counteract the elastic resistance of the inner bladder;

resulting in no muscle contraction or output force: The portion of air pressure that offsets this elastic effect is referred to as the dead-zone pressure [24]. Then,

$$p _ { c } = p - p _ { d }$$

In the equation; Pc is the correction pressure in the pneumatic muscle model, and Pa is the dead-zone pressure: In summary, considering the friction between the braided mesh and the bladder as well as the dead-zone pressure, the more complete static driving model of the braided pneumatic muscle (i.e , the improved McKibben-type pneumatic muscle model) is given by:

$$F = F _ { G } ( p _ { k } ) + F _ { N } + F _ { f }$$

3.2.2. Kinematic Modeling of the Entire Exoskeleton Robot

Figure 2 illustrates the geometric distribution of the actuator: Human muscle distribu tion follows a similar pattern: the upper arm is thicker than the forearm at the proximal end, while the lower arm is thicker at the distal end. "In a relaxed state, the pneumatic muscle group links the upper of the upper arm to that of the forearm, and the lower of the upper arm to its corresponding forearm Through the wearable layer; this forms a truncated cone structure with a larger upper section and a smaller lower section. Assuming that radial deformation of the pneumatic muscle group does not affect the wearable layer or alter its diameter; and that non-working torque may induce unobservable tangential micro-displacements at the fixed ends, the two rings can be treated as infinitesimally small the differential element method .  Here, dx represents the infinitesimal arc length. Thus, we can consider the pneumatic muscle group as fixed at a of each with a differential length dx, and modeled as an idealized line with no area, thickness, or volume. The focus of the study is to treat the pneumatic muscle group as the projection of the cutting plane and analyze its bending action during the execution of movements. ring ring ring: using being pair rings,

Based on the geometric relationship of the truncated cone and trigonometric functions , the projection length of the pneumatic muscle group on the side view of the truncated cone can be calculated using the Pythagorean theorem.

In the in
<!-- PAGE 8 -->
itial straightened state, the arm is extended, and the pneumatic muscle group forms an angle 01 with the vertical direction. At this point; the length of the pneumatic muscle group is L1. When the arm is bent to an angle &amp; , the pneumatic muscle group forms an angle 02 with the vertical direction; and its length becomes L.

$$l _ { 0 } = \sqrt { h _ { 1 } ^ { 2 } + ( R _ { 1 } - r _ { 1 } ) ^ { 2 } + h _ { 2 } ^ { 2 } + ( R _ { 2 } - r _ { 2 } ) ^ { 2 } }$$

In the initial state, the length of the pneumatic muscle group is given by:

$$L _ { 0 } = \frac { l _ { 0 } } { \cos \theta _ { 0 } }$$

When the arm isbent at an angle of &amp;, the relative positions of the upper arm and forearm truncated cones change. On the developed side view of the truncated cone, the new projected length lof the pneumatic muscle group is calculated as follows:

$$l = \sqrt { ( h _ { 1 } \cos \alpha ) ^ { 2 } + [ ( R _ { 1 } - r _ { 1 } ) + ( R _ { 2 } - r _ { 2 } ) \cos \alpha ] ^ { 2 } + ( h _ { 2 } \cos \alpha ) ^ { 2 } + [ ( R _ { 2 } - r _ { 2 } ) \sin \alpha ] ^ { 2 } } \quad ( 1 3 )$$

The total length of the pneumatic muscle assembly is expressed as:

$$L = \frac { l } { \cos \theta }$$

The contraction amount is given by / = Lo L Substituting Equations (2) and (4) yields:

$$\Delta L & = \frac { \sqrt { h _ { 1 } ^ { 2 } + ( R _ { 1 } - r _ { 1 } ) ^ { 2 } + h _ { 2 } ^ { 2 } + ( R _ { 2 } - r _ { 2 } ) ^ { 2 } } } { \cos \theta _ { 0 } } \\ & - \frac { \sqrt { ( h _ { 1 } \cos \alpha ) ^ { 2 } + [ ( R _ { 1 } - r _ { 1 } ) + ( R _ { 2 } - r _ { 2 } ) \cos \alpha ] ^ { 2 } + ( h _ { 2 } \cos \alpha ) ^ { 2 } + [ ( R _ { 2 } - r _ { 2 } ) \sin \alpha ] ^ { 2 } } } { \cos \theta } \\$$

where R1 and r1 denote the upper and lower base radii of the conical section of the upper arm, respectively; and h1 represents its height; Rz and r2 denote the upper and lower base

$$\varepsilon = 1 - \frac { L } { L _ { 0 } }$$

into three regions: within the working range, the stiffness exhibits an approximately linear trend; under certain conditions, the stiffness increases rapidly in a nonlinear manner; while under others, it decreases rapidly in a nonlinear fashion: Therefore, the measurement data corresponding to tensile forces ranging from 0 N to a specified value are fitted a firstorder polynomial, whereas the remaining data are fitted a third-order polynomial: using using

$$F = \begin{cases} k _ { 1 1 } \varepsilon + C , & \text { if } \varepsilon \geq 0 \\ k _ { n 1 3 } \varepsilon ^ { 3 } + k _ { n 1 2 } \varepsilon ^ { 2 } + k _ { n 1 3 } \varepsilon + C , & \text { if } \varepsilon < 0 \end{cases}$$

Here, F denotes the tensile force exerted by the McKibben muscle, k represents the elongation stiffness, and C is the tensile force at a given moment. To ensure continuity of the function; the constant C is set to be equal in both cases. By employing a lower bending stiffness , the McKibben muscle element can bend immediately when subjected to compressive loading, thereby exhibiting a more rapid decrease in stiffness.

## 4. Prototype Fabrication

4.1. Design and Fabrication of a Single Pneumatic Muscle

## 4.1.1. Sealed Connection Design for Pneumatic Muscle

According to both the literature and engineering
<!-- PAGE 9 -->
 practice, fluid leakage within McK ibben pneumatic muscles is a major drawback. To mitigate the risk of leakage, the structural design of the system aims to minimize the number of connection and enhance performance: Accordingly, a 4.= 8F-type five-way barbed connector is employed at the interface between the McKibben pneumatic muscle and the air pump. seal points ing

The 4.8F-type five-way barbed connector is widely used in various industrial fluid transport systems. Its unique structural makes it highly suitable for pneumatic muscle systems, with the most prominent advantages its simplicity of connection and excellent compatibility   During installation; the expansion layer of the McKibben pneumatic muscle is placed over the narrow end of the barbed connector and secured tightly with a cable tie, preventing slippage caused by axial forces after assembly: As illustrated in Figure 3a, the 4.8F-type five-way barbed connector exhibits outstanding performance: When the internal fluid pressure increases , the expansion layer of the pneumatic muscle presses tightly against the upper end of the connector; creating a sealing effect:. This self-sealing capability can be further enhanced by increasing the number of expansion layers , thereby significantly improving sealing reliability. Furthermore, the 4 L.8F-type five-way barbed connector enables both the distribution of a single inlet flow into design being sealing self -

five outlets and the convergence of five outlet flows into a single passage. This characteristic aligns with the gas and distribution requirements of multi-unit McKibben pneumatic muscles. On one hand, it reduces the need for additional fittings and joints; on the other; it shortens the overall pipeline length, enhances system integration; simplifies the structure, and facilitates manufacturing. Additionally it improves the overall reliability of the This component is fabricated from high-quality engineering plastics , offering advantages such as lightweight construction; low cost; and corrosion resistance: Owing to these material properties  the connector can operate reliably under pressurized gas conditions for extended periods while resisting chemical corrosion and wear damage, thereby greatly extending the service life of the connection assembly and enhancing the overall reliability and performance of the pneumatic system. well mixing system.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000005_2745b3596b17e702fa3fc68341a7b324b3f63a6f33cd41a59612497c06a52a15.png)

Figure 3. (a) Actual of F-Type Pagoda Head. (b) Force balance test of the four-channel output of the 4.8F five-way connector: Image

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000006_428ad54a0ffaba6d4b1f46daa86547416db1f395f5ed2393d43eef6e3135f354.png)

Four unbraided pneumatic artificial muscles were mounted in parallel and connected to a 4.8F five-way connector; and multiple force measurement tests were conducted indedesign of the 4.8F five-way connector and the identical inner diameters of all branch channels, press
<!-- PAGE 10 -->
ure losses and flow distribution discrepancies among the branches were effectively minimized.

## 4.1.2 Selection of Constraint Layer and Expanding Bladder Materials

When selecting materials for the McKibben pneumatic muscle actuator; factors such as mechanical properties , physical characteristics, and environmental conditions must be comprehensively considered . Based on extensive literature review, material testing, and design validation; the PET flame-retardant nylon braided mesh tube (with flattened widths of 6 mm and 10 mm) was selected as the constraint layer material, while a thickened latex balloon and a medical-grade rubber hose (inner diameter 5 mm, outer diameter 7 mm thickness 1 mm) were chosen as the expansion bladders. According to manufacturer data, the PET flame-retardant nylon braided mesh features a braiding angle of less than 259 and a diameter expansion ratio of 1.5, offering excellent elasticity, high tensile strength, and strong abrasion resistance. These properties make it well-suited for use as the constraint of the McKibben pneumatic muscle actuator: Although medical rubber can also serve as an actuator bladder; its open-ended structure results in poor air tightness. Moreover; the wall thickness of the medical rubber tube is significantly than that of the thickened latex balloon, leading to higher actuator stiffness. Consequently, achieving a given output force requires more time. Through analysis of relevant literature and open-source projects , it was observed that the thickened latex balloon exhibits superior expansibility and air wall layer tubing greater

tightness, with a lower elastic modulus that allows it to reach the desired force output more easily: Under constant pressure, it achieves contraction ratios and higher force outputs. However; due to its relatively thin wall, it cannot withstand high internal pressures and tends to lose force under sustained contact loads. For simple elbow flexion movements slowly lifting the forearm)  the required muscle torque typically ranges from 5 to 15 N-m. For more forceful flexion tasks lifting an object) , the torque may reach 20-50 Nm Or a hybrid McKibben pneumatic muscle configuration; in which actuators composed of two different bladder materials\_medical rubber and thickened latex balloons are braided together and operate cooperatively   This design leverages the high mechanical strength of medical rubber to ensure system stability, while the latex balloon's high elasticity enhances rapid response performance: The physical prototype is shown in Figure 4. large (e.g (e.g using tubing

Figure 4. Two types of McKibben pneumatic muscle actuators: (a) the elongated balloon McKibben actuator; which uses thickened latex balloon as the inner tube and a PET flame-retardant nylon braided sleeve as the constraint and (b) the rubber hose McKibben actuator; which uses medical-grade rubber hose as the inner tube and PET flame-retardant nylon braided sleeve as the constraint layer. layer;

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000007_dc6ccd9902789c91fe78a7c023f5370341a71f096ae6959cebd08f5fceae089e.png)

It is important to 
<!-- PAGE 11 -->
note that pneumatic systems inherently exhibit response delays. Figure 5ab illustrate the dynamic pressure responses of pneumatic artificial muscles fabri cated with medical rubber tubing and balloon-type bladders , respectively during pressure control experiments. In each test, a pressure command was applied at t = 0.5 s. The black dashed line denotes the target pressure (Command), while the colored solid lines represent the measured pressure responses obtained from four repeated trials conducted under identical conditions. step

For the medical rubber tube-based actuator, the artificial muscle demonstrates relatively pressure rise the inflation phase, reaching the target pressure of approximately 0.2 MPa within 1.5 s. During the steady-state phase, the pressure remains stable, and the response curves from repeated trials almost completely overlap, indicating excellent pressure performance and repeatability: During deflation; the pressure decreases rapidly; with only minor hysteresis observed near zero pressure. rapid during tracking

In contrast; the balloon-type actuator is also capable of achieving the commanded pressure, and the overall response trends remain consistent across repeated trials. However, both the inflation and deflation processes exhibit longer response times. Noticeable pressure fluctuations are observed the pressure rise and steady-state phases , and more pronounced hysteresis appears deflation These behaviors can be primarily attributed to the lower effective structural stiffness of the balloon bladder; the viscoelastic properties of the material, and its non-uniform expansion characteristics, which collectively result in more pronounced nonlinear dynamics during pressure response. during during

Figure 5. (a) Pneumatic response of the medical rubber tube-based expandable bladder actuator: (b) Pneumatic response of the elongated balloon-type expandable bladder actuator fabricated from thickened latex material.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000008_8e46898b743b102a1ec5820e7f873aa3e7aebab638270b833bbda0a3de74cd2f.png)

The durability of the materials under cyclic pressurization was evaluated. The medical-grade rubber showed excellent structural stability repeated inflation-deflation No rupture, or noticeable degradation was observed within the tested pressure range, indicating high fatigue resistance and service life. In contrast, the latex balloon-based muscle exhibited a clear pressure-dependent fatigue behavior: As shown in Figure 6, the sustainable life cycle decreased with increasing internal pressure, from approximately 105 at 150 kPa to around cycles at 350 kPa. tubing during cycles. leakage, long 104 cycles

Figure 6. Life of the artificial muscle with a thickened latex balloon bladder: cycle

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000009_b6f076c94ff99dd0b634974b9a7c7d5971b56aec7168af1355788eb436ed524d.png)

## 4.1.3. Single Pneumatic Muscle Contraction Experiment

Contraction characteristic. To accurately evaluate the influence of different bladde
<!-- PAGE 12 -->
r materials on the performance of McKibben pneumatic muscles , a series of pressurization experiments were conducted as described in this section. Identical 4.8F-type straight barbed connectors made of the same material, with uniform diameter and length, were used to connect individual McKibben pneumatic muscle samples (without inclusion in the braided assembly). This ensured that all samples had identical joints, thereby eliminating connection-induced discrepancies and minimizing experimental error: For each

type of bladder material, ten independent experiments were performed (n = 10), and the mean value of repeated measurements was used as the final experimental result. This approach reduced the influence of random factors , enhancing the accuracy and reliability of the results\_

As shown in Figure 7ab,d,e, during testing, one end of the actuator with the barbed connector was placed horizontally on a smooth foam board to maintain alignment. The actuator was fully extended, and a ruler was positioned alongside it to measure its initial length. Pressurization was then initiated gradually; with the valve regulating the air supply to increase pressure at a controlled rate Throughout the process, the actuator's length change was continuously observed and recorded. When the actuator length stabilized and no longer exhibited noticeable variation; the corresponding gas pressure value was immediately read and recorded as the maximum effective deformation pressure. Subsequently, the actuator's length at this pressure was compared to its initial length to determine the contraction ratio. Pressurization was then continued, and the deformation behavior of the actuator was monitored until localized abnormal bulging appeared at the distal end (as illustrated in Figure 7c,f). The corresponding gas pressure at this was recorded as the critical pressure of the material. Further experimental details and quantitative results are presented in the subsequent figures and tables. point

As shown in Table 1 and Figure 8, the average critical pressure and average maximum effective deformation of the thickened latex balloon McKibben pneumatic muscle actuators are lower than those of the rubber hose McKibben actuators; however, the average contraction ratio of 29.58% is significantly higher than the 20.83% observed for the rubber hose actuators. This outcome aligns with mathematical modeling: bladders with greater wall thickness exhibit higher stiffness , resulting in lower contraction ratios but greater load-bearing capacity: According to studies by Chou, Hannaford, and others , the tension-length relationship of McKibben muscles possesses the following characteristics: 1. Hysteresis: The tension-length curve exhibits a hysteresis due to Coulomb friction; independent of actuation speed, with the loop's width and height depending on the to internal pressure; higher pressure results in higher tension. 3. Stiffness Characteristics: Actuator stiffness increases with pressure and remains nearly constant within a certain length range. 4. Passive Elasticity: Even in the absence of applied pressure, the actuator exhibits intrinsic elasticity due to the material properties of the bladder and shear forces between the cons
<!-- PAGE 13 -->
traint fibers. loop

Because the rubber hose bladder has a significantly greater wall thickness than the latex balloon; it exhibits slower response and higher passive elasticity.

Table 1. Comparison of Performance Parameters for Different Types of McKibben Pneumatic Muscle Actuators.

| Type of Pneumatic Muscle Actuator              | Average Measured Critical Pressure (kPa)   | Average Maximum Effective Deformation Pressure (kPa)   | Average Contraction Ratio (%)   |
|------------------------------------------------|--------------------------------------------|--------------------------------------------------------|---------------------------------|
| Strip Balloon McKibben                         |                                            |                                                        |                                 |
| Pneumatic Muscle Actuator Rubber Hose McKibben | 189                                        | 175                                                    | 29.58                           |
| Pneumatic Muscle Actuator                      | 250                                        | 200                                                    | 20.83                           |

Based on these performance differences , for elbow flexion and extension movements that require mimicking muscle groups with relatively low load but large displacement; the thickened latex balloon McKibben actuators are preferable: Conversely; when rubber hose

McKibben actuators are used as tendons or joint sleeves, their higher pressure tolerance allows them to contract tightly around the elbow joint under external forces or load-bearing conditions, providing strong anti-slip performance, as illustrated in Figure 2. The anti-slip mechanism is similar to the aforementioned analysis: the sufficiently high friction not only prevents slippage but also stabilizes joint motion; effectively simulating the functional characteristics of natural muscle groups.

Figure 7. (a) Rubber-tube McKibben pneumatic muscle actuator before inflation. (b) rubber-tube McKibben pneumatic muscle actuator after inflation. (c) The pneumatic artificial muscle actuator with a medical rubber tube bladder exhibits deformation and bulging at the end effector when the applied pressure reaches the critical limit of the introduced material. (d) elongated-balloon McKibben pneumatic muscle actuator before inflation. (e) elongated-balloon McKibben pneumatic muscle actuator after inflation. (f) The pneumatic artificial muscle actuator with a latex elongated balloon bladder exhibits deformation and bulging at the end effector when the applied pressure reaches the critical limit of the introduced material.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000010_89595c6d6c06e61fdfe6fa2fa691dc709c942eeceb9d34fd845c5fe3d5a4d607.png)

To investigate the output force-pressure relationship of a single pneumatic muscle and to validate the proposed static model, quasi-static experiments were conducted on single McKibben type pneumatic artificial muscle actuator: Under different input pressure levels, the output force was measured while the corr
<!-- PAGE 14 -->
esponding muscle length variation was synchronously recorded.

Figure 8. Error bar chart of performance test data, where SBPM represents the strip-type pneumatic muscle and RTPM represents the rubber-tube pneumatic muscle\_

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000011_5207da1d015d4bab61c0b263edde6571cb6bdb9e25b1838d87f4dde80615c60b.png)

Force prediction was based on the improved McKibben static model proposed ear whose general form is given in Equation (10) The model comprehensively incorporates geometric constraint relationships, nonlinear terms associated with the bladder material (Equation (4)), friction effects (Equation (8)), and dead-zone pressure compen sation (Equation (9)) The measured dead-zone pressures for the two flexible bladder materialsmedical rubber and latex balloon-type bladderswere 0.0072 MPa and 0.0036 MPa, respectively. The stress-strain behavior of the bladder material was approx imated using a first-order polynomial, and the equivalent material parameter (E1) was identified by minimizing the error function defined in Equations (3)-(14) via a least-squares method. For different bladder materials, the model structure and friction coefficient remained unchanged, while only (E1) varied with material type ((E1 ~ 0.91) MPa for the medical rubber tube bladder and (E1 ~ 1.39) MPa for the latex balloon-type bladder). Other geometric parameters , including the initial length (Lo) initial braid angle (0 = 259 inner and outer diameters , as well as the friction coefficient ((kf 0.12)), were determined through structural Or experimental calibration and kept constant throughout the analysis. Figure 9 compares the model-predicted output force with the experimental measurements as a function of input pressure. For the medical rubber tube bladder; the model exhibits excellent agreement with the experimental data over the entire pressure range achieving coefficient of determination 0.993) and a root mean square error (RMSE) of 0.62 N. For the balloon-type bladder; after recalibration of the dead-zone pressure and material parameter; the model similarly maintains strong predictive performance, yielding 0.991) and an RMSE of approximately 0.69 N. These results indicate that the output force of a single pneumatic muscle is predominantly governed by the pressure-geometry relationship, while differences in bladder materials can be effectively captured by a single equivalent material parameter (E1). This confirms the robustness and general applicability of the proposed model across different flexible bladder configurations. lier, tubing design (R2 (R2

Figure 9. (a) Force-Pressure diagram of Artificial muscle with a rubber tube bladder: (b) Artificial muscle with a thickened latex balloon bladder:

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000012_bdde9f8e5bca953abceaf4a388450dd3141d15a4eee32e74b761138db1944d1a.png)

## 4.2. Design and Fabrication of the McKibben Pneumatic Muscle Fabric Assembly

In this study, the plain-weaving method was employed to achieve contraction of less than 10
<!-- PAGE 15 -->
% for a single McKibben pneumatic muscle actuator: Building on the multiple possibilities offered by plain weaving, multi-strand weaving schemes will be further explored and optimized. Beyond the McKibben pneumatic muscle discussed here, the plain-weaving approach can also be applied to other types of pneumatic muscles, such as the Kappler air-gripper and the Leiber tubular pneumatic belt actuator; enhancing certain performance characteristics and providing an effective strategy for future structural design and application.

From the standpoint of wearable device development; fabric-based McKibben actua tors offer improved conformity to the body and are suitable for integration into wearable systems. According to related studies, the efficacy and comfort of wearable assistive devices , such as passive orthoses , require maintaining an appropriate distance between the device and the human 'generally not exceeding 30 mm. For integration under clothing, a distance of less than 20 mm is preferable to ensure both comfort and aesthetic appearance: body

From a structural stability perspective; the specific configuration formed by plain weaving effectively constrains the expansion direction of the actuator during inflation. The weaving angle and influence the deformation behavior under pneumatic pressure, thereby limiting excessive radial expansion and ensuring that the actuator contracts or extends primarily its axial direction while maintaining a stable working form. These characteristics underscore the critical role of plain weaving in ensuring actuator stability and operational accuracy: Regarding mechanical performance, plain weaving significantly enhances the tensile strength of the actuator: Materials commonly used for weaving such as nylon and other fibers , possess high inherent strength, preventing rupture or damage under substantial tensile loads. Furthermore, the weaving method imparts flexibility to the actuator; allowing it to undergo compliant deformation during complex movements without compromising its structural integrity. From a force transmission efficiency perspective, plain weaving improves the ability of internal pneumatic pressure to be converted into external output force. It ensures a more uniform pressure distribution; mitigating localized stress concentrations and contributing to stable actuator performance: These properties enable the actuator to better emulate biological muscle motion, making it highly suitable for applications in bionic robots and rehabilitation devices. Additionally, plain weaving enhances abrasion resistance, preventing surface damage caused by friction with external components during prolonged operation. pattern along

Multiple experiments have demonstrated a strong correlation between the contraction performance of McKibben pneumatic muscle fabric assemblies and the weaving tightness.

In this study, all McKibben pneumatic muscle fabric assemblies were hand-woven. To quantitatively analyze this influence, the weaving tightness was measured as follows: reference segment of length (L = 18.5mm) was selected. During plain weaving, the intersecting structure of the McKibben actuators forms a diamond-like pattern (Figure 10) with the vertices of the d
<!-- PAGE 16 -->
iamonds defined as nodes. By counting the number of nodes within the reference segment, the tightness of the fabric can be assessed: a higher number of nodes indicates a denser weave, whereas fewer nodes correspond to a looser weave

Figure 10. Schematic Diagram of the Quantitative Regulation of Fabric Tightness in McKibben Pneumatic Muscles.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000013_3ac3355e76614936755c812ae379fa234a6c1ac6d8b9f063207fdfce33e8a1e1.png)

Fabric Group Performance Testing Experiment

The fabric assembly was placed parallel to a ruler on a flat surface with the inlet end fixed to the table and the opposite end connected to a freely movable, vertically aligned metal rod capable of horizontal motion. a hand-weaving method, the initial length (Lo) of the fabric assembly was constrained to (19 +0.5cm). After measuring the initial length, the assembly was pressurized to the maximum effective deformation pressure. Once stabilized , the length (L) of the fabric assembly was measured, and the contraction ratio (e) was calculated according to Equations (3)-(27). The resulting data are presented in the following table: Using

Considering factors such as load capacity, durability, and conformity; the 4-node weaving pattern was selected as the standard and applied in the elbow flexion / extension assistive exoskeleton robot.

As can be observed from Table 2 and Figure 11, the effect of different node counts on fabric contraction was evaluated through four groups of McKibben pneumatic muscle fabric assemblies with 2, 3, 4, and 5 nodes, respectively. Each group underwent 10 repeated trials. One-way ANOVA and Tukey HSD multiple comparison analyses yielded the following conclusions:  the average contraction ratios for 3-node and 4-node fabrics were 28.34% and 31.47%, respectively, both significantly higher than the 23.58% observed for 2-node fabrics (p 0.05) , indicating that increasing the node count to 3-4 effectively enhances contraction performance: In contrast, the 5-node fabric exhibited an average contraction ratio of only 25.33%, showing no significant difference compared with the 2-node fabric contraction efficiency: Multiple comparison results indicate that although the 3-node and 4-node fabrics differ numerically; the difference is not statistically significant (p 0.05). These findings demonstrate that; under the present experimental conditions, 3-4 nodes are optimal for enhancing the contraction performance of McKibben pneumatic muscle fabrics, and that simply increasing the number of nodes does not necessarily improve performance:

Figure 11. (a) ErrorBar Chart of Fabric Contraction Ratio Test Data for Different Node Numbers . #** indicates p &lt; 0.001, demonstrating a highly significant difference in contraction ratio under different numbers of nodes. (b) Analysis of contraction ratio differences for braided structures with different numbers of nodes.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000014_ddb4de633cb0e0e1fa7e76ecbd55071f3d74d2b48ae1d12dd0aa8f508a4b6698.png)

T
<!-- PAGE 17 -->
able 2 Contraction ratio measurements of braided groups with different numbers of nodes.

| Number of Nodes   |   Contraction Ratio in i-th Trial (%) |   Contraction Ratio in i-th Trial (%) |   Contraction Ratio in i-th Trial (%) |   Contraction Ratio in i-th Trial (%) |   Contraction Ratio in i-th Trial (%) |   Average Contraction Ratio (%) |
|-------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|
| 2                 |                                 26.31 |                                 25.26 |                                 24.73 |                                 24.21 |                                 26.84 |                           25.47 |
| 3                 |                                 29.72 |                                 27.56 |                                 28.1  |                                 28.64 |                                 27.02 |                           28.21 |
|                   |                                 30.27 |                                 30.48 |                                 31.35 |                                 32.43 |                                 30.81 |                           31.07 |
| 5                 |                                 25.94 |                                 25.41 |                                 24.32 |                                 24.86 |                                 24.94 |                           25.29 |

## 5. Complete System Assembly

To address the versatility challenges of wearable exoskeleton robots, the overall structure can be adjusted according to individual anatomical characteristics , accommodating users with different body sizes and muscle distributions. The main framework is made from 210T taffeta waterproof fabric and secured to the wearable layer hook-and-loop fasteners. This design leverages the fabric's tensile strength and stiffness to meet garment requirements while maintaining adjustable looseness for comfort: using

Anatomically, the upper arm muscles controlling elbow motion are divided into anterior and posterior groups. The anterior group includes the flexors the biceps brachii and brachialis\_while the posterior group consists of the extensor; primarily the triceps brachii. Contraction of the biceps brachii enables elbow flexion and forearm supination, and also assists shoulder flexion. Its functional contribution is maximal when elbow flexion approaches 80-909 . The brachialis, located to the biceps brachii, contributes to elbow flexion and contracts around the elbow joint under external load to prevent overextension. deep

The base mounting frame employs iron straps to secure the McKibben pneumatic muscle fabric assemblies, which are then cross-stitched onto the wearable layer to allow pivoting around the arm axis. The McKibben fabric assemblies are further fixed to the wearable layer either via a crisscross method or by wrapping once around the iron strap. The ends are looped and secured with cable ties around the metal strap, ensuring that excess muscle length does no
<!-- PAGE 18 -->
t participate in contraction while maintaining airtightness and allowing sliding freedom along the strap. Different fabric materials are selected for sections corresponding to specific muscle groups to accurately simulate their function.

Contraction of the triceps brachii enables elbow extension. When extended, the generated muscle force decomposes into radial and tangential components, which could cause posterior displacement of the ulna; however; extension relies primarily on the tangential force component. fully

To achieve large contraction displacements during motion; long-strip balloon-type McK ibben pneumatic muscle fabric assemblies are selected to simulate muscles such as the brachii and brachioradialis. The brachialis, which bears higher loads, is simulated rubber-hose-type McKibben pneumatic muscle fabric assemblies due to their greater load capacity:   Similarly; the triceps brachii, which requires both load-bearing and contraction efficiency is simulated a combination of the two McKibben actuator types, forming the extensor group. The final assembly drawing of the complete machine is shown in Figure 12 biceps using using

Figure 12. Human Body Model Experiment: (a) Initial State; (b) Flexed State; (c) Extended State.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000015_4f7ce6c21cd58442937b38dbcbfc6940a1502f2b644b6bfc0ab7e13ec3d43499.png)

## 6. Physical Experiments

6.1. Model Tests

## 6.1.1. Experimental Design

To prevent subconscious human responses from affecting the test results, this experiment employed a plastic human model to evaluate the wearable exoskeleton robot. At the start of the experiment; air at 0.150 MPa and 0.200 MPa was supplied to the two pneumatic muscle assemblies in the flexor region, causing the model to assume the corresponding bent posture.  The air supply to both channels was then sequentially shut off, reducing the pressures to zero, followed by venting the tubing: Subsequently, air at 0.150 MPa was supplied to the pneumatic muscle fabric assemblies of the extensor group, causing the arm to extend, as illustrated in Figure 12.

To investigate the relationship between bending angle and pneumatic pressure, an experiment was designed based on the quasi-static characteristics of McKibben pneumatic muscles reported by Michele Gabrio Antonelli.

Given that the average measured critical pressure and maximum effective deformation pressure of rubber-hose McKibben artificial muscles are significantly higher than those of long-strip balloon McKibben muscles, a multi-channel adjustable pressure valve was to supply different pressures to the two types of McKibben muscles, while keeping the pressure increment AP identical for both.  The distal end of a mannequin arm model was fixed to the table, with the upper-arm axis maintained parallel to the horizontal plane. The initial posture of the wearable robot on the mannequin arm was measured and calibrated with no power input to obtain a reference angle of 09 . Air at (Po 100 kPa) was supplied to the rubber-hose McKibben muscle, and air at (Po = 75kPa) to the balloon-type McKibben muscle, and the initial data were rec
<!-- PAGE 19 -->
orded . The input pressure was then gradually increased in increments of AP = 10kPa. After each pressure increment; the pneumatic muscle actuator was allowed to reach a quasi-static state before measuring and calibrating the arm posture, producing (0;), where (i) denotes the number of pressure increments. A completing one of measurements, the muscles were depressurized to restore the original posture before proceeding with the next increment:. This procedure was repeated 10 times. Each experiment was conducted three times (n 3). The bending angle data showed an average standard deviation of 1.568 and a mean coefficient of variation of 11.12%, indicating considerable dispersion:  Therefore; the median value was used for data processing as summarized in Table 3. used fter cycle

Table 3. Bending Angle of Two Types of Pneumatic Muscle Actuators under Different Inflated Pressures.

| Bending Angle                                           |     |   12 |   14 |   18 |   20 |   23 |   29 |   36 |   38 |   42 |   46 |
|---------------------------------------------------------|-----|------|------|------|------|------|------|------|------|------|------|
| Strip Balloon Pneumatic Muscle Inflation Pressure (kPa) |  75 |   85 |   95 |  105 |  115 |  125 |  135 |  145 |  155 |  165 |  170 |
| Rubber Hose Pneumatic Muscle Inflation Pressure (kPa    | 100 |  110 |  120 |  130 |  140 |  150 |  160 |  170 |  180 |  190 |  200 |

## 6.1.2. Characterization Results and Discussion

As shown in Figure 13, each bar represents the average bending angle at a specific pneumatic pressure, while the error bars indicate the data variability: With increasing pressure, the bending angles of both types of pneumatic muscles exhibit an upward trend, indicating that higher pressure results in greater bending   The rubber-hose pneumatic muscles display lower variability at certain pressures , suggesting more stable performance under these conditions. In contrast; the long-strip balloon muscles show greater variability at higher pressures , indicating potential performance instability

Overall, the experimental trends align with Equations (3)-(17), showing a positive correlation between pressure and bending angle, with distinct phases of linear stiffness increase, stiffness growth, and stiffness reduction. rapid

A comprehensive analysis indicates that pneumatic pressure is the primary factor affecting muscle bending angle; yet the response characteristics differ between materials. Rubber-hose muscles demonstrate better stability within specific pressure ranges, whereas long-strip balloon muscles exhibit noticeable fluctuations at high pressures. The scatter observed in the highpressure region suggests that; besides pressure, factors like inherent material nonlinearity and manufacturing-induced structural variations can complicate the bending response: In practical applications, for stable bending performance, rubber-hose muscles with pressure controlled in the mid-to-low range are preferable: For larger bending angles where some performance variability is acceptable, long-strip balloon muscles perform better at high pressures.

Figure 13. (a) Error bar plot of the bending angle of the latex balloon-bladder artificial muscle
<!-- PAGE 20 -->
 under different air pressures. (b) Error bar plot of the bending angle of the medical rubber-bladder artificial muscle under different air pressures.   (Red lines indicate the confidence interval, and black lines indicate the standard deviation)

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000016_f0bc096e2bbcabea4d2c900e0d82175951e707d80f31f6ffd3ccaad44d5d0168.png)

## 6.2. User Trials

## 6.2.1. Experimental Design with Human Participants

To validate the effectiveness and safety of the proposed pneumatic exoskeleton for elbow flexion assistance, user experiments were conducted from two perspectives: enhancement of elbow torque and reduction in biological muscle load, assessed via electromyography (EMG).

Figure 14 illustrates the experimental control setup, comprising a pressure control unit for adjusting air pressure, an oil-free air compressor (Model OTS-550, rated pressure Taizhou; Zhejiang, China) , a PC controller (equipped with a space bar for emergency depressurization)  pneumatic tubing, and the wearable elbow exoskeleton. The control workflow proceeds as follows: The PC sends a pressure command, after which the control unit and pump supply air, causing the exoskeleton to generate the assisted motion.

Figure 14. Experiment Control Procedure

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000017_baee63d9787fd618d2cf65a693716687d22ee225c17bad97a3a079a238698e19.png)

Torque Enhancement Test. Eight healthy university students of similar age (20-25 years) were recruited as participants. The statistical results of the forearm length of the sample individuals are shown in Table 4. To eliminate potential gender-related effects, the cohort consisted of four male and four female subjects. A single-blind experimental design was adopted. All participants were informed of the experimental procedures to testing and provided written informed consent. prior

Table 4. User data

| Subject             |   Subject 1 |   Subject 2 |   Subject 3 |   Subject 4 |   Subject 5 |   Subject 6 |   Subject 7 |   Subject 8 |
|---------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Forearm Length (cm) |        23.7 |        27.4 |        26.8 |        24.1 |        23.9 |        25.3 |        26.1 |        24.6 |

This experiment was designed to evaluate the improvement in elbow flexion torque provided by the exoskeleton under assisted conditions. The experimental protocol was adapted from established user testing procedures [15], and age-matched participants were selected to reduce inter-subject variability: the experiment; participants were seated , with the upper limb wearing the exoskeleton placed naturally on a table: The distal end of the forearm was fixed using a single-degree-of-freedom force sensor; and a non-extensible fabric strap was used to connect the hand to the sensor endpoint, ensuring stable and reliable force transmission: Under the unassisted condition; participants were instructed to generate elbow flexion torque und
<!-- PAGE 21 -->
er isometric conditions for 5 s. After completing the trial, a 15 min rest was provided to minimize the influence of muscle fatigue. Subsequently; the same experimental procedure was repeated five times under the exoskeleton-assisted condition. During period

During the experiment; participants stood upright with the upper arm naturally hanging close to the torso. Following experimental cues, performed elbow flexion until the forearm reached a horizontal position relative to the ground and maintained this posture for 5 s, followed by 5 s of relaxation. This sequence constituted one and was repeated five consecutive times. Three experimental conditions were evaluated: wearing the exoskeleton with pneumatic assistance; wearing the exoskeleton without pressurization, and not wearing the exoskeleton. A 15 min rest interval was provided between conditions to reduce the effects of muscle fatigue on EMG measurements they cycle

EMG Test. To further assess the influence of exoskeleton assistance on users' biological the exoskeleton primarily provides elbow flexion assistance, EMG measurements focused exclusively on the biceps brachii muscle.

Under the assisted condition, the driving pressure was adjusted according to the characteristics of the artificial muscle materials:  175 kPa for the balloon-type actuator and 200 kPa for the medical rubber tube-based actuator. Throughout the experiment; the pneumatic system was controlled via a computer interface, and participants were able to trigger an emergency stop to enable depressurization; ensuring experimental safety: The acquired EMG signals were subsequently analyzed to quantify changes in biceps brachii activation levels across different experimental conditions. rapid

## 6.2.2. Functional Performance Results and Discussion

Torque Enhancement. To quantitatively evaluate the practical assistive effect of the exoskeleton, torque outputs measured under unassisted and assisted conditions were compared, and the averaged results are reported in Table 4. The torque enhancement was defined as AM 2 Mo where (M1) denotes the elbow flexion torque with assistance and (Mo) denotes the torque without assistance. This definition minimizes the influence of the wearable robot's self-weight on the measured outcomes. M1

Elbow flexion torque data from eight participants (including unassisted torque, assisted torque, and torque enhancement) were analyzed one-way analysis of variance (ANOVA) The results indicate a significant difference in elbow flexion torque between the unassisted and assisted conditions. As shown in Figure 15a, the inter-group F-statistic corresponds to a p-value 0.05 (x = 0.05), demonstrating a statistically significant increase in elbow flexion torque when the assistive device is worn. As further illustrated in Table 5 and Figure 15a-c, each individual trial exhibits a significant difference, with torque enhancement accounting for 9.838-23.091% of the unassisted torque: These results confirm that the exoskeleton provides effective assistance for elbow flexion-extension movements using

Table 5. Torque Comparison Between Assisted and Unassisted Conditions\_

| Subject ID   |   Unassisted Torque (N-m) |   Assisted Torque (N-m) | Torque Enhancement
<!-- PAGE 22 -->
 (N-m)   |
|--------------|---------------------------|-------------------------|----------------------------|
|              |                      9.2  |                   10.8  | 1.60                       |
| 2            |                     14.53 |                   16.85 | 2.32                       |
| 3            |                     13.62 |                   14.96 |                            |
|              |                     10.87 |                   13.38 | 2.51                       |
| 5            |                     10.11 |                   11.94 | 1.83                       |
|              |                     11.5  |                   14.07 | 2.57                       |
|              |                     11.65 |                   13.62 | 1.97                       |
| 8            |                     10.78 |                   12.89 | 2.11                       |

Figure 15. Torque test results. (a) Comparison of Elbow Torque Before and After Wearing the Elbow Flexion Extension Assistive System. ** indicates p 0.01, indicating that the torque difference between the Assisted and "Unassisted" conditions is highly significant: (b) Trend of elbow torque enhancement before and after wearing the elbow assistive system. (c) Paired t-test performed on five repeated measurements for each participant.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000018_f35a8513886209779d0bf8f3071033a291da27b05552611ffd3ce0838abf87a7.png)

Notably, the most pronounced torque enhancements were observed in Participants 4 and 6 (one male and one female in their twenties), suggesting that the assistive performance of the wearable robot is minimally affected by differences. Consistent with prior reported by Wang Youhua et al. [16], the carrying angle (defined as the angle between the forearm and upper arm when the elbow is fully extended) decreases with increasing elbow flexion angle; and at the same elbow flexion posture, the average carrying angle in females is significantly larger than that in males (p 0.05). Moreover; dominant and non-dominant limbs, as well as limbs of different sexes , exhibit noticeable differences in carrying angle: During elbow deformity correction or prosthetic and assistive device fitting, preserving an appropriate carrying angle is essential for restoring limb appearance and elbow function. The McKibben muscle-based bio-inspired elbow flexion / extension assistive system proposed in this study explicitly accounts for such individual anatomical differences , thereby improving adaptability and wearability: gender findings

A one-way analysis of variance (ANOVA) was performed on the elbow flexion torque data from the eight participants under three conditions: without assistance, with assistance, and torque augmentation. The analysis revealed significant differences in elbow flexion torque between the unassisted and assisted conditions. As shown in Figure 15c, the F-statistic corresponding p-value is less than 0.05 (œ 0.05) , indicating statistically significant difference: These results demonstrate that the wearable exoskeleton effectively increases elbow flexion t
<!-- PAGE 23 -->
orque.

The torque augmentation was calculated as AM = M1 where M1 represents the torque with robotic assistance and represents the baseline torque. This approach minimizes the influence of the exoskeleton's own weight on the experimental results. Mo shown in Figure 15a,c, each experimental group exhibited statistically significant differences. The torque augmentation; expressed as a percentage of the unassisted torque, ranged from 9.838% to 23.091%, indicating effective assistance for elbow flexion and extension. The most pronounced effects were observed in Groups 2 and 4, each including one male and one female participant; suggesting that the wearable exoskeleton is minimally affected by gender differences. As

According to Wang Youhua et al, the carrying angle (the angle between the forearm and upper arm when the elbow is fully extended) decreases with increasing elbow flexion. At the same elbow flexion angle, females typically have a larger carrying angle than males 0.05), and significant differences exist between dominant and non-dominant limbs as well. When designing elbow deformity correction devices or prosthetic assistive equipment; it is important to maintain an appropriate carrying angle to optimize limb morphology and elbow function.

The McKibben-muscle-based bionic design of the present study, along with the elbow flexion and extension assistive system, explicitly accounts for individual anatomical differences, enhancing overall adaptability: As shown in Figures 15 and 16, while within-group variability is small, inter-group differences are substantial; indicating significant individual effectsThis suggests that further improvements in user-specific adaptation are possible through more detailed individual parameter collection to enable precise personalized fitnoteworthy (Figure 16a) that when the pressure increases from (0.18,0.155) to (0.2, 0.175), the torque increment becomes significantly smaller: This is mainly because the contraction ratio of the woven muscles reaches its limit, resulting in an increase in the overall exoskeleton stiffness and thus producing a certain antagonistic effect.

Figure 16. (a): Effect of pneumatic pressure on the torque of different participants. (b): 3D scatter plot of torque enhancement across participants.~Intergroup Differences and Intragroup Data Dispersion.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000019_1fb82c92fc354533845844047aff6f38152dcde82b31970961390e4a6e7debfb.png)

Overall, multiple experimental trials confirmed the assistive efficacy of the wearable exoskeleton for elbow movements , with minimal influence from and generally adaptability:   However; individual variability significantly affects adaptation outcomes. These results demonstrate the practical value of McKibben-muscle-based bionic designs in assistive systems and provide guidance for future iterations , emphasizing the need to optimize individualized mechanisms to accommodate diverse users. gender good fitting

EMG To further validate the effectiveness of the exoskeleton, muscle activa tion trends under different wearing conditions were compared . Surface electromyogr
<!-- PAGE 24 -->
aphic (sEMG) signals were acquired\_ a high-precision surface EMG recording system (Model ErgoLAB EMG, Product No. KF2O2SXM-01 , Beijing Kingfar International Inc., Haidian District, Beijing, China). Figure 17 presents the EMG signals after full-wave rectification and temporal smoothing; Three conditions were analyzed: wearing the exoskeleton with pneumatic assistance, wearing the exoskeleton without pressurization; and not wearing the exoskeleton. The results show that, under the assisted condition, the overall activation level of the biceps brachii is markedly lower than in the other two conditions , confirming that the exoskeleton effectively reduces biological muscle load while providing mechani cal assistance\_ Analys. using

Figure 17. Scatter plots of experimental data for each group

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\actuators-15-00021-v2\actuators-15-00021-v2_output_artifacts\image_000020_8c1360c50ed4f385497bcb4ee55375463a92b3702a3a60fdfdec3fc29294a546.png)

Notably; when wearing the exoskeleton without pressurization; biceps brachii activation does not decrease compared to the baseline and even shows a slight increase during

certain phases. This phenomenon is likely attributable to the mass of the exoskeleton itself (approximately 0.59 kg) and the structural constraints it imposes on arm movement. In the absence of effective assistance, these factors may increase the muscular effort required to perform elbow flexion tasks.A short and hysteresis during flexion-extension transitions were also observed, with a characteristic time scale on the order of 1-2 s. delay

## 7. Discussion

This study presents a systematic investigation of a wearable elbow assistive system actuated by McKibben pneumatic artificial muscles, encompassing structural design; material selection; and experimental validation: Through torque enhancement experiments , electromyography (EMG) analysis, and dynamic response and repeatability tests, the as sistive effectiveness , muscle load reduction capability; and pneumatic performance of the device were evaluated from multiple perspectives. The results demonstrate that the proposed wearable robot can reliably provide effective assistance, confirming its feasibility and engineering practicality for upper-limb assistive applications. As summarized in Table 5 the overall structural weight and contraction capability of the proposed system fall within the typical performance range reported for recent PAM-based joint and wearable systems, while emphasizing simplified and lightweight mechanical design. Table 6 provides performance comparison with representative PAM-based joint and wearable assistive systems reported in the literature Most existing systems employing conventional PAM actuators achieve contraction ratios in the range of approximately 20-30%, with reported system weights typically around 1.0-1.5 kg and response times of about 2 s. In comparison the proposed joint prototype braided PAM achieves a higher contraction ratio (30.81%) while substantially reducing the overall system weight to 0.59 kg and shortening the system-level response time to 1.5 s. Although differences in application scenarios , structural designs, an
<!-- PAGE 25 -->
d evaluation protocols may affect direct numerical comparison; the results indicate that the braided PAM configuration enables a favorable balance between contracwearable joint assistance applications. using

Table 6. Performance comparison with representative PAM-based joint and wearable systems.

| Wearable Devices       | Application          | Actuation   | Contraction %)   | Weight (kg)   | Response Time   |
|------------------------|----------------------|-------------|------------------|---------------|-----------------|
| Xiloyannis et al. [25] | Wearable Exoskeleton | PAM         | ~25              | ~1.5          | 2 s             |
| Caldwell et al. [26]   | Wearable assist      | PAM         | 20-30            |               | 2 s             |
| Al-Fahaam et al. [27]  | Joint actuator       | PAM         | 20-25            | ~1.0          | 2 s             |
| Zhang et al. [28]      | Soft joint system    | PAM         | 30               |               | 2 s             |
| This work              | Joint prototype      | Braided PAM | 30.81            | 0.59          | 1.5 s           |

Nevertheless , the experimental results also reveal inter-subject variability in assistive performance. As shown by the above experimental results, data dispersion within each group is relatively small, whereas differences between groups are more pronounced , indicating that system performance is influenced by individual factors such as forearm length, muscle strength, and device quality: The forearm lengths of the eight participants are shown in Table 4. At the same time, the results suggest that the system exhibits low sensitivity to gender-related differences and maintains overall adaptability: However; individual variability remains a key factor affecting assistance effectiveness, highlighting the potential for further optimization in wearable structure adjustability and parameter personalization. The PET flame-retardant braided mesh performs well as a constraint material, but alternative materials Kevlar, UHMWPE) could be considered for higher fitting good

tensile strength and lower creep. Future work incorporate more refined anthropometric data and biomechanical modeling methods to enhance individualized system adaptation. will

In addition; the current study primarily evaluates system performance under quasistatic elbow joint tasks. Although consistent dynamic responses and repeatability were observed across multiple inflation-deflation cycles, comprehensive modeling of tran sient dynamic behavior remains a challenge. It should be noted that the current evaluation focuses on externally prescribed joint motions and does not explicitly account for user motion intent or voluntary neuromuscular interaction. As indicated by the system-level response time reported in Table 5, the present design prioritizes stable torque amplification and structural simplicity over transient response. Therefore, the reported dynamic performance reflects a baseline assessment under intention-independent conditions. Moreover; the current study does not implement an active control strategy; future work could incorporate a feedback-based control algorithm, such as a pressure-angle based control, to enable user-
<!-- PAGE 26 -->
intent-aware assistance. Research will also focus on transient response characteristics , hysteresis, and nonlinear mechanisms of the pneumatic to further improve real-time performance: good rapid loop system

## 8. Conclusions

Based on the above research, this study conducted the systematic design; fabrica tion; and preliminary validation of a McKibben pneumatic muscle-driven elbow flexion /extension assistive system; achieving the intended outcomes. In terms of system design, the actuator layout was optimized according to the anatomical distribution of elbow muscles, and an adjustable attachment mechanism was employed to enhance adaptability across different users. Regarding material selection; comparative experiments identified PET flame-retardant nylon braided sleeves as the constraint with thickened latex strips and medical-grade rubber serving as the inflatable bladder; thereby ensuring balance between stability, rigidity; and flexibility: Structurally; analysis of multi-node McKibben actuator contraction revealed optimal performance with three to four nodes; accordingly, the prototype adopted a four-node planar braided configuration; and a 4.8F five-way "pagoda' connector was used to address gas leakage in the prototype: Validation using both anthropomorphic models and human participants demonstrated that the system could smoothly perform elbow flexion and extension while enhancing elbow joint torque flexion; providing effective assistance for rehabilitation training: layer, tubing during

Despite achieving these foundational functions, several limitations remain. The current system is limited to elbow flexion /extension and does not extend to shoulder abduction/ adduction or multi-degree-of-freedom hand movements, restricting its application in complex upper-limb rehabilitation and assistance.  The control strategy has not fully incorporated the user' s voluntary motion intent; which may lead to asynchrony between assisted and actual movements during high-intensity, rapid, or non-standard actions, potentially affecting user experience and training outcomes Additionally, the system relies on an external air supply, limiting its portability in outdoor or mobile scenarios, and pressure fluctuations may affect motion accuracy and stability  Future work will focus on optimizing control algorithms to achieve more precise recognition of user intent; exploring lightweight, high-strength, and wearable-friendly materials t0 enhance overall system per formance and comfort; and improving attachment mechanisms and fabrication techniques to accommodate diverse user anatomies and usage scenarios.  Furthermore, additional experimental validation across different user populations and multi-scenario applications will be conducted to continuously refine system performance and clinical applicability: daily

## References

- 1 Rocha, C.D.; Carneiro, I; Torres , M; Oliveira, H.P; Pires, EJS.; Silva, MF. Post-stroke upper limb rehabilitation: Clinical practices , compensatory movements, assessment, and trends. Prog: Biomed. 2025, 7, 042001. [CrossRef]
- 3 Tran, P; Jeong, S.; Herrin, KR; Desai, J .P. Hand exoskeleton systems, clinical rehabilitation practices , and future prospects. IEEE Trans . Med. Rob
<!-- PAGE 27 -->
ot. Bionics 2021, 3, 606-622. [CrossRef]
- 2 Zhu, J ; Wen, IR; LJ; Sun, XH; Lin, PF; Liu, S.W. Post-traumatic stress disorder in patients with amyotrophic lateral sclerosis and its correlation with clinical symptoms. Healthc. Rehabil. 2025, 1, 100010. [CrossRef] Yang
- 4 Mao, Z.; Suzuki, S.; Nabae, H; Miyagawa, S.; Suzumori, K; Maeda, S. Machine learning-enhanced soft robotic inspired by system
- 5 Mao, Z.; Suzuki, S.; Wiranata, A.; Y; Miyagawa, S. Bio-inspired circular soft actuators for simulating defecation process of human rectum. J. Artif:  Organs 2025, 28,252-261. [CrossRef] Zheng
- 7 Y; I;Hu, X. Robust active disturbance rejection control for modular fluidic soft actuators. Int. J. Hydromechatron 2024, 7, 293-309. [CrossRef] Zhang' Wang'
- 6 Jia, Y; Z; Du, S.; Zhong, W; Xu, Y; Pu; C.; Páez, LMR; Qian, P. Linear active disturbance rejection motion control of a novel pneumatic actuator with linear-rotary compound motion. Int. J. Hydromechatron: 2024, 7,382-399. [CrossRef] Zhang'
- 8 Kurumaya, S.; Nabae, H; Endo, G.; Suzumori, K. Design of thin McKibben muscle and multifilament structure. Sens. Actuators Phys. 2017, 261, 66-74. [CrossRef]
- 9 Koizumi, S.; Kurumaya, S.; Nabae, H; Endo, G.; Suzumori, K. Braiding thin McKibben muscles to enhance their contracting abilities. IEEE Robot
10. Abe, T; Koizumi, S.; Nabae, Endo, G.; Suzumori, K.; Sato, N.; Adachi, M.; Takamizawa, F. Fabrication of "18 weave muscles and their application to soft power support suit for upper limbs Autom. Lett. 2019, 4, 2532-2538. [CrossRef] H; using
- 11 Na, G.; Nabae, H.; Suzumori, K: Braided thin mckibben muscles for musculoskeletal robots Sens Actuators 2023 , 357, 114381. [CrossRef] Phys.
- 13 Chou, C.-P; Hannaford, B. Measurement and modeling of McKibben pneumatic artificial muscles. IEEE Trans. Robot. Autom. 1996, 12, 90-102. [CrossRef]
12. Soleymani, R; Khajehsaeid, H. A mechanical model for McKibben pneumatic artificial muscles based on chain extensibil ity and 3D application of the network alteration theories. Int. J. Solids Struct. 2020, 202, 620-630. [CrossRef] limiting
- 14 Antonelli, MG:; Beomonte Zobel, P; D' Ambrogio, W; Durante, F; Raparelli, T. An analytical formula for designing McKibben pneumatic muscles. Int. J. Mech. Eng;
15. memory (SMA)-based artificial muscle for assisting with elbow flexion and forearm supination / pronation. IEEE Robot. Autom. Lett. 2022, 7, 6028-6035. [CrossRef] alloy

Author Contributions: HJ: Writingoriginal draft, Writingreview and editing: QZ.: WritAll authors have and agreed to the published version of the manuscript. read

Funding: This paper was supported by Innovative Research Group of Chongqing Municipal Education Commission (CXQT19026), and Cooperative Project between Chinese Academy of Sciences and University in Chongqing (HZ2021011). Moreover; this work was supported by Young Project of Science and Technology Research Program of Chongqing Education Commission of China (No. KJQN202501166) and the Research Startup Fund of Chongqing University of Technology (0119240197). Furthermore, this work was supported by a confidential program of the Chongqing Municipal Human Resources and Social Security Bureau (Grant No. CSTB2O2SYCJH-KYXMOO46).

Institutional Review Boar
<!-- PAGE 28 -->
d Statement: The study was conducted in accordance with the Declaration of Helsinki, and approved by the Ethics Committee of Chongqing Seventh Peoples Hospital (Affiliated Central Hospital of Chongqing University of Technology) (date of approval: 11 March 2025).

Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.

Data Availability Statement: The original contributions presented in this study are included in the article. Further inquiries can be directed to the corresponding author.

Conflicts of Interest: The authors declare that there are no conflicts of interest.

16. Peng, YH; Sakai, Y; Funabora, Y; Yokoe, K; Aoyama, T.; Doki, S. Funabot-Sleeve: A Wearable Device Employing McKibben Artificial Muscles for Haptic Sensation in the Forearm. IEEE Robot. Autom. Lett. 2025, 10, 1944-1951. [CrossRef]
17. bio-inspired and McKibben muscle-actuated suit for natural kinesthetic perception. Biomim. Intell. Robot. 2023, 3, 100127. [CrossRef]
18. close-to-body application in assistive wearable robots. IEEE Robot. Autom. Lett. 2020, 5, 3042-3049. [CrossRef]
20. Hocking, EG.; Wereley, NM. Analysis of nonlinear elastic behavior in miniature pneumatic artificial muscles. Smart Mater: Struct 2012, 22, 014016. [CrossRef]
19. D.; Yu, J. Design and control of the McKibben artificial muscles actuated humanoid manipulator: In Rehabilitation of the Human Bone-Muscle System; IntechOpen: London, UK, 2022 Gong
21. Proceedings of the ASME International Mechanical Engineering Congress and Exposition; Chicago, IL, USA, 5-10 November 2006; pp. 357-367 .
23. Wereley, NM. Wind tunnel of a helicopter rotor edge actuated via pneumatic artificial muscles. J. Intell. Mater. Syst. Struct. 2011, 22, 1513-1528. [CrossRef] testing trailing flap
22. Lester; B.T.; Scherzinger; W.M. Trust-region based return mapping algorithm for implicit integration of elastic-plastic constitutive models\_ Int. J. Numer. Methods 2017, 112, 257-282. [CrossRef] Eng;
24. Solano, B.; Laloy; J ; Rotinat-Libersa, C. Compact and lightweight hydraulic actuation system for high performance millimeter scale robotic applications: Modeling and experiments. In Proceedings of the Smart Materials , Adaptive Structures and Intelligent Systems, San CA, USA, 28 February\_4 March 2010; pp. 405-411. Diego,
25. tendon-driven soft robotic In Proceedings of the 2016 6th IEEE International Conference on Biomedical Robotics and glove.
11. 26 Working Group. Dielectric haloscopes: A new way to detect axion dark matter. Rev. Lett. 2017, 118, 091801. [CrossRef] [PubMed] Phys.
28. Zhang, Q:; Liu, R; Li, Y; Liang, Y; Lin, X. A bionic cerebellar motion control model and its application in arm control: Xue Gong Xue Zhi J. Biomed. Shengwu Yixue Gongchengxue Zazhi 2020, 37, 1065-1072 Sheng Cheng Eng
13. 27 . Al-Fahaam, H; Davis, S.; Nefti-Meziani, S. The design and mathematical modelling of novel extensor bending pneumatic artificial muscles (EBPAMs) for soft exoskeletons Robot. Auton. Syst. 2018, 99, 63-74. [CrossRef]

DisclaimerlPublisher's Note: The statements, opinions and data contained in all publications are solely those of the individual people or property resulting from any ideas, methods, instructions or products referred to in the content:.