# HackStack

## Problem Statement

A Fire evacuation system is simply a tool to use to help the Fire Brigade or a person who is stuck in building to safely get out as quickly and effectively as possible.
Our Project is a Graph based wireless navigation and indoor positioning system by which we can get the exact location of the victim inside the building.

## Proposed solution

We are focusing on building a mobile app which ensures safe evacuation of people who are stuck in fire and couldn't find easy and safest way to exit. This app is based on the Dijkstra's algorithm where we tend to find the optimal path to the exit by considering the weight on the Nodes which are calculated based on smoke and temperature values. These values are generated by IoT based device that measures temperature and smoke. These values are sent to cloud and can be used by any client or server based on their needs.

The main features of our application are:

1.  Indoor Positioning
2.  Safe Navigation
3.  Rescue Operation Assistance
4.  Emergency Rescue Request
5.  User-Friendly UI

## Run down on app

This project is combination of Cloud, IoT, and Data stuctures domains. In this project we have 4 microprocessors, and each microprocessor have 1 tempreture and 1 smoke sensors which will work as a Node. Each node has predefined connection to other node based on feasiblity of connection. Then this will work as bluetooth beacons for the room. There is ESP code which will find the nearest Node for the mobile user. In case of fire the weights between the Nodes will change and also the priority will differ.  We are using Dijkistra's Algorithm to find the shortest path from current Node to exit Node. This values will change dynamically and will be displayed on the application.

## Code Base

### ESP + Server

ESP + Server folder contains the code for getting the nearest bluetooth beacon and will work as a RIF ID. Server will be responsible for computing the shortest path and updating in the cloud database so that it can be retrieved by application.

### Firebase

Firebase is a cloud data storage platform by google and helps to store the data dynamically in real time. The backend portion of this application is wriiten in python and all data send or recieved are parsed using JSON format. 

https://www.researchgate.net/publication/339096717_An_IoT-based_Emergency_Evacuation_System
