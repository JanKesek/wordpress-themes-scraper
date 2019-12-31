var https=require("https")
var myobject=require("./result.json")
for(var attributename in myobject){
    https.get(myobject[attributename][0], (resp) => {
        console.log("Success" + myobject[attributename])
    }).on("error", (err) => {
        console.log("Error: " + myobject[attributename] + " " + err)
    })
}
