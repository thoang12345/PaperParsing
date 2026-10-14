## IntroducƟon

The goal of this project is to design an alarm clock uƟlizing the tools and equipment that we have learned about up to this point in the semester. Technical requirements for the design of the alarm were to include a potenƟometer to adjust Ɵme, incorporate at least one switch to control the countdown, use a seven-segment display to visibly display the countdown, and to sound an audible alarm with a piezo buzzer. This set up is a very simple, but applicable design to show how a countdown Ɵmer might perform on a small scale. To accomplish this goal, I knew I wanted to add addiƟonal switches to beƩer control the funcƟons of starƟng, stopping, and adjusƟng the alarm clock countdown. The potenƟometer, piezo buzzer, and seven segment display were easy to visualize and incorporate due to recent experience in other lab assignments. In terms of design layout, I wanted to keep it simple and easy for me to keep track of. I first built a circuit that included all required equipment and assigned pins to necessary inputs and outputs. Reusing some coding and circuit layout from previous exercises, including Lab 4, Lab 3, and Lab 2 material streamlined this process.

## Project 1 EMCH 368-003 Christopher Flohr Joud Satme 2/28/26

----page-break-here----

## Materials

- -UNO R3 Controller Board- This microcontroller provides digital and analog input/output pins, power regulaƟon, communicaƟon. It acts as a programmable environment to control the behavior of the alarm clock.
- -830 Tie-Points Breadboard-The breadboard acts as a medium to connect electrical components for the circuit.
- -BuƩon (x3)- A switch interrupts the flow of electricity. In this seƫng, the switches momentarily complete a circuit that calls for a change of state in the circuit.
- -Breadboard Jumper Wires-Wires electrically connect different components.
- -Resistors (x7)- resistors are components that resist flow of electrical energy. In this seƫng the resistors are added to protect electrical components in the circuit.
- -Piezo Buzzer-A small element that vibrates when it receives electricity. In this case, we use the piezo to receive a signal when the alarm hits zero, to give an audible element of the alarm clock.
- -4 Digit 7-Segment Display- A device used to show numbers. In this circuit, the 7segment display will visibly display the countdown.
- -PotenƟometer- A variable resistor with three pins. The middle pin moves across the resistor to provide variable resistance. In this seƫng, the potenƟometer's variable resistance is equated to a varying amount of Ɵme on the clock.
- -USB Cable- Universal Serial Bus cable is a communicaƟon and power cable to connect the circuit to a computer. In this project, the USB cable uploads the program code to the Arduino board and provides power to the circuit.

----page-break-here----

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000000_7636dbbb0e9f902fd8c4614b3968eb286ca579e6d2731e2d25a318202a3beae9.png)

Figure 1- UNO R3 Controller Board [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000001_5e644dffad49e5f28b399a1fde8ed7b7ba60c4cea4e5a5a40eda7c947a67d12a.png)

Picture description: The image shows a close-up of a breadboard with a white background. The breadboard is divided into rows and columns, with each cell containing a series of small holes. The rows are marked with red lines, and the columns are marked with blue lines. The breadboard appears to be empty, with no components or wires connected to the holes. There are no important labels, values, or relationships discernible from the image.

Figure 2- 830 Tie-Points Breadboard [1]

Figure 3- BuƩon (x3) [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000002_8bc304675eeb31370e2a0f80c853abb384d9c1b2877212c6e5cc8297b6b42428.png)

Figure 4- Breadboard Jumper Wires [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000003_96c0ebda53520761db400a5183532037a9c7c286ef21366c5f9c00ec96a56179.png)

----page-break-here----

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000004_9c43c35f7abf8aa249de3195bdbcd3d4aa908565437b52e3e9ceae32a1480de4.png)

Figure 5- Resistors (x7) [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000005_335036442c384cdc64a13a2d1dfce9d916e5225e0943af93e71fdb63176c0010.png)

Figure 6- Piezo Buzzer [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000006_b322a1a7997b2632426337ddf74afcda410d76e9680939b3084b59ff064292d0.png)

Figure 7-4 Digit 7-Segment Display [1]

Figure 8- PotenƟometer [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000007_6555c7ee8161ca12bc64e7416349688cb483e72b9213db638c80c272f11cacb2.png)

Figure 9- USB Cable [1]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000008_0a8d6781d5326d890d619fac243a3ae68152aee4e0ed400a6d366fe79e9700e8.png)

----page-break-here----

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000009_e8bc82fdb8b3f5af436d1aed522cb99ff58054519d410939c3e2cc42a334ac65.png)

Figure 10-SchemaƟc RepresentaƟon of Electrical Circuit [2]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000010_286e1aefcc31a8c0e48f823f1adc3cc8ebb4c6ce1f446323801af128fddc2bf8.png)

Picture description: The figure is a circuit diagram for a digital clock project. It consists of a breadboard with various electronic components connected to it. The main content includes a 7-segment display, a 555 timer IC, a 10kΩ resistor, a 100nF capacitor, and a 10kΩ potentiometer. The 7-segment display shows the time "8:08". The 555 timer IC is used to generate a square wave signal, which is then used to control the 10kΩ resistor and the 100nF capacitor to create the time display. The 10kΩ potentiometer is used to adjust the frequency of the square wave signal. The circuit is powered by a 9V battery. The diagram is drawn on a grid paper with a scale of 1:1000.

## Hardware Design Procedure

Building the circuit for the alarm clock was streamlined by reusing concepts from previous lab assignments. Seƫng up the 4 digit 7-segment display followed the procedure listed in lab 4. Then I connected the three switches to analog pins, with each switch grounded with resistors. Next, I placed the potenƟometer connected to power and ground with the middle pin connected to A0 pin. Finally, I added the piezo to connect to pin A4 and ground.

----page-break-here----

Building the circuit:

1. Connect a red wire to the 5V pin and put the other end in one of the long (+) bus lines in the breadboard. If needed, connect opposite (+) bus line to power.
2. Connect a black wire to the ground pin to the adjacent long (-) bus line on the breadboard. If needed, connect opposite (-) bus line to ground.
3. Place the 4-digit 7-segment display on the breadboard.
4. Connect pins E, D, DP, C, G, A, F, B to digital pins 6,5,4,3,7,9,8,2, respecƟvely.
5. For pins, D1, D2, D3, and D4, first wire them to 1k resistors then from the resistors, wire to digital pins 10, 11, 12, 13, respecƟvely. [4]
6. Place 3 switches on the breadboard. Connect power to each switch and ground the other end with 1K resistors.
7. Connect the buƩons to A1, A2, A3 pins to set up buƩon funcƟons.
8. Place a potenƟometer on the board. Wire power to one end, ground the other end. Wire the middle pin to A0.
9. Place piezo on the board, connect one end to ground. Connect the other end to A4.

----page-break-here----

Figure 11-Physical Circuit

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000011_33e8dcfa1deef6d7dc05c9fc96d65751e079666a19ee007a7225a272b653d5a8.png)

Picture description: The image shows a close-up view of a circuit board with various electronic components and wires. The main content includes a digital display showing the number "500," a microcontroller, a 7-segment display, a potentiometer, a breadboard, a USB port, and several resistors. The circuit board is connected to a power source, and the components are interconnected with wires. The image also includes labels for each component, such as "Potentiometer," "Breadboard," "Resistors," "Microcontroller," "7 segment display," "USB," and "Wires." The circuit appears to be a simple electronic project, possibly a digital display or a counting device.

Figure 12-Electrical SchemaƟc [2]

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000012_34af05200391c4197e7eac230f05bf90ae4bc56900c42f841a12078d8202554e.png)

Picture description: The image is a schematic diagram of an electronic circuit, specifically a circuit board with a central component labeled "Arduino UNO." The circuit includes various components such as resistors, capacitors, and a potentiometer, connected by wires. There are also two rectangular blocks with text, which appear to be labels or descriptions for the circuit. The schematic is drawn on a grid paper, with the components and connections clearly outlined. The circuit seems to be designed for a specific function, possibly related to digital or electronic projects.

## Algorithm and Code

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000013_50cb5fd1fcb8875843119f96b291fa6cb41e9d513aa27bd0f3af5c702178f01f.png)

Picture description: The figure is a flowchart titled "Figure 13-Coding Flowchart [3]". It consists of a series of interconnected rectangles and diamonds, with arrows indicating the flow of the process. The rectangles represent different stages or steps in the coding process, while the diamonds represent decision points. The flowchart appears to be a visual representation of a coding process, possibly for a programming task or algorithm. The text "great job" is written in red marker on the right side of the image, suggesting that the flowchart has been completed successfully. The image also includes a red arrow pointing to the left, which may indicate a previous step or a different path in the process.

Seƫng up the code to control the alarm clock was the most challenging part of the project. IniƟally, the code was set up with 'while' loops and 'if-else' statements. The coding never worked as intended and I needed assistance from peers. The final coding worked when the structure was switched to be based on the different 'modes' of the alarm clock using the 'switch' and 'case' funcƟons. The last adjustment that was made was the inclusion of the 'rising edge' which checks if the state of the buƩon has changed, rather than just detecƟng when the buƩon is being held down. This allowed for adjusƟng the Ɵme to happen without simultaneously holding the Change BuƩon down. The explanaƟon of the coding is as follows:

----page-break-here----

- -Add in the 7-segment library for Arduino. Set up constant integers for the potenƟometer, start buƩon, change buƩon, piezo, and alarm cutout. Set up iniƟal readings for the state of the circuit. (Figure 14) [4]
- -Void setup begins serial communicaƟon at 9600 baud. Sets buƩons to be inputs and the piezo to be an output. Code reused from the 7-segment display lesson sets up the 7-segment. (Figure 15) [4]
- -Void loop begins. Refresh the 7-segment display and begin reading inputs. Case 0 is established as the Ɵme mode. Read the potenƟometer and map the value to a Ɵme between 0 and 5 minutes. Sets the countdown Ɵme. Rising edge on the start buƩon changes the mode to running mode. (Figure 15)
- -Case 1 is running mode. If loop counts down from set Ɵme, if countdown Ɵme = 0, switches to mode 3, alarming. If rising edge on the start stop buƩon pauses the Ɵmer, switch to case 2, paused mode. While paused, give the opƟon to resume countdown, or change Ɵme based on the change buƩon. (Figure 16)
- -Case 3 is the alarming state. Set the piezo to output with the 'tone' funcƟon, based on the Sound lab. Using an if loop to set the buzzer Ɵming sequence to have a gap of 3 seconds between beeps. While alarming, print to the Serial Monitor 'The alarm is

----page-break-here----

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000014_dc05dc1041d2710aa845c8456cccf8b9e9286c38f6a52fb8fd549ba64f0b01cf.png)

because the loops keep reading the same lines of code. AddiƟonally, when trying to add a three My knowledge and familiarity with the Arduino and components are improved and I am geƫng more comfortable with the concepts and equipment. This project gave me new ideas

on. Please press the alarm buƩon to turn off.' Once Rising edge on the alarm cutoff buƩon, the 'noTone' funcƟon is used to stop the piezo and mode is returned to 0. (Figure 17) -Outside the mode funcƟons, keep track of state of buƩons, format Ɵme leŌ on countdown, and display the number on the 7-segment display before repeaƟng the lines of code. (Figure 17) Conclusion The result of the project did result in a funcƟonal alarm clock that meets the requirements laid out in the instrucƟons. There are aspects of the circuit that were more challenging than expected. The physical layout of components proved to be hard to keep track of and took up a lot of space. In future projects, I hope to be more efficient in spacing and uƟlizing available digital/analog pins. For me, the most difficult part of the project was geƫng funcƟonal code that worked with my circuit. My iniƟal idea of using loops instead of switch state coding did not work second delay to the piezo beeps, I tried adding the delay (3000) funcƟon directly at the end of the code. This caused my circuit to run far behind because it added the delay aŌer reading through the code each Ɵme.

----page-break-here----

that I look to implement going forward. Many of these lessons will be applied to the final Car

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000015_1620ebb6ebc0268f69824e81c60686ae3af5b6b3fcd647f911e95775175819d9.png)

## Appendix

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000016_ede3c5227b326c11d3e5d9a5223d2b31d026040578b0903fa15c47c60b44983f.png)

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000017_cf0d3b7c82b015074502d107d0b6016a1711cbf4c548b2e90d8e658259ab7403.png)

```
Alarm_clock_codeino #include "SevSeg.h" SevSeg sevseg; constants const int Ipotentiometer const int startButton A3; button const int changeButton A2; stopped, adjust countdown time const int piezo A4; const int alarmButton A1; cutout 10 int potValue 11 12 int changeVal 0; //High/Low from alarm change button when timing false 13 startVal /High/Low reading from stop start button 14 int lastChange extra variable define state Of countdown 15 int lastStart 1/0 when when high for both change and start 16 int lastalarm 17 18 long beepTime 19 long potTime 21 long countdownTime 22 23 int minutes 24 int seconds 25 long previousTime 26 27 int mode set time, mode run , mode pause, mode alarm 28 29 void setup( ) Serial.begin(9600); pinMode(startButton, INPUT) ; pinMode(changeButton, INPUT) ; DinMode(alarmButton. INPUT ) pot int and
```

## Figure 14- Code (pg. 1)

```
Alarm_clock_codeino pinMode(alarmButton, INPUT) ; pinMode(piezo, OUTPUT ) ; byte numDigits byte digitPins[] {10, 11, 12, 13}; byte segmentPins[] {9 3, 5, 8, 7, 4} ; bool resistorsonSegments true; byte hardwareConfig COMMON_CATHODE ; sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsonSegments, false); sevseg setBri ghtness(100) void loop( ) startVal digitalRead(startButton) changeVal digitalRead(changeButton); int alarmVal digitalRead(alarmButton); sevseg.refreshDisplay( ); switch(mode) { case 0:  tine mode if(changeval button activated potTime map(analogRead(pot) , 1023 , countdownTime potTime; if(startVal HIGH && lastStart countdownTime 0) { previousTime millis( ); mode break;
```

----page-break-here----

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000018_d8d0e48f78483d7ae4c15a8c1c981a61d96c87b7ec8547d9e6aaa198cd33e30c.png)

![Image](/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Output/docling/doclingOCR/Project1_AlarmClock_Report/image_000019_17d2ca487c36ef7f608921989646b9927fa7c5256818e85abeadffa54799ce70.png)

## Figure 15- Code (pg 2)

```
Alarm_clock_codeino case running mode if(millis previousTime 1000) { /  checks to see if 1 second has passed not previousTime previousTime 1000; if(countdownTime 0) { countdownTime (countdownTime 1) ; else{ beepTime mode if(startVal HIGH 8& lastStart LOW) { / / this pauses the clock mode break; case if(startVal HIGH resume previousTime millis(); mode if(changeVal HIGH && lastChange LOW) { / /while paused, mode to change time mode break; case if(beepTime 0) {
```

Figure 16- Code (pg 3)

```
Alarm_clock codeino if(beepTime 0) { tone(piezo, 2500 , 250) ; 100 beepTime millis( ); 101 102 103 if (millis( ) beepTime 3000) { 104 tone(piezo, 2500, 250) 105 beepTime millis( ); the count 106 107 108 Serial println( The alarm is on . Please press the alarm button to turn off."); 109 110 111 if(alarmVal HIGH && lastAlarm LOW) { 112 noTone(piezo) ; 113 countdownTime 114 beepTime 115 mode 116 117 118 break; 119 120 lastStart startVal; 121 lastChange changeVal; 122 lastalarm alarmVal 123 minutes countdownTime 60; 124 seconds countdownTime 60; 125 int number (minutes 100) seconds; 126 sevseg.setNumber(number) ; 127 128 129
```

Figure 17- Code (pg 4)

----page-break-here----

## References

1. ELEGOO UNO, 'ELEGOO UNO Project Super Starter Kit with Tutorial and UNO R3 Board CompaƟble with Arduino IDE,' Amazon [Online]. Available:

hƩps://www.amazon.com/dp/B01D8KOZF4?maas=maas\_adg\_D460F095D342E4F0FE45D23700

8B6DCD\_afap\_abs&amp;ref\_=aa\_maas&amp;tag=maas.

2. Cirkit Designer, 'Cirkit Designer - Online Circuit Design Tool.' [Online]. Available:

hƩps://app.cirkitdesigner.com/project.

3. Lucidchart, 'Lucid Flowchart Design Tool.' [Online]. Available:

hƩps://lucid.app/lucidchart/0dff2584-2307-47b2-980b-

e0e7e64beae2/edit?beaconFlowId=59654C19D476AA25&amp;invitaƟonId=inv\_959e0588-034d-

4085-85f1-54961ec72834&amp;page=0\_0#.

4. T. Russo, 'EMCH 368 Mechatronics Lab 4 LCD', EMCH 368, University of South Carolina, edited 6/23/24 5. T. Russo, 'EMCH 368 Mechatronics Lab 3 Sound', EMCH 368, University of South Carolina, edited 6/23/24 6. J. Satme, 'EMCH 368 Mechatronics Lab 1 IntroducƟon to Microcontrollers and Circuits', EMCH 368, University of South Carolina, edited 1/6/25.