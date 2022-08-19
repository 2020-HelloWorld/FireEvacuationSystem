import 'dart:async';

import 'package:flutter/material.dart';

import 'HomePage.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  void initState(){
    super.initState();
    //Automatically pushes new page after 5 seconds after loading this page
    Timer(
        Duration(seconds: 2),
            ()=> Navigator.pushReplacement(context,MaterialPageRoute(
            builder: (context)=>HomePage()
        ))
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.only(left: 40.0),
        child: Container(
          alignment: Alignment.center,
          child: SingleChildScrollView(
            child: Column(
              children: [
                Text("TEAM RUNTIME TERROR",
                  style: TextStyle(
                    fontSize: 80,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                SizedBox(
                  height: 20,
                ),
                Text(
                    "FIRE EVACUATION SYSTEM FOR BUILDINGS",
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.w500,
                  ),
                )
              ],
            ),
          )
        ),
      ),
    );
  }
}
