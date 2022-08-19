import 'package:flutter/material.dart';

class RescuerDashboard extends StatefulWidget {
  const RescuerDashboard({Key? key}) : super(key: key);

  @override
  State<RescuerDashboard> createState() => _RescuerDashboardState();
}

class _RescuerDashboardState extends State<RescuerDashboard> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text("Recuer Dashboard"),
    );
  }
}
