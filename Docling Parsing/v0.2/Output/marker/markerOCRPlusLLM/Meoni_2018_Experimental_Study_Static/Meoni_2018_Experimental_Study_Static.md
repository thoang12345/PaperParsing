

{0}------------------------------------------------

#### *Article*

# **An Experimental Study on Static and Dynamic Strain Sensitivity of Embeddable Smart Concrete Sensors Doped with Carbon Nanotubes for SHM of Large Structures**

**Andrea Meoni <sup>1</sup> , Antonella D'Alessandro <sup>1</sup> , Austin Downey 2,3 ID , Enrique García-Macías <sup>4</sup> , Marco Rallini <sup>1</sup> , A. Luigi Materazzi <sup>1</sup> , Luigi Torre <sup>1</sup> , Simon Laflamme 3,5, Rafael Castro-Triguero <sup>6</sup> and Filippo Ubertini 1,\***

<sup>1</sup> Department of Civil and Environmental Engineering, University of Perugia, Perugia 06125, Italy; andrea.meoni@unipg.it (A.M.); antonella.dalessandro@unipg.it (A.D.); marco.rallini@unipg.it (M.R.); annibale.materazzi@unipg.it (A.L.M.); luigi.torre@unipg.it (L.T.)

<sup>2</sup> Department of Mechanical Engineering, Iowa State University, Ames, IA 50010, USA; adowney2@iastate.edu

<sup>3</sup> Department of Civil, Construction, and Environmental Engineering, Iowa State University, Ames, IA 50010, USA; laflamme@iastate.edu

<sup>4</sup> Department of Continuum Mechanics and Structural Analysis, School of Engineering, Universidad de Sevilla, Sevilla 41004, Spain; egarcia28@us.es

<sup>5</sup> Department of Electrical and Computer Engineering, Iowa State University, Ames, IA 50010, USA

<sup>6</sup> Department of Mechanics, Campus de Rabanales, University of Cordoba, Cordoba 14014, Spain; me1catrr@uco.es

**\*** Correspondence: filippo.ubertini@unipg.it; Tel.: +39-075-585-3954

Received: 7 February 2018; Accepted: 7 March 2018; Published: 9 March 2018

**Abstract:** The availability of new self-sensing cement-based strain sensors allows the development of dense sensor networks for Structural Health Monitoring (SHM) of reinforced concrete structures. These sensors are fabricated by doping cement-matrix mterials with conductive fillers, such as Multi Walled Carbon Nanotubes (MWCNTs), and can be embedded into structural elements made of reinforced concrete prior to casting. The strain sensing principle is based on the multifunctional composites outputting a measurable change in their electrical properties when subjected to a deformation. Previous work by the authors was devoted to material fabrication, modeling and applications in SHM. In this paper, we investigate the behavior of several sensors fabricated with and without aggregates and with different MWCNT contents. The strain sensitivity of the sensors, in terms of fractional change in electrical resistivity for unit strain, as well as their linearity are investigated through experimental testing under both quasi-static and sine-sweep dynamic uni-axial compressive loadings. Moreover, the responses of the sensors when subjected to destructive compressive tests are evaluated. Overall, the presented results contribute to improving the scientific knowledge on the behavior of smart concrete sensors and to furthering their understanding for SHM applications.

**Keywords:** smart concrete sensors; self-sensing materials; structural health monitoring; strain sensitivity; carbon nanotubes; cement-based materials

## **1. Introduction**

Most current local monitoring systems (e.g., strain gauges, accelerometers, optical sensors, vibrating wire, etc.) provide limited assessment of the actual integrity of the monitored structure. Innovative solutions such as piezoelectric composites [\[1,](#page-15-0)[2\]](#page-15-1), micro-electromechanical systems (MEMs) [\[3\]](#page-15-2), or fiber optic strain sensors [\[4\]](#page-15-3), offer alternative monitoring solutions although hardly

{1}------------------------------------------------

scalable to large-scale infrastructures without incurring high costs and utilizing complex signal processing algorithms [5,6]. Along these lines, recent advances in materials and nanotechnologies have permitted the development of novel multifunctional materials, which find a broad spectrum of applications in civil and aerospace engineering [7–9]. In particular, the superior electrical and mechanical properties of nanoengineered powders, such as Carbon NanoTubes (CNTs) and nanofibers, have resulted in several demonstrations of conductive cementitious materials with excellent sensing capabilities [10–15]. Such materials offer great promise for the monitoring of large-scale Reinforced Concrete (RC) structures. In virtue of the similarity of these composites and standard concrete, it is possible to develop mechanically robust sensors with vast potentials for conducting strain-based and vibration-based Structural Health Monitoring (SHM) [16–18]. Despite some limitations in the extensive manufacturing of composites doped with CNTs that have been reported in the literature, including the relatively high cost of the nanoparticles and complex fabrication processes related to their dispersion [19], the development of dense networks of embedded sensors offers a promising cost-efficient solution [20–22]. A network of small embedded sensors can monitor the host structure without interfering with its structural integrity. Nonetheless, some aspects concerning the electromechanical behavior of these sensors, including the static and dynamic response, as well as their behavior under large strains up to failure, still remain aSince the '90s, the development of nanoengineered conductive particles has represented an important resource for the progress of engineering technologies [23,24]. Examples of application include smart nanocomposites, conductive coatings, nanodevices and nanoengineered materials [25–31]. Among other carbon-based fillers [15,32], CNTs have showed particularly promising capabilities. CNTs exhibit notable electrical and morphological characteristics suitable to produce electrically conductive networks throughout engineering materials such as concrete [11,33–35]. Furthermore, such particles have been reported to provide piezoresistive capability to insulating materials, leading to the creation of self-sensing materials with great potential in the field of SHM [36–40]. Self-sensing materials can be used to automatically assess the condition of a structural component through the analysis of data collected on-site, as well as to detect incipient damage and estimate prognosis with substantial economic benefits [41,42]. The self-sensing ability of CNT-reinforced cement-based materials or sensors is obtained through mapping variations in strain to variations in electrical characteristics of the material such as electrical resistivity or conductivity [43–51]. Research on CNT-based composites has primarily focused on dispersion strategies in different types of matrices [19,40,52], fabrication processes [53–55], and electromechanical response under quasi-static loads [56–61]. With regard to the application of nanocomposite cement-based sensors to SHM, it is worth noting the work by Han et al. [62], who investigated the use of MWCNT/cement composites as embedded strain sensors for traffic monitoring. Through vehicular loading testing, those authors reported good corresponding relationships between compressive stress and electrical response of the sensors. Saafi [63] developed CNT-reinforced cement-based sensors for crack detection applications in RC structures. Interfaced to a low-cost wireless communication system, small cubic CNT/cement sensors were embedded into  $100 \times 100 \times 100 \text{ mm}^3$  RC elements. Through three-point bending tests, Saafi's results demonstrated sudden increases in the effective resistivity of the sensors when cracks initiate and start to propagate. Naeem et al. [64] analyzed the stress and crack sensing capabilities of MWCNT/cement composites subjected to flexural loadings. Additionally, those authors furthered the study by embedding MWCNT/cement sensors in different locations of reinforced mortar beams. A noteworthy contribution was made by Downey et al. [65], who proposed a novel biphasic DC measurement approach for use in the resistance measurement of self-sensing materials. Those authors demonstrated the applicability of the proposed approach for damage detection and localization using three different ( $40 \times 40 \times 160 \text{ mm}^3$ ,  $51 \times 51 \times 51 \text{ mm}^3$  and  $100 \times 100 \times 500 \text{ mm}^3$ ) nanocomposite cement-based beams. The use of self-sensing cementitious materials for vibration-based monitoring was previously investigated by the authors [66,67], with particular attention to fabrication processes and electromechanical modelling of dynamic behaviors [51]. Research has demonstrated the potential

{2}------------------------------------------------

of self-sensing cementitious materials at vibration-based SHM, but concluded that further studies are needed to better investigate signal quality and sensors' response characteristics with varying amount of nanotubes and with or without aggregates.

This paper presents an experimental study on the behavior of a set of cement-based strain sensors fabricated with and without aggregates and with different MWCNT contents. The objective is to investigate the possibilities of CNT-reinforced cement-based sensors to be embedded in two key engineering materials, namely, cured cement paste and concrete, whereby concrete is the most used construction material worldwide, while cement paste is the matrix of any cement-based material. The investigation covers strain sensitivity and linearity of the sensors under both quasi-static and sine-sweep dynamic uni-axial compressive loadings. A study on the response of the sensors subjected to destructive tests carried out using a displacement controlled compression load completes the work. Overall, the presented results extend those obtained in previous research [\[19\]](#page-16-3) regarding the effect of aggregates and different filler contents on the sensors' behavior.

The paper is organized as follows. Section [2](#page-2-0) describes the material properties and the preparation process of the samples. Also, the experimental methodology and the laboratory configuration for the electrical, electromechanical and destructive tests are illustrated. Section [3](#page-6-0) presents the experimental results. Section [4](#page-14-0) concludes the paper with a discussion of the obtained results.

#### <span id="page-2-0"></span>**2. Materials and Methods**

### *2.1. Materials and Preparation Process of Samples*

The cementitious sensors under investigation were fabricated with and without aggregates (cured cement paste and concrete matrices). The water/cement ratio was taken as 0.45 for all the admixtures. The cement was type 42.5, Pozzolanic. The mean diameter of sand particles was lower than 4 mm, while the mean diameter of medium gravel particles was between 4 and 8 mm. For neat concrete and nanofilled materials, a second-generation superplasticizer based on polycarboxylate ether polymers was introduced in a variable amount in order to obtain similar workability for all the admixtures. Tables 1 and 2 list the different mix designs of cement pastes and concretes without filler (Table 1) and with different contents of MWCNTs (Table 2). The quantities refer to one cubic meter of produced material. In Table 2,  $\Delta V_P$ ,  $\Delta V_M$  and  $\Delta V_C$  represent the incremental volume with respect to the reference cubic meter, composed of nanotubes and surfactant for composite cured cement paste and concrete, respectively,  $n_{\%}$  is the percentage of added filler with respect to the mass of the cement, and  $C_p$ ,  $C_m$  and  $C_c$  are the particular cement contents in the mixes of cement paste and concrete, respectively. The filler contents ranged from 0 to 1%, with step increments of 0.25%, and 1.5% for all specimens.

The carbon nano-fillers were MWCNTs, Arkema Graphistrength C100 [\[68\]](#page-18-7). They appear as black powder, with a carbon content greater than 90% in weight, and an apparent density of 50–150 kg/m<sup>3</sup> . The mean number of walls is between 5 and 15, with an outer mean diameter of 10–15 nm and a length of 0.1–10 µm. The surface area of the MWCNTs is approximately 100–250 m2/g. Their elastic modulus is greater than 1 TPa and their tensile strength is around 150 GPa.

Figure [1](#page-3-2) describes the preparation procedure for the fabrication of paste and concrete cubes with MWCNTs. The process is divided into two subsequent steps. First, the carbon nanotubes were dispersed into water with a physical surfactant (i), mechanically mixed (ii) and sonicated (iii). Second, the suspension was added to cement and fine and coarse aggregates to achieve cement paste and concrete, respectively (iv). A plasticizer was added to obtain a similar workability of the fresh mixtures. The materials were casted into oiled molds, and the electrodes were embedded to a depth of about 40–45 mm (v). After 48 h, the samples were unmolded and cured for 28 days under laboratory conditions (vi). The fabricated samples are cubes of 5 cm sides in order to minimize the flexural efforts.

{3}------------------------------------------------

<span id="page-3-0"></span>**Table 1.** Mix design of cement paste and concrete without carbon fillers relative to one cubic meter of self-sensing materials. *Sensors* **2018**, *18*, x FOR PEER REVIEW 4 of 19

| Water                  | 574  | 234  |
|------------------------|------|------|
| Surfactant             | -    | -    |
| Sand (0–4 mm)          | -    | 951  |
| Medium Gravel (4–8 mm) | -    | 638  |
| Superplasticizer       | -    | 2.62 |
| Water/Cement Ratio     | 0.45 | 0.45 |

<span id="page-3-1"></span>**Table 2.** Mix design of cement paste and concrete with carbon fillers relative to one cubic meter of self-sensing materials. **Table 2.** Mix design of cement paste and concrete with carbon fillers relative to one cubic meter of

| Components             | Cement Paste [kg/m³]                                                  | Concrete [kg/m³]                                                     |
|------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| Cement 42.5 Pozzolanic | $C_p = 1277 \cdot \frac{1\text{ mm}^3}{1\text{ m}^3 + \Delta V_{PA}}$ | $C_c = 524 \cdot \frac{1\text{ mm}^3}{1\text{ m}^3 + \Delta V_{Co}}$ |
| Water                  | $0.45 \cdot C_p$                                                      | $0.45 \cdot C_c$                                                     |
| MWCNTs                 | $n_0 \cdot C_p$                                                       | $n_0 \cdot C_c$                                                      |
| Surfactant             | $n_0 \cdot C_p$                                                       | $n_0 \cdot C_c$                                                      |
| Sand (0–4 mm)          | -                                                                     | $1.8 \cdot C_c$                                                      |
| Medium Gravel (4–8 mm) | -                                                                     | $1.22 \cdot C_c$                                                     |
| Superplasticizer       | variable                                                              | variable                                                             |
| Water/Cement Ratio     | 0.45                                                                  | 0.45                                                                 |

<span id="page-3-2"></span>![](_page_3_Diagram_6.jpeg)

**Figure 1.** Preparation procedure of paste and concrete samples with carbon nanotubes. **Figure 1.** Preparation procedure of paste and concrete samples with carbon nanotubes.

distance of 10 mm. They were instrumented with two 20 mm long strain gauges installed on opposite sides. Figure 2a shows the geometry of the samples, the position of the electrodes and strain gauges, and the dimensions of a single electrode. For concrete specimens, the wire mesh was modified to be embedded at a distance of 12 mm (Figure 2a) so as to not interfere with coarse aggregates. Steel reinforcement bars were not included into the specimens and, therefore, the interest of the developed sensors focuses on compressive loadings. The applied loads during the electromechanical tests were uniaxial, perpendicular to the electrodes. The strain gauges were positioned at the center of the samples' surfaces along the loading direction to measure the applied strain. The presence of different levels of MWCNTs resulted in different visual appearance for the samples. Figure 2b is a picture of samples with 1.5, 1.0, 0.75, 0.5, 0.25 and 0% MWCNTs contents. All the experiments were conducted under laboratory conditions at room temperature and humidity. Each cube was equipped with five embedded mesh stainless steel electrodes placed at a mutual distance of 10 mm. They were instrumented with two 20 mm long strain gauges installed on opposite sides. Figure [2a](#page-4-0) shows the geometry of the samples, the position of the electrodes and strain gauges, and the dimensions of a single electrode. For concrete specimens, the wire mesh was modified to be embedded at a distance of 12 mm (Figure [2a](#page-4-0)) so as to not interfere with coarse aggregates. Steel reinforcement bars were not included into the specimens and, therefore, the interest of the developed sensors focuses on compressive loadings. The applied loads during the electromechanical tests were uniaxial, perpendicular to the electrodes. The strain gauges were positioned at the center of the samples' surfaces along the loading direction to measure the applied strain. The presence of different levels of MWCNTs resulted in different visual appearance for the samples. Figure [2b](#page-4-0) is a picture of samples with 1.5, 1.0, 0.75, 0.5, 0.25 and 0% MWCNTs contents. All the experiments were conducted under laboratory conditions at room temperature and humidity.

{4}------------------------------------------------

<span id="page-4-0"></span>![](_page_4_Picture_14.jpeg)

**Figure 2.** (a) Geometry of specimens and electrodes (dimensions are in mm); (b) Picture of samples with 1.5, 1.0, 0.75, 0.5, 0.25 and 0% (from left to right) MWCNTs.

## 2.2. Electrical Tests

Electrical tests were conducted using DC current with a 4-probe method. A stabilized current was applied at two electrodes at a mutual distance of 30 mm, and the voltage,  $V(t)$ , between the two adjacent electrodes, which were at a mutual distance of 10 mm, was measured for each sample. The data acquisition system used for acquiring measurements and providing the stabilized current was an NI PXIe-1073 device equipped with a high speed digital multimeter, model NI PXI-4071 and a current generator, model NI PXI-4130, capable of providing a four-quadrant  $\pm 20$  V and  $\pm 2$  A output on a single isolated channel. The electrical resistance of the specimens, evaluated after 6000 s of constantly applied current to achieve a stable level of polarization in the material, was obtained using Ohm's law:

$$R_I = \frac{V(t)_{I=t_p}}{I}, \quad (1)$$

where  $I$  is the applied constant current,  $V(t)$  is the measured variations of voltage over time, and  $t_p$  is the polarization time. The electrical conductivity,  $\sigma$ , was computed as follows:

$$\sigma = \left( R_{I=t_p} \cdot \frac{A}{d} \right)^{-1} = \left( \frac{V_{I=t_p}}{I} \cdot \frac{A}{d} \right)^{-1}, \quad (2)$$

where  $R$  is the electrical resistance,  $A$  is the value of the section area of the sample,  $d$  is the distance between the electrodes.

## 2.3. Electromechanical Tests

The electromechanical tests for the assessment of the self-sensing capabilities were conducted using a servo-controlled pneumatic universal testing machine, model IPC Global UTM14P, with 196 kN of load capacity. The sensors were subjected to two different loading histories: the first one consisted of quasi-static loading-unloading cycles between 0.5 and 2 kN at a constant low speed (Figure 3a), while the second one consisted of a sine-sweep dynamic load with amplitude varying between 0.5 and 1.5 kN at increasing frequencies, from 0.25 Hz to 0.5, 1, 2, 4, and 6 Hz (Figure 3b). It is important to note that the selected frequency range contains the typical natural frequencies of large civil structures. The average compressive strain of the specimens was obtained by the two resistive strain gauges applied onto opposite faces, while the voltage variations over time were recorded through the data

{5}------------------------------------------------

acquisition system. In a similar way to the electrical characterization tests, the 4-probe method was used for this test. The data acquisition system was an NI PXIe-1073, instrumented with a high speed digital multimeter, NI PXI-4071, a source measure unit, model NI PXI-4130, providing a stabilized voltage or current on a single isolated channel, and a data acquisition card, NI PXIe-4330, for strain gauge measurements.

The electrical sensitivity derives from several effects: the intrinsic resistance of carbon nanofillers and the cementitious matrix, the contact conduction among the nanotubes, and the tunneling and field emission conductions due to the nanosize dimensions of the nanotubes [22,61,69]. The relationship between the variation of electrical resistance,  $\Delta R$ , and the axial strain,  $\epsilon$ , can be assumed as follows (similar to the electrical strain gauges):

$$\Delta R / R_0 = -GF \cdot \epsilon, \quad (3)$$

where  $R_0$  is the electrical resistance without load, and  $GF$  is the gauge factor of the material.

<span id="page-5-0"></span>![](_page_5_Figure_21.jpeg)

**Figure 3.** (a) Quasi-static uniaxial load; (b) Sine-weep dynamic uniaxial load.

#### 2.4. Destructive Tests

Destructive compression tests were performed by applying a uniaxial compression load under displacement control to the nanocomposite cement-based sensors using an electric-servo test machine, model Advantest 50-C7600 by Controls, equipped with a servo-hydraulic control unit model 50-C 9842. The axial displacement, applied with a constant speed of  $2.0 \mu\text{m/s}$ , was measured through three linear variable differential transformers (LVDTs) connected to the test machine. The average displacement,  $h$ , was considered to obtain the axial strain,  $\epsilon$ , following the equation:

$$\epsilon = \frac{l' - l}{l} = \frac{(l - h) - l}{l}, \quad (4)$$

where  $l$  is the original length and  $l'$  is the final length of the specimen. Applied stress on the sample,  $\sigma_F$ , was calculated as follows:

$$\sigma_F = F / A, \quad (5)$$

where  $F$  is the applied load measured through the load cell of the machine, and  $A$  is cross-section of the sample.

During the application of the compression load and up to failure of the specimens, electrical measurements were carried out with a 4-probe method using a high speed digital multimeter, model NI PXI-4071, and a DC current generator, model NI PXI-4130, both hosted into a chassis, model NI PXIe-1073, as illustrated in the case of electrical tests. This allowed testing of the sensing function within the whole range of deformation of the material.

{6}------------------------------------------------

#### <span id="page-6-0"></span>**3. Results**

### *3.1. Percolation Threshold*

Figure [4](#page-6-1) plots the calculated electrical conductivity for cured paste and concrete specimens according to Equation (2). Results show that the percolation threshold is identifiable at 1% MWCNT content for paste specimens, and between 1% and 1.5% MWCNT content for composite concrete. The paste specimen with 1.5% weight content of nanotubes with respect to the weight of cement exhibits a reduction in electrical conductivity compared to the one with 1.0% MWCNT content. This can be attributed to a less homogeneous MWCNT dispersion because this specimen is the one containing the largest amount of nanotubes among those investigated. Another observation on the results is that paste samples without nanotubes are more conductive than plain concrete specimens, while after percolation, the two materials reach approximately the same conductivity. It follows that the addition of nanotubes has less effect on the variation of electrical conductivity in the case of cement paste compared to the case of concrete. In addition, the presence of aggregates in the concrete mixes results in a smaller effective volume to be filled by the MWCNTs particles, therefore making conductive chains more difficult to form in a cement and sand matrix relative to a cement-only matrix [\[70\]](#page-18-9). *Sensors* **2018**, *18*, x FOR PEER REVIEW 7 of 19 The paste specimen with 1.5% weight content of nanotubes with respect to the weight of cement exhibits a reduction in electrical conductivity compared to the one with 1.0% MWCNT content. This can be attributed to a less homogeneous MWCNT dispersion because this specimen is the one containing the largest amount of nanotubes among those investigated. Another observation on the results is that paste samples without nanotubes are more conductive than plain concrete specimens, while after percolation, the two materials reach approximately the same conductivity. It follows that the addition of nanotubes has less effect on the variation of electrical conductivity in the case of cement paste compared to the case of concrete. In addition, the presence of aggregates in the concrete mixes results in a smaller effective volume to be filled by the MWCNTs particles, therefore making conductive chains more difficult to form in a cement and sand matrix relative to a cement-only matrix [70].

<span id="page-6-1"></span>![](_page_6_Figure_5.jpeg)

**Figure 4.** Electrical conductivity variation for different MWCNTs content in (**a**) cured paste samples; and (**b**) concrete samples. **Figure 4.** Electrical conductivity variation for different MWCNTs content in (**a**) cured paste samples; and (**b**) concrete samples.

#### *3.2. Linearity of the Sensors under Quasi-Static Compression Loads 3.2. Linearity of the Sensors under Quasi-Static Compression Loads*

The strain sensing capability of the different specimens and their linearity are investigated through compressive tests with quasi-static loads. The plots in Figures 5 and 6 report the relative change in electrical resistance versus the applied strain of cured nanocomposite paste and concrete samples, respectively. In both cases, the base materials without nanotubes exhibit clear strain sensitivity that is characterized by a significant non-linear relationship between the relative change in electrical resistivity and the applied deformation (Figures 5a and 6a). This phenomenon is more evident in the concrete sample where the response of the base material also exhibits a hysteresis (Figure 6a). The addition of carbon nanotubes to the base materials regularizes such a strain-sensing response, making it more linear and reversible, up to a volume fraction of carbon nanotubes that is slightly below the percolation threshold (Figures 5b–d and 6b–d). At percolation, the response becomes slightly non-linear for both materials (Figures 5e and 6e), while the linearity seems to recover for a higher nanotube content (Figures 5f and 6f). The strain sensing capability of the different specimens and their linearity are investigated through compressive tests with quasi-static loads. The plots in Figures [5](#page-7-0) and [6](#page-8-0) report the relative change in electrical resistance versus the applied strain of cured nanocomposite paste and concrete samples, respectively. In both cases, the base materials without nanotubes exhibit clear strain sensitivity that is characterized by a significant non-linear relationship between the relative change in electrical resistivity and the applied deformation (Figures [5a](#page-7-0) and [6a](#page-8-0)). This phenomenon is more evident in the concrete sample where the response of the base material also exhibits a hysteresis (Figure [6a](#page-8-0)). The addition of carbon nanotubes to the base materials regularizes such a strain-sensing response, making it more linear and reversible, up to a volume fraction of carbon nanotubes that is slightly below the percolation threshold (Figures [5b](#page-7-0)–d and [6b](#page-8-0)–d). At percolation, the response becomes slightly non-linear for both materials (Figures [5e](#page-7-0) and [6e](#page-8-0)), while the linearity seems to recover for a higher nanotube content (Figures [5f](#page-7-0) and [6f](#page-8-0)).

{7}------------------------------------------------

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Figure 5.** Relative change in electrical resistance versus applied strain of nanocomposite cement paste specimens under quasi-static compression loads. In the plots, *R*0 is the electrical resistance value with a preload of 0.5 kN, and equations of quadratic regression lines are reported: cured paste with (**a**) 0.00% MWCNTs; (**b**) 0.25% MWCNTs; (**c**) 0.50% MWCNTs; (**d**) 0.75% MWCNTs; (**e**) 1.00% MWCNTs; (**f**) 1.50% MWCNTs. **Figure 5.** Relative change in electrical resistance versus applied strain of nanocomposite cement paste specimens under quasi-static compression loads. In the plots, *R*<sup>0</sup> is the electrical resistance value with a preload of 0.5 kN, and equations of quadratic regression lines are reported: cured paste with (**a**) 0.00% MWCNTs; (**b**) 0.25% MWCNTs; (**c**) 0.50% MWCNTs; (**d**) 0.75% MWCNTs; (**e**) 1.00% MWCNTs; (**f**) 1.50% MWCNTs.

### *3.3. Strain Sensitivity and Signal Quality*

Figure [7](#page-8-1) shows values of the gauge factor, *GF*, computed from the electromechanical tests depicted in Figures [5](#page-7-0) and [6,](#page-8-0) highlighting in particular the effect of a varying content of MWCNTs. As already observed above, both cured cement-paste and concrete specimens have demonstrated a clear strain-sensing capability though non-linear in nature, corresponding to relatively high *GF* values. Increasing the content of MWCNTs changes the conductive mechanisms and, therefore, the values of *GF*. Relatively large values of *GF* are obtained at 0.5% MWCNT contents for cement paste and 1.0% MWCNT for concrete specimens. The cement paste specimen with 1.5% MWCNTs seems to be an outlier, which could be associated with a less homogeneous MWCNT dispersion, as already commented on when introducing the percolation curves. These optimal amounts of MWCNTs resulting in the largest values of *GF* are close to the identified percolation thresholds, as also discussed in other literature works [\[56\]](#page-17-8), confirming that the specimens exhibit an enhanced piezoresistive behavior near

{8}------------------------------------------------

the percolation threshold. When the MWCNT content exceeds this optimal quantity, the nanotubes create a continuous network, and consequently an applied strain does not significantly modify the interactions between nanotubes that are already in contact. On the other hand, when the MWCNT content is lower than the optimal value, a reduction in  $GF$  is observed because the average distance between nanotubes is too large to allow the transfer of electrons from one nanotube to the other.

<span id="page-8-0"></span>![](_page_8_Figure_10.jpeg)

**Figure 6.** Relative change in electrical resistance versus applied strain of nanocomposite concrete specimens under quasi-static compression loads. In the plots,  $R_0$  is the electrical resistance value with a preload of 0.5 kN, and equations of quadratic regression lines are reported: concrete with (a) 0.00% MWCNTs; (b) 0.25% MWCNTs; (c) 0.50% MWCNTs; (d) 0.75% MWCNTs; (e) 1.00% MWCNTs; (f) 1.50% MWCNTs.

<span id="page-8-1"></span>![](_page_8_Figure_12.jpeg)

**Figure 7.** Gauge factor as a function of MWCNT content for (a) cured paste specimens; and (b) concrete specimens.

{9}------------------------------------------------

Figures 8 and 9 report the time histories of the relative change in electrical resistance,  $\Delta R/R_0$  and of the applied strain,  $\Delta\epsilon$ , for cement paste and concrete specimens, considering the MWCNT contents corresponding to the optimal gauge factor values. It can be visually observed that concrete sensors exhibit noisier signals in comparison to cured cement paste sensors. Among cement paste ones, only the sensor containing 1.5% MWCNTs exhibits some signal distortions. It can be hypothesized that signal quality is highly affected by the quality of MWCNT dispersion, which is less homogenous in concrete in comparison to cement paste due to the presence of the aggregates and also among paste sensors in the case of the specimen with an MWCNT content of 1.5%, as already commented on above.

<span id="page-9-0"></span>![](_page_9_Figure_3.jpeg)

**Figure 8.** Time histories of the relative change in electrical resistance,  $\Delta R/R_0$ , and of the applied strain  $\Delta\varepsilon$ , obtained from the electromechanical tests. In the plots,  $R_0$  is the electrical resistance value with a preload of 0.5 kN: (a) Quasi-static load applied on cured paste with 0.00% MWCNTs; (b) Sine-sweep dynamic load applied on cured paste with 0.00% MWCNTs; (c) Quasi-static load applied on cured paste with 0.50% MWCNTs; (d) Sine-sweep dynamic load applied on cured paste with 0.50% MWCTs; (e) Quasi-static load applied on cured paste with 1.50% MWCNTs; (f) Sine-sweep dynamic load applied on cured paste with 1.50% MWCNTs.

{10}------------------------------------------------

<span id="page-10-0"></span>![](_page_10_Figure_6.jpeg)

**Figure 9.** Time histories of the relative change in electrical resistance,  $\Delta R/R_0$ , and of the applied strain,  $\Delta\epsilon$ , obtained from the electromechanical tests. In the plots,  $R_0$  is the electrical resistance value with a preload of 0.5 kN: (a) Quasi-static load applied on concrete with 0.00% MWCTs; (b) Sine-sweep dynamic load applied on concrete with 0.00% MWCNTs; (c) Quasi-static load applied on concrete with 0.50% MWCNTs; (d) Sine-sweep dynamic load applied on concrete with 0.50% MWCNTs; (e) Quasi-static load applied on concrete with 1.00% MWCNTs; (f) Sine-sweep dynamic load applied on concrete with 1.00% MWCNTs.

{11}------------------------------------------------

### *3.4. Slow and Fast Varying Response of the Sensors*

Another aspect potentially affecting the strain sensing behavior of cement-based nanocomposite sensors is represented by strain velocity effects. To better understand this aspect, Figures [10](#page-12-0) and [11](#page-12-1) show comparisons between the responses of the cement paste and concrete sensors under quasi-static and sine-sweep dynamic compression loads. Tables [3](#page-11-0) and [4](#page-11-1) summarize the results obtained for cement paste and concrete specimens, respectively. In order to characterize the hysteretic behavior of the samples, the hysteresis area of the relative change in electrical resistance versus applied strain curves has been computed as the mean value of the areas enclosed by the loading/unloading cycles. These results show that the plain materials, besides behaving nonlinearly, also exhibit an important hysteretic behavior under the sine-sweep dynamic load, indicating a strong dependence of their electrical response under varying strain velocity. An increase in the MWCNT content has the effect of strongly reducing such a hysteretic response.

<span id="page-11-0"></span>**Table 3.** Summary of the strain sensitivity analyses conducted on cured nanocomposite cement paste specimens, including Gauge Factors (GFs), and the hysteresis areas of the relative change in electrical resistance versus applied strain curves, considering both quasi-static and sine-sweep dynamic compression loads.

| Content MWCNTs | GF | Hysteresis (Quasi-Static<br>Area [ µε ] Loading) |      | Area [ µε ] Loading | Hysteresis (Sine-Sweep<br>Area [ µε ] Loading) |      | Area [ µε ] Loading |
|----------------|----|--------------------------------------------------|------|---------------------|------------------------------------------------|------|---------------------|
| 0.00%          | 17 | 8.00                                             | × 10 | - 4                 | 1.67                                           | × 10 | - 2                 |
| 0.25%          | 2  | 4.09                                             | × 10 | - 3                 | 3.17                                           | × 10 | - 3                 |
| 0.50%          | 18 | 4.79                                             | × 10 | - 2                 | 9.25                                           | × 10 | - 3                 |
| 0.75%          | 8  | 4.89                                             | × 10 | - 3                 | 2.46                                           | × 10 | - 3                 |
| 1.00%          | 6  | 1.06                                             | × 10 | - 3                 | 3.30                                           | × 10 | - 4                 |
| 1.50%          | 12 | 2.67                                             | × 10 | - 3                 | 2.52                                           | × 10 | - 3                 |

<span id="page-11-1"></span>**Table 4.** Summary of the strain sensitivity analyses conducted on nanocomposite concrete specimens, including Gauge Factors (GFs), and the hysteresis areas of the relative change in electrical resistance versus applied strain curves, considering both quasi-static and sine-sweep dynamic compression loads.

| Content MWCNTs | GF | Hysteresis (Quasi-Static)\nArea [ µε ] Loading |                | Area [ µε ] Loading |                | Hysteresis (Sine-Sweep)\nArea [ µε ] Loading | Area [ µε ] Loading |                |
|----------------|----|------------------------------------------------|----------------|---------------------|----------------|----------------------------------------------|---------------------|----------------|
|                |    | (Empty/Merged)                                 | (Empty/Merged) | (Empty/Merged)      | (Empty/Merged) |                                              | (Empty/Merged)      | (Empty/Merged) |
| 0.00%          | 23 | 2.32                                           | × 10           | − 3                 | 3.66           | × 10                                         | − 3                 |                |
| 0.25%          | 4  | 3.00                                           | × 10           | − 5                 | 3.70           | × 10                                         | − 4                 |                |
| 0.50%          | 14 | 6.00                                           | × 10           | − 5                 | 2.90           | × 10                                         | − 4                 |                |
| 0.75%          | 12 | 3.50                                           | × 10           | − 4                 | 4.60           | × 10                                         | − 4                 |                |
| 1.00%          | 20 | 1.40                                           | × 10           | − 4                 | 1.50           | × 10                                         | − 4                 |                |
| 1.50%          | 3  | 2.60                                           | × 10           | − 4                 | 4.00           | × 10                                         | − 5                 |                |

{12}------------------------------------------------

<span id="page-12-0"></span>![](_page_12_Figure_8.jpeg)

**Figure 10.** Relative change in electrical resistance versus applied strain of nanocomposite cured paste specimens. In the plots,  $R_0$  is the electrical resistance value with a preload of 0.5 kN. Comparison between results obtained under sine-sweep dynamic compression loads and those obtained under quasi-static compression loads: cured paste with (a) 0.00% MWCNTs; (b) 0.50% MWCNTs; (c) 1.50% MWCNTs.

<span id="page-12-1"></span>![](_page_12_Figure_10.jpeg)

**Figure 11.** Relative change in electrical resistance versus applied strain of nanocomposite concrete specimens. In the plots,  $R_0$  is the electrical resistance value with a preload of 0.5 kN. Comparison between results obtained under sine-sweep dynamic compression loads and those obtained under quasi-static compression loads: concrete with (a) 0.00% MWCNTs; (b) 0.50% MWCNTs; (c) 1.00% MWCNTs.

{13}------------------------------------------------

### 3.5. Response of the Sensors Subjected to Destructive Tests

In this subsection, the electromechanical response of cured nanocomposite cement paste and concrete specimens under large deformations up to failure is investigated. Of interest are the sensing capabilities of these composites when cracking initiates and propagates. Figures 12 and 13 show stress and relative change in electrical resistance versus axial strain obtained from destructive compression tests carried out on cement paste and concrete specimens, respectively. In order to avoid possible measurement errors in estimating small axial strain values using data outputted by LVDTs displacement sensors installed in the testing machine, strain values in x-axes of Figures 12 and 13 are normalized by the strain at peak stress, denoted as  $\varepsilon_p$ . In both figures, plain samples are compared to the nanocomposite ones with the optimal gauge factor, corresponding to 0.5% and 1.0% MWCNT content for cement paste and concrete, respectively.

<span id="page-13-0"></span>![](_page_13_Figure_12.jpeg)

**Figure 12.** Comparison between stress and relative change in electrical resistance versus relative applied strain for paste specimens obtained from axial destructive tests (the circle indicates the peak stress point). Cured paste with (a) 0.00% MWCNTs and (b) 0.50% MWCNTs.

<span id="page-13-1"></span>![](_page_13_Figure_14.jpeg)

**Figure 13.** Comparison between stress and relative change in electrical resistance versus relative applied strain for concrete specimens obtained from destructive tests (the circle indicates the peak stress point). Concrete with (a) 0.00% MWCNTs and (b) 1.00% MWCNTs.

{14}------------------------------------------------

Plain cured cement paste exhibits a highly non-linear variation in the relative change in electrical resistance under the applied strain. In particular, when the strain reaches  $\varepsilon_P$ , a sudden increase in the electrical resistance of the material is observed due to the formation of compression cracks (Figure 12a). Afterwards, any sensing function is lost. On the other hand, cement paste doped with 0.5% MWCNTs exhibits a linear strain-sensing behavior, keeping the sensing capability at the ultimate strain. However, a slight change in the gauge factor is noted at peak stress (Figure 12b). Strain sensitivity is essentially lacking in the case of plain concrete specimens (Figure 13a), while the addition of nanotubes results in a high variation in the relative change in electrical resistance under strain, though slightly non-linear. Different from the case of cement paste, the sensing function is lost after reaching the maximum axial stress (Figure 13b). Note that the addition of MWCNTs is seen to increase the axial compressive strength of cement paste, as well as the ratio between the ultimate axial strain of concrete and the corresponding  $\varepsilon_P$ , therefore increasing its ductility.

### <span id="page-14-0"></span>**4. Discussion**

This paper has investigated the electrical properties and the strain sensitivity of two different cementitious materials with increasing complexity of internal structure, namely, cured Portland cement paste and concrete, doped with various contents of MWCNTs.

The electrical tests, conducted with a 4-probe DC measurement methods, resulted in the identification of percolation thresholds between 1.0 and 1.5% with respect to the mass of the cement. Cementitious sensors were subjected to electromechanical tests in order to investigate their strain-sensing capability.

Test results highlighted that both plain and nanocomposite cement-based materials exhibit strain sensing capabilities, whereby their relative change in electrical resistivity is affected by the applied strain. Plain cement paste and plain concrete, however, exhibit a significantly non-linear and hysteretic response. The addition of carbon nanotubes regularizes such a strain-sensing response, making it linear and reversible, up to a volume fraction of carbon nanotubes that is slightly below the percolation threshold. At percolation, the response becomes slightly non-linear, while the linearity seems to recover for a higher nanotube content.

When applying quasi-static and sine-sweep dynamic compression loads, cement paste sensors exhibit a better quality of signals compared to concrete sensors in terms of noise levels. Cement paste sensors exhibiting the most linear behavior under quasi-static loads also exhibit the least hysteretic response under sine-sweep dynamic loads. A similar trend for concrete sensors is not so apparent.

Destructive compression tests under controlled displacement conditions were performed in order to investigate the strain sensing capability under a large compressive strain up to the ultimate conditions of the materials. The results have highlighted the better strain sensing capability of the composite materials in comparison to plain ones. Cement paste doped with nanotubes held such a strain-sensing capability even after the peak compressive stress. An improvement in mechanical properties due to the introduction of carbon nanotubes is also evidenced for both paste and concrete specimens.

## **5. Conclusions**

Results of the present research have confirmed that cement-based sensors doped with carbon nanotubes are promising for civil engineering applications, but the amount of nanotubes, the quality of their dispersion and the presence of aggregates are key factors that can highly affect their strain sensing behavior. Overall, it is concluded that nanocomposite cured cement paste sensors are more appropriate than concrete ones for strain sensing under quasi-static and sine-sweep loads because concrete samples exhibited a higher level of noise, conceivably due to lower homogeneous nanotube dispersion. The same result was obtained in destructive tests where nanocomposite cement paste has been found to be capable of maintaining the strain-sensing capabilities even after reaching the maximum compressive stress. Moreover, using cement paste sensors, a lower level of carbon nanotubes, 

{15}------------------------------------------------

in this research identified as approximately 0.5% with respect to the mass of cement, can be sufficient to achieve a good and linear strain sensitivity.

The presented results evidence the potential application of cement-based composites doped with carbon nanotubes as embedded sensors in key locations under compression of a full-scale structure (e.g., upper part of RC beams, columns, arches, etc.). Additional research questions need to be addressed by future studies, including the developments of cost-efficient dispersion and manufacturing processes, as well as the assessment of the influence of environmental conditions (temperature and humidity) on the electromechanical response of nanocomposite cement-based materials.

**Acknowledgments:** The support of the Italian Ministry of Education, University and Research (MIUR) through the funded Project of Relevant National Interest "SMART-BRICK: Novel strain-sensing nano-composite clay brick enabling self-monitoring masonry structures" is gratefully acknowledged. This work is also partly supported by the National Science Foundation Grant No. 1069283, which supports the activities of the Integrative Graduate Education and Research Traineeship (IGERT) in Wind Energy Science, Engineering and Policy (WESEP) at Iowa State University. Enrique García-Macías was also supported by an FPU contract-fellowship from the Spanish Ministry of Education Ref: FPU13/04892. Their support is gratefully acknowledged.

**Author Contributions:** Andrea Meoni contributed to the write-up and to data analysis; Antonella D'Alessandro coordinated the write-up and the experimental activity; Austin Downey established the protocol for electrical measurements; Enrique García-Macías developed theoretical micromechanics models interpreting the results and led the revision process of the manuscript; Marco Rallini and Luigi Torre led material processing and analysis; Luigi Materazzi, Simon Laflamme, Rafael Castro-Triguero and Filippo Ubertini provided scientific guidance on SHM; Simon Laflamme and Filippo Ubertini proof-read the manuscript.

**Conflicts of Interest:** The authors declare no conflict of interest.

#### **References**

- <span id="page-15-0"></span>1. Dodds, J.S.; Meyers, F.N.; Loh, K.J. Piezoelectric characterization of PVDF-TrFE thin films enhanced with ZnO nanoparticles. *IEEE Sens. J.* **2012**, *12*, 1889–1890. [CrossRef]
- <span id="page-15-1"></span>2. Rathod, V.T.; Jain, A. Ultrasonic guided wave sensitivity of piezopolymer films subjected to thermal exposure. *ISSS J. Micro Smart Syst.* **2018**, 1–10. [CrossRef]
- <span id="page-15-2"></span>3. Kavitha, S.; Daniel, R.J.; Sumangala, K. High performance MEMS accelerometers for concrete SHM applications and comparison with COTS accelerometers. *Mech. Syst. Signal. Process.* **2016**, *66*, 410–424. [CrossRef]
- <span id="page-15-3"></span>4. Ramakrishnan, M.; Rajan, G.; Semenova, Y.; Farrell, G. Overview of fiber optic sensor technologies for strain/temperature sensing applications in composite materials. *Sensors* **2016**, *16*, 99. [CrossRef] [PubMed]
- <span id="page-15-4"></span>5. Zhou, X.; Xi, L.; Lee, J. Reliability-centered predictive maintenance scheduling for a continuously monitored system subject to degradation. *Reliab. Eng. Syst. Safety* **2007**, *92*, 530–534. [CrossRef]
- <span id="page-15-5"></span>6. Spencer Jr, B.F.; Ruiz-Sandoval, M.E.; Kurata, N. Smart sensing technology: Opportunities and challenges. *Struct. Control Health Monit.* **2004**, *11*, 349–368. [CrossRef]
- <span id="page-15-6"></span>7. Laflamme, S.; Ubertini, F.; Saleem, H.; D'Alessandro, A.; Downey, A.; Ceylan, H.; Materazzi, A.L. Dynamic Characterization of a Soft Elastomeric Capacitor for Structural Health Monitoring. *J. Struct. Eng.* **2014**. [CrossRef]
- 8. Rathod, V.T.; Kumar, J.S.; Jain, A. Polymer and ceramic nanocomposites for aerospace applications. *Appl. Nanosci.* **2017**, *7*, 519–548. [CrossRef]
- <span id="page-15-7"></span>9. Han, B.; Wang, Y.; Dong, S.; Zhang, L.; Ding, S.; Yu, X.; Ou, J. Smart concretes and structures: A review.
  - *J. Intell. Mater. Syst. Struct.* **2005**, *26*, 1303–1345. [CrossRef]
- <span id="page-15-8"></span>10. Shah, S.P.; Konsta-Gdoutos, M.S.; Metexa, Z.S.; Mondal, P. Nanoscale Modification of Cementitious Materials. In *Nanotechnology in Construction 3*; Bittnar, Z., Ed.; Springer: Berlin/Heidelberg, Germany, 2009; pp. 125–130; ISBN 978-3-642-00979-2.
- <span id="page-15-9"></span>11. Mondal, P.; Shah, S.P.; Marks, L.D. Nanoscale characterization of cementitious materials. *ACI Mater. J.* **2008**, *105*, 174–179.
- 12. Azhari, F.; Banthia, N. Cement-based sensors with carbon fibers and carbon nanotubes for piezoresistive sensing. *Cem. Concr. Comp.* **2012**, *34*, 866–873. [CrossRef]
- 13. Li, H.; Xiao, H.; Ou, J. Effect of compressive strain on electrical resistivity of carbon black-filled cement-based composites. *Cem. Concr. Comp.* **2006**, *28*, 824–828. [CrossRef]

{16}------------------------------------------------

- 14. Wen, S.; Chung, D.D.L. Partial Replacement of Carbon Fiber by Carbon Black in Multifunctional Cement-Matrix Composites. *Carbon* **2007**, *45*, 505–513. [CrossRef]
- <span id="page-16-0"></span>15. Chuah, S.; Pan, Z.; Sanjayan, J.G.; Wang, C.M.; Duan, W.H. Nano reinforced cement and concrete composites and new perspective from graphene oxide. *Constr. Build. Mater.* **2014**, *73*, 113–124. [CrossRef]
- <span id="page-16-1"></span>16. Brownjohn, J.M.W. Structural health monitoring of civil infrastructure. *Philos T. R. Soc.* **2007**, *365*, 589–622. [CrossRef] [PubMed]
- 17. Schumacher, T.; Thostenson, E.T. Development of structural carbon nanotube–based sensing composites for concrete structures. *J. Intell. Mater. Syst. Struct.* **2014**, *25*, 1331–1339. [CrossRef]
- <span id="page-16-2"></span>18. Magalhaes, F.; Cunha, A.; Caetano, E. Vibration based structural health monitoring of an arch bridge: From automated OMA to damage detection. *Mech. Syst. Sig. Proc.* **2012**, *28*, 212–228. [CrossRef]
- <span id="page-16-3"></span>19. D'Alessandro, A.; Rallini, M.; Ubertini, F.; Materazzi, A.L.; Kenny, J.M. Investigations on scalable fabrication procedures for self-sensing carbon nanotube cement-matrix composites for SHM applications. *Cem. Concr. Comp.* **2016**, *65*, 200–213. [CrossRef]
- <span id="page-16-4"></span>20. D'Alessandro, A.; Fabiani, C.; Pisello, A.L.; Ubertini, F.; Materazzi, A.L.; Cotana, F. Innovative concretes for low carbon constructions: A review. *Int. J. Low-Carbon Tech.* **2016**, *12*, 289–309. [CrossRef]
- 21. Liu, M.; Frangopol, D.M.; Kwon, K. Fatigue reliability assessment of retrofitted steel bridges integrating monitoring data. *Struct. Safety* **2010**, *32*, 77–89. [CrossRef]
- <span id="page-16-5"></span>22. Han, B.; Ou, J. Embedded piezoresistive cement-based stress/strain sensors. *Sens. Actuators A Phys.* **2007**, *138*, 294–298. [CrossRef]
- <span id="page-16-6"></span>23. Muto, N.; Yanagida, H.; Nakatsuji, T.; Sugita, M.; Ohtsuka, Y.; Arai, Y. Design of intelligent materials with self-diagnosing function for preventing fatal fracture. *Smart Mater. Struct.* **1992**, *1*, 324–329. [CrossRef]
- <span id="page-16-7"></span>24. Chen, P.-W.; Chung, D.D.L. Carbon fiber reinforced Concrete for smart structures capable of non-destructive flaw detection. *Smart Mater. Struct* **1993**, *2*, 22–30. [CrossRef]
- <span id="page-16-8"></span>25. Ji, T.; Zhang, X.; Li, W. Enhanced thermoelectric effect of cement composite by addition of metallic oxide nanopowders for energy harvesting in buildings. *Constr. Build. Mater.* **2016**, *115*, 576–581. [CrossRef]
- 26. Yang, Y.; Li, M.; Wu, Y.; Choo, T.E.S.G.; Ding, J.; Zong, B.; Yang, Z.; Xue, J. Nanoscaled self-alignment of Fe3O4 nanodiscs in ultrathin rGO films with engineered conductivity for electromagnetic interference shielding. *Nanoscale* **2016**, *8*, 15989–15998. [CrossRef] [PubMed]
- 27. Bragaru, A.; Kusko, M.; Vasile, E.; Simion, M.; Danila, M.; Ignat, T.; Mihalache, I.; Pascu, R.; Craciunoiu, F. Analytical characterization of engineered ZnO nanoparticles relevant for hazard assessment. *J. Nanopart. Res.* **2013**, *15*, 1352. [CrossRef]
- 28. Xiong, X.; Busnaina, A. Direct assembly of nanoparticles for large-scale fabrication of nanodevices and structures. *J. Nanopart. Res.* **2008**, *10*, 947–954. [CrossRef]
- 29. García, A.; Schlangen, E.; van de Ven, M.; Liu, Q. Electrical conductivity of asphalt mortar containing conductive fibers and fillers. *Constr. Build. Mater.* **2009**, *23*, 3175–3181. [CrossRef]
- 30. Li, G.Y.; Wang, P.M.; Zhao, X. Pressure-sensitive properties and microstructure of carbon nanotube reinforced cement composites. *Cem. Concr. Comp.* **2007**, *29*, 377–382. [CrossRef]
- <span id="page-16-9"></span>31. Howser, R.N.; Dhonde, H.B.; Mo, Y.L. Self-sensing of carbon nanofiber concrete columns subjected to reversed cyclic loading. *Smart Mater. Struct.* **2011**, *20*, 085031. [CrossRef]
- <span id="page-16-10"></span>32. Rhee, I.; Lee, J.S.; Kim, Y.A.; Kim, J.H. Electrically conductive cement mortar: Incorporating rice husk-derived high-surface-area graphene. *Constr. Build. Mater.* **2016**, *125*, 632–642. [CrossRef]
- <span id="page-16-11"></span>33. Han, B.; Yu, X.; Ou, J. Multifunctional and smart nanotube reinforced cement-based materials. In *Nanotechnology in Civil Infrastructure*; Gipalakrishnan, K., Birgisson, B., Taylor, P., Attoh-Okine, N., Eds.; Springer: New York, NY, USA, 2011; pp. 1–48.
- 34. Makar, J.; Beaudoin, J. Carbon nanotubes and their application in the construction industry. In Proceedings of the 1st International Symposium on Nanotechnology in Construction (NICOM 2003), 2003; Bartos, P., Ed.; Springer: Verlag, Berlin Heidelberg, 2003; pp. 331–341.
- <span id="page-16-12"></span>35. Chen, S.J.; Collins, F.G.; Macleod, A.J.N.; Pan, Z.; Duan, W.H.; Wang, C.M. Review Paper. Carbon nanotube-cement composites: A retrospect. *IES J. Part A Civ. Struct. Eng.* **2011**, *4*, 254–265. [CrossRef]
- <span id="page-16-13"></span>36. Tamimi, A.; Hassan, N.M.; Fattah, K.; Talachi, A. Performance of cementitious materials produced by incorporating surface treated multiwall carbon nanotubes and silica fume. *Constr. Build. Mater.* **2016**, *114*, 934–945. [CrossRef]

{17}------------------------------------------------

- 37. Siddique, R.; Mehta, Ar. Effect of carbon nanotubes on properties of cement mortars. *Constr. Build. Mater.* **2014**, *50*, 116–129. [CrossRef]
- 38. Camacho-Ballesta, C.; Zornoza, E.; Garcés, P. Performance of cement-based sensors with CNT for strain sensing. *Adv. Cem. Res.* **2016**, *28*, 274–284. [CrossRef]
- 39. Ubertini, F.; Laflamme, S.; D'Alessandro, A. Smart cement paste with carbon nanotubes. In *Innovative Developments of Advanced Multifunctional Nanocomposites in Civil and Structural Engineering*; Loh, K.J., Nagarajaiah, S., Eds.; Woodhead Publishing: Cambridge, UK, 2016; pp. 97–120.
- <span id="page-17-0"></span>40. Anand, S.V.; Mahapatra, D.R. Quasi-static and dynamic strain sensing using carbon nanotube/epoxy nanocomposite thin films. *Smart Mater. Struct.* **2009**, *18*, 045013. [CrossRef]
- <span id="page-17-1"></span>41. Yining, D.; Chen, Z.; Han, Z.; Zhang, Y.; Pacheco-Torgal, F. Nano-carbon black and carbon fiber as conductive materials for the diagnosing of the damage of concrete beam. *Constr. Build. Mater.* **2013**, *43*, 233–241.
- <span id="page-17-2"></span>42. Mosquera, V.; Smyth, A.W.; Betti, R. Rapid Evaluation and Damage Assessment of Instrumented Highway Bridges. *Earthq. Eng. Struc.* **2012**, *41*, 755–774. [CrossRef]
- <span id="page-17-3"></span>43. Yu, X.; Kwon, E. A carbon nanotube/cement composite with piezoresistive properties. *Smart Mater. Struct.* **2009**, *18*, 5. [CrossRef]
- 44. Hou, T.C.; Lynch, J.P. Conductivity-based strain monitoring and damage characterization of fiber reinforced cementitious structural components. *Proc. SPIE* **2005**, *5765*, 419–429.
- 45. Luo, J.; Duan, Z.; Zhao, T.; Li, Q. Hybrid effect of carbon fiber on piezoresistivity of carbon nanotube cement-based composite. *Adv. Mater. Res.* **2011**, *143*, 639–643. [CrossRef]
- 46. Konsta-Gdoutos, M.S.; Aza, C.A. Self sensing carbon nanotube (CNT) and nanofiber (CNF) cementitious composites for real time damage assessment in smart structures. *Cem. Conc. Comp.* **2014**, *53*, 110–128. [CrossRef]
- 47. Zhu, Z.H. Piezoresistive strain sensors based on carbon nanotube networks: Contemporary approaches related to electrical conductivity. *IEEE Nanotechnol. Mag.* **2015**, *9*, 11–23. [CrossRef]
- 48. Li, H.; Xiao, H.; Ou, J. A study on mechanical and pressure-sensitive properties of cement mortar with nanophase materials. *Cem. Concr. Res.* **2003**, *34*, 435–438. [CrossRef]
- 49. Wen, S.; Chung, D.D.L. Model of piezoresistivity in carbon fiber cement. *Cem. Concr. Res.* **2006**, *36*, 1879–1885. [CrossRef]
- 50. Galao, O.; Baeza, F.J.; Zornoza, E.; Garcés, P. Strain and damage sensing properties on multifunctional cement composites with CNF admixture. *Cem. Concr. Comp.* **2014**, *46*, 90–98. [CrossRef]
- <span id="page-17-4"></span>51. D'Alessandro, A.; Ubertini, F.; Materazzi, A.L.; Porfiri, M.; Laflamme, S. Electromechanical Modelling of New Nanocomposite Carbon Cement-based Sensors for Structural Health Monitoring. *Struct. Health Monit.* **2014**. [CrossRef]
- <span id="page-17-5"></span>52. Hilding, J.; Grulke, E.A.; Zhang, Z.G.; Lockwood, F. Dispersion of carbon nanotubes in liquids. *J. Dispers. Sci. Technol.* **2003**, *24*, 1–41. [CrossRef]
- <span id="page-17-6"></span>53. Han, B.; Ding, S.; Yu, X. Intrinsic self-sensing concrete and structures: A review. *Measurements* **2015**, *59*, 110–128. [CrossRef]
- 54. Nadiv, R.; Vasilyev, G.; Shtein, M.; Peled, A.; Zussman, E.; Regev, O. The multiple roles of a dispersant in nanocomposite systems. *Compos. Sci. Technol.* **2016**, *133*, 192–199. [CrossRef]
- <span id="page-17-7"></span>55. Ubertini, F.; Laflamme, S.; Ceylan, H.; Materazzi, A.L.; Cerni, G.; Saleem, H.; D'Alessandro, A.; Corradini, A. Novel Nanocomposite Technologies for Dynamic Monitoring of Structures: A Comparison between Cement-Based Embeddable and Soft Elastomeric Surface Sensors. *Smart Mater. Struct.* **2014**, *23*, 12. [CrossRef]
- <span id="page-17-8"></span>56. Cao, J.; Chung, D.D.L. Electric polarization and depolarization in cement-based materials, studied by apparent electrical resistance measurement. *Cem. Concr. Res.* **2004**, *34*, 481–485. [CrossRef]
- 57. Wen, S.; Chung, D.D.L. Damage monitoring of cement paste by electrical resistance measurement. *Cem. Concr. Res.* **2000**, *30*, 1979–1982. [CrossRef]
- 58. Loh, K.J.; Gonzalez, J. Cementitious Composites Engineered with Embedded Carbon Nanotube Thin Films for Enhanced Sensing Performance. *J. Phys. Conf. Ser.* **2015**, *628*, 012042. [CrossRef]
- 59. Xie, P.; Gu, P.; Beaudoin, J.J. Electrical percolation phenomena in cement composites containing conductive fibers. *J. Mater. Sci.* **1996**, *31*, 4093–4097. [CrossRef]
- 60. Wen, S.; Chung, D.D.L. Double percolation in the electrical conduction in carbon fiber reinforced cement-based materials. *Carbon* **2007**, *45*, 263–267. [CrossRef]

{18}------------------------------------------------

- <span id="page-18-0"></span>61. Wansom, S.; Kidner, N.J.; Woo, L.Y.; Mason, T.O. AC-impedance response of multi-walled carbon nanotube/cement composites. *Cem. Concr. Comp.* **2006**, *28*, 509–519. [CrossRef]
- <span id="page-18-1"></span>62. Han, B.; Yu, X.; Kwon, E. A self-sensing carbon nanotube/cement for traffic monitoring. *Nanotechnology* **2009**, *20*. [CrossRef] [PubMed]
- <span id="page-18-2"></span>63. Saafi, M. Wireless and embedded carbon nanotube networks for damage detection in concrete structures. *Nanotechnology* **2009**, *20*, 395502. [CrossRef] [PubMed]
- <span id="page-18-3"></span>64. Naeem, F.; Lee, H.K.; Kim, H.K.; Nam, I.W. Flexural stress and crack sensing capabilities of MWNT/cement composites. *Compos. Struct.* **2017**, *175*, 86–100. [CrossRef]
- <span id="page-18-4"></span>65. Downey, A.; D'Alessandro, A.; Baquera, M.; García-Macías, E.; Rolfes, D.; Ubertini, F.; Laflamme, S.; Castro-Triguero, R. Damage detection, localization and quantification in conductive smart concrete structures using a resistor mesh model. *Eng. Struct.* **2017**, *148*, 924–935. [CrossRef]
- <span id="page-18-5"></span>66. Ubertini, F.; Materazzi, A.L.; D'Alessandro, A.; Laflamme, S. Natural frequencies identification of a reinforced concrete beam using carbon nanotube cement-based sensors. *Eng. Struct.* **2014**, *60*, 265–275. [CrossRef]
- <span id="page-18-6"></span>67. Materazzi, A.L.; Ubertini, F.; D'Alessandro, A. Carbon nanotube cement-based transducers for dynamic sensing of strain. *Cem. Conc. Comp.* **2013**, *37*, 2–11. [CrossRef]
- <span id="page-18-7"></span>68. Page McAndrew, T.; Laurent, P.; Havel, M.; Roger, C. Arkema graphistrength®multi-walled carbon nanotubes, Technical Proceedings of the 2008 NSTI Nanotechnology Conference and Trade Show, NSTI-Nanotech. *Nanotechnology* **2008**, *1*, 47–50.
- <span id="page-18-8"></span>69. Han, B.; Yu, X.; Ou, J. *Self-Sensing Concrete in Smart Structures*; Butterworth-Heinemann: Oxford, UK; Elsevier: Amsterdam, The Netherlands, 2014.
- <span id="page-18-9"></span>70. García-Macías, E.; D'Alessandro, A.; Castro-Triguero, R.; Pérez-Mira, D.; Ubertini, F. Micromechanics modeling of the electrical conductivity of carbon nanotube cement-matrix composites. *Compos. Part B Eng.* **2017**, *108*, 451–469. [CrossRef]

![](_page_18_Picture_3.jpeg)