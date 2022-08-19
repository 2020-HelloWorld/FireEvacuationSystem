import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class UserMap extends StatelessWidget {
  final userIndex;
  const UserMap({Key? key, required this.userIndex}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      body: StreamBuilder(
          stream: FirebaseFirestore.instance.collection('Person').snapshots(),
          builder:
              (ctx, AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            }
            var doc = snapshot.data!.docs[this.userIndex-1];
            var data = doc.data() as Map;
            bool _danger = data["Emergency"];


                  return SingleChildScrollView(
                    child: Column(
                      children: [
                          Padding(
                            padding: const EdgeInsets.only(left: 20.0,top: 10),
                            child: Container(
                                height: 100,
                                width: 150,
                                decoration: BoxDecoration(
                                  color: _danger?Colors.red:Colors.green
                                ),
                                child: FittedBox(
                                  child: FlatButton(
                                    onPressed: (){
                                      _danger = _danger?false:true;
                                      final docUser = FirebaseFirestore.instance.collection("Person").doc("P-${this.userIndex.toString()}");
                                      docUser.update({
                                        "Emergency":_danger,
                                      });
                                    },
                                    child: Icon(Icons.error),
                                  ),
                                ),
                              ),
                          )

                      ],
                    ),
                  );
          }),
    );
  }
}

