
<!-- PAGE 1 -->
![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000000_4fa8588a4a27d34de6215f60fb998ece8877739993988e2fe2cfdd17ecb9ea14.png)

Article

## A Prototypical Silencer-Resonator Concept Applied to a Heat Pump Mock-UpExperimental and Numerical Studies

Sebastian Wagner 1,t and Yohko Aoki 2,*

- Institute for Acoustics and Building Physics IABP, University of Stuttgart, 70174 Stuttgart, Germany
- Correspondence: yohko.aoki@ibp fraunhoferde
- Fraunhofer Institute for Building Physics IBP, 70569 Stuttgart; Germany
- Current address: Bosch Home Comfort Group GmbH, 73249 Wernau (Neckar) , Germany:

## Abstract

Modern; electrically operated heat pumps are characterized by a high degree of efficiency and represent an attractive alternative to conventional heating systems.   However; the noise emissions from heat pumps installed outside can lead to increasing noise pollution in densely populated residential areas, which represents an obstacle to widespread use. As part of a research project; a heat pump mock-up was built based on an outdoor unit in the Fraunhofer IBP: With this mock-up  investigations have now been carried out with a prototypical silencer-resonator concept. The aim was to reduce the sound power on the outlet side of the heat pump mock-up. To estimate the effect of this silencer-resonator concept for heat pumps, FEM simulations were first carried out COMSOL Multiphysics with simplified model.   The simulation results validated the silencer-resonator concept for heat pumps and indicated the considerable potential for sound reduction. A measurement was then set up, with which different silencer lengths and absorber thicknesses in the silencer were tested. The measured sound attenuation was higher than the simulated values.  The results showed that porous absorbers with sufficient thickness can achieve effective performance in the mid-frequency range. A maximum sound power reduction of 5.7 dB was achieved with the 0.15 m absorber: Additionally, Helmholtz resonators were implemented to attenuate the low-frequency range and tonal With these resonators sound attenuation was increased to 7.7 dB. using peaks.

Keywords: heat pump acoustic; fem-simulation; silencer; resonator

## 1. Introduction

In the past years, events such as energy crises and wars have caused the energy prices to In parallel, heat pumps have been identified as a technology; especially those using outside air as a heat source. In recent years, the number of heat pumps installed in dense urban areas has increased continuously: Hence, noise emission from heat pumps is becoming a serious issue\_ Therefore, acoustic research on heat pumps has become a major challenge in the development process of heat pump manufacturers. explode. key

As mentioned in
<!-- PAGE 2 -->
 [1], about 90% of the emitted noise from outdoor units is caused by the fan. This airborne noise contributes significantly to the overall noise emissions from heat pumps. To reduce noise emission from the fan, research is focusing on the optimization of the fan blade geometry; e-g-, in [2-5], while manufacturers try to optimize inflow conditions on the suction side of the fan. Czwielong et al. [6] investigated the integration of micro-perforated plate absorbers (MPAs) into the housings of heat exchangers.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000001_acd3cda202116f845b3e3d63ed5868f4f2a237974efbd6417dc2dc3e2cf5fb0e.png)

Academic Editor: Ilias Stavrakas and Jian Kang

Received: 2 December 2025

Revised: 14 January 2026

Accepted: 19 January 2026

Published: 27 January 2026

Copyright: @ 2026 by the authors

Licensee MDPI, Basel, Switzerland\_

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000002_1d857ae610518ae23d759de2c756add235dedcc7e02f21797dda1baff4f73bbc.png)

MPAs led to a reduction in sound emissions of up to 2.9 dB in the load range and their use was proven to be an effective method for acoustically optimizing cooling systems without impairing aerodynamic efficiency: Lucius et al. [7] experimentally and numerically compared the noise levels in two configurations: one with and one without a heat exchanger The showed that the heat exchanger significantly influences the turbulence and thus the noise level of the fan. The sound radiation of the fan was simulated and it was indicated that the configuration with the heat exchanger exhibits higher noise le-vels, but with deviations of up to 10 dB compared to the measurements. partial study

Also; as described in [10], Active Noise Control (ANC) techniques have been to heat pumps and show potential to reduce airborne noise on the outlet side: On the back of the heat pump mock-up, a sound power reduction of 0.5 dB was achieved, and on the pressure side of the fan (front) , a significant reduction of 7.8 dB was reached . Nevertheless , for heat pumps in particular; any additional power consumption can deteriorate their efficiency:   Furthermore, due to the often-large size of the fans used and the associated complex free-field sound radiation characteristics , simple Single Input Single Output (SISO) multichannel Multi Input Multi Output (MIMO) ANC system with multiple loudspeakers and microphone sensors would be required.  The complexity and cost of such a system are therefore relatively high [11] An additional problem 
<!-- PAGE 3 -->
is that, in outdoor applications, the acoustic behavior of the system, which changes over time ie., due to the temperature differences between winter and summer, must be considered. Most adaptive algorithms are capable of compensating only for smaller variations [11]. applied

Gustafson et al.  investigated [8,9] various heat exchanger geometries in terms of acoustics and efficiency: concluded that that the design of heat exchangers with flat tubes should be prioritized to enhance the acceptance of heat pumps. Since the fan in the outdoor unit is a primary source of noise, high airflows and pressure lead to higher noise levels. Gustafson et al. also emphasized that future developments should focus on optimizing heat exchanger designs to further minimize noise and maximize performance:. They drops

For these reasons, this paper focuses on the application of passive noise reduction measures.  It presents a noise attenuation concept on the pressure side of the fan with a porous absorber in combination with Helmholtz (HH) resonators. This work is part of a publicly funded project network, QUEEN-HP MENESA, which focuses on the noise and vibration emissions of heat pumps. In this project, the acoustic emission of an outdoor unit was investigated with a heat pump mock-up at the Fraunhofer Institute for BuildPhysics IBP. Acoustic measurements with this mock-up have shown that depending on the operating point; the broadband noise or the tonal peaks dominate the frequency spectra [12,13]. For the sound attenuation of the tonal peaks in the lower frequency range as well as the broad band noise in the mid frequency range, different sound attenuation methods have to be applied [10], such as an acoustic silencer and Helmholtz resonators. ing

Furthermore, to the best of our knowledge, no previous studies have frequency-specific and broadband noise attenuation mechanisms to a heat pump mock up. Existing research generally focuses on single attenuation mechanism or a limited frequency range.  In comparison to [10], we only use passive methods for sound attenuation to reduce the complexity of components and keep the costs low.  Therefore, the combined silencer-resonator approach investigated in this study represents an advanceapplied

Due to the associated wavelengths , the passive absorber is not effective at low frequencies. At these frequencies; the absorber dimensions are small compared to the acoustic mainly affects the mid- to high-frequency range. For this reason, Helmholtz resonators were employed to specifically target and attenuate the low-frequency components.

ment beyond previous work by integrating reactive and dissipative principles to achieve more comprehensive noise reduction across both tonal and broadband components.

Section 2 presents the heat pump mock-up, and Section 3 introduces the applied sound
<!-- PAGE 4 -->
 attenuation methods. FEM simulations were performed with the simulation soft ware COMSOL Multiphysics (version 6.2) [14] with a simplified simulation model to estimate the impact of the sound attenuation (Section 4). In Section 5, the acoustic measures were implemented in the heat pump mock-up and the concept was validated via acoustic measurements

## 2 Heat Pump Mock-Up

already presented in previous publications [12,13], in collaboration with the Fraun hofer Institute for Solar Energy Systems a mock-up of a heat pump outdoor unit has been designed to investigate the aeroacoustic interaction between a heat exchanger (HEX) and a fan (see Figure 1). The mock-up is composed of a support frame and the heat-pump core (air duct) , which has the same cross-sectional area as the HEX, 1.0 m height and 0.9 m width. A seven-blade fan of 0.67 m diameter in a fan duct was mounted on the front (see Figure Ic). The air duct is indicated by the red rectangular outline in Figure 1a. The fan duct is located at the center of the core (see Figure Id). The frame and the cover in front of the fan were not part of the numerical model. As ISE, panel panel

Figure 1. Heat pump mock-up; (a) pressure side view of the mock-up in the reverberation chamber; (b) suction side view of the mock-up in the semi anechoic chamber [12]; (c,d) sketch of the heat pump mock-up with the shown distance between the HEX and the fan duct of 0.4 m

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000003_ed10a471b222e1d51face25b41d20d9cda01434892e6a9210716c5f2a8e35303.png)

With this heat pump mock-up, various acoustic investigations have been performed , such as the measurement of the radiated sound power as well as the radiation characteristics. Furthermore, it was possible to investigate several HEX-fan configurations by changing the distance between HEX and the fan, changing the HEX-type, or installing the HEX inclined on the suction side. The experimental studies shown in this paper were performed with a perpendicularly installed fin tube heat exchanger (FT-HEX) and with a distance between the fan duct and the FT-HEX of 0.4 m (see Figure Id). Within the acoustic measurements, four different fan speeds were considered. Table 1 gives an overview of these fan with the related blade passing frequencies (BPFs) and percentages related to the maximum fan The fan used in the heat pump mock-up was a seven-blade axial fan manufactured by Ziehl-Abegg: The flow rate ranged from approximately 3200 /h at 424 rpm to approximately 10,000 /h at 1060 rpm. speeds speed. m3 m3

Table 1. Considered fan and BPFs for selected fan operation conditions [6]. speeds

| Fan rotation (rpm) speed     |   424 (40%) |   635 (60%) |   848 (80%) |   1060 (100%) |
|--------------------
<!-- PAGE 5 -->
----------|-------------|-------------|-------------|---------------|
| Blade passing frequency (Hz) |        49.4 |        74.1 |        98.9 |         123.7 |

## 3. Applied Noise Control Techniques

According to a previous study [6], at low frequencies the sound power spectra are dominated by the tonal noise around the BPF and its higher harmonics. The peak around the BPF is visible in all spectra, except for the fan setting of 424 rpm, because the peak is located at the lower limit of the x-axis, 50 Hz. Except for the fan speed of 1060 rpm, the broadband noise with the maximum around 900 Hz determines the overall sound power level. speed setting

The aim of this paper is to attenuate the broadband noise as as the tonal components by applying passive control techniques such as acoustic silencers and Helmholtz resonators.  This section briefly introduces the principles and physical arrangements of these sound attenuation methods on the heat pump mock-up. well two

## 3.1. Acoustic Silencer

The term 'acoustic silencer' often refers to any type of passive noise control device [15] In this paper; the silencer refers to the dissipative silencer; which consists of the porous material and the perforated plate as the protective facing, to attenuate sound by converting the acoustical energy into heat in the porous material [15]. The performance of the silencer is a function of the geometry and the acoustic properties of the absorbers.

The acoustic performance of a porous material is evaluated in terms of the absorption coefficient; which depends on the porosity; the size of the pores and the flow resistance: The thickness of the absorption layer also has a significant effect on the absorption performance. Figure 2 shows the sound absorption coefficient for the applied porous absorber CARUSO ISO-Bond as a function of the absorber thickness, d. The material parameters are of the porous absorber are summarized in Table 2. Figure 2 shows that the absorption coefficients generally increase with frequencies. At low frequencies, sound absorption in the porous material is mainly due to the viscous-inertial losses, related to the velocity of air in the porous medium. When a porous absorber is backed by a rigid wall; the particle velocity at the wall is zero, and thus the absorption is poor at low frequencies. When the thickness is roughly to a quarter wavelength, the first particle velocity at the front face of the material reaches the maximum; and thus the absorption increases. equal

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000004_4180c4cb27e1834431f63a5924ef7d6643609bd325c6ea2d344ee161b3eeb9db.png)

Frequency [Hz]

Figure 2. Absorption coefficient &amp; for Caruso ISO-Bond as a function of thickness (normal sound
<!-- PAGE 6 -->
 incidence) layer

Table 2. Properties of the porous absorber CARUSO-ISO-Bond"

| Parameter                            | Value   |
|--------------------------------------|---------|
| Flow resistivity = (Pa s/m-2)        | 11,000  |
| Viscous characteristic length ^ (um) | 100     |
|                                      | 200     |
| Porosity (%)                         | 98      |
| Tortuosity X                         | 1.6     |

However; the actual problem with industrial applications is at low frequencies. The absorption curve is shifted roughly by one octave band lower per doubling of the thickness. For an absorption coefficient of &amp; &gt; 0.8, for frequencies below 500 Hz, a very thick absorber is necessary [16,17]   Therefore, porous absorbers are often used for the attenuation of medium to high frequencies.

Figure 3 shows the heat pump mock-up with the attached silencer in front of the fan: As shown in the figure, the silencer consisted of an outer absorber with the thickness of dA and an inner cylinder with the diameter of Both outer and the inner cylinder were filled with porous absorber; referred to as "PA in Figure 3. To ensure a flow around the cylinder as undisturbed as possible, the cylinder in the center was selected with diameter of 0.2 m, corresponding to the diameter of the fan motor housing: The outer diameter of the duct corresponded to the diameter of the outlet opening at the heat pump mock-up with 0.67 m The length of the silencer is described by Lsil and represents the length of the outer absorber ring as well as the inner cylinder: ring dinside' ring dinside doutlet

Figure 3. Sketch of the heat pump mock-up with the attached silencer; filled   with  porous absorber (PA).

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000005_cca7c985f544333b25539a7057b9cb67a57044a97173fb893ef773fa25b3eb02.png)

To protect absorbers from dirt and mechanical damage [3], the inner absorber cylinder was encased with the perforated plate (PP) while the outer absorber was covered with either PP or micro-perforated plate (MPP) The geometrical properties of both sheet metals are listed in Table 3. In the present investigations, the MPP is not used as an acoustic absorber; but rather as an alternative absorber protection with less porosity than the PP: ring

Table 3. Properties of the two sheet metals used in the experiments\_

| Sheet Metal     |   Hole Diameter (mm) |   Period (mm) |   Sheet Thickness (mm) |   Porosity (%) |
|-----------------|----------------------|---------------|------------------------|----------------|
| Perforated      |                  1.5 |             3 |                    0.7 |           19.7 |
| Microperforated |                  0.7 |             3 |                    
<!-- PAGE 7 -->
0.7 |            4.3 |

## 3.2. Acoustic Helmholtz Resonator

To handle tonal peaks at the relevant BPFs and their harmonics in the low-frequency range, Helmholtz (HH) resonators are an effective alternative. A HH resonator consists of a connecting orifice and a backing volume: Compared to the porous absorbers, the HH resonator is found to produce only narrow-band attenuation (See Figure 4). The peak frequency is controlled by the shape of the orifice and the size of a backing volume [18]: Figure 4 shows the sound attenuation of the HH Resonators that were used in this study The resonance frequency is observed to be at 125 Hz to dampen the BPF

Figure 4. Sound attenuation curve of the applied Helmholtz resonator Fraunhofer IBP) .

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000006_bde4156fecead38f1b8b0bebb799d4d70fa4edb404d48d5b7c1d91e27f452c80.png)

As shown in Figure 5, a total of eight HH resonators (green boxes) were attached to the outlet of the absorber (orange ring) For geometrical reasons, the diagonally placed resonators were mounted on the channel with their short front side. ring

Figure 5. Simulation model with absorber ring (orange) and Helmholtz resonators (green).

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000007_2fa39bdfddd2291ece669bade249cb09ebe69069f9f75792d829b5431a9aa84c.png)

The back volume of the resonators was defined by a simulation study to achieve the desired resonant frequency of 125 Hz, which is close to the BPF for the fan of 1060 rpm. Figure 6 shows the inner dimensions of the resonators.  The length of the resonator orifice corresponds to the thickness of the wooden wall, which was 15 mm, and it had a diameter of 50 mm The volume of the vertically and horizontally mounted resonators was VRI 0.0075 m3 , whereas the volume of the diagonally placed resonators was 0.0064 m3 . As can be seen in Figure 6b, the back volume of the diagonally placed resonators had to be reduced due to the changed hole position. speed VR2

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000008_de918af0463b68089e3e33fad7931ab109cef017a3f812059fcf6c6f6155e350.png)

39.2 cm

Figure 6. Geometries with inner dimensions of (a) horizontally and vertically placed resonators and (b) diagonally placed resonators.

## 4. Acoustic Simulations

To estimate the effect of a passive control techniques for heat pumps, the first step was to perform Finite Element Method (FEM) simulations with the simulation software COMSOL Multiphysics a simplified model. Due to limited computing capacities; the frequency at 2820 Hz was defin
<!-- PAGE 8 -->
ed to be the highest frequency for the calculation of sound attenuation. Hence, the highest third octave band in which the damping was calculated was the one with a center frequency of 2500 Hz. At this upper limit, the minimum wavelength is Amin co/f = 0.137 m. By using six elements per wavelength at the upper frequency limit of 2820 Hz and co = 343 m/s as the of sound in air, the maximum element size is obtained with Equation (1): using speed

$$\Delta _ { c l l } = \frac { \lambda _ { \min } } { n } = \frac { c _ { 0 } } { f \cdot n } = \frac { 3 4 3 \, m \cdot s ^ { - 1 } } { 2 8 2 0 \, H z \cdot 6 } = \, 0 . 0 2 \, m .$$

## 4.1. Effect of the Acoustic Silencer

Figure 7a illustrates a heat pump with an acoustic silencer; highlighting the mod elled in FEM with a dotted red line. As shown in the figure, instead of a rotating sound source, the rotating blades of a fan, in the simplified model, a plane sound wave with a constant sound pressure level of p = 1 Pa (peak amplitude, Lp = 91 dB) was defined for the inlet side using the plane-wave radiation node. At the outlet side, a plane-wave radiation condition was applied to allow an outgoing plane wave to leave the modelling domain with minimal reflections. The inner cylinder was divided into three sections. Up to the silencer inlet and behind the silencer (blue areas) , the cylinder surface was defined as an impervious sound reflecting wall. Inside the cylinder in front of the motor and in the outer absorber ring (dark grey areas) , a porous absorber was covered by a perforated sheet. The porous absorber was modelled by the equivalent fluid model with Delany-Bazley-Miki parameters with a flow resistivity of = 11,000 Pa s m 2 while both perforated plates are modelled as acoustic impedance layer with a complex impedance that includes both resistive (dissipative) and reactive (inertial) effects. As a medium of propagation, air at a temperature of 20 C and density of 1.2 kg/m3 was defined. As shown in Figure 7b, the frequency-dependent sound power attenuation was calculated by determin the difference between the sound power on the source surface (Lw1) and the outlet surface (Lw2). part using an ing

=9.6cn

Hx

Figure 7. (a) Sketch of the heat pump mock-up with an acoustic silencer (PA porous absorber) , highlighting the modelled in FEM with a red dotted line; (b) FEM-model of the duct with silencer. part -

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000009_adfa01746f477fd049a288857fd1fa997bf313e93a1c34e8b402a8da9350d517.png)

Within the numerical study, three silencer lengths and three absorber thicknesses dA were studied to investigate their effect on the radiated sound power: Table 4 gives an overview of the investigated silencer configurations. Apart fro
<!-- PAGE 9 -->
m dA = 0.05 m, the specific flow resistance of the absorber; the product of the length related flow resistivity and the absorber thickness were in the recommended range of the acoustic absorber suggested by Fuchs [17]: Lsil

$$8 0 0 \ P a s \ m ^ { - 1 } < \Xi \cdot d _ { A } < \ 2 4 0 0 \ P a \ s \ m ^ { - 1 } .$$

Table 4. Investigated silencer configurations in the numerical study (all parameters) and experimental study (parameters without parenthesis) .

| Parameter              | Unit   | Value            |
|------------------------|--------|------------------|
| Silencer length, Lsil  | m      | 0.2, (0.25), 0.3 |
| Absorber thickness, dA | m      |                  |

Figure 8 shows an example of the calculated distribution of sound pressure levels (dB) at 1000 with Lsil = 0.2 m and dA 0.05 m. The result clearly shows the reduction of the sound pressure level in the duct generated by the silencer: While the sound pressure levels on the inlet side in front of the silencer are as high as dictated in the boundary condition, the low sound pressure level values on the right side, the outlet side, demonstrate the effect of the silencer. To highlight the effect of the absorber; two measured sound power spectra were shown for the two fan speeds 635 rpm and 848 rpm in Figure 9\_ The black, continuous spectra represent the initial situation of the measured sound power without silencer ("no silenc.") The experimental setup for the sound power measurements is presented in Section 5.1.

The other curves show the predicted sound power level the measured sound power with the simulated sound attenuation by the porous absorber of thicknesses 0.05 m (blue dashed) , 0.1 m (green solid) and 0.15 m (orange dotted) with a silencer length of 0.3 m It must be noted that the simulated attenuation is independent of the fan because the fan was replaced by the plane sound wave Due to the upper bound of the frequency range in the simulation; the attenuation above 25 kHz is set to zero For both operating points, the calculations prove that the porous absorber can significantly reduce the level maximum within the medium- to high-frequency range. using speed setting

Figure 8. Sound pressure level distribution in the duct and the silencer of Lsil 0.2 m and dA 0.05 m at 1000 Hz\_

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000010_2a8874ebe9894cc75b9f02d340230f636ff624de376265e14d3868ba58e87e07.png)

Figure 9 Measured A-weighted sound power spectra without a silencer (~) and with the simulated attenuation due to silencer use of Lsil

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000011_0f68312972708bb577f4fe514b6e5313e8910a55bf2844b0a9f
<!-- PAGE 10 -->
25002688de171.png)

At low frequencies, where the absorber thickness is shorter by far than one quarter of the wavelength, the silencer is ineffective: The curves for the thickness of 0.10 m and 0.15 m are almost identical, thus indicating that increasing the thickness of the absorber has no further effect on the overall sound power level. Figure 10 summarizes the calculated overall sound power level reduction for configurations with different silencer lengths and absorber thicknesses. The different silencer lengths are represented by the different line styles, solid lines denote Lsil 0.2 m, dashed ones are Lsil 0.25 m, while dotted one are LSil 0.3 mDifferent colors represent the different fan speeds. As expected, the highest attenuation is obtained with the maximum length of the silencer, Lsil = 0.3 m. The maximum reduction in the overall sound power level of 4.4 dB was measured at the speed of 423 rpm. On the other hand, no significant increase in attenuation was obtained in the simulations by increasing absorber thicknesses above 0.10 m for all This indicates that a further widening of the absorber ring does not result in meaningful sound attenuation in the present application. ie ALw speeds.

Figure 10. Calculated overall sound attenuation with different silencer lengths and absorber thick nesses. (-) Lsil = 0.2 m, (~) Lsil = 0.25 m, () Lsil 0.3 m; (a) 423 rpm (orange) 635 rpm (green); (b) 848 rpm (blue) 1060 rpm (red).

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000012_b6b9a66f36c786867b96295eba6158ad9b4ce73ddd58604ba73d4d7c287f7c00.png)

## 4.2. Effect of Helmholtz Resonators

The simulated sound power curves shown in Figure prove that the acoustic silencer is inefficient in the low-frequency range. Figure 9 also clarifies how the reduction in the levels in the mid-frequency range results in the tonal peaks in the low-frequency range becoming level-determining; As described in [19], acoustic resonator concepts in particular represent an effective alternative to silencers in the low-frequency range.

As presented in Section 3.2, in total, eight HH resonators were placed at the outlet of the absorber ring. It must be noted that the length of the duct of the simplified simulation model was extended by 0.1 m in the flow direction for the attachment of the resonators while the length of the silencer, Lsil, remained the same. Again, as in the previous model, a free outflow condition was at the outlet side. The resonators were designed to resonate at 125 Hz for the presentation of the sound pressure distribution. applied

Figure 11 shows the calculated sound pressure levels in the horizontal and ver tical symmetry planes of the simulation model with the porous absorber and eight HH resonators.

Figure 11.
<!-- PAGE 11 -->
 Calculated sound pressure level distribution with a silencer of Lsil = 0.3 m and dA = 0.15 m and resonators at 125 Hz

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000013_a50868ad08c8bfb8ee34a415f873c1734a59ab1301c6e5869f58a19a0d268a69.png)

There are constant sound pressure levels Lp = 91 dB in the area in front of the entry into the reactive silencer. After entering the reactive silencer; there is a reduction of the sound pressure in the duct right up to the outlet side to approximately Lp = 75 dB. As

expected, the lowest levels occurred directly in front of the resonator outlets, with sound pressure levels of Lp 55 dB.

## 5. Measurements

The simulation study confirmed that the applied passive control techniques with the acoustic silencer and HH resonators can effectively reduce the emitted sound power. In this section; the effect of the silencer is experimentally examined.

## 5.1. Experimental Setup

A schematic view of the measurement setup to characterize the sound-reducing measure is given in Figure 12. To ensure a low sound reflection on the inlet side, the heat pump mock-up was positioned in the semi-anechoic chamber close to the installation wall. A installation wall was designed to separate the semi-anechoic field and the reverberation chamber with an exhaust outlet. At the outlet side, the air was blown out into a reverberation chamber. For the exhaust air from the reverberation chamber; the air outlets in the wall as well as the door were constantly kept open with a defined gap width. Figure 12b shows the measurement setup in the reverberation chamber with the position of the six microphones and the place for the reference sound source. The sound power was determined the comparison method with a reference sound source according to [20]. Table 5 summarises the measurement equipment which is used for sound power determination and the calibration of the The frequency range of the microphones extends from approximately 3.15 Hz to 20,000 Hz with a sensitivity of 50 mV Pa top special using setup.

Figure 12 (a) Sketch of the experimental setup (not true to scale); left side semi-anechoic chamber; right side reverberation chamber; (b) Measurement setup in the reverberation chamber to measure the sound attenuation with positioned reference sound source:

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000014_bcf98b6bb7e337d310e923e9a0158186b6d6d79570173aa73c26f914ed2801dd.png)

Table 5. Measurement equipment for the determination of sound. used

| Type                   | Model                        | Manufacturer   |
|------------------------|------------------------------|----------------|
| Microphone
<!-- PAGE 12 -->
s            | 1 inch; Type 46AE            | GRAS           |
| Calibrator             | 4231 (94 dB SPE bei 1000 Hz) | Bruel & Kjaer  |
| Reference Sound source | Model 4204                   | Bruel & Kjaer  |

Figure 13a shows the mock-up's rear side, which was placed in the semi-anechoic chamber to minimize any reflections back into the mock-up or into the reverberation chamber:  Figure 13b shows the outlet side of the heat pump mock-up with an attached silencer filled with the porous absorber; Caruso-ISO-Bond

Figure 13. Experimental setup for investigating the silencer concept: (a suction side in the semi anechoic chamber; (b) outlet side of the heat pump mock-up with an attached dissipative silencer:

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000015_7c922f377d8accd8be941b2a1d4d718040377d1faf6f72a088ed6889a2ebc6d4.png)

## 5.2. Effect of the Acoustic Silencer

Based on the experimental setup described in Section 5.1, the following subsection focuses on the sound attenuation of the silencer and its influence on the acoustic spectra.

As a starting point, the heat pump mock-up with a free blowing fan and no attachments was positioned at the installation wall. Similar to the numerical study, two silencer lengths and three absorber thicknesses were examined. The maximum absorber thickness was specified as dA 0.15 m due to the limitation of the installation wall between the semi anechoic and the reverberation chambers .

Figure 14 shows the sound attenuation of the silencer with dA = 0.15 m and Lsil 0.3 m with the perforated sheet metal for different fan speeds (dashed curves) The sound attenuations show similar spectra for all operating points. For the comparison with the simulation results, the sound attenuation was averaged over all fan speeds and was added as a solid black curve The maximum sound attenuation of 10.7 dB was measured at 423 rpm, in the third octave band around 400 Hz. there are deviations in the curves, which are due to the different spectrum characteristics in this frequency range, determined by the tonal peaks of the blade passing frequency and partly also by its first harmonic. Hz,

Figure 14. Measured sound attenuation with the silencer of dA 0.15 m and Lsil = 0.3 m with the perforated sheet metal for different fan speeds: 424 rpm (~), 635 rpm (~),848 rpm (~) 1060 rpm (~), average ( )

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000016_3c0a564cf8fda0f7927c16729e6ba499c841ea1cabb2553dcd0d47e7a1c613c4.png)

In the frequency range between 160 Hz and 500 Hz; the curves show a strong increase in sound attenuation, which can be explained by the effect of the porous absorber (see Figure 2)
<!-- PAGE 13 -->


Due to the undisturbed passing of higher frequencies through the silencer; above the third-octave band of 1600 Hz the sound attenuation decreases continuously. Above 4000 Hz, the maximum differences of about 2 dB occur in the sound attenuation. Figure 15 gives an overview of the investigated silencer configurations with the corresponding measured overall sound power level reductions. Looking at the configurations with the length = 0.2 m (dashed lines) , an increased level reduction with higher absorber thickness is evident for all fan speeds. For the speeds 424 rpm (orange) , a level reduction in the overall sound power level of 4.0 dB was achieved with the installed perforated plate and thickness of d3 0.15 m The same configuration resulted in a maximum 4.2 dB at 848 rpm (blue). In contrast; at maximum fan of 1060 rpm (red), only reduction in the sound power level of 3.0 dB was measured. again Lsil ALw ALw ALw

Figure 15. Measured sound attenuation caused by the silencer with different lengths and absorber 0.2 m, (-) Lsil 0.3 m; (a) 423 rpm (orange), 635 rpm (green); (b) 848 rpm (blue) 1060 rpm (red)

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000017_6b774a45e82d031cb5bd4816c5444b20aa1899a5f5e6622b9e38533c7c0ca8df.png)

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000018_165def5f9d1a79e9f9c38d58ec290d6d6f03d944015172813c691f633530a262.png)

Extending the silencer up to 0.30 m (dotted lines) increases the sound attenuation as expected. However; the measured values show that lengthening the silencer by a factor of 1.5 is not accompanied by an equivalent sound attenuation. Only at 423 rpm (orange) and 848 rpm (blue) the sound attenuation in the overall sound power level is increased by a factor of 1.5 and 1.4, respectively but others are not This uneven change is due to the different source spectra. Since a single number is calculated by the power summation of all frequency bands, the value is often controlled by the peak value. Therefore, when similar noise reduction is applied in all cases.

Figure 16 compares the measured A-weighted sound power spectra with different silencer lengths covered by PP. The graphs confirm the maximum level reduction in the third-octave spectra around 500 Hz as shown in Figure 16. The diagrams again illustrate that with the porous absorber; the peaks in the low-frequency range of the spectra BPF) are attenuated either only weakly or not at all. The silencer has no effect on the tonal at 74 Hz with 635 rpm. At 848 rpm, at least the level of the first harmonic of the blade passing frequency around 200 Hz was reduced by 6 dB with a length of 0.3 m due to the shift of tonal peaks. p
<!-- PAGE 14 -->
eaks ALw

As a next a comparison with the different sheet metal is shown (see Figure 17). As can be seen in the spectra, the MPP causes reduction in the levels at the low-frequency tonal peaks at 74 Hz in the spectrum ALw 2 dB, and only ALw = 0.8 dB at 848 rpm. However; when considering the range of medium frequencies between 250 Hz and 2000 Hz, the installation of the perforated sheet metal proves to be significantly more efficient for sound attenuation. In the above-mentioned range, a level reduction of up to 13.3 dB step, ALw

at 630 Hz is achieved with the PP, and at 848 rpm up to = 9.4 dB at 400 Hz. The results show that the low porosity of the micro-perforated resulted in an excessively high flow resistance on the facing: Consequently; the acoustic particle velocity at the panel surface was strongly attenuated, preventing effective sound energy transmission into the but rather as a resistive barrier, which inhibited the intended dissipation mechanisms in the backing material. ALw panel facing

Figure 16. Measured A-weighted sound power spectra without the silencer and with the silencer of dA 0.15 m and of Lsil = 0.2 m (--), or Lsil = 0.3 m '); (a) 635 rpm; (b) 848 rpm.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000019_2920677f330de48e53d3c5e0a4d2c812f1f8f9c754e10db586de10c1fc333ac5.png)

Figure 17. Measured A-weighted sound power spectra without the silencer and with the silencer of dA 0.15 m and Lsil 0.3 m covered by MPP ");(a) 635 rpm; (b) 848 rpm

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000020_6bb66ceafb09214d4a63b284d1279597fa3d89d8ac680eb1990fbe852aa72d5a.png)

Figure 18 shows the A-weighted sound power spectra in third octave bands with the silencer of 0.3 m length and with different absorber thicknesses. In Figure 18a-d, the solid black line represents the initial without an attached silencer. It can clearly be seen that in the frequency range between 250 Hz and 1000 the acoustic silencer provides performance in reducing broadband sound. A striking feature in the spectra for the fans speed of 635 rpm and of 1060 rpm is the jump in sound attenuation around 500 Hz via the doubling of the absorber thickness. The latter leads to a minimum sound attenuation of 4.7 dB at 1060 rpm. setup Hz, good ALw

Figure 18. Measured A-weighted sound power spectra without the silencer (-) and with the silencer of Lsil 0.3 m and dA 0.05 m (~), dA 0.10 m (), dA (c) 848 rpm, (d) 1060 rpm

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000021_acb5b3c4c1e3a661424a78f93e2445159689414ba8189ba47296bc2d6fae9f28.png)

As can 
<!-- PAGE 15 -->
be seen in Figure 18, installing the silencer can also lead to level increases , specifically in the 1/3 octave band centred at 160 Hz at all operation In addition to the measurement uncertainties, as variations of up to 4l dB are common, the silencer housing could be the cause of the level increase. Since the increase occurs at all operating points, structural resonance of the housing could be a contributing factor: However; based on the existing data, the exact cause of the level increases at BPF harmonics cannot fully explain the observed level increases. The results illustrate that after the application of the silencer; the sum levels are determined by the low-frequency tonal components. 1060 rpm, for example  a level reduction of = 9.2 dB could be achieved in the one-third octave band around 1000 Hz, but for an improved low-frequency sound attenuation; the thickness of the porous absorber would have to be increased. speeds. At ALw

## 5.3. Effect of Helmholtz Resonators

As a next step  additional resonators were installed on the silencer. While the pre-vious subsection addressed broadband attenuation achieved by the silencer; the following section investigates narrowband noise reduction using Helmholtz resonators The resonators were attached to a silencer with the length of Lsil 0.3 m Figure 19 shows the installation of eight resonators symmetrically mounted at the outlet of the silencer: Due to the angular geometry, a smooth transition between the silencer and the resonators could not be realized.

Figure 19. (a) Fully silencer-resonator concept, silencer with PP and HH resonators; (b) Zoomed in view. applied

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000022_b28bccb003da4a604af25e433353239a69d83a26ccf0c54f50e9eadfe170dcbf.png)

Figure 20 shows the comparison of the sound power spectra without the silencer and with the combination of silencers and resonators. In contrast to the measurements without resonators (Res. closed) the sound power level in the one-third octave band around 125 Hz was reduced by 6 dB. Consequently; the attachment of the resonators also has an effect on the overall sound power level\_with all resonators open, the overall sound power level could be reduced by = 7.7 dB compared to the initial ALw ALw setup.

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000023_6ff75b86539d6ed7b812ba3cac53c2aee6b94b42e69a1426ca6899e52bcab6d4.png)

Frequency (Hz)

Figure 20. Measured A-weighted sound power spectra without the silencer (-), and with the silencer of dA 0.15 m and Lsil 0.3 m and the HH resonator but closed hole and the fully applied silencer-resonator concept ()

In the presence of a graz
<!-- PAGE 16 -->
ing mean flow over the neck of a Helmholtz resonator, the grazing flow effect may occur [21] A shear layer develops at the aperture and interacts with the oscillatory particle velocity in the neck, altering the complex acoustic impedance; which can shift the resonance frequency, increase damping and, under certain conditions , reduce the resonator S absorption effectiveness. Due to the air flow through the neck, there is a potential risk of coupling between vortex shedding and the acoustic field, which may lead to flow-induced resonance under specific flow velocities and geometrical configurations of the neck. In the present study, however; no flow-induced tonal noise was observed.

## 5.4. Comparison of Experiments and Simulations

To assess whether the experimentally observed trends can be reproduced numerically, the final subsection presents a FEM-based validation of the measured results. For the comparison; the experimentally determined sound attenuation at 1060 rpm, as well as the configuration with Lsil 0.3 m and dA = 0.15 m. First, the comparison of the frequency dependent sound attenuation is considered in Figure 21a. The dashed line represents the simulated frequency-dependent sound attenuation, while the solid curve presents

the measured and averaged sound attenuation (see Figure 14) of the silencer\_resonator concept. The grey areas in the figures indicate the range above the frequency limit from the simulation. In general, the results show fairly agreement between 100 Hz and 1000 though the sound attenuation is underestimated by the simulation throughout almost the entire frequency range. good Hz,

Figure 21. (a) Simulated and measured sound attenuation for the fan of 1060 rpm (~); (b) Measured A-weighted sound power spectra without the silencer; with the silencer of Lsil = 0.3 m and dA 0.15 m (~) and measured A-weighted sound power spectra in the initial situation with simulated attenuation due to the silencer (--)speed

![Image](D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output_artifacts\image_000024_327c4c06eb9cbad65e496b6bef6a88cc1b3d4578b2cc59f08441db4e2ff6e029.png)

The general underestimation of the simulation is due to simplifications made in the simulation model, such as a plane-wave sound source and neglecting the air flow. A plane-wave source mainly excites the fundamental mode and may not effectively excite higher-order modes or complex sound fields, which is important for accurately representing tonal peaks in some geometries. In real environments , there are reflections and a diffuse sound field with various angles of attack, whereby a plane-wave source assumes uniform sound propagation. At the outlet, an outgoing plane wave was applied as a boundary condition, whereas in the sound propagates spherically into 
<!-- PAGE 17 -->
the room In the present simulation model, the airflow is not considered; the FEM model describes only the propagation of a plane wave within the duct. Consequently; flow-induced noise is not modelled. Also; the structural vibrations of the mock-up and the resulting sound radiation into the room are not considered in this study. using reality

Below 100 Hz, the sound attenuation differs by up to 2.5 dB. The negative values in this range of sound attenuation indicate a level increase due to the attachment of the silencer and the resonators The effective frequency of the resonators is also clearly visible in the simulations. The measurement shows clear peaks in the range of the first and second harmonics of the BPF, and thus an improved attenuation effect at 250 Hz and 375 Hz. In contrast, these do not appear in the simulation results, which results in a difference between the simulation and the measurement up to 3.4 dB at these positions. The latter is related to the definition of a plane wave as a sound source. Especially with the blade passing frequency and its harmonics, an oblique sound incidence occurs in the duct under real conditions , whereas this does not occur in the simulations due to the simplified boundary conditions. In the upper frequency range from 1000 Hz to 2500 Hz, both the measured and the simulated sound attenuation The decrease in the sound attenuation in this range of the measured and calculated sound power spectra is shown. Due to the simplified assumption; the calculated sound attenuation around the BPF and its harmonics cannot be represented as in the measurements In the real model, however; transverse duct modes peaks drop.

and an oblique sound incident additionally cause an increase in sound attenuation at these frequencies (see Figure 21a)

## 6. Conclusions

This paper presents experimental and numerical studies on a sound attenuation concept; applied to a heat pump mock-up. This investigation contributes to lowering the barrier for heat pump installation; especially in dense urban areas where the mitigation of noise sources is of great importance.

This is comparable to the 7.8 dB reported when using active noise control (ANC) in [8].  Although ANC offers a more compact solution, which is advantageous in spaceconstrained applications such as heat pumps, the passive method presented here provides similar attenuation without the need for electrical power. However it is an ongoing process to make the silencer-resonator concept more compact for an easier installation on heat pumps.  Furthermore, the additional costs associated with installing the resonators are considered to be very low. Especially in the higher-priced segment where acoustics are a parameter, are a cost-effective way to improve acoustics. Maintenance costs are also considered to be very low; as consist of only 
<!-- PAGE 18 -->
a hollow body and can, ideally, be integrated into the air duct. Moreover; the presented concept can be combined with other acoustic treatments , such as MPA [6] or the optimization of fan geometries [2-5] or various air duct optimisation: they key they

Initially; the effectiveness of the concepts was simulated by FEM with a simplified simulation model and a plane wave as a sound source\_ With the simplification of the sound source, the effect of a silencer-resonator concept was validated in the simulation study. As a next the silencer-resonator concept was applied to the heat pump mock-up. The experimental results verified that the simplified simulation model can well the actual performance of sound attenuation concepts. The numerical model captures the broadband acoustic trends in a qualitative manner; however; it fails to reproduce the observed tonal components. This limitation arises from the plane-wave assumption employed in the simu for tone generation. Consequently; the model is suitable for predicting overall broadband behaviour but not for resolving narrowband or tonal features.  Within the experimental studies, several silencer lengths and absorber thicknesses were investigated. The results show a sound attenuation of the mid-frequency range around 1000 Hz through the porous absorber: By reducing the sound power level around 1000 tonal peaks at low frequencies have a greater influence on the overall sound power level.  This is why HH resonators were additionally applied on the pressure side of the heat pump mock-up. With this measure, the BPF for a fan speed of 1060 rpm was reduced by about 6 dB. The latter led to a total reduction in the overall sound power level at this fan of 7.7 dB. step, predict good Hz, speed

The developed silencer concept for heat pumps reduces noise emissions while only minimally affecting the efficiency of the airflow path.   Compared to so-called acoustic enclosures , the additional airflow resistance is significantly lower: It also offers a clear advantage over concepts involving strong flow redirection in terms of pressure loss and energy efficiency:

However; it should be noted that the current design limits their application to industrial heat pumps at the most. For this reason, the resonators for heat pumps in the 5 kW-15 kW range (single-family houses and small multi-family houses) would have to be adapted to the individual size and tested with the new To guarantee the acoustic to its integration into the air duct, the absorber is already well protected against sunlight:. Nevertheless, temperature fluctuations, humidity and dirt can influence absorption belarge design.

## References

- 1 Graf, HR. Luft /Wasser-Wärmepumpenanlagen Grundlagen und Massnahmen; Federal Office of Energy: Ittigen; Switzerland , 2002. Available online: https: , /laerm.ch / wp-content
<!-- PAGE 19 -->
 / uploads / waermepumpen\_bae pdf (accessed on 18 January 2026).
- 3 Krömer; FJ.; Becker; S. Off-Design Sound Emission of Low-Pressure Axial Fans Under Distorted Inflow Conditions: An Experimental Study. Acta Acust. United Acust. 2019, 105, 95-108. [CrossRef]
- 2 Krömer; F; Becker, S. Experimental investigation of the off-design sound emission of low-pressure axial fans with different fan blade skew. In Proceedings of 1lth European Congress and Exposition on Noise Control Engineering (Euronoise), Crete, Greece, 27-31 2018. May
- Zhao, X; Sun, J ; Z. Prediction and measurement of axial flow fan aerodynamic and aeroacoustic performance in a split-type air-conditioner outdoor unit. Int. J. Refrig. 2013, 36, 1098-1108. [CrossRef] Zhang'
- 5 of 3D-Metal-Printed Perforated Leading Edges on Airfoil and Axial Fan Noise. In Proceedings of the AIAA Aviation 2020 Forum, Virtual Event, 15-19 June 2020; American Institute of Aeronautics and Astronautics: Reston, VA, USA, 2020; p. 06152020, ISBN 978-1-62410-598-2.
- Czwielong F; Floss , S.; Kaltenbacher, M; Becker; S. Sound reduction in heat exchanger modules by integrating plate absorbers with sub-millimeter openings. Acta Acust. 2021, 5, 35. [CrossRef]
- 8 Gustafsson O.; Haglund Stignor; C ; Dalenbäck, J.-O. Heat exchanger aspects related to noise in heat pump applications. Appl. Therm. 2016, 93, 742-749. [CrossRef] design Eng;
- Lucius , A. Schneider; M; Aeroacoustic Simulation and Experimental Validation of Sound Emission of an Axial Fan Applied in a Heat Pump. In Proceedings of the International Congress on Acoustics 2019, Aachen, Germany, 9-13 September 2019.
- 9 indirect noise levels in heat pump applications. Appl. Therm. 2014, 66, 104-112 [CrossRef]
- HPT\_Heat Pumping Technologies. Final Report\_Part 9 Annex 51: Acoustic Signatures of Heat PumpsHPT\_Heat Pumping Technologies. Available online: https: / /heatpumpingtechnologies org / publications / final-report-part-9-annex-51-acousticsignatures-of-heat-pumps , (accessed on 16 July 2025).
10. Anai, K; Kato S. Applicability of Active Noise Control Technique to Heat Water Heater for Household Use: In Proceedings of the International Congress on Sound and Vibration 2021, Virtual, 11-16 July 2021 . Pump
12. Wagner; S.; Rohlfing, J. Effects of the fan-heat exchanger interaction on the noise emission of heat pumps: Experimental and numerical studies. In Proceedings of the FAN2022 Conference, Senlis, France, 27-29 June 2022
- 13 Wagner; S.; Adachi, S. Simulationsbasierte und experimentelle Untersuchung der Strömungsakustik von Wärmepumpen. In Proceedings of the DAGA 2020, Hannover; Germany, 16-19 March 2020.

haviour.  For instance, alternative porous materials with higher mechanical robustness , such as porous metals metal-rubber composites, porous aluminium or comparable structures) , could be considered. In add
<!-- PAGE 20 -->
ition; the porous absorber can be protected by an acoustically transparent covering layer such as fiberglass fabric, which would significantly enhance resistance to mechanical wear and environmental influences while preserving the acoustic performance: To further improve sound attenuation; acoustic simulations with moving noise sources will be performed. (e.8-

Author Contributions: YA. review editing and supervision, S.W. methodology; investigation and writing: All authors have read and agreed to the published version of the manuscript:.

Funding: The authors would like to thank the Federal Ministry for Economic Affairs and Climate Action (BMWK) and the Project Management Agency Jülich (PTJ) for their founding and support of the project QUEEN-HP MENESA, funding number O3EN4043.

Data Availability Statement: The data and results involved in this study have been presented in detail in the paper.

Conflicts of Interest: Author Sebastian Wagner is an employee of Bosch Home Comfort Group GmbH. The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

- 14 Comsol Multiphysics GmbH. COMSOL Multiphysik-Software zur Optimierung von Designs. Available online: www.comsolde / (accessed on 13 March 2023). https: /
- 16 W. Schalldämpfung der Ansauge- und Auspuffgeräusche von Dieselanlagen auf Schiffen. VDI-Z 1937, 81,770-776. Piening'
15. Fasold, W; Veres, E. Schallschutz und Raumakustik in der Praxis: Planungsbeispiele und Konstruktive Lösungen, 2nd ed.; Huss-Medien Verl. Bauwesen: Berlin, Germany, 2003; ISBN 3345008017.
- Fuchs , HV. Schallabsorber und Schalldämpfer: Innovative Akustische Konzepte und Bauteile mit Praktischen Anwendungen in Konkreten Beispielen , 2nd ed.; Springer: Berlin / Heidelberg, Germany, 2007; ISBN 9783540356226.
18. ISBN 9780415237291.
19. Cai, C.; Mak, CM; Wang X. Noise attenuation performance improvement by adding Helmholtz resonators on the periodic ducted Helmholtz resonator Appl. Acoust. 2017, 122, 8-15. [CrossRef] system.
21. Dickey, NS.; Selamet, A.; MS An experimental study of the impedance of perforated plates with grazing flow: J. Acoust Soc. Am. 2001, 110, 2360-2370. [CrossRef] [PubMed] Ciray
20. DIN 3741.2011-01; Akustik\_Bestimmung der Schallleistungs-und Schallenergiepegel von Geräuschquellen aus Schalldruckmessungen\_Hallraumverfahren der Genauigkeitsklasse, 1. Beuth GmbH: Berlin, Germany, 2011. Verlag

DisclaimerlPublisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and /or the editor(s) . MDPI and /or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content:.