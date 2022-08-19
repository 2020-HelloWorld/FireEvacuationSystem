import 'package:flutter/material.dart';

import 'Rescuer/RescuerDashboard.dart';
import 'User/UserList.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(80.0),
        child: Container(
          width: 400,
          child: SingleChildScrollView(
            child: Column(
              children: <Widget>[
                Text(
                  "USER",
                style: TextStyle(
                  fontSize: 40,
                  fontWeight: FontWeight.w700,
                ),
                ),
                Text(
                    "If you are a registered employee in the building and you need a direction out of the building during incase of fire emergency, click the button below",
                  style: TextStyle(
                    fontStyle: FontStyle.italic
                  ),
                ),
                Container(
                  margin: EdgeInsets.only(top: 20),
                  height: 60,
                  width: 200,
                  child: FlatButton(
                    child: Text("User Click Here",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,

                      ),
                    ),
                    onPressed: (){
                      Navigator.push(context,MaterialPageRoute(
                          builder: (context)=>UserList()
                      ));
                    },
                  ),
                  decoration: BoxDecoration(
                      color: Colors.deepPurple.shade700.withOpacity(0.4),
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                            color: Colors.grey.shade200,
                            offset: Offset(2,2),
                            spreadRadius: 3,
                            blurRadius: 5
                        )
                      ]
                  ),
                ),

                SizedBox(
                  height: 100,
                ),


                Text(
                  "RESCUE",
                  style: TextStyle(
                    fontSize: 40,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                Text(
                  "If you are the part of professional fire rescue crew, and need the location of all the victims inside the building, press the below button",
                  style: TextStyle(
                      fontStyle: FontStyle.italic
                  ),
                ),
                Container(
                  margin: EdgeInsets.only(top: 20),
                  height: 60,
                  width: 200,
                  child: FlatButton(
                    child: Text("Rescuer Click Here",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,

                      ),
                    ),
                    onPressed: (){
                      Navigator.push(context,MaterialPageRoute(
                          builder: (context)=>RescuerDashboard()
                      ));
                    },
                  ),
                  decoration: BoxDecoration(
                      color: Colors.deepPurple.shade700.withOpacity(0.4),
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                            color: Colors.grey.shade200,
                            offset: Offset(2,2),
                            spreadRadius: 3,
                            blurRadius: 5
                        )
                      ]
                  ),
                ),

              ],
            ),
          )
        ),
      )
    );
  }
}
