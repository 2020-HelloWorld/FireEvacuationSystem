import 'package:flutter/material.dart';

class VictimLoc extends StatelessWidget {
  final name;
  final emergency;
  final room;
  const VictimLoc({Key? key, required this.name, required this.room, required this.emergency}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        height: 50,
        decoration: BoxDecoration(
          color: this.emergency?Colors.red:Colors.green
        ),
        child:Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Padding(
              padding: const EdgeInsets.only(left:15.0),
              child: Text(
                "${this.name}",
                style: TextStyle(
                  fontSize: 20
                ),
              ),
            ),
        Padding(
          padding: const EdgeInsets.only(right:20.0),
          child: Text(
          "${this.room}",
          style: TextStyle(
              fontSize: 20
          ),
          ),
        )
          ],
        ) ,
      ),
    );
  }
}
