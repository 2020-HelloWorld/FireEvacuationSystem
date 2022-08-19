import 'package:flutter/material.dart';
import 'package:way_out/Pages/SplashScreen.dart';

void main(){
  runApp(MyApp());
}
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "WayOut",
      home: SplashScreen(),
    );
  }
}
