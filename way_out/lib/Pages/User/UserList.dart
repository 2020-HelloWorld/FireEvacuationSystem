import 'package:flutter/material.dart';
import 'package:way_out/Pages/User/UserMap.dart';

class UserList extends StatefulWidget {
  const UserList({Key? key}) : super(key: key);

  @override
  State<UserList> createState() => _UserListState();
}

class _UserListState extends State<UserList> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(50.0),
      child: Container(
        alignment: Alignment.center,
        child: SingleChildScrollView(
          child: Column(
            children: [
              Row(
                children: [
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {
                          Navigator.push(context,MaterialPageRoute(
                              builder: (context)=>UserMap(userIndex: 1)
                          ));
                        },
                        child: Text("1"),),
                    ),
                  ),
                  SizedBox(width: 70,),
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {
                          Navigator.push(context,MaterialPageRoute(
                              builder: (context)=>UserMap(userIndex: 2)
                          ));
                        },
                        child: Text("2"),),
                    ),
                  ),
                ],
              ),
              SizedBox(height: 100,),
              Row(
                children: [
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {
                          Navigator.push(context,MaterialPageRoute(
                              builder: (context)=>UserMap(userIndex: 3)
                          ));
                        },
                        child: Text("3"),),
                    ),
                  ),
                  SizedBox(width: 70,),
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {
                          Navigator.push(context,MaterialPageRoute(
                              builder: (context)=>UserMap(userIndex: 4)
                          ));
                        },
                        child: Text("4"),),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
