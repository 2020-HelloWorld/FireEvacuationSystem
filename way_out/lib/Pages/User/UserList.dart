import 'package:flutter/material.dart';

class UserList extends StatefulWidget {
  const UserList({Key? key}) : super(key: key);

  @override
  State<UserList> createState() => _UserListState();
}

class _UserListState extends State<UserList> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(100.0),
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
                        onPressed: () {},
                        child: Text("1"),),
                    ),
                  ),
                  SizedBox(width: 100,),
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {},
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
                        onPressed: () {},
                        child: Text("3"),),
                    ),
                  ),
                  SizedBox(width: 100,),
                  Container(
                    height: 100.0,
                    width: 100.0,
                    child: FittedBox(
                      child: FloatingActionButton(
                        onPressed: () {},
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
