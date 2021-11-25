"piedra"=x
"tijeras"=y
"papel"=z

w=input()
v=input()
    if v==w or w==v:
    console.log("empate")
    else if w==x and v==y:
    console.log("gana w");
    else if w==y and v==x:
    console.log("gana v");
    else if w==z and v==x:
    console.log("gana w");
    else if w==x and v==z:
    console.log("gana v");
    else if w==z and v==y:
    console.log("gana v");
    else if w==y and v==z:
    console.log("gana w") ;
    else:("escoja correcto")
