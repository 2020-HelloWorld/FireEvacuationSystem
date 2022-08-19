import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class RescuerDashboard extends StatefulWidget {
  const RescuerDashboard({Key? key}) : super(key: key);

  @override
  State<RescuerDashboard> createState() => _RescuerDashboardState();
}

class _RescuerDashboardState extends State<RescuerDashboard> {
  @override
  //https://stackoverflow.com/questions/54345910/snapshot-data-length-in-the-itemcount-does-not-work-the-getter-length-was-ca
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder(
          stream: FirebaseFirestore.instance.collection('Person').snapshots(),
          builder:
              (ctx, AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            }
            return ListView.builder(
                itemCount: snapshot.data?.docs.length,
                itemBuilder: (ctx, index) {
                  var doc = snapshot.data!.docs[index];
                  var data = doc.data() as Map;
                  return Container(
                    child: Row(
                      children: [
                        Text("${data["Room"]}, Is it emergency? ${data["Emergency"]}")
                      ],
                    )
                  );
                });
          }),
    );
  }
}
