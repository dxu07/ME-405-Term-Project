'''!@file                       mainpage.py
    @brief                      Brief doc for mainpage.py
    @details                    Detailed doc for mainpage.py 

    @mainpage                   Nerf Gun Pen Plotter 
    
    @section sec_intro          Introduction
                                For this project, we designed a 2.5 DOF Nerf Gun pen plotter that uses 
                                nerf darts to draw pictures on a white board. This plotter utilizes Nucleo STM32476 microcontroller 
                                that interfaces with the TMC4210 serial interface IC and the TMC2208 stepper driver, which we used to 
                                control our stepper motors. Commands to for specific tasks were sent from our PC to the MCU through serial/uart. 
                                In the following sections, we will discuss some of the features of the of the Nerf Gun Pen Plotter. Code specific 
                                details can be found in the code documentation. 
                                
                                @image html nerf_profile.jpg "Figure 1: Nerf Gun Pen Plotter"
                                
                                
    @section sec_demo           Project Demo
                                The Nerf Gun Pen Plotter has two primary functions: Pen Plotting and Find Red. 
                                
                                
    @subsection sec_demo1       Pen Plotter      
                                The pen plotter takes in an hpgl file, reads it, and plots according to its instructions. 
                                In this demonstration, we have prepared an image that incorporates both a straight lines 
                                and curves to demonstrate its drawing capabilites. \n
                                
    @htmlonly                   <iframe src="https://player.vimeo.com/video/719266625?h=54a4727f35&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="720" height="405" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Nerf Camera"></iframe>
    @endhtmlonly
                                \n 
                                A comparison of the image drawn by the nerf gun and the reference image 
                                used is shown below. The reference image is overlayed on top of the drawn image. \n
                                
                                @image html drawing_comp.png "Figure 2: Drawn image vs Reference Image"
                                
                                \n
                                Obviously, there are several limitations that come with using a nerf gun. From the demonstration, 
                                it can be seen that the nerf darts don't always shoot straight. Additionally, the nerf darts themselves 
                                are rather large, so there needs to be a significant space between the darts in order to decrease the 
                                probability of darts hitting each other. Another issue is that the nerf magizine is only limited to 18 bullets, 
                                which forced us to constantly reload the gun. If we had more time, we would have likely designed a larger magazine 
                                so the drawing process could have been much smoother. Lastly, the suction on the darts were not great either, causing some
                                darts to fall off after a while.
                                

    @subsection sec_demo2       Finding Red
                                An additional functionality that we added was the ability for the nerf gun to automatically 
                                detect and shoot at the color red. 
    
    @htmlonly                   <iframe src="https://player.vimeo.com/video/719224223?h=a2495adf7c&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="720" height="405" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Nerf Camera"></iframe>
    @endhtmlonly
                                \n
                                To accomplish this functionality, we used a webcam that was attached to the side of the gun. 
                                Using a program ran on the computer, we utulized OpenCV modules to help detect the color red.
                                Then using the field of view, direct anglular instructions were sent from the PC to the MCU 
                                instead of cartesian coordinates. Additional details can be found in the camera documentation. 
    
    @section sec_mechdesign     Mechanical Design
                                The following sections will discuss the different mechanical design elements used in our project. \n \n
                                A list of the mechanical components and where it can be bought: \n
                                Nerf Gun: https://www.amazon.com/Turbine-Motorised-Blaster-Customising-Capabilities/dp/B0824SGQP1 
                                    \n
                                NEMA 17 Stepper Motors: https://www.amazon.com/dp/B00PNEQI7W?ref=nb_sb_ss_w_as-reorder-t1_ypp_rep_k0_1_13&amp&crid=3MQN5NFPV80OP&amp&sprefix=nema+stepper+
                                    \n
                                Limit Switches: https://www.amazon.com/MXRS-Hinge-Momentary-Button-Switch/dp/B07MW2RPJY/ref=sr_1_3?keywords=limit+switch&qid=1654909607&sr=8-3
                                    \n
                                Lazy Susan: https://www.mcmaster.com/lazy-susans/square-turntables-7/width~4/ 
                                    \n
                                
    @subsection sec_nerf        Nerf Gun 
                                The nerf gun used in this project is the Nerf Elite 2.0 Turbine CS-18 Motorised Blaster. 
                                
                                @image html nerfgun.jpg "Figure 3: Nerf Elite 2.0 Turbine CS-18 Motorised Blaster"
                                
                                This is an electrical, automatic nerf gun. In order to access the electronics in this project, 
                                the entire back portion of the  nerf gun was removed, as shown in the image below.
                                
                                @image html back_nerf.jpg "Figure 4: Back of Nerf Gun"
                                
    @subsection sec_CAD         CAD Design
                                The main structure of the automatic nerf gun was designed in SolidWorks and then 3D-printed with PLA. 
                                Details on assembly can be found in the SolidWorks Assembly file in the repository. 
                                
                                @image html CAD.png "Figure 5: CAD of the Nerf Gun Turret Assembly"
                                
                                The nerf gun fits in between the two supports. The horizontal and vertical sliders are designed so that 
                                the center of gravity of the gun can be found. This help with the stepper motor control so that less torque 
                                is needed to move the gun. We found that by having the supports hold the gun at the center of gravity, the stepper 
                                motors were less likely to skip steps or fail in holding. \n
                                
                                The CAD is also designed to interface with two NEMA 17 stepper motors. These are 4-wire, bi-polar stepper motors. 
                                One of the NEMA 17 motors fits onto the top of the side supports to interface with the nerf gun of azimuthal direction control. 
                                The other NEMA 17 motor connects the bottom plate and the top plate for polar direction control.
                                
    @section sec_elecdesign     Electrical Design
                                The automatic Nerf gun incorporates two DC motors to fire bullets: 
                                one which spins a set of counter rotating wheels, and one which 
                                actuates a piston that pushes darts out of the magazine and into 
                                the wheels, launching them out of the barrel of the gun. We had originally 
                                planned to incorporate a DC motor driver to control them directly, but upon inspecting 
                                the internals of the Nerf gun recognized that there was additional control circuitry. 
                                Instead, we opted to simply replace the two switches used as triggers with small signal 
                                relays. \n
                                    
                                Additionally, we observed that in automatic fire mode, the accuracy of the Nerf gun was 
                                significantly reduced, and the fire rate was potentially too fast to move our assembly in 
                                time to fire each dart in the correct location. To facilitate single fire mode, we would need 
                                to ???hold??? the fire trigger just long enough to fire a single dart, and no longer so that multiple 
                                darts weren???t fired by accident. To facilitate this, we implemented an IR breakbeam sensor at the 
                                end of the Nerf gun???s barrel. When a dart is fired, the sensor pulls a GPIO pin low, and we can 
                                detect this on the MCU via an interrupt. This enabled us to fire a single dart at a time, as 
                                well as detect when a misfire or jam occurred, as the dart would not have been detected in a 
                                specified time period. \n
                                
                                @image html nerf_schematic.png "Figure 6: Nerf control board schematic"                                
                                
                                \n
                                Figure 6 shows the electrical design of the Nerf control board. In addition to the two double-pull 
                                double-throw small signals relays used to control the gun, headers for connecting to the IR sensor, 
                                Nerf gun internal circuitry, and MCU are included. The board additionally provides power to the Nerf gun, 
                                stepping down the 12 volts used to power the stepper motors to 5 volts via the DC-DC converter, and to 6 
                                volts via the linear voltage regulator. While the Nerf gun uses 4 D-cell batteries, totaling 6 volts, we 
                                found that it was able to operate at 5V, albeit with slightly higher current draw. The DC-DC converter is 
                                able to provide 1.2 amps, while the LDO theoretically provide 1.5 amps, but require a substantial heatsink 
                                to achieve this power output. Solder jumpers allow us to select between the two voltage sources, as well as 
                                a direct voltage input for use with a second 6 volt power supply. \n
                                
                                @image html nerf_pcb_2d.png "Figure 7: 2-D layout of Nerf control board PCB"
                                
                                \n
                                
                                @image html nerf_pcb.png "Figure 8: 3D Render of Nerf control board PCB"
                                
                                The schematic and PCB were designed in Altium Designer. Figure X shows the PCB layout in 2-dimensions, while 
                                Figure 8 shows a 3D render of the board, including the component bodies. We ordered the PCBs from Osh Park and 
                                got SMD stencils from Osh Stencils. Our electronic components were sourced from Mouser, as well as the manufacturer 
                                of the DC-DC converter, Monolithic Power Systems. We assembled the boards by hand using a hot air rework station and 
                                soldering iron.                                                           
                                
                                
    @section sec_calcs          Calculations
                                As part of our drawing task, we developed forward and inverse kinematics for the nerf gun based off of its geometry. 
                                The two degrees of freedom we had to account for were the x-angle (polar) and the y-angle (azimuthal). In order to plot
                                an image, we needed to establish a set of equations to related x,y coordinates to angular coordinates. To do this we utilized a 
                                Newton-Raphson solver function to iteratively find the actuator angles. The reference drawings we used to do our calcalations are 
                                provided below.

                                @image html side.png "Figure 9: Side View"
                                @image html top.png "Figure 10: Top View"
                                
                                Below are the equations that we derived and used in our Newton-Raphson.
                                
                                @image html equation.png "Figure 11: Kinematics Equations"
                                
                                Details on how the equations are used can be found in our source code documentation.

    @section sec_task           Task Diagram                                
                                In order to run our code, we utilized a cooperative task schedular in the microcontroller. Data is shared between different
                                tasks so that our program can simultaneously move, calculate coordinates, and receive commands. A task diagram this process is shown below. 
                                
                                @image html task_diagram.png "Figure 12: Task Diagrams"
        

  
    
    @author             Daniel Xu
    @author             Alex Radovan
    
    @copyright          License Info

    @date               June 10, 2022
'''