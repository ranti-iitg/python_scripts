mystring = """# Assignment 1

ROS: an open-source Robot Operating System.
As the scope of robotics continue to grow and required breadth of expertise is well beyond the capabilities of any single researcher. In this sense ROS was created it provides a collection of software frameworks for robot software development on a heterogeneous computer cluster.
The philosophical goals of ROS can be summarized as:
1. Peer-to-peer: A system built using ROS consists of a number of processes, potentially on a number of different hosts, connected at runtime in a peer-to-peer topology
2. Tools-based: Microkernel  design,  where  a  large  number  of small tools are used to build and run the various ROS components
3. Multi-lingual: The ROS framework is easy to implement in any modern programming language. We have already implemented it in Python, C++, and Lisp.
4. Thin: ROS is designed to be as thin as possible, A corollary to this is that ROS is easy to integrate with other robot software frameworks: ROS has already been integrated with OpenRAVE, Orocos, and Player. 
5. Free and Open-Source->ROS is  distributed under the terms of the BSD license, which allows the development of both non-commercial and commercial  projects.

The fundamental concepts of the ROS implementation
1. Nodes: Nodes are processes that perform computation. ROS is designed to be modular at a fine-grained scale; a robot control system usually comprises many nodes.

2. Messages: Nodes communicate with each other by passing messages. A message is simply a data structure, comprising typed fields. Standard primitive types (integer, floating point, boolean, etc.) are supported, as are arrays of primitive types. Messages can include arbitrarily nested structures and arrays (much like C structs). 

3. Topics: Messages are routed via a transport system with publish / subscribe semantics. A node sends out a message by publishing it to a given topic. The topic is a name that is used to identify the content of the message. A node that is interested in a certain kind of data will subscribe to the appropriate topic. There may be multiple concurrent publishers and subscribers for a single topic, and a single node may publish and/or subscribe to multiple topics. In general, publishers and subscribers are not aware of each others' existence

4. Services: The publish / subscribe model is a very flexible communication paradigm, but its many-to-many, one-way transport is not appropriate for request / reply interactions, which are often required in a distributed system. Request / reply is done via services, which are defined by a pair of message structures: one for the request and one for the reply. A providing node offers a service under a name and a client uses the service by sending the request message and awaiting the reply. 

Tools designed to be used with ROS
1. Debugging a single node ->ROS is designed to minimize the difficulty of debugging
in   such   settings,   as   its   modular   structure   allows   nodes
undergoing active development to run alongside pre-existing,
well-debugged  nodes. 

2. Logging and playback->ROS  supports  this  approach  by  pro-
viding generic logging and playback functionality. Any ROS
message  stream  can  be  dumped  to  disk  and  later  replayed

3. Coordinate Frames/Transforms->

The tf package provides a distributed, ROS-based framework for calculating the positions of multiple coordinate frames over time. 

4. Packaged subsystems-> ROS provides a tool called
roslaunch ,which reads an XML description of a graph and instantiates the graph on the cluster

5. Visualization and Monitoring: However, a more powerful concept is a visualization program which uses a plugin architecture: this is done in the rviz program, which is distributed with ROS. Visualization panels can be dynamically instantiated to view a large variety of datatypes, such as images, point clouds, geometric primitives (such as object recognition results), render robot poses and trajectories, etc.


"""
import re
print re.sub(' +',' ',mystring)

